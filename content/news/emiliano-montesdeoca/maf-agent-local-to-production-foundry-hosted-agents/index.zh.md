---
title: "您的本地 MAF 代理刚刚在生产环境中找到了家"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents 为您的 Microsoft Agent Framework 代理提供身份、扩展、会话持久性和无需额外配置的可观测性。以下是实际效果。"
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

让代理在本地运行是有趣的部分。棘手的部分是之后的一切：不用抓狂地部署它、管理会话、设置身份、连接可观测性。通常这意味着大量自定义基础设施粘合代码。

Foundry Hosted Agents 刚刚为 Microsoft Agent Framework (MAF) 用户消除了大部分粘合代码。

## Foundry Hosted Agents 实际做什么

当您将 MAF 代理部署到 Foundry Hosted Agents 时，平台会处理一个令人惊讶的长列表，这些都是您否则需要自己构建的：

- **缩放到零** — 代理空闲时不花费任何费用，并自动重新启动
- **每个会话的 VM 隔离沙箱** — 每个用户会话都有自己的沙箱，具有在缩减事件中存活的文件系统持久性
- **内置 Entra ID** — 每个代理都获得自己的身份，可以调用 Foundry 模型、Toolbox 和 Azure 服务，而无需将密钥嵌入镜像
- **版本化部署** — 每个部署都是不可变的快照，支持蓝/绿和金丝雀发布
- **零配置可观测性** — `APPLICATIONINSIGHTS_CONNECTION_STRING` 在运行时注入，使 MAF 的 OpenTelemetry 跟踪自动流入 App Insights

最后一点确实很好。无需额外配置，无需额外设置。跟踪就这样出现了。

## 代码差异很小

这是我最欣赏这个集成的地方。您无需重写代理。只需包装它：

**.NET 中：**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Python 中：**

```python
server = ResponsesHostServer(agent)
server.run()
```

就这样。您在本地测试的相同逻辑就是在生产中运行的。平台用会话管理、身份和扩展基础设施来包装它。

## 两种协议，一个代理

Hosted Agents 支持两种端点样式：

- **Responses** (`/responses`) — 兼容 OpenAI，管理会话历史和流式传输。聊天形式代理的良好默认选择。
- **Invocations** (`/invocations`) — 您定义请求/响应模式。适合非对话工作流。

如果您构建的东西看起来像对话，从 Responses 开始。如果您构建的是接受结构化输入并返回结构化输出的 API 形式代理，Invocations 给您灵活性。

## 使用 `azd` 的部署流程

当您使用 MAF 代理运行 `azd up` 时：

1. 可选地创建 Foundry 项目并部署模型
2. 打包代码并将镜像推送到 Azure Container Registry
3. 从 ACR 镜像供应计算
4. 为代理分配专用 Entra ID
5. 公开稳定端点 (`https://{project_endpoint}/agents/{agent_name}`)
6. 从此处理其他一切

会话持续最多 30 天。空闲计算在 15 分钟后取消供应，并在下一个请求时透明地恢复。从代理的角度来看，没有任何变化。

## 总结

"在本地运行"和"在生产中运行"之间的距离历来对 AI 代理来说既漫长又痛苦。Foundry Hosted Agents + MAF 显著缩小了这一差距。如果您已经有了用 Agent Framework 构建的本地代理，今天就值得一试。

团队说 GA 即将到来 — 目前处于预览阶段。查看 [MAF Hosted Agent 集成文档](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) 和 [.NET 示例](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) 开始使用。

原始文章: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
