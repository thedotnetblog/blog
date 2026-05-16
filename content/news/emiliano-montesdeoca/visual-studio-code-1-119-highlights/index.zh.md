---
title: "VS Code 1.119：代理会话的 OpenTelemetry、浏览器集成和安全性"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119（2026 年 5 月）为代理会话添加了 OpenTelemetry 追踪、浏览器标签页共享、信任和安全改进以及 1.119.1 安全补丁。"
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) 于 2026 年 5 月 6 日发布（随后发布了 1.119.1 安全补丁）。此版本专注于代理可观察性、浏览器交互和减少中断。

## 代理会话的 OpenTelemetry 追踪

对于在生产环境中运行代理或调试代理工作流的人来说，这是最重要的功能。通过两个设置启用：

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

追踪遵循 GenAI 语义约定。每个代理请求创建一个 `invoke_agent` 根 span，带有嵌套子 span：`chat`、`execute_tool` 和 `execute_hook`。Token 使用情况按请求报告——包括缓存读取和缓存创建计数。

适用于本地代理、Copilot CLI 后台代理和 Claude 代理。任何兼容 OTLP 的后端都接受追踪——[独立 Aspire 仪表板](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone)非常适合本地开发。

## 代理现在可以访问浏览器标签页

代理可以请求访问内置浏览器标签页——但不是自动的。你必须通过上下文选择器、拖放或建议的上下文明确共享标签页。浏览器中有一个共享按钮用于撤销访问。当代理尝试打开与已打开（未共享）标签页相同域的新标签页时，VS Code 会建议重用现有标签页。

## Token 使用优化

实验性轻量级模型现在管理代理任务列表，释放主模型用于这项日常工作。减少不需要完整推理能力的任务的 token 使用。

## 信任和安全

减少中断：VS Code 1.119 减少了来自代理的网络访问和向临时文件夹写入的提示。1.119.1 补丁解决了特定的安全问题——如果还没有更新，值得升级。

## 快速切换到 Markdown 预览

小但实用：现在可以快速将当前编辑器切换到 Markdown 预览，无需导航。

## VS Code Agents（Insiders 预览版）

重新设计的代理会话界面——新的仓库选择器（本地/仓库/远程）、子会话改进、Web 和移动端改进、进度动画——在 Insiders 上的 [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents) 中可用。

完整更新日志：[code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119)。
