---
title: "从笔记本到生产：用两个命令将 AI 代理部署到 Microsoft Foundry"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI 现在有了 'azd ai agent' 命令，可以在几分钟内将你的 AI 代理从本地开发带到 Foundry 的生产端点。这是完整的工作流程。"
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

你知道"在我的机器上能跑"和"已部署并正在处理流量"之间的鸿沟吗？对于 AI 代理来说，这个鸿沟一直痛苦地大。你需要配置资源、部署模型、配置身份、设置监控 — 这些都是在任何人能实际调用你的代理之前要做的。

Azure Developer CLI 刚刚把这变成了[两个命令的事](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/)。

## 新的 `azd ai agent` 工作流

让我带你看看这实际是什么样子。你有一个 AI 代理项目 — 比如说一个酒店礼宾代理。它在本地运行正常。你想让它在 Microsoft Foundry 上运行。

```bash
azd ai agent init
azd up
```

就这样。两个命令。`azd ai agent init` 在你的仓库中生成基础设施即代码，`azd up` 在 Azure 上配置一切并发布你的代理。你会得到一个直接指向 Foundry 门户中你的代理的链接。

## 底层发生了什么

`init` 命令在你的仓库中生成真实的、可检查的 Bicep 模板：

- 一个 **Foundry Resource**（顶层容器）
- 一个 **Foundry Project**（你的代理所在的地方）
- **模型部署**配置（GPT-4o 等）
- 带有适当 RBAC 角色分配的**托管身份**
- 服务映射用的 `azure.yaml`
- 带有代理元数据和环境变量的 `agent.yaml`

关键是：这一切都是你的。它是仓库中的版本化 Bicep。你可以检查它、自定义它，并与你的代理代码一起提交。没有魔法黑盒。

## 开发内循环

我真正喜欢的是本地开发体验。当你在迭代代理逻辑时，不想每次改变提示词都重新部署：

```bash
azd ai agent run
```

这会在本地启动你的代理。配合 `azd ai agent invoke` 发送测试提示，你就有了一个紧密的反馈循环。编辑代码、重启、调用、重复。

`invoke` 命令的路由也很智能 — 当本地代理在运行时，它会自动指向本地。不在运行时，指向远程端点。

## 实时监控

这是说服我的功能。一旦你的代理部署完成：

```bash
azd ai agent monitor --follow
```

流经你的代理的每个请求和响应都会实时传输到你的终端。对于调试生产问题，这是无价之宝。不用挖 Log Analytics，不用等指标聚合 — 你看到的就是现在正在发生的事情。

## 完整的命令集

快速参考：

| 命令 | 功能 |
|------|------|
| `azd ai agent init` | 用 IaC 搭建 Foundry 代理项目 |
| `azd up` | 配置 Azure 资源并部署代理 |
| `azd ai agent invoke` | 向远程或本地代理发送提示 |
| `azd ai agent run` | 在本地运行代理用于开发 |
| `azd ai agent monitor` | 从已发布的代理流式传输实时日志 |
| `azd ai agent show` | 检查代理健康状态和状态 |
| `azd down` | 清理所有 Azure 资源 |

## 为什么这对 .NET 开发者重要

虽然公告中的示例是基于 Python 的，但基础设施的故事是语言无关的。你的 .NET 代理得到相同的 Bicep 脚手架、相同的托管身份设置、相同的监控管道。如果你已经在用 `azd` 部署 .NET Aspire 应用或 Azure 部署，这直接融入你现有的工作流。

AI 代理的部署鸿沟一直是生态系统中最大的摩擦点之一。从一个工作原型到一个具有适当身份、网络和监控的生产端点，不应该需要一周的 DevOps 工作。现在只需要两个命令和几分钟。

## 总结

`azd ai agent` 现在可用。如果你一直因为基础设施设置看起来工作量太大而推迟部署 AI 代理，试试看。查看[完整教程](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/)获取包括前端聊天应用集成在内的完整步骤。
