---
title: "Microsoft Agent Framework Part 3: From Tools to Workflows — The Building Blocks Click Into Place"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Part 3 of the .NET AI building blocks series covers the Microsoft Agent Framework — from single agents with tools to multi-agent workflows with memory. Here's what actually matters."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

If you've been following the Building Blocks for AI in .NET series, you know Part 1 gave us `IChatClient` (the universal model interface) and Part 2 gave us `Microsoft.Extensions.VectorData` (semantic search and RAG). Both are foundational, both are useful on their own. But this is where everything starts to connect.

Part 3 is about the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — and honestly, it's the piece I've been waiting to see land in .NET. 1.0 shipped in April. The API is stable. It's time to actually build agents.

## What an Agent Actually Is (vs. a Chatbot)

Before diving into code, let's get this distinction out of the way. A chatbot receives input, calls a model, returns output. Simple loop.

An agent has *autonomy*. It can reason about a task, decide which tools to use, call those tools, evaluate results, and decide what to do next — all without you writing explicit step-by-step logic for every scenario. You give it tools and instructions, and it figures out the orchestration.

Think of it this way: `IChatClient` is like having a conversation. An agent is like handing someone a task list.

## Your First Agent in 10 Lines

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

The `.AsAIAgent()` extension method is the bridge. Same pattern as `.AsIChatClient()` from MEAI — it wraps a provider's SDK in a stable abstraction. It works with Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry, or local models via Foundry Local or Ollama.

Streaming works too:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Giving the Agent Tools

This is where agents stop being fancy chatbots. Tools are functions the model can decide to call based on what the user asks. No routing logic needed on your part — the model figures it out.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Two things to notice here. First, `AIFunctionFactory` is from MEAI — same tool factory you'd use with a plain `IChatClient`. If you've already defined tools for your chat scenarios, they work here too.

Second, those `Description` attributes matter a lot. They're how the model understands what a tool does and when to use it. Treat them as documentation for your AI, not for humans.

## Sessions: Conversations That Actually Remember

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Without a session, each `RunAsync` call is stateless. With a session, the agent knows which joke you're referring to. The `AgentSession` preserves conversation history between turns.

For production stateless services, sessions serialize cleanly:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... store it somewhere ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

This is critical if your agent runs in a serverless or horizontally-scaled environment.

## AIContextProvider: Memory That Persists Across Sessions

Sessions preserve conversation history *within* a session. But what about knowing things about a user across sessions? `AIContextProvider` handles that.

It has two hooks:
- **`ProvideAIContextAsync`** — runs *before* each interaction, injects context into the agent (e.g., "The user's name is Emiliano")
- **`StoreAIContextAsync`** — runs *after* each interaction, lets you learn from what was said and persist it

The pattern is elegant: you can stack multiple providers — one for user preferences, one for recent interactions, one that queries your VectorData store for relevant documents. That last one is exactly the RAG pattern from Part 2, now running automatically as part of every agent call.

## Multi-Agent Workflows

This is where the framework earns its name. The Agent Framework includes a graph-based workflow system where executors (agents, functions, whatever) connect via edges.

Some patterns that are natively supported:

- **Sequential**: Agent A's output feeds Agent B
- **Concurrent (fan-out/fan-in)**: Dispatch to multiple agents in parallel, collect results
- **Conditional routing**: Route work to different agents based on output
- **Writer-critic loops**: One agent writes, another evaluates, loop until approved
- **Sub-workflows**: Compose workflows hierarchically

A writer-critic example:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Clean, readable, and the condition-based routing means you don't write loop logic yourself. The framework drives the iteration.

## Human-in-the-Loop

Not everything should run fully autonomously. For sensitive operations — database writes, financial transactions, sending communications — you want a human to approve before the agent executes.

The framework has built-in support for this via `FunctionApprovalRequestContent` and `FunctionApprovalResponseContent`. The agent proposes the tool call, your application code presents it to the user, and the response determines whether execution proceeds.

This is the right way to think about agents in enterprise settings: not fully autonomous, but *autonomy-with-guardrails*.

## The Full Picture

If you step back for a second:

- **MEAI** gives you a universal interface to any model
- **VectorData** gives your agents access to your organization's knowledge through semantic search
- **Agent Framework** orchestrates everything — it uses `IChatClient` under the hood, composes with context providers, and coordinates through workflows

Each piece was designed to compose with the others. You can use any of them independently, but together they form a coherent stack for building AI applications in .NET.

Check out the [original post by Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) and the [Agent Framework GitHub repo](https://github.com/microsoft/agent-framework/tree/main/dotnet) for the full samples.

## Wrapping Up

The Microsoft Agent Framework Part 3 post closes the loop on the building blocks series (with MCP coming next). For .NET developers who want to build AI agents — not just chatbots, actual agents that use tools, remember things, and coordinate — this is your path forward.

The 1.0 stable release means you can build on this in production. The composition with MEAI and VectorData means you're not learning a parallel set of abstractions. It all fits together.

If you've been waiting to jump into agent development in .NET, the timing is right now.
