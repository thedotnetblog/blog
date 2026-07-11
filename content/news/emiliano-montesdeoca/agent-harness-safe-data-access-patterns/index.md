---
title: 'The Real Agent UX Win Is Safe Autonomy, Not Maximum Autonomy'
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: 'File access, approvals, and memory design are the practical triad for trustworthy agent behavior in production.'
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Original source: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

This is one of the more useful agent engineering posts this year because it refuses the common trap of demo-first autonomy. Instead, it focuses on how agents should operate around real user data and real consequences.

The three building blocks highlighted here are exactly right.

File access gives agents useful grounding in user-owned data.

Approval gating prevents silent execution of consequential actions.

Durable memory avoids repetitive interactions without sacrificing control.

Most teams overinvest in tool breadth and underinvest in permission semantics. That is backward. An agent with ten tools and weak approval boundaries is less valuable than an agent with three tools and predictable control points.

The best practical pattern in this article is layered approval strategy:

Always require approval for high-impact tools like trading or destructive operations.

Auto-approve low-risk reads to preserve flow.

Use scoped standing approvals for repetitive trusted actions within a session.

This creates a healthy risk gradient. Users are not interrupted for harmless reads, but they are still in the loop when consequences become expensive or irreversible.

I also like the explicit split between file memory and Foundry memory. Teams should stop trying to force one memory model to solve every problem. Coarse, explicit file artifacts are excellent for user-visible state like reports and watchlists. Fact-level memory extraction is better for preferences and conversational context. Mixing both gives better outcomes than trying to pretend either one is sufficient.

My opinionated take: the future of agent quality will be measured less by clever prompts and more by safety ergonomics. If your approval prompts are noisy, users click through blindly. If your memory boundaries are unclear, users stop trusting the assistant. If your data access defaults are permissive, security teams will shut the project down.

For .NET and Python teams adopting this pattern, the key move is to treat policy callbacks and approval rules as core business logic, versioned and tested like any other critical code. Do not leave them as ad-hoc lambdas buried in samples.

Agent systems that earn trust are not the ones that do the most. They are the ones that do exactly what users intended, no more, no less, with clear interruption points when risk rises.

That is the difference between an impressive demo and software people are willing to delegate real work to.
