---
title: "Getting Started with Microsoft Agent Framework"
date: 2025-01-15
author: "Emiliano Montesdeoca"
description: "Build your first multi-agent workflow with the Microsoft Agent Framework — orchestrate specialized agents, connect tools, and handle human-in-the-loop approvals in .NET."
tags:
  - agent-framework
  - ai
  - dotnet
  - multi-agent
  - azure
---

The Microsoft Agent Framework (MAF) is a .NET SDK for building multi-agent AI systems. Rather than a single "do everything" prompt, you compose specialized agents — each with their own tools and instructions — and let them hand off work to each other.

This tutorial walks you through building a simple two-agent system: a **triage agent** that routes requests and a **resolver agent** that handles them.

## Prerequisites

- .NET 8 or later
- NuGet: `Microsoft.AI.Agents.Core`
- An Azure OpenAI or OpenAI API key

## Step 1: Install packages

```bash
dotnet new console -n AgentDemo
cd AgentDemo
dotnet add package Microsoft.AI.Agents.Core
dotnet add package Microsoft.SemanticKernel
```

## Step 2: Define your first agent

Agents are defined with a name, instructions, and a set of tools (Semantic Kernel plugins):

```csharp
using Microsoft.AI.Agents.Core;
using Microsoft.SemanticKernel;

var kernel = Kernel.CreateBuilder()
    .AddAzureOpenAIChatCompletion(
        deploymentName: "gpt-4o",
        endpoint: Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!,
        apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!
    )
    .Build();

var triageAgent = new ChatCompletionAgent
{
    Name = "TriageAgent",
    Instructions = """
        You are a triage agent. Classify incoming requests as either:
        - 'billing' — questions about invoices, payments, or subscriptions
        - 'technical' — questions about bugs, features, or how the product works
        Then hand off to the appropriate agent.
        """,
    Kernel = kernel
};
```

## Step 3: Define the resolver agent

```csharp
var resolverAgent = new ChatCompletionAgent
{
    Name = "ResolverAgent",
    Instructions = """
        You are a support resolver. You receive pre-triaged requests and provide
        clear, concise answers. Always end with a confirmation question.
        """,
    Kernel = kernel
};
```

## Step 4: Set up handoff topology

MAF's `HandoffBuilder` lets you declare a routing graph between agents:

```csharp
var chat = new AgentGroupChat(triageAgent, resolverAgent)
{
    ExecutionSettings = new AgentGroupChatSettings
    {
        TerminationStrategy = new ApprovalTerminationStrategy()
    }
};
```

## Step 5: Run the workflow

```csharp
chat.AddChatMessage(new ChatMessageContent(
    AuthorRole.User,
    "My invoice from last month looks wrong — I was charged twice."
));

await foreach (var response in chat.InvokeAsync())
{
    Console.WriteLine($"[{response.AuthorName}]: {response.Content}");
}
```

MAF will call the triage agent first, which classifies the issue as "billing" and hands off to the resolver agent. You'll see each agent's turn in the output.

## What to explore next

- **Tool calling** — give agents access to APIs, databases, or file systems via SK plugins
- **Human-in-the-loop** — use `ApprovalTerminationStrategy` to pause for human confirmation before high-risk actions
- **AG-UI integration** — stream agent events to a frontend using the AG-UI protocol for real-time visibility
- **Observability** — connect to Azure Monitor or OpenTelemetry to trace agent decisions

The [MAF documentation](https://devblogs.microsoft.com/agent-framework/) and samples on GitHub cover production patterns including state persistence and long-running workflows.
