---
title: "azd + GitHub Copilot：AI 驱动的项目设置和智能错误修复"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI 现已与 GitHub Copilot 集成，可以生成项目基础架构并修复部署错误——无需离开终端。"
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *本文为自动翻译。如需阅读英文原文，请[点击这里]({{< ref "index.md" >}})。*

你是否有过这样的经历：想把现有应用部署到 Azure，却盯着空白的 `azure.yaml` 发呆，想不起来 Express API 到底该用 Container Apps 还是 App Service？这种时刻即将成为历史。

Azure Developer CLI（`azd`）现已与 GitHub Copilot 以两种实用的方式集成：`azd init` 时的 AI 辅助项目脚手架，以及部署失败时的智能错误排查。两项功能都完全在终端内运行——正是我想要的方式。

## 在 azd init 中使用 Copilot 设置

运行 `azd init` 时，现在会出现"Set up with GitHub Copilot (Preview)"选项。选择它，Copilot 会分析你的代码库，根据实际代码生成 `azure.yaml`、基础架构模板和 Bicep 模块。

```
azd init
# 选择："Set up with GitHub Copilot (Preview)"
```

前提条件：

- **azd 1.23.11 或更高版本** — 用 `azd version` 检查，或用 `azd update` 更新
- **有效的 GitHub Copilot 订阅**（Individual、Business 或 Enterprise）
- **GitHub CLI（`gh`）** — 必要时 `azd` 会提示登录

我觉得真正实用的是它能双向工作。从零开始构建？Copilot 从一开始就帮你配置正确的 Azure 服务。有现有应用想部署？把 Copilot 指向它，无需重构代码即可生成配置。

### 它实际做什么

假设你有一个 Node.js Express API，依赖 PostgreSQL。不必手动在 Container Apps 和 App Service 之间抉择，也不必从零编写 Bicep，Copilot 检测到你的技术栈后会生成：

- 包含正确 `language`、`host` 和 `build` 设置的 `azure.yaml`
- Azure Container Apps 的 Bicep 模块
- Azure Database for PostgreSQL 的 Bicep 模块

并在做任何更改前运行预检——验证 git 工作目录是否干净，提前请求 MCP 服务器工具的授权。一切都在你知情的情况下进行。

## Copilot 驱动的错误排查

部署错误无可避免。缺少参数、权限问题、SKU 可用性问题——而错误信息很少告诉你真正需要知道的那一件事：*如何修复*。

没有 Copilot 时的循环：复制错误 → 搜索文档 → 读三篇不相关的 Stack Overflow 回答 → 运行一些 `az` CLI 命令 → 重试并祈祷。有了集成在 `azd` 中的 Copilot，这个循环消失了。任何 `azd` 命令失败时，它会立即提供四个选项：

- **Explain** — 用通俗语言解释出了什么问题
- **Guidance** — 逐步修复指导
- **Diagnose and Guide** — 完整分析 + Copilot 应用修复（经你批准）+ 可选重试
- **Skip** — 自己处理

关键在于：Copilot 已经了解你的项目、失败的命令和错误详情。它的建议针对*你的具体情况*，而非泛泛的文档。

### 设置默认行为

如果你总是选择同一个选项，可以跳过交互式提示：

```
azd config set copilot.errorHandling.category troubleshoot
```

可选值：`explain`、`guidance`、`troubleshoot`、`fix`、`skip`。还可以启用自动修复和重试：

```
azd config set copilot.errorHandling.fix allow
```

随时重置为交互模式：

```
azd config unset copilot.errorHandling.category
```

## 总结

这正是真正有价值的 Copilot 集成。运行 `azd update` 获取最新版本，在下一个项目中试试 `azd init`。

阅读[原文公告](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/)。
