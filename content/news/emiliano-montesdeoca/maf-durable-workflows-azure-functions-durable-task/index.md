---
title: "Durable Workflows in Microsoft Agent Framework: From In-Memory to Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAF's workflow programming model now supports durable execution backed by Durable Task — here's how to build composable agent workflows that survive process restarts and scale across Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

One of the pain points with early AI agent workflows: they're fragile. A long-running multi-step workflow tied to a single process means process restart = lost state. For simple demos this is fine. For production workloads it isn't.

Microsoft Agent Framework's workflow programming model now supports **durable execution**, backed by the Durable Task framework, with Azure Functions hosting. Here's how the programming model works and why the durability story matters.

## The Core Building Blocks

**Executors** are the fundamental unit of work. Each one is typed — it takes a specific input and produces a specific output:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // look up the order, return it
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflows** wire executors into directed graphs using a fluent builder. The framework handles execution, data flow between steps, and error propagation.

You can model:
- Sequential chains (step A → step B → step C)
- Parallel fan-out/fan-in (run agents A, B, C in parallel, aggregate results)
- Conditional branching
- Human-in-the-loop approvals (pause workflow, wait for external signal)

## The In-Memory Runner for Local Dev

Getting started is fast:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

The core package includes a lightweight in-process runner. No external dependencies, no database, no Azure resources. Works great for local development and unit testing.

## Adding Durability with Durable Task

When a workflow needs to survive process restarts — because it's long-running, because it has human-in-the-loop steps, because it fans out across many parallel agent calls — the in-memory runner isn't enough.

MAF's Durable Task integration stores workflow state in Azure Storage. If the process restarts, the workflow resumes from where it left off. The programming model stays the same; you just swap the runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

The same executors, the same workflow graph — backed by durable state.

## Azure Functions Hosting

The third layer is Azure Functions hosting. Your workflow becomes a Function app: trigger the workflow via an HTTP endpoint, and the durable runtime handles scaling, state, and reliability.

This means a multi-agent workflow with parallel calls, conditional branches, and human approvals can scale across a serverless Functions environment without custom state management.

## Why This Matters

The combination is significant for real AI systems:

- **Parallel agent calls** — fan out to multiple specialized agents simultaneously without blocking, aggregate results when all complete
- **Long-running processes** — workflows that involve human approval or external events can pause and resume across hours or days
- **Scale** — Azure Functions scales the execution horizontally; the Durable Task framework handles coordinating the parallel state

If you're building MAF workflows beyond simple local demos, this is the path to production-grade execution.

Original post: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
