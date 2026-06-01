---
title: "The Handoff Pattern: When One Agent Isn't Enough"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework's Handoff orchestration pattern lets agents decide who handles the next turn — without losing conversation context or breaking topology rules."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

At some point every multi-agent system outgrows a simple router. The first sign is usually when a specialist agent needs to ask a follow-up question, or realizes mid-turn that another agent should continue. A fixed pipeline breaks there. A one-shot router breaks there.

That's exactly the problem the Handoff orchestration pattern in Microsoft Agent Framework is designed for.

## How Handoff Works

The developer declares a graph: here are the agents, here are the edges between them. The framework does the rest — it synthesizes a handoff tool per outbound edge and injects it into each agent. When an agent decides to pass control, it calls the tool. The framework enforces the topology.

Three things make this different from just having agents call each other:

1. **One shared transcript** — the receiving agent sees the full conversation history. No starting from scratch.
2. **Topology enforcement** — an agent can only hand off to declared targets. You catch routing bugs at authoring time, not in production.
3. **Natural termination** — when the active agent finishes its turn without calling a handoff tool, the workflow yields to the user. No polling, no explicit exit conditions.

## A Minimal Example

In .NET, building a handoff workflow looks like this:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage can send to either specialist. Both specialists can send back to triage. The graph is acyclic-friendly but supports back-edges when you need them ("I need more info" → back to research).

## When to Use Handoff (and When Not To)

Handoff is a good fit when:

- **Ownership can change mid-conversation** — an agent may realize it's the wrong specialist
- **Back-edges matter** — you might need to revisit an earlier step without restarting
- **Routing decisions are fuzzy** — the choice to hand off is contextual and better made by the model than typed predicates

It's *not* the right choice when:

- Your pipeline is fixed and sequential — use the `Sequential` workflow for that
- Each step is independent — agents sharing a transcript where only one of them needed it is just noise
- You need strict processing guarantees — the non-determinism of model-driven routing isn't what you want

## Back-Edges and Human-in-the-Loop

One of the more interesting shapes Handoff enables is genuine back-edges. An agent can decide "I don't have enough information" and route back to a research step, not with a hardcoded loop, but because the model decides it's the right call.

Human-in-the-loop interactions also compose naturally. When a specialist needs user input, the workflow yields back to the user via the default turn loop, collects the response, and resumes with full context. The agent never lost the conversation.

## Wrapping Up

Handoff is one of those patterns that sounds simple but enables a lot once you internalize it: decentralized routing, shared context, enforced topology, natural termination. It's the right next step when your agents start saying "actually, someone else should handle this."

Read the full walkthrough in the original post: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
