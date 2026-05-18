---
title: "Aspire 13.3：Kubernetes 支持、浏览器日志和 Aspireify 技能"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "13.2 发布五周后，Aspire 13.3 带来 45 项新功能，包括一流的 AKS 部署、AI 辅助的入门技能、浏览器日志捕获和结构化命令结果。"
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

五周对于一个版本来说并不长，但 Aspire 13.3 让人感觉不是这样。主要内容非常重要：使用 Helm 进行 Kubernetes 和 AKS 一流部署、名为 Aspireify 的代理辅助入门技能、直接在仪表板中捕获浏览器日志，以及结构化命令结果。还包括 45 项新功能、134 项改进和 93 个错误修复。

让我们来看看亮点。

## Aspireify：代理辅助入门

将 Aspire 添加到现有项目听起来很简单——添加 AppHost，完成。实际上需要大量研究：哪些端口重要、哪些环境变量是真正的依赖项、哪些 Docker Compose 服务应该映射到 Aspire 集成。

新的 **Aspireify 技能** 正是为此为您的编码代理提供了引导工作流程。当 `aspire init` 创建骨架 AppHost 时，Aspireify 技能会帮助代理检查存储库、了解其已有的工作方式，并连接 AppHost 以适应应用程序——而不是反过来。

默认立场是"最小化对代码的更改"。如果您的应用程序已经读取 `DATABASE_URL`，代理会使用 `WithEnvironment()` 进行映射，而不是要求您重写配置。如果端口是硬编码的，该技能会告诉代理何时保留它。

这正是那种能真正节省时间而不是生成更多审查工作的 AI 工具。

## 一流的 Kubernetes 和 AKS 部署

这在愿望清单上已经有一段时间了。Aspire 13.3 提供了**使用 Helm 的 Kubernetes 和 AKS 一流部署支持**。您现在可以直接从 Aspire 工具中将 AKS 指定为部署目标。

对于已经在 AKS 上运行生产工作负载的团队，这弥补了一个重要缺口。您的 Aspire 应用模型现在有了从本地开发到 Kubernetes 的清晰路径，无需手动编写 Helm 图表。

## 仪表板中的浏览器日志

这是那些在调试前端问题之前看起来很小的功能之一。

新的 `WithBrowserLogs()` API 将跟踪的浏览器资源附加到任何支持端点的资源。Aspire 使用私有 CDP 管道启动 Chromium，并将控制台日志、网络请求和错误直接流式传输到资源的日志流中：

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost 同样支持：

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

控制台错误、失败的网络请求、客户端异常——所有这些都在您已经观察追踪和指标的同一仪表板中可见。不再需要为了基础内容切换到浏览器 DevTools。

## 结构化命令结果

资源命令获得了重大升级。到目前为止，命令返回成功/失败。现在它们返回结构化结果：流经模型、仪表板 UI、CLI 和 MCP 工具的文本、JSON 或 Markdown。

仪表板通过标题中的新通知中心将这一切联系在一起。命令结果以带时间戳的通知形式出现，带有 Markdown 渲染和"查看响应"操作。

这使资源命令真正可组合。集成现在可以公开一个返回有意义输出的命令——比如隧道 URL——而不仅仅是在某处更改状态。

## 结论

Aspire 13.3 仅凭 Kubernetes 支持就值得升级。浏览器日志和结构化命令结果感觉像是那种在日常开发工作流程中快速积累的生活质量改进。

完整发布说明：[What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
