---
title: "Visual Studio 2026 四月更新：云代理、自定义代理和调试器代理"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026 四月更新 (18.5) 添加了云代理集成、用户级自定义代理、C++ 工具正式发布以及调试器代理——该代理会根据实际运行时行为验证修复。"
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[Visual Studio 2026 四月更新 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) 包含云代理集成、用户级自定义代理、C++ 工具正式发布以及全新的调试器代理。

## 云代理：将工作委托给远程 Copilot 会话

在聊天窗口的代理选择器中选择 **Cloud**，可以将任务移交给 Copilot 远程编码代理。你描述工作内容，代理在你的仓库中创建 GitHub issue，完成后打开 PR。你会收到带有"查看 PR"/"在浏览器中打开"按钮的通知——在你继续编码期间，甚至在 IDE 关闭时都能运行。

## 自定义代理现在跟随你

存储在 `%USERPROFILE%/.github/agents/` 的自定义代理不再绑定到单个仓库——它们会跨项目跟随你。存储路径可通过"工具 > 选项 > GitHub > Copilot > Chat"配置。代理选择器中的 `+` 按钮允许直接创建新代理。它们获得与仓库范围代理相同的功能：工作区感知、工具、模型选择和 MCP 连接。

内置代理：Agent、Ask、Copilot CLI、Debugger、Modernize、Profiler。

## C++ 代码编辑工具正式发布

`get_symbol_call_hierarchy` 和 `get_symbol_class_hierarchy` 这两个工具现在默认开启。它们为 Copilot 提供 C++ 代码库的语言导航，覆盖继承层次结构和函数调用链。通过 Copilot Chat 中的工具图标启用。与支持工具调用的模型配合效果最佳。

## 调试器代理：修复根据实际运行时行为进行验证

从 GitHub 或 Azure DevOps issue（或自然语言描述）开始，切换到调试器模式，代理会：

1. 创建最小复现器
2. 生成故障假设
3. 用跟踪点和条件断点对应用程序进行检测
4. 运行真实的调试会话
5. 分析实时遥测数据
6. 提出精确的修复方案

整个过程中你保持在循环中——这是交互式的，不是完全自主的。

## IntelliSense 优先级修复

VS 现在在 IntelliSense 列表激活时抑制 Copilot 补全。一次只显示一个建议。这是一个常见的摩擦点，现在默认启用。

完整发布说明和下载请访问 [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/)。
