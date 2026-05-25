---
title: ".NET 11 Preview 4: 模板 MCP 服务器、Runtime-Async 库、进程 API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 已发布。重点内容：SDK 中的 MCP 服务器模板、使用 runtime-async 编译的运行时库、用于移动端的 dotnet watch，以及进程 API 的重大扩展。"
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 已发布。每次 .NET 主要预览版的发布都会在运行时、SDK、库、ASP.NET Core、MAUI、C# 和 Entity Framework 中添加大量条目。与其重复完整列表，这里是让我眼前一亮的内容。

## MCP 服务器模板进入 .NET SDK

最有趣的条目：SDK 中现在包含了 MCP 服务器项目模板。这意味着 `dotnet new mcp-server`（或最终名称的命令）开箱即用。对于在 .NET 中构建 MCP 工具的开发者，这大大减少了启动摩擦。MCP 在平台工具链中的集成标志着生态系统的发展方向。

## 使用 Runtime-Async 编译的运行时库

运行时本身现在使用 runtime-async 功能编译其标准库。这是一个影响性能的内部更改——运行时中的 async 状态机变得更加高效。这里的意义不在于用户可见的 API 更改，而在于 runtime-async 已足够成熟，可以用于 BCL 本身，这是关于该功能成熟度的有力信号。

## JIT 优化和硬件内置函数

Preview 4 继续 JIT 工作。硬件内置函数和代码生成改进在这里发布——详细信息在运行时发布说明中。这类更改通常会在不修改代码的情况下提升密集计算循环的吞吐量。

## 进程 API 扩展

Preview 4 中 `System.Diagnostics.Process` 有重大更新：

- `Process.RunAndCaptureTextAsync` — 启动进程、捕获 stdout/stderr、等待退出，一次调用完成，无死锁风险
- `KillOnParentExit` — 父子进程之间的轻量级生命周期耦合
- 基于 `SafeProcessHandle` 的 API，对 trimmer 更友好

如果你曾经编写过样板代码来捕获进程输出而不引起死锁（同时异步读取 stdout *和* stderr），`RunAndCaptureTextAsync` 就是你一直缺少的 API。

## 用于 Android 和 iOS 的 dotnet watch

`dotnet watch` 现在支持 .NET MAUI Android 和 iOS 项目的设备选择。无需在构建循环中手动管理设备连接，即可更快地在移动端迭代。

## 基于 Span 的压缩 API

新的基于 span 的 Deflate、ZLib 和 GZip 编码器/解码器 API 加入库中。处理压缩数据时减少分配——如果你在进行高吞吐量数据处理，这一点很有意义。

## 试用

[下载 .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — 这是预览版，尚未准备好用于生产，但值得在项目中运行以在 RC 周期之前尽早发现问题。

原始文章：[.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
