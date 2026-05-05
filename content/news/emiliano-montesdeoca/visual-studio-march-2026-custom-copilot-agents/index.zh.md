---
title: "Visual Studio 3月更新允许构建自定义Copilot代理 — find_symbol是一大亮点"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026年3月更新带来了自定义Copilot代理、可复用的代理技能、语言感知的find_symbol工具、以及从Test Explorer进行的Copilot性能分析。"
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *本文为自动翻译。查看原始版本，请[点击这里]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}})。*

Visual Studio刚刚获得了最重要的Copilot更新。Mark Downie [发布了3月版本](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/)，标题是自定义代理——但说实话，`find_symbol`工具可能才是最能改变你工作流的功能。

## 仓库中的自定义Copilot代理

想让Copilot遵循你团队的编码标准？自定义代理定义为`.github/agents/`中的`.agent.md`文件。每个代理都有完整的工作区感知、代码理解、工具、首选模型和MCP连接访问权限。

## 代理技能：可复用的指令包

技能从仓库的`.github/skills/`或个人资料的`~/.copilot/skills/`自动加载。

## find_symbol：语言感知导航

新的`find_symbol`工具为Copilot的代理模式提供了基于语言服务的符号导航。代理不再搜索文本，而是可以找到符号的所有引用并访问类型信息和作用域。

对于.NET开发者来说这是巨大改进——拥有深层类型层次结构的C#代码库受益匪浅。

## 用Copilot分析测试性能

Test Explorer上下文菜单中新增了**Profile with Copilot**。Profiling Agent自动运行测试并分析性能。

## 实时调试中的Perf Tips

性能优化现在在调试过程中进行。Visual Studio内联显示执行时间。看到慢的行？点击Perf Tip向Copilot请求优化建议。

## 从Solution Explorer修复NuGet漏洞

当检测到NuGet包漏洞时，Solution Explorer中直接显示**Fix with GitHub Copilot**链接。

## 总结

自定义代理和技能是标题，但`find_symbol`是隐藏的亮点——它从根本上改变了Copilot重构.NET代码时的准确性。下载[Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/)来体验所有新功能。
