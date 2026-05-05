---
title: "GPT-5.5 Is Here and It's Coming to Azure Foundry — What .NET Developers Need to Know"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 is generally available in Microsoft Foundry. Here's the progression from GPT-5 to 5.5, what's actually improved, and how to start using it in your agents today."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

Microsoft just announced that [GPT-5.5 is generally available in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). If you've been building agents on Azure, this is the update you've been waiting for.

Let me break down what actually changed and why it matters for developers building on this stack.

## The GPT-5 progression

It helps to understand the arc. This isn't just a version bump:

- **GPT-5**: unified reasoning and speed into a single system
- **GPT-5.4**: stronger multi-step reasoning, early agentic capabilities for enterprise use
- **GPT-5.5**: deeper long-context reasoning, more reliable agentic execution, improved computer-use accuracy, better token efficiency

Each step has been deliberately aimed at production agentic workloads. GPT-5.5 continues that arc with a specific focus on sustained, high-stakes professional workflows — not just one-shot queries.

## What's actually different

**Improved agentic coding**: GPT-5.5 holds context across large codebases, can diagnose architectural-level failures, and anticipates downstream testing requirements. That last point is interesting — the model reasons about *what else* a fix affects before making a move. Less back-and-forth to get to a working result.

**Token efficiency**: Higher-quality outputs with fewer tokens and fewer retries. This translates directly to lower cost and latency for production deployments. If you're running agents at scale, this compounds fast.

**Long-context analysis**: Handles extensive documents, codebases, and multi-session histories without losing the thread. For agentic workflows that maintain large working state, this matters.

There's also a **GPT-5.5 Pro** variant for the most demanding enterprise workloads — deeper reasoning, higher cost.

## Pricing

| Model | Input ($/M tokens) | Cached Input | Output ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

GPT-5.5 is priced at the same input rate as GPT-5 but the token efficiency improvements mean you're actually paying less per useful output. Worth running a benchmark on your specific workload before committing.

## Why Foundry matters here

Access to a frontier model is just the starting point. What matters for .NET developers is how you operationalize it.

Foundry Agent Service lets you define agents in YAML or wire them up with Microsoft Agent Framework, GitHub Copilot SDK, LangGraph, or OpenAI Agents SDK — and run them as isolated hosted agents with:
- A persistent filesystem
- A distinct Microsoft Entra identity
- Scale-to-zero pricing

One command to deploy. No infrastructure to manage. Your agents get GPT-5.5 as the model underneath.

## Getting started

If you're already using Azure AI Foundry, GPT-5.5 shows up as a new model option. Point your client at it and you're done:

```csharp
// C# — just update the model name
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "You are a helpful assistant.", name: "MyAgent");
```

If you haven't tried Foundry yet, [ai.azure.com](https://ai.azure.com/) is where to start. The model catalog has a direct link to try GPT-5.5.

## Wrapping up

GPT-5.5 is a real step forward for production agentic workloads. The combination of better long-context handling, improved agentic execution, and token efficiency makes it worth evaluating for anything you're running at scale.

The frontier is moving fast. Keep building.

See the [full announcement](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) for the complete feature breakdown and enterprise details.
