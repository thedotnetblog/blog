---
title: "您的 AI 代理有一个身份问题（这是解决它的模板）"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Curity 和 Microsoft 的新 azd 模板展示了如何构建使用具有精细作用域的短期 OAuth 令牌的 AI 代理——这样代理永远无法看到它们不应该看到的数据。"
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

在每个 AI 代理项目中都有这样一个时刻：演示完美运行，代理解释自然语言，调用正确的 API，返回正确的数据。然后你开始思考真实用户。

什么能阻止一个用户的代理会话看到另一个用户的数据？如果代理通过提示注入被欺骗会怎样？如果它以意外的方式调用工具会怎样？

这些不是边缘情况。这些是你需要在发布之前做出的设计决策。

Curity 和 Microsoft 的新 `azd` 模板为您提供了针对这个问题的可工作参考。

## 核心问题：身份验证 ≠ 授权

大多数代理示例都很好地处理了用户身份验证。它们对授权处理得很差。知道用户是*谁*并不能告诉你他们应该看到*什么数据*。

传统客户端应用程序进行可预测的 API 调用。AI 代理是不确定性的——它解释自然语言并决定调用什么。它可以很有创意。它也可能出错。如果通过提示注入被操纵，你需要不依赖于 AI 良好行为的规则。

这个模板演示的解决方案：**为每一跳携带正确信息的短期令牌**。

## 令牌链如何工作

该模板使用带有令牌交换的 OAuth 2.0 访问令牌，在每个步骤缩小权限。用户令牌在到达 MCP 服务器之前会被交换两次：

1. **第一次交换** — 缩小作用域并将不透明令牌转换为 JWT
2. **第二次交换** — 添加代理身份和 MCP 服务器跳的新受众

MCP 服务器令牌的样子：

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

`customer_id` 由授权服务器嵌入令牌中，而不是作为代理控制的参数传递。API 检查令牌，而不是代理的指令。

这意味着：即使有人欺骗代理尝试获取另一个客户的数据，令牌也不会授权它。

## 模板部署什么

用几个 `azd` 命令，您将获得：

- Microsoft Foundry 上的后端代理（C#、Microsoft A2A 和 MCP SDK）
- 公开示例投资组合 API 的 MCP 服务器
- Curity Identity Server 作为授权服务器，以及用于身份验证的 Entra ID
- 处理令牌交换和审计日志的外部和内部 API 网关
- 所有 Azure 基础设施的 Bicep：Container Apps、VNet、ACR、Azure AI Foundry、Key Vault、Azure SQL Database、存储

整个模式是可检查和可定制的。

## 值得借鉴的设计原则

即使您不使用 Curity，该模式也是可转移的：**代理永远不应该拥有永久 API 访问权限**。每个操作都应使用仅具有该特定调用所需最小作用域的短期令牌，为特定代理身份颁发，携带 API 进行授权决策所需的声明。

这能抵御创意代理、错误和提示注入，而"只要确保代理不做坏事"永远做不到这一点。

## 总结

AI 代理的安全模式在整个行业中仍在研究中。这个模板是我见过的最完整的参考实现之一——它涵盖了实际的授权流程，而不仅仅是身份验证。

原始文章：[Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
