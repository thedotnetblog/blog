---
title: ".NET 11 终于修复了进程 API"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process 迎来了多年来最大的更新。RunAndCaptureTextAsync、KillOnParentExit、SafeProcessHandle API，以及对标准句柄重定向的完全控制 — 再也不需要死锁样板代码了。"
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

每个曾经需要启动进程并捕获其输出的 .NET 开发者都写过某种变体的危险样板代码：异步读取 stdout、异步读取 stderr、`WaitForExitAsync`，不要忘记排空两个流，否则会死锁。这是一个众所周知的陷阱，已经存在多年了。

.NET 11 终于正确地解决了这个问题。

## RunAndCaptureTextAsync

核心新增：一个单一的静态方法，可以启动进程、捕获 stdout 和 stderr，并等待退出而不会死锁。

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

一次调用。无需手动排空流。无需精心放置的 `WaitForExit`。如果你只需要运行某个命令并获取其输出，这就是你想要的 API。

对于想要等待退出但不捕获输出的情况，还有 `Process.RunAsync`。

## KillOnParentExit

已启动进程的常见问题：如果父进程崩溃或被终止，子进程会作为孤儿继续运行。`KillOnParentExit` 允许你在进程启动时声明，当父进程退出时子进程也应该被终止。

这个功能以平台特定的方式存在过（Windows 上的 job objects，Linux 上的 prctl），但需要 p/invoke 或第三方库才能在 .NET 中使用。现在它是 `ProcessStartInfo` 上的一等公民属性。

## 基于 SafeProcessHandle 的 API

新的轻量级 API 表面是围绕 `SafeProcessHandle` 而不是完整的 `Process` 类构建的。完整的 `Process` 类携带大量状态，难以裁剪 — `SafeProcessHandle` 路径对于需要最小化输出大小的应用程序（WASM、原生 AOT）更加友好。

## 对句柄继承的完全控制

此次更新还添加了对子进程继承哪些句柄以及如何重定向标准句柄的精细控制。以前你可以重定向 stdin/stdout/stderr，但无法在 OS 层面精确指定要继承哪些句柄。新 API 暴露了这种控制。

## 为何重要

`Process` 类用于工具、构建系统、测试运行器以及任何调用其他可执行文件的应用程序。旧的 API 表面可以追溯到 .NET Framework，已经显示出老化的迹象。这不是破坏性变更 — 旧 API 仍然有效 — 但新代码应该优先使用新表面。

对于裁剪的应用程序或 AOT 编译场景，`SafeProcessHandle` 路径特别受欢迎。旧的 `Process` 类带来了大量反射繁重的代码，使得裁剪变得复杂。

原文链接：[Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
