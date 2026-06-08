---
title: "Agent Harness, Hosted Agents, and CodeAct: This Is the Agent Framework Update I Would Focus On"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "The Build 2026 Agent Framework announcement is packed, but the most important threads are the harness model, Foundry hosted agents, and CodeAct for reducing orchestration overhead."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

The big Agent Framework Build announcement covers a lot, but three themes stand out to me immediately:

- **the harness becoming a more first-class runtime story**
- **Foundry hosted agents providing a production path**
- **CodeAct reducing multi-step orchestration overhead**

Those are the parts I would keep my eyes on.

## The harness is becoming the real center of gravity

The source post describes the harness as “**the layer where model reasoning meets real execution**.”

That is the right description, and it is also the reason I think this part matters more than many individual feature bullets.

The moment an agent needs:

- file access
- shell execution
- planning modes
- todos
- session memory
- approval workflows

you are no longer talking about a prompt plus a model.

You are talking about runtime behavior.

That is where frameworks either become useful or become toys.

And Microsoft Agent Framework is clearly trying to become more useful in exactly that layer.

## Hosted agents are where the local-to-production story gets real

I also think the hosted agents piece is one of the most strategically important parts of the announcement.

The source post explicitly says it is “**the easiest way to give that agent a production home**.”

That phrase matters because most agent frameworks are still much stronger at local experimentation than at operational deployment.

If Foundry hosted agents can make it materially easier to move from local development into:

- scaling
- observability
- managed identity
- session handling
- versioning

then that closes one of the biggest gaps in the current agent ecosystem.

That is a meaningful improvement.

## CodeAct is the most exciting technical idea in the update

If I had to pick the most interesting technical concept in the post, I would probably choose **CodeAct**.

The problem it is trying to solve is very real: too many multi-step agent workflows are expensive because the orchestration loop itself burns too many model turns.

So when the source post shows a result like:

- **52.4%** faster
- **63.9%** fewer tokens

that gets my attention immediately.

Now, of course, those are benchmark-style numbers tied to a representative workload, not a universal law. But the broader idea is still compelling.

If the model can collapse a tool-calling chain into a more efficient execution shape, that can change the economics of agent systems quite a bit.

## What I think developers should actually take from this update

The important lesson is not “look how many features shipped.”

The lesson is that the framework is strengthening in the places real applications need most:

- runtime shell
- deployment path
- execution efficiency
- built-in operational patterns

That is the sort of maturity signal I care about much more than another superficial AI feature checklist.

## My take

This update matters because it is not just adding more surface area.

It is strengthening the runtime and deployment story around agents in ways that should matter for real applications, especially for teams that want to move from local experiments to systems they can actually run and maintain.

That is where the framework becomes more compelling.

And if I were following this release closely, the harness, hosted agents, and CodeAct are absolutely where I would spend most of my attention.

Original post: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)