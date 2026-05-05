---
title: "C#와 .NET Native AOT로 Node.js 네이티브 애드온 작성하기"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "C# Dev Kit 팀이 C++로 작성된 Node.js 애드온을 .NET Native AOT로 교체했습니다 — 결과는 더 깔끔하고 안전하며, .NET SDK만 있으면 됩니다."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *이 글은 자동 번역되었습니다. 영어 원문은 [여기]({{< ref "index.md" >}})에서 확인할 수 있습니다.*

제가 좋아하는 시나리오입니다. .NET 도구를 개발하는 팀이 C++로 작성하고 `node-gyp`으로 컴파일하는 네이티브 Node.js 애드온을 사용하고 있었습니다. 동작했습니다. 하지만 팀원 누구도 직접 건드리지 않을 패키지를 빌드하기 위해 모든 개발자 기기에 Python(그것도 구버전)을 설치해야 했습니다.

그래서 매우 합리적인 질문을 했습니다: .NET SDK가 이미 설치되어 있는데, 왜 C++를 쓰는 걸까요?

답은 Native AOT였고, 결과는 정말 우아합니다.

## 기본 아이디어

Node.js 네이티브 애드온은 Node.js가 런타임에 로드할 수 있는 공유 라이브러리(Windows의 `.dll`, Linux의 `.so`, macOS의 `.dylib`)입니다. 인터페이스는 [N-API](https://nodejs.org/api/n-api.html)—안정적이고 ABI 호환 가능한 C API입니다. N-API는 라이브러리가 어떤 언어로 만들어졌는지 신경 쓰지 않고, 올바른 심볼을 내보내는지만 확인합니다.

.NET Native AOT는 정확히 그것을 만들 수 있습니다. C# 코드를 임의의 진입점을 가진 네이티브 공유 라이브러리로 미리 컴파일합니다. 이것이 전부입니다.

## 프로젝트 설정

프로젝트 파일은 최소화됩니다:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot`은 `dotnet publish` 시 공유 라이브러리를 생성하도록 SDK에 지시합니다. `AllowUnsafeBlocks`는 함수 포인터와 고정 버퍼를 사용하는 N-API interop에 필요합니다.

## 진입점 내보내기

Node.js는 라이브러리가 `napi_register_module_v1`을 내보낼 것을 기대합니다. C#에서는 `[UnmanagedCallersOnly]`가 정확히 그 역할을 합니다:

```csharp
public static unsafe partial class RegistryAddon
{
    [UnmanagedCallersOnly(
        EntryPoint = "napi_register_module_v1",
        CallConvs = [typeof(CallConvCdecl)])]
    public static nint Init(nint env, nint exports)
    {
        Initialize();
        RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
        return exports;
    }
}
```

주목할 점들: `nint`는 네이티브 크기 정수로 `intptr_t`의 관리형 등가물입니다. `u8` 접미사는 UTF-8 문자열 리터럴을 담은 `ReadOnlySpan<byte>`를 생성하여 인코딩 할당 없이 N-API에 직접 전달됩니다. `[UnmanagedCallersOnly]`는 Node.js가 찾는 정확한 진입점 이름으로 메서드를 내보냅니다.

## N-API를 호스트 프로세스에 대해 해석하기

N-API 함수는 별도의 라이브러리가 아닌 `node.exe` 자체에서 내보냅니다. 따라서 무언가에 링크하는 대신, 시작 시 실행 중인 프로세스에 대해 해석합니다:

```csharp
private static void Initialize()
{
    NativeLibrary.SetDllImportResolver(
        System.Reflection.Assembly.GetExecutingAssembly(),
        ResolveDllImport);

    static nint ResolveDllImport(
        string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        if (libraryName is not "node") return 0;
        return NativeLibrary.GetMainProgramHandle();
    }
}
```

이를 통해 P/Invoke 선언이 `[LibraryImport]`와 소스 생성 마샬링으로 올바르게 동작합니다.

## 실제 내보낸 함수

그들이 구현한 레지스트리 읽기 함수:

```csharp
[UnmanagedCallersOnly(CallConvs = [typeof(CallConvCdecl)])]
private static nint ReadStringValue(nint env, nint info)
{
    try
    {
        var keyPath = GetStringArg(env, info, 0);
        var valueName = GetStringArg(env, info, 1);

        if (keyPath is null || valueName is null)
        {
            ThrowError(env, "Expected two string arguments: keyPath, valueName");
            return 0;
        }

        using var key = Registry.CurrentUser.OpenSubKey(keyPath, writable: false);

        return key?.GetValue(valueName) is string value
            ? CreateString(env, value)
            : GetUndefined(env);
    }
    catch (Exception ex)
    {
        ThrowError(env, $"Registry read failed: {ex.Message}");
        return 0;
    }
}
```

`try/catch`에 대한 중요한 참고사항: `[UnmanagedCallersOnly]` 메서드에서 처리되지 않은 예외는 호스트 프로세스를 충돌시킵니다. 항상 예외를 잡아 `ThrowError`를 통해 JavaScript에 전달하세요.

## TypeScript에서 호출하기

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, Python 없음, C++ 없음.

## 얻은 것

즉각적인 승리는 기여자 경험이었습니다: 특정 Python 버전이 더 이상 필요 없고, `yarn install`은 Node.js와 .NET SDK만으로 동작합니다. CI 파이프라인도 단순해졌습니다. 성능은 C++ 구현과 비슷했습니다.

## 마무리

C# Dev Kit 팀은 Python/C++ 복잡성을 팀 모두가 이미 작성하고 디버그할 줄 아는 깔끔한 C# 코드로 대체했습니다. 모든 문자열 마샬링 헬퍼를 포함한 전체 안내는 [.NET 블로그 원문](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)을 참고하세요.
