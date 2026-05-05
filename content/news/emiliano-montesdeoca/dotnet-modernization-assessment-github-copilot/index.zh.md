---
title: "GitHub Copilot 的现代化评估是你还没用上的最好迁移工具"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "GitHub Copilot 的现代化扩展不仅仅建议代码更改 — 它生成完整的迁移评估，包含可操作的问题、Azure 目标比较和协作工作流。以下是评估文档为何是一切关键的原因。"
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}})。*

将传统 .NET Framework 应用迁移到现代 .NET 是那种每个人都知道应该做但没人想开始的任务。它从来不是简单的"更改目标框架"。而是消失的 API、不再存在的包、工作方式完全不同的托管模型，以及关于什么要容器化、什么要重写、什么要保持不变的无数小决策。

Jeffrey Fritz 刚刚发布了一篇 [GitHub Copilot 现代化评估的深入解析](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/)，说实话？这是我见过的 .NET 最好的迁移工具。不是因为代码生成 — 那现在已经是标配了。而是因为它生成的评估文档。

## 它不仅仅是代码建议引擎

VS Code 扩展遵循**评估 → 计划 → 执行**模型。评估阶段分析你的整个代码库，生成一份结构化文档，捕获一切：什么需要更改、需要配置哪些 Azure 资源、使用什么部署模型。下游的一切 — 基础设施即代码、容器化、部署清单 — 都源自评估发现的内容。

评估存储在项目的 `.github/modernize/assessment/` 下。每次运行产生一份独立的报告，因此你可以积累历史记录，并在修复问题时跟踪迁移态势的演变。

## 两种开始方式

**推荐评估** — 快捷路径。从策划好的领域（Java/.NET 升级、云就绪、安全）中选择，无需配置即可获得有意义的结果。非常适合初次了解应用的状态。

**自定义评估** — 定向路径。精确配置要分析的内容：目标计算（App Service、AKS、Container Apps）、目标操作系统、容器化分析。选择多个 Azure 目标来并排比较迁移方法。

那个比较视图真的很有用。一个应用在 App Service 上可能有 3 个必须解决的问题，在 AKS 上可能有 7 个。看到两者有助于在确定迁移路径之前做出托管决策。

## 问题分解是可操作的

每个问题都带有严重程度级别：

- **必须** — 必须修复，否则迁移失败
- **潜在** — 可能影响迁移，需要人工判断
- **可选** — 推荐的改进，不会阻止迁移

每个问题都链接到受影响的文件和行号，提供详细描述说明什么地方有问题以及为什么对目标平台重要，给出具体的修复步骤（不仅仅是"修复这个"），并包含官方文档链接。

你可以将单个问题分配给开发者，他们拥有行动所需的一切。这就是告诉你"有个问题"的工具和告诉你如何解决的工具之间的区别。

## 涵盖的升级路径

针对 .NET 具体来说：
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

每条升级路径都有检测规则，知道哪些 API 被移除、哪些模式没有直接等价物、哪些安全问题需要关注。

对于管理多个应用的团队，还有一个 CLI 支持多仓库批量评估 — 克隆所有仓库，全部评估，获取每个应用的报告加上汇总的组合视图。

## 我的看法

如果你坐拥传统 .NET Framework 应用（说实话，大多数企业团队都是这样），这就是*那个*应该开始使用的工具。仅评估文档就值得投入时间 — 它将模糊的"我们应该现代化"变成了一个具体的、有优先级的工作项列表，指明了前进的方向。

协作工作流也很聪明：导出评估、与团队分享、无需重新运行即可导入。决策者不是运行工具的人的架构评审？涵盖了。

## 总结

GitHub Copilot 的现代化评估将 .NET 迁移从一个可怕的、不明确的项目转变为一个结构化的、可跟踪的过程。从推荐评估开始了解你的现状，然后使用自定义评估来比较 Azure 目标并制定迁移计划。

阅读[完整演练](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/)并获取 [VS Code 扩展](https://aka.ms/ghcp-appmod/vscode-ext)在你自己的代码库上试试。
