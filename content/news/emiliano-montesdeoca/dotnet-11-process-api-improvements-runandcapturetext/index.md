---
title: ".NET 11 Finally Fixes the Process API"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process gets its biggest update in years. RunAndCaptureTextAsync, KillOnParentExit, SafeProcessHandle APIs, and full control over standard handle redirection — no more deadlock boilerplate."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Every .NET developer who has ever needed to spawn a process and capture its output has written some variation of the same dangerous boilerplate: async read from stdout, async read from stderr, `WaitForExitAsync`, don't forget to drain both streams or you'll deadlock. It's a well-known trap that's been there for years.

.NET 11 finally fixes this properly.

## RunAndCaptureTextAsync

The headline addition: a single static method that starts a process, captures stdout and stderr, and waits for exit without deadlocking.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

One call. No manual stream draining. No carefully positioned `WaitForExit`. If you just need to run something and get its output, this is the API you want.

There's also `Process.RunAsync` for the case where you want to wait for exit without capturing output.

## KillOnParentExit

A common problem with spawned processes: if the parent crashes or is killed, child processes keep running as orphans. `KillOnParentExit` lets you declare at process start time that the child process should be terminated when the parent process exits.

This is a feature that's existed in platform-specific ways (job objects on Windows, prctl on Linux) but required p/invoke or third-party libraries to use from .NET. Now it's a first-class property on `ProcessStartInfo`.

## SafeProcessHandle-Based APIs

The new lightweight API surface is built around `SafeProcessHandle` rather than the full `Process` class. The full `Process` class carries a lot of state and is difficult to trim — the `SafeProcessHandle` path is more trimmer-friendly for applications that need to minimize output size (WASM, native AOT).

## Full Control Over Handle Inheritance

The update also adds fine-grained control over which handles a child process inherits and how standard handles are redirected. Previously you could redirect stdin/stdout/stderr but couldn't specify exactly which handles to inherit at the OS level. The new APIs expose that control.

## Why This Matters

The `Process` class is used in tooling, build systems, test runners, and any application that shells out to other executables. The old API surface dated back to .NET Framework and was showing its age. This isn't a breaking change — the old APIs still work — but new code should prefer the new surface.

For trimmed applications or AOT compilation scenarios, the `SafeProcessHandle` path is particularly welcome. The old `Process` class brought in a lot of reflection-heavy code that complicated trimming.

Original post: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
