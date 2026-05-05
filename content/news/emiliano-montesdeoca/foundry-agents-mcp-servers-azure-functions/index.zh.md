---
title: "将 Azure Functions 上的 MCP 服务器连接到 Foundry 代理 — 方法在这里"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "一次构建 MCP 服务器，部署到 Azure Functions，通过适当的身份验证连接到 Microsoft Foundry 代理。你的工具随处可用 — VS Code、Cursor，现在还有企业级 AI 代理。"
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}})。*

这是我喜欢 MCP 生态系统的一点：你只需构建一次服务器，它就能在任何地方运行。VS Code、Visual Studio、Cursor、ChatGPT — 每个 MCP 客户端都能发现并使用你的工具。现在，微软正在向这个列表中添加另一个消费者：Foundry 代理。

Azure SDK 团队的 Lily Ma [发布了一份实用指南](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)，介绍如何将部署在 Azure Functions 上的 MCP 服务器与 Microsoft Foundry 代理连接。如果你已经有了 MCP 服务器，这纯粹是增值 — 无需重新构建。

## 为什么这种组合有意义

Azure Functions 为托管 MCP 服务器提供了可扩展的基础设施、内置身份验证和无服务器计费。Microsoft Foundry 为你提供能够推理、规划和行动的 AI 代理。连接两者意味着你的自定义工具 — 查询数据库、调用业务 API、运行验证逻辑 — 成为企业 AI 代理可以自主发现和使用的能力。

关键点：你的 MCP 服务器保持不变。你只是将 Foundry 添加为另一个消费者。在 VS Code 设置中运行的相同工具现在为你的团队或客户交互的 AI 代理提供动力。

## 身份验证选项

这是文章真正增值的地方。根据你的场景提供四种身份验证方法：

| 方法 | 使用场景 |
|------|---------|
| **基于密钥**（默认） | 开发或没有 Entra 身份验证的服务器 |
| **Microsoft Entra** | 使用托管标识的生产环境 |
| **OAuth 身份透传** | 每个用户单独认证的生产环境 |
| **无身份验证** | 开发/测试或仅公开数据 |

对于生产环境，使用代理身份的 Microsoft Entra 是推荐路径。OAuth 身份透传适用于用户上下文重要的场景 — 代理提示用户登录，每个请求携带用户自己的令牌。

## 设置方法

大致流程：

1. **将 MCP 服务器部署到 Azure Functions** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)、Python、TypeScript 和 Java 的示例均可用
2. **在你的函数应用上启用内置 MCP 身份验证**
3. **获取你的端点 URL** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **在 Foundry 中添加 MCP 服务器作为工具** — 在门户中导航到你的代理，添加新的 MCP 工具，提供端点和凭据

然后在 Agent Builder 操场中发送一个会触发你某个工具的提示来测试它。

## 我的看法

这里的组合性故事变得非常强大。用 .NET（或 Python、TypeScript、Java）构建一次 MCP 服务器，部署到 Azure Functions，每个 MCP 兼容的客户端都能使用它 — 编码工具、聊天应用，现在还有企业 AI 代理。这是一个真正有效的"一次编写，到处使用"模式。

特别是对于 .NET 开发者，[Azure Functions MCP 扩展](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)让这一切变得简单明了。你将工具定义为 Azure Functions，部署，就拥有了一个具备 Azure Functions 所提供的所有安全性和可扩展性的生产级 MCP 服务器。

## 总结

如果你有在 Azure Functions 上运行的 MCP 工具，将它们连接到 Foundry 代理是一个快速的胜利 — 你的自定义工具变成了企业 AI 能力，具有适当的身份验证，且服务器本身无需代码更改。

阅读[完整指南](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/)了解每种身份验证方法的分步说明，查看[详细文档](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry)了解生产环境配置。
