---
title: "Azure DevOps MCP Server 登陆 Microsoft Foundry：这对你的 AI 代理意味着什么"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server 现已在 Microsoft Foundry 中可用。只需几次点击，即可将你的 AI 代理直接连接到 DevOps 工作流 — 工作项、仓库、管道。"
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP（Model Context Protocol）正在迎来它的高光时刻。如果你一直在关注 AI 代理生态系统，你可能已经注意到 MCP 服务器到处涌现 — 通过标准化协议赋予代理与外部工具和服务交互的能力。

现在 [Azure DevOps MCP Server 已在 Microsoft Foundry 中可用](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/)，这是那种让你思考实际可能性的集成之一。

## 这里到底发生了什么

Microsoft 已经发布了 Azure DevOps MCP Server 的[公开预览版](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — 那是 MCP 服务器本身。新的是 Foundry 集成。你现在可以直接从工具目录将 Azure DevOps MCP Server 添加到 Foundry 代理中。

对于还不熟悉 Foundry 的人：它是 Microsoft 用于大规模构建和管理 AI 驱动应用程序和代理的统一平台。模型访问、编排、评估、部署 — 全部在一个地方。

## 配置

配置出奇地简单：

1. 在你的 Foundry 代理中，进入 **Add Tools** > **Catalog**
2. 搜索 "Azure DevOps"
3. 选择 Azure DevOps MCP Server（preview）并点击 **Create**
4. 输入你的组织名称并连接

就这样。你的代理现在可以访问 Azure DevOps 工具了。

## 控制代理可以访问什么

这是我欣赏的部分：你不会被困在全有或全无的方式中。你可以指定哪些工具对代理可用。如果你只想让它读取工作项但不碰管道，可以这样配置。最小权限原则，应用到你的 AI 代理上。

这在企业场景中很重要，你不希望一个代理因为有人让它"帮忙发布"就意外触发部署管道。

## 为什么这对 .NET 团队很有趣

想想这在实践中能实现什么：

- **冲刺规划助手** — 可以拉取工作项、分析速度数据并建议冲刺容量的代理
- **代码审查机器人** — 因为能实际读取你的仓库和关联的工作项，所以理解你的 PR 上下文的代理
- **事件响应** — 可以创建工作项、查询最近的部署并将 bug 与最近的更改关联的代理
- **开发者入职** — "我应该做什么？"得到基于实际项目数据的真实回答

对于已经在 CI/CD 管道和项目管理中使用 Azure DevOps 的 .NET 团队来说，拥有一个能直接与这些系统交互的 AI 代理是迈向有用自动化的重要一步。

## 更大的 MCP 图景

这是更广泛趋势的一部分：MCP 服务器正在成为 AI 代理与外部世界交互的标准方式。我们在 GitHub、Azure DevOps、数据库、SaaS API 中都能看到它们 — 而 Foundry 正在成为所有这些连接汇聚的中心。

如果你在 .NET 生态系统中构建代理，MCP 值得关注。协议是标准化的，工具正在成熟，Foundry 集成使其无需手动配置服务器连接即可访问。

## 总结

Foundry 中的 Azure DevOps MCP Server 目前处于预览阶段，所以预计它会继续发展。但核心工作流是可靠的：连接、配置工具访问，让你的代理使用你的 DevOps 数据工作。如果你已经在 Foundry 生态系统中，只需几次点击就能开始。试试看你能构建什么工作流。

查看[完整公告](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/)获取完整的配置步骤和更多详情。
