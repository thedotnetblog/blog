---
title: ".NET 11이 드디어 프로세스 API를 수정합니다"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process가 수년 만에 가장 큰 업데이트를 받습니다. RunAndCaptureTextAsync, KillOnParentExit, SafeProcessHandle API, 표준 핸들 리다이렉션에 대한 완전한 제어 — 더 이상 데드락 보일러플레이트 코드는 없습니다."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

프로세스를 시작하고 출력을 캡처해야 했던 모든 .NET 개발자는 동일한 위험한 보일러플레이트 코드의 변형을 작성해 왔습니다: stdout의 비동기 읽기, stderr의 비동기 읽기, `WaitForExitAsync`, 두 스트림을 모두 비우는 것을 잊으면 데드락이 발생합니다. 이것은 수년간 존재해 온 잘 알려진 함정입니다.

.NET 11이 마침내 이것을 제대로 수정합니다.

## RunAndCaptureTextAsync

핵심 추가 사항: 프로세스를 시작하고, stdout과 stderr를 캡처하고, 데드락 없이 종료를 기다리는 단일 정적 메서드.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

한 번의 호출. 수동 스트림 드레인 없음. 신중하게 배치된 `WaitForExit` 없음. 단순히 무언가를 실행하고 출력을 얻어야 한다면, 이것이 원하는 API입니다.

출력을 캡처하지 않고 종료를 기다리는 경우를 위한 `Process.RunAsync`도 있습니다.

## KillOnParentExit

시작된 프로세스의 일반적인 문제: 부모 프로세스가 충돌하거나 종료되면, 자식 프로세스는 고아로 계속 실행됩니다. `KillOnParentExit`를 사용하면 프로세스 시작 시 부모 프로세스가 종료될 때 자식 프로세스도 종료되어야 한다고 선언할 수 있습니다.

이것은 플랫폼별 방식(Windows의 job objects, Linux의 prctl)으로 존재했던 기능이지만 .NET에서 사용하려면 p/invoke나 서드파티 라이브러리가 필요했습니다. 이제 `ProcessStartInfo`의 일급 프로퍼티가 되었습니다.

## SafeProcessHandle 기반 API

새로운 경량 API 표면은 전체 `Process` 클래스가 아닌 `SafeProcessHandle`을 중심으로 구축되었습니다. 전체 `Process` 클래스는 많은 상태를 가지고 있어 트리밍하기 어렵습니다 — `SafeProcessHandle` 경로는 출력 크기를 최소화해야 하는 애플리케이션(WASM, 네이티브 AOT)에 더 트리머 친화적입니다.

## 핸들 상속에 대한 완전한 제어

업데이트는 또한 자식 프로세스가 상속하는 핸들과 표준 핸들이 리다이렉트되는 방식에 대한 세밀한 제어를 추가합니다. 이전에는 stdin/stdout/stderr를 리다이렉트할 수 있었지만 OS 수준에서 정확히 어떤 핸들을 상속할지 지정할 수 없었습니다. 새로운 API는 그 제어를 노출합니다.

## 왜 중요한가

`Process` 클래스는 툴링, 빌드 시스템, 테스트 러너, 그리고 다른 실행 파일을 호출하는 모든 애플리케이션에서 사용됩니다. 이전 API 표면은 .NET Framework 시절의 것으로 노후화되어 있었습니다. 이것은 호환성을 깨는 변경이 아닙니다 — 이전 API는 계속 작동합니다 — 하지만 새 코드는 새 표면을 선호해야 합니다.

트리밍된 애플리케이션이나 AOT 컴파일 시나리오에서는 `SafeProcessHandle` 경로가 특히 환영받습니다. 이전 `Process` 클래스는 트리밍을 복잡하게 만드는 리플렉션 heavy 코드를 많이 가져왔습니다.

원본 게시물: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
