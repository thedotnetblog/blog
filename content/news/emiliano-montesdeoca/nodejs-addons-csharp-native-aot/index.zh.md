---
title: "用 C# 和 .NET Native AOT 编写 Node.js 原生插件"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "C# Dev Kit 团队用 .NET Native AOT 替换了 C++ 编写的 Node.js 插件——结果更简洁、更安全，只需要 .NET SDK。"
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *本文为自动翻译。如需阅读英文原文，请[点击这里]({{< ref "index.md" >}})。*

这是一个我很喜欢的场景：一个开发 .NET 工具的团队，用 C++ 编写了原生 Node.js 插件，通过 `node-gyp` 编译。它能运行。但每个开发者的机器上都需要安装 Python——而且是旧版本的 Python——仅仅为了构建一个团队里没有人会直接接触的包。

于是他们提出了一个很合理的问题：我们已经装了 .NET SDK，为什么还要写 C++？

答案是 Native AOT，结果相当优雅。

## 基本思路

Node.js 原生插件是一个共享库（Windows 上的 `.dll`，Linux 上的 `.so`，macOS 上的 `.dylib`），Node.js 可以在运行时加载它。接口叫做 [N-API](https://nodejs.org/api/n-api.html)——一个稳定的、ABI 兼容的 C API。N-API 不关心是什么语言产生了这个库，只关心它是否导出了正确的符号。

.NET Native AOT 恰好可以做到这一点。它将 C# 代码提前编译成具有任意入口点的本地共享库。这就是全部的技巧。

## 项目配置

项目文件非常简洁：

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` 告诉 SDK 在 `dotnet publish` 时生成共享库。`AllowUnsafeBlocks` 是 N-API interop 使用函数指针和固定缓冲区所必需的。

## 导出入口点

Node.js 期望你的库导出 `napi_register_module_v1`。在 C# 中，`[UnmanagedCallersOnly]` 正是做这件事的：

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

值得注意的几点：`nint` 是本机大小的整数——`intptr_t` 的托管等价物。`u8` 后缀生成包含 UTF-8 字符串字面量的 `ReadOnlySpan<byte>`，直接传递给 N-API，无需任何编码分配。`[UnmanagedCallersOnly]` 用 Node.js 所寻找的确切入口点名称导出方法。

## 将 N-API 解析到宿主进程

N-API 函数由 `node.exe` 本身导出，而不是单独的库。因此不是链接到某个库，而是在启动时对运行中的进程进行解析：

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

有了这个，P/Invoke 声明通过 `[LibraryImport]` 和源生成的 marshalling 就能正常工作了。

## 一个真实的导出函数

这是他们构建的注册表读取器：

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

关于 `try/catch` 的重要说明：`[UnmanagedCallersOnly]` 方法中未处理的异常会导致宿主进程崩溃。始终要捕获异常并通过 `ThrowError` 转发给 JavaScript。

## 从 TypeScript 调用

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#，无需 Python，无需 C++。

## 他们获得了什么

立竿见影的好处是改善了贡献者体验：不再需要特定版本的 Python，`yarn install` 只需 Node.js 和 .NET SDK 就能工作。CI 流水线也得到了简化。性能与 C++ 实现相当。

## 总结

C# Dev Kit 团队用团队里每个人都能编写和调试的简洁 C# 代码，替换了 Python/C++ 的复杂性。如需包含所有字符串 marshalling 辅助方法的完整演练，请查看 [.NET 博客上的原文](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)。
