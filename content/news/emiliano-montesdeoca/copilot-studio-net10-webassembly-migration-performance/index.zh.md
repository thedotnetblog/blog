---
title: "Copilot Studio 如何迁移到 .NET 10 WebAssembly 并提速 20%"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 WASM 的改进不仅仅适用于新项目。以下是 Copilot Studio 从 .NET 8 升级后测量到的结果：自动指纹识别、默认启用 WasmStripILAfterAOT 以及真实的执行性能数据。"
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Copilot Studio 团队做了所有 Blazor WASM 开发者都好奇的事情：他们实际上将一个生产应用程序从 .NET 8 升级到了 .NET 10 并测量了结果。这篇文章分享了具体数字，这很罕见也非常有用。

## 升级过程很无聊（这是好事）

更新目标框架、刷新包引用、修复破坏性更改。就这样。.NET 10 构建现在已在生产环境中运行。迁移本身并不是有趣的部分——.NET 10 中的变化才是。

## 自动资源指纹识别

以前，部署 WASM 应用意味着需要编写自定义脚本来用 SHA256 哈希重命名已发布的资源以进行缓存清除。Copilot Studio 有一个 PowerShell 脚本做的正是这件事——重命名文件、将 `integrity` 属性注入 JavaScript 加载器、手动管理一切。

在 .NET 10 中，所有这些都是内置的。已发布的资源会自动添加指纹，直接从 `dotnet.js` 导入，并在无需手动干预的情况下进行完整性验证。团队删除了重命名脚本。

范围上的小变化，复杂性的显著降低。

## WasmStripILAfterAOT 现在默认启用

在 .NET 8 中，从 AOT 编译的程序集中删除 IL 是选择性的。在 .NET 10 中这是默认行为。AOT 编译后，原始 IL 字节码从输出中删除——运行时不需要它，保留它会无故膨胀包大小。

Copilot Studio 使用了一种特定的优化：它同时提供 JIT 引擎（快速启动）和 AOT 引擎（最大稳态性能），并行加载两者，并在准备好后从 JIT 切换到 AOT。它还会对两个引擎之间相同的文件进行去重。

新的 IL 剥离行为意味着 AOT 程序集不再与其 JIT 对应项逐位匹配，因此去重的文件更少：
- .NET 8：59 个共享文件
- .NET 10：22 个共享文件

净结果：AOT 引擎的包大小增加了约 15%。在快速 LAN 上 AOT 下载慢约 6%，在 4G 上慢约 17%。但这一切都在应用程序已经可交互后在后台发生。

## 性能数字

这是重要的部分：

- 首次调用时 **快约 20%**（冷路径）
- 后续调用时 **快约 5%**（热路径）

改进在"大型机器人"中最为明显——AOT 编译代码主导的大型复杂代理。对于更简单的工作流，收益较小。

## 如果您仍在使用 .NET 8

迁移过程真的很简单：更新 `<TargetFramework>`、刷新包引用、删除任何自定义指纹识别脚本，您将自动从 `WasmStripILAfterAOT` 中受益。如果您正在 AOT 编译，预期会有类似的性能提升。

文章中的一个注意事项：如果您在 `WebWorker` 中加载 .NET WASM 运行时，请在初始化时设置 `dotnetSidecar = true`。

原文：[Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
