---
title: "使用.NET可组合技术栈构建AI驱动的会议应用"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft构建了ConferencePulse——一个通过组合Microsoft.Extensions.AI、DataIngestion、VectorData、MCP和Agent Framework打造的实时会议Blazor应用。以下是各部分如何组合在一起的说明。"
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[使用.NET可组合技术栈构建AI驱动的会议应用](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft通过组合五个.NET扩展库，构建了ConferencePulse——一个用于实时会议演讲的Blazor Server应用。该应用在MVP Summit上投入使用。

## ConferencePulse的功能

ConferencePulse在实时演讲期间运行，提供以下功能：根据演讲内容AI生成的投票、通过RAG管道从实时知识库提取信息的观众问答、自动生成的洞察，以及由多个并发AI代理生成的演讲摘要。技术栈为.NET 10、Blazor Server、Aspire，分为五个项目：Web、Core、Ingestion、Agents、Mcp和AppHost。

## Microsoft.Extensions.AI：万物的统一抽象

`IChatClient`是统一的抽象层——配置一次，同一接口可用于Azure OpenAI、OpenAI、Anthropic或任何其他提供商。六行代码即可获得具备函数调用、OpenTelemetry追踪和日志中间件的完整配置客户端：

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

同一个`IChatClient`在后续数据摄取的增强步骤中被复用——无需为此创建单独的客户端。

## DataIngestion管道

演讲内容通过管道流转：`MarkdownReader` → `HeaderChunker`（500个token，50个token重叠）→ `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter`（Qdrant）。增强器使用同一个`IChatClient`在索引前生成摘要并提取关键词。观众问题、问答对和投票结果在演讲进行期间实时摄取——知识库在演讲过程中持续增长。

## VectorData：与提供商无关的搜索

无论底层存储是Qdrant还是Azure AI Search，`VectorStoreCollection.SearchAsync()`的工作方式相同。支持混合搜索（向量+全文检索）。观众问答的RAG管道查询该集合，获取相关文本块作为上下文传递给聊天客户端。

## MCP：作为工具的演讲内容

演讲内容通过MCP公开，任何兼容MCP的客户端都可以访问。服务器和客户端均已实现——服务器将演讲知识作为MCP工具公开，客户端允许在代理管道中调用这些工具。

## Agent Framework：并行多代理摘要

演讲摘要由三个并发运行的代理生成——`PollSummaryAgent`、`QuestionSummaryAgent`和`InsightSummaryAgent`——然后合并。这使用了Microsoft Agent Framework的群聊或并行执行模式。每个代理处理一个关注点，编排器合并各代理的输出。

## 设计原则

文章提出了一个值得铭记的观点：使用最简单的适用工具。简单生成任务使用直接的`IChatClient`调用；结构化数据提取使用工具/函数调用；只有在需要自主多步骤推理时才使用完整的代理。库的分层设计强制执行这一原则——你可以使用`Microsoft.Extensions.AI`而无需引入完整的Agent Framework。

查看[完整文章](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/)以获取完整的项目结构和源代码链接。
