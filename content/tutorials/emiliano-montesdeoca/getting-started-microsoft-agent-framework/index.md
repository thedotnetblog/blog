---
title: "Getting Started with Microsoft Agent Framework"
date: 2026-03-05
author: "Emiliano Montesdeoca"
description: "Build your first multi-agent workflow with the Microsoft Agent Framework — orchestrate specialized agents, connect tools, and keep the control flow understandable in .NET."
tags:
  - agent-framework
  - ai
  - dotnet
  - multi-agent
  - azure
---

The Microsoft Agent Framework (MAF) is a .NET SDK for building multi-agent AI systems. It is useful when a single prompt is no longer the cleanest way to solve the problem. Once your application needs routing, specialization, tool access, or approval gates, one giant instruction block tends to become hard to reason about and even harder to maintain.

The better pattern is to split responsibilities. One agent can classify the request, another can answer it, and a third can handle retrieval, summarization, or action-taking. MAF gives you the structure to do that without turning your application into a pile of ad hoc prompt strings.

This tutorial walks through a small support-style workflow with two agents: a **triage agent** that routes requests and a **resolver agent** that handles them. The example is deliberately simple, but the same shape scales to internal helpdesks, document assistants, customer workflows, or any other app where the first step is not the same as the last step.

## Why multi-agent orchestration matters

A single agent is easy to start with, but it often becomes crowded as the app grows. The prompt has to recognize intent, choose a response style, decide when to use tools, avoid risky operations, and format the output. That is a lot of behavior to pack into one place.

Multi-agent orchestration makes the responsibilities explicit. The triage agent can stay narrow and only classify the request. The resolver agent can focus on the actual answer. If you later add a summarizer, a retrieval agent, or a policy reviewer, each one can be tuned independently instead of forcing one prompt to do everything.

That separation also helps when something goes wrong. If the triage step is bad, you fix classification. If the answer is weak, you tune the resolver. If the handoff is wrong, you inspect the orchestration. Each failure has a smaller surface area.

## Prerequisites

- .NET 8 or later
- NuGet package `Microsoft.AI.Agents.Core`
- NuGet package `Microsoft.SemanticKernel`
- An Azure OpenAI or OpenAI API key
- A console app you can run locally while you experiment

## Step 1: Install packages

Start with a fresh console app and add the packages the framework expects:

```bash
dotnet new console -n AgentDemo
cd AgentDemo
dotnet add package Microsoft.AI.Agents.Core
dotnet add package Microsoft.SemanticKernel
```

At this point you have the minimum pieces needed to define agents, connect them to a model, and orchestrate a conversation. Keeping the first project small is useful because it lets you verify the model configuration before you add more moving parts.

## Step 2: Create a shared kernel

MAF agents usually share a kernel so they can use the same model configuration and any shared services you attach later. That keeps the setup in one place and avoids copy-pasting connection code into every agent. In real applications, the shared kernel is also where you would centralize logging, retrieval, tool registration, or other services that need to be available across agents.

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
        Return the category clearly and then hand off to the appropriate agent.
        """,
    Kernel = kernel
};
```

The important idea here is not the specific API call, but the boundary. The kernel owns the model connection and the agents own the behavior. That makes the code easier to scale when the number of agents grows from two to five or from five to twenty.

## Step 3: Define the triage agent

The triage agent should do one thing well: decide what kind of request is coming in. Keep the instructions narrow and concrete. If you ask the agent to classify, summarize, rewrite, and answer all at once, the classification step will usually get less reliable.

The example above uses a very small taxonomy on purpose. In a real system you might expand it to include categories like `billing`, `technical`, `account`, `sales`, or `escalation`. The key is that the labels should be stable and easy for the rest of the system to consume.

When you define this kind of router agent, treat it like infrastructure. The more precise the contract, the easier it is to evolve the rest of the workflow without breaking routing behavior.

## Step 4: Define the resolver agent

Once the request has been routed, the resolver agent can focus on the actual answer. This agent does not need to re-decide the category. It should assume that the request is already classified and spend its effort on clarity, completeness, and tone.

```csharp
var resolverAgent = new ChatCompletionAgent
{
    Name = "ResolverAgent",
    Instructions = """
        You are a support resolver. You receive pre-triaged requests and provide
        clear, concise answers. If the answer depends on missing information,
        explain what you still need. Always end with one confirmation question.
        """,
    Kernel = kernel
};
```

This is where specialization pays off. The triage agent can stay terse and deterministic. The resolver can be more conversational and user-facing. If you later want a third agent for technical diagnostics or policy review, you can add it without rewriting the triage prompt.

## Step 5: Compose the workflow

For this demo, the orchestration layer is a small group chat. That keeps the moving parts visible without forcing you to write custom routing code on day one.

```csharp
var chat = new AgentGroupChat(triageAgent, resolverAgent)
{
    ExecutionSettings = new AgentGroupChatSettings
    {
        TerminationStrategy = new ApprovalTerminationStrategy()
    }
};
```

The chat object owns the turn-taking. The model decides which agent should speak next, and the termination strategy decides when the conversation should stop. In a larger app, you can replace this with a more explicit handoff graph or a policy that matches your production workflow. The point is that the app still owns the control flow even when the model helps with the routing.

## Step 6: Run a realistic request

Once the agents are configured, send a real user message through the workflow:

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

In this example, the triage agent should identify the request as billing-related and the resolver agent should handle the user-facing response. Watching the turn-by-turn output is useful because it shows you exactly where the workflow is succeeding and where it still needs tuning.

## What is happening under the hood

The request enters the shared kernel, but it does not go straight to a single generic answer. First, the triage agent interprets the intent and reduces the problem to a smaller decision. Then the resolver agent uses that decision to produce the actual response.

That sequence is the main design win. You are not asking one model call to perform every job at once. Instead, you are letting each agent do a smaller job well. The result is easier to debug, easier to evolve, and usually easier to trust.

This approach also gives you room to add guardrails. For example, a future version might require approval before the resolver performs a sensitive action, or it might route certain requests to a retrieval agent that queries a knowledge base before responding.

## How to keep the design maintainable

- Keep each agent narrowly scoped so its instructions stay readable and testable.
- Give tools to the agent that actually needs them instead of loading every capability into the router.
- Log the intermediate turns so you can see which agent made each decision.
- Make termination explicit so the workflow does not continue longer than necessary.

These are small habits, but they matter once the system starts handling real users. A clear agent boundary today is much cheaper to maintain than a clever prompt that slowly turns into a dependency graph you cannot explain.

## What to explore next

The most natural follow-up is tool calling. Once the agents can route requests reliably, you can give a specialist agent access to APIs, databases, or file systems through Semantic Kernel plugins. That turns the system from a text-only demo into something that can actually perform useful work.

After that, look at human-in-the-loop patterns, AG-UI integration for streaming events to a frontend, and observability with Azure Monitor or OpenTelemetry. The [MAF documentation](https://devblogs.microsoft.com/agent-framework/) and GitHub samples cover those production patterns in more depth, including state persistence and long-running workflows.
