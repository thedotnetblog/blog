---
title: "A2A v1 发布：Microsoft Agent Framework for .NET 中的跨平台代理通信"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "A2A 协议 v1.0 已发布，Microsoft Agent Framework .NET 包已更新——用于跨提供商连接和公开 AI 代理的稳定互操作性标准。"
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[A2A v1 发布：Microsoft Agent Framework for .NET 中的跨平台代理通信](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — A2A 协议刚刚达到 v1.0，.NET 的 A2A Agent（客户端）和 A2A Hosting（服务端）包均已更新。

## A2A v1 的实质

A2A 是一个面向 AI 代理的开放互操作协议，由来自 AWS、Cisco、Google、IBM Research、Microsoft、Salesforce、SAP 和 ServiceNow 的代表组成的技术指导委员会支持。v1 标签意味着这现在是一个稳定的、可用于生产的标准。实现它的 SDK 和 Agent Framework 包仍处于预览阶段，但协议本身已锁定。

v1 在 v0.3 基础上增加了多租户支持、用于密码学身份的已签名 Agent Cards、改进的安全流程和 Web 对齐架构。

## 连接远程 A2A 代理

远程 A2A 代理在代码中只是一个 `AIAgent` — 相同的 `RunAsync`、相同的流式传输、相同的会话处理：

```csharp
// 通过 well-known URI 发现
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// 直接配置
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// 流式传输同样适用
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## 将代理公开为 A2A 端点

您已构建的任何 `AIAgent` — 无论是在 Microsoft Foundry、Azure OpenAI、OpenAI、Anthropic 还是 AWS Bedrock 上 — 都可以在 ASP.NET Core 中用两行代码公开为 A2A 端点：

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

代理卡片会自动在 `/.well-known/agent-card.json` 处提供。

## 实际意义

稳定的 v1 协议意味着您可以将 .NET 代理与用 Python、Java 或任何其他语言构建的代理连接，而无需担心破坏性更改。已签名 Agent Cards 中的密码学身份也为代理间的信任验证提供了基础。

有关完整的更改日志和从 v0.3 的迁移说明，请参阅[完整文章](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/)。
