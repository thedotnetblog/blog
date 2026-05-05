---
title: "Azure MCP Server 2.0 正式发布——自托管智能云自动化来了"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 稳定版发布，支持自托管远程部署、57 个 Azure 服务中的 276 个工具，以及企业级安全性——这是 .NET 开发者构建智能工作流需要了解的内容。"
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

*本文为自动翻译。如需查看原文，请[点击这里]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}})。*

如果你最近一直在用 MCP 和 Azure 构建东西，你可能已经知道本地体验非常好。接入一个 MCP 服务器，让你的 AI 智能体与 Azure 资源对话，然后继续工作。但一旦你需要在团队中共享这个设置？那就会变得复杂。

不再是这样了。Azure MCP Server [刚刚发布 2.0 稳定版](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)，而主打功能正是企业团队一直在要求的：**自托管远程 MCP 服务器支持**。

## 什么是 Azure MCP Server？

快速回顾一下。Azure MCP Server 实现了 [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) 规范，并将 Azure 功能暴露为结构化、可发现的工具，AI 智能体可以调用。把它看作是你的智能体和 Azure 之间的标准化桥梁——配置、部署、监控、诊断，都通过一个统一的接口。

这些数字说明一切：**跨越 57 个 Azure 服务的 276 个 MCP 工具**。这是真正的覆盖范围。

## 重大突破：自托管远程部署

关键是这样的。在你的本地机器上运行 MCP 对于开发和实验来说没问题。但在真实的团队场景中，你需要：

- 开发者和内部智能体系统的共享访问
- 集中化配置（租户上下文、订阅默认值、遥测）
- 企业网络和策略边界
- 与 CI/CD 流程的集成

Azure MCP Server 2.0 解决了所有这些问题。你可以将其部署为一个集中管理的内部服务，具有基于 HTTP 的传输、适当的身份验证和一致的治理。

对于身份验证，你有两个不错的选择：

1. **托管标识**——在 [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) 旁边运行时
2. **代表流 (OBO 流)**——OpenID Connect 委托，使用已登录用户的上下文调用 Azure API

对于我们 .NET 开发者来说，OBO 流特别有趣。这意味着你的智能工作流可以使用用户的实际权限运行，而不是某个过度特权的服务账户。最小权限原则，内置其中。

## 安全加固

这不仅仅是一个功能发布——它也是一个安全发布。2.0 版本添加了：

- 更强的端点验证
- 针对面向查询工具中注入模式的保护
- 更严格的开发环境隔离控制

如果你要将 MCP 暴露为共享服务，这些保障措施很重要。非常重要。

## 你可以在哪里使用它？

客户端兼容性范围很广。Azure MCP Server 2.0 可与以下配合使用：

- **IDE**：VS Code、Visual Studio、IntelliJ、Eclipse、Cursor
- **CLI 智能体**：GitHub Copilot CLI、Claude Code
- **独立版**：用于简单设置的本地服务器
- **自托管远程**：2.0 的新星

此外，还有针对 Azure 美国政府版和由 21Vianet 运营的 Azure 的主权云支持，这对于受管制的部署至关重要。

## 为什么这对 .NET 开发者很重要

如果你使用 .NET 构建智能应用——无论是使用 Semantic Kernel、Microsoft Agent Framework，还是你自己的编排——Azure MCP Server 2.0 让你能够以生产级的方式让你的智能体与 Azure 基础设施交互。没有自定义 REST 包装。没有服务特定的集成模式。只是 MCP。

结合几天前发布的 [MCP 应用流畅 API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)，.NET MCP 生态系统正在快速成熟。

## 开始使用

选择你的路径：

- **[GitHub 仓库](https://aka.ms/azmcp)**——源代码、文档，一切
- **[Docker 镜像](https://aka.ms/azmcp/download/docker)**——容器化部署
- **[VS Code 扩展](https://aka.ms/azmcp/download/vscode)**——IDE 集成
- **[自托管指南](https://aka.ms/azmcp/self-host)**——2.0 的旗舰功能

## 总结

Azure MCP Server 2.0 正是那种在演示中看起来不起眼但在实践中改变一切的基础设施升级。具有适当身份验证、安全加固和主权云支持的自托管远程 MCP 意味着 MCP 已为在 Azure 上构建真实智能工作流的真实团队做好准备。如果你一直在等待"企业就绪"的信号——就是现在。
