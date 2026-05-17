---
title: "Microsoft Agent Framework 第3部分：从工具到工作流 — 构建块完美契合"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: ".NET AI 构建块系列第3部分涵盖 Microsoft Agent Framework — 从带工具的单一代理到带内存的多代理工作流。这是真正重要的内容。"
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*本文已自动翻译。要查看原始版本，请[点击此处]({{< ref "index.md" >}})。*

如果你一直在关注 .NET AI 构建块系列，你知道第1部分给了我们 `IChatClient`（通用模型接口），第2部分给了我们 `Microsoft.Extensions.VectorData`（语义搜索和 RAG）。两者都是基础性的，单独使用都很有用。但这里是一切开始连接的地方。

第3部分关于 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — 说实话，这是我一直期待看到在 .NET 中落地的部分。1.0 在4月发布。API 稳定了。是时候真正构建代理了。

## 代理到底是什么（vs. 聊天机器人）

在深入代码之前，让我们厘清这个区别。聊天机器人接收输入，调用模型，返回输出。简单循环。

代理有*自主性*。它可以对任务进行推理，决定使用哪些工具，调用这些工具，评估结果，然后决定下一步做什么 — 所有这些都不需要你为每个场景编写明确的步骤逻辑。你给它工具和指令，它自己处理编排。

这样理解：`IChatClient` 就像进行对话。代理就像把任务清单委托给某人。

## 10行代码写出你的第一个代理

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

`.AsAIAgent()` 扩展方法是桥梁。与 MEAI 的 `.AsIChatClient()` 相同的模式 — 它将提供商的 SDK 包装在一个稳定的抽象中。适用于 Azure OpenAI、OpenAI、GitHub Models、Microsoft Foundry 或本地模型。

流式处理也可以：

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## 给代理提供工具

这里是代理不再只是高级聊天机器人的地方。工具是模型可以根据用户请求决定调用的函数。你不需要路由逻辑 — 模型自己搞清楚。

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

有两点需要注意。首先，`AIFunctionFactory` 来自 MEAI — 与普通 `IChatClient` 使用的工具工厂相同。如果你已经为聊天场景定义了工具，它们在这里也能用。

其次，`Description` 属性非常重要。这是模型理解工具用途以及何时使用它的方式。把它们当作给 AI 的文档，而不是给人类的。

## 会话：真正有记忆的对话

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

没有会话，每次 `RunAsync` 调用都是无状态的。有了会话，代理知道你指的是哪个笑话。`AgentSession` 在轮次之间保留对话历史。

对于生产中的无状态服务，会话可以干净地序列化：

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... 存储在某处 ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

如果你的代理在无服务器或水平扩展环境中运行，这非常关键。

## AIContextProvider：跨会话的持久记忆

会话在*会话内*保留对话历史。但是，跨会话了解用户的信息呢？`AIContextProvider` 处理这个问题。

它有两个钩子：
- **`ProvideAIContextAsync`** — 在每次交互*之前*运行，向代理注入上下文
- **`StoreAIContextAsync`** — 在每次交互*之后*运行，允许学习和持久化

这个模式很优雅：你可以堆叠多个提供者 — 一个用于用户偏好，一个用于最近的交互，一个查询 VectorData 存储以获取相关文档。最后一个正是第2部分的 RAG 模式，现在作为每次代理调用的一部分自动运行。

## 多代理工作流

这里是框架名副其实的地方。它包括一个基于图的工作流系统，其中执行器（代理、函数、任何东西）通过边连接。

一些原生支持的模式：

- **顺序**：代理A的输出流入代理B
- **并发（扇出/扇入）**：并行分发到多个代理，收集结果
- **条件路由**：根据输出将工作路由到不同代理
- **写作-批评循环**：一个代理写作，另一个评估，循环直到批准
- **子工作流**：层次化地组合工作流

写作-批评示例：

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

简洁、可读，基于条件的路由意味着你不需要自己编写循环逻辑。

## 人在回路中

并非所有事情都应该完全自主运行。对于敏感操作 — 数据库写入、金融交易、发送通信 — 你希望在代理执行之前有人类批准。

框架通过 `FunctionApprovalRequestContent` 和 `FunctionApprovalResponseContent` 内置支持此功能。代理提出工具调用，你的应用代码将其呈现给用户，响应决定是否继续执行。

这是在企业环境中思考代理的正确方式：不是完全自主，而是*带护栏的自主性*。

## 全貌

退一步看：

- **MEAI** 为你提供任何模型的通用接口
- **VectorData** 通过语义搜索让你的代理访问组织的知识
- **Agent Framework** 编排一切 — 内部使用 `IChatClient`，与上下文提供者组合，通过工作流协调

每个部分都被设计为与其他部分组合。查看 [Jeremy Likness 的原始帖子](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/)和 [Agent Framework GitHub 仓库](https://github.com/microsoft/agent-framework/tree/main/dotnet)获取完整示例。

## 总结

Microsoft Agent Framework 第3部分的帖子完成了构建块系列的闭环。对于想要构建 AI 代理的 .NET 开发者 — 不只是聊天机器人，而是真正使用工具、记忆事物、协调行动的代理 — 这是你的前进之路。

稳定的 1.0 版本意味着你可以在生产环境中构建这个。如果你一直在等待深入 .NET 代理开发，现在是时候了。
