---
title: "Azure Functions MCP 扩展正在变得越来越实用"
date: 2026-06-26
author: "Emiliano Montesdeoca"
description: "Azure Functions MCP 扩展的最新更新加入了 resources、prompts、MCP Apps、更强的身份验证选项，以及更好的 .NET builder 体验。更大的故事是，Azure 上的 serverless MCP 正在真正变得适合生产。"
tags:
  - Azure Functions
  - MCP
  - .NET
  - Azure
  - Serverless
---

*本文已自动翻译。要查看原文，请[点击此处]({{< ref "index.md" >}})。*

Azure Functions MCP 扩展早就已经不再停留在“看，你可以暴露一个工具”这个阶段了。

这次最新更新把这一点讲得很清楚。

到了现在，故事已经广泛得多了：

- 工具
- 资源
- 提示词
- MCP Apps
- 内置身份验证
- 更好的 .NET 配置 API

这也改变了我看待这个平台的方式。

## 这个扩展正在从预览新鲜感成熟为真正的构建材料

早期的 MCP 公告主要是在让协议可用。虽然有用，但还是比较原始。

现在，这个扩展正在成长为更完整的东西，适合面向生产的团队：

- 更丰富的基础类型支持
- 更好的身份验证支持
- 结构化内容和 schema
- 通过 builder 更自然的 .NET 配置
- 通往 Foundry 集成的更清晰路径

这才是你想看到的。

## 为什么 Azure Functions 非常适合 MCP

我仍然认为 Azure Functions 是远程 MCP 服务器最实用的托管选择之一。

你可以得到：

- 无服务器托管
- 可扩展执行
- 熟悉的 trigger 和 binding 模式
- 内置的身份集成
- 与 API 风格工具面良好的匹配

而随着 MCP 扩展的加入，“我有一个有用的函数”和“我有一个 agent 可以发现的工具面”之间的差距仍在缩小。

## .NET fluent builder 的故事尤其好

.NET 方面的新增内容之所以吸引我，是因为它们延续了代码中更具表达力配置的趋势。

能够以 fluent 方式声明元数据、schema、UI 绑定以及更丰富的 MCP 行为，会让这个扩展感觉更像一等公民的开发工具，而不是一个薄薄的协议外壳。

这正是我想要的方向。

## 我的看法

这里真正的故事不是某一个单独功能。真正的变化在于，Azure Functions MCP 扩展正在成为一个现实可行的平台选择，适合那些想在 Azure 上托管 MCP 能力但又不想从零开始构建一切的团队。

而且对 .NET 开发者来说，体验还在持续变好。

原始文章：[Azure Functions MCP Extension: What’s New at Build 2026](https://devblogs.microsoft.com/azure-sdk/functions-mcp-updates-build-2026/)