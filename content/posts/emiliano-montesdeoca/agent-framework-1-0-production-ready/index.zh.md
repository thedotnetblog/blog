---
title: "Microsoft Agent Framework 正式发布 1.0 — 这些才是 .NET 开发者真正需要关注的"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0 已具备生产环境就绪能力，拥有稳定的 API、多代理编排以及所有主流 AI 提供商的连接器。以下是作为 .NET 开发者你需要了解的内容。"
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *本文为自动翻译。如需查看原文，请[点击此处]({{< ref "agent-framework-1-0-production-ready.md" >}})。*

如果你一直在关注 Agent Framework 从早期 Semantic Kernel 和 AutoGen 时代走来的历程，这次的消息意义重大。Microsoft Agent Framework 刚刚[发布了 1.0 版本](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) — 生产就绪、API 稳定、长期支持承诺。它同时支持 .NET 和 Python，并且真正可以承载实际工作负载。

让我跳过公告的噪音，专注于你用 .NET 构建 AI 驱动应用时真正重要的内容。

## 简短版本

Agent Framework 1.0 将之前的 Semantic Kernel 和 AutoGen 统一为一个开源 SDK。一个代理抽象。一个编排引擎。多个 AI 提供商。如果你之前一直在 Semantic Kernel（企业模式）和 AutoGen（研究级多代理工作流）之间来回切换，现在可以停了。这就是那个唯一的 SDK。

## 入门简单得几乎不公平

这是一个在 .NET 中运行的代理：

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

就这些。几行代码，你就有了一个在 Azure Foundry 上运行的 AI 代理。Python 的等效代码同样简洁。随着需求增长，逐步添加函数工具、多轮对话和流式输出 — API 表面会平稳地扩展，不会变得奇怪。

## 多代理编排 — 这才是真正的核心

单个代理对演示来说够了，但生产场景通常需要协调。Agent Framework 1.0 附带了经过实战考验的编排模式，直接来自 Microsoft Research 和 AutoGen：

- **顺序执行** — 代理按顺序处理（写手 → 审核 → 编辑）
- **并发执行** — 并行分发给多个代理，汇聚结果
- **移交** — 一个代理根据意图委托给另一个代理
- **群组聊天** — 多个代理讨论并收敛到一个解决方案
- **Magentic-One** — 来自 MSR 的研究级多代理模式

所有这些都支持流式处理、检查点、人机回路审批以及暂停/恢复。检查点部分至关重要 — 长时间运行的工作流在进程重启后依然可以恢复。对于我们这些用 Azure Functions 构建过持久工作流的 .NET 开发者来说，这感觉很熟悉。

## 最重要的功能

以下是我认为值得了解的要点：

**中间件钩子。** 你知道 ASP.NET Core 有中间件管道吗？同样的概念，但用于代理执行。拦截每个阶段 — 添加内容安全、日志记录、合规策略 — 而无需触碰代理的提示词。这就是让代理达到企业级标准的方式。

**可插拔内存。** 对话历史、持久键值状态、基于向量的检索。选择你的后端：Foundry Agent Service、Mem0、Redis、Neo4j，或者自己实现。内存是将无状态的 LLM 调用变成真正能记住上下文的代理的关键。

**声明式 YAML 代理。** 在版本控制的 YAML 文件中定义代理的指令、工具、内存和编排拓扑。通过单个 API 调用加载和运行。这对于想要在不重新部署代码的情况下迭代代理行为的团队来说是颠覆性的。

**A2A 和 MCP 支持。** MCP（Model Context Protocol）让代理能够动态发现和调用外部工具。A2A（Agent-to-Agent 协议）实现跨运行时协作 — 你的 .NET 代理可以与其他框架中运行的代理进行协调。A2A 1.0 支持即将推出。

## 值得关注的预览功能

1.0 中有些功能以预览形式发布 — 功能可用但 API 可能会演进：

- **DevUI** — 一个基于浏览器的本地调试器，用于实时可视化代理执行、消息流和工具调用。可以把它想象成 Application Insights，但用于代理推理。
- **GitHub Copilot SDK 和 Claude Code SDK** — 直接从编排代码中使用 Copilot 或 Claude 作为代理工具。在同一工作流中将编程代理与其他代理组合在一起。
- **Agent Harness** — 一个可定制的本地运行时，为代理提供对 shell、文件系统和消息循环的访问。可以理解为编码代理和自动化模式。
- **Skills** — 可复用的领域能力包，为代理提供开箱即用的结构化能力。

## 从 Semantic Kernel 或 AutoGen 迁移

如果你有现有的 Semantic Kernel 或 AutoGen 代码，有专门的迁移助手可以分析你的代码并生成逐步迁移计划。[Semantic Kernel 迁移指南](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel)和 [AutoGen 迁移指南](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen)会引导你完成所有步骤。

如果你一直在使用 RC 包，升级到 1.0 只需更改版本号。

## 总结

Agent Framework 1.0 是企业团队一直在等待的生产里程碑。稳定的 API、多提供商支持、真正能在大规模下运行的编排模式，以及从 Semantic Kernel 和 AutoGen 的迁移路径。

该框架已[在 GitHub 上完全开源](https://github.com/microsoft/agent-framework)，你今天就可以通过 `dotnet add package Microsoft.Agents.AI` 开始使用。查看[快速入门指南](https://learn.microsoft.com/en-us/agent-framework/get-started/)和[示例](https://github.com/microsoft/agent-framework)来动手实践。

如果你一直在等待"可以安全用于生产"的信号 — 就是现在。
