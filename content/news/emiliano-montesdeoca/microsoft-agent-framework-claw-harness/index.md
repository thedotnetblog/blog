---
title: "Build your own claw and agent harness with Microsoft Agent Framework"
description: "A Microsoft Agent Framework series builds a CLI-style personal finance assistant in .NET and Python, showing how tools, plans, memory, approvals, and observability form an agent harness."
date: 2026-11-10
author: "Emiliano Montesdeoca"
tags: [".NET", "Microsoft Agent Framework", "AI Agents", "Python", "Developer Tools"]
slug: microsoft-agent-framework-claw-harness
---

“Claw” is a playful name for a capable command-line agent that can plan, call tools, remember context, and act on a user’s behalf. Underneath the personality is an **agent harness**: a loop around a language model that supplies tools, planning, memory, approvals, observability, and a path to deployment.

Microsoft’s new series builds that kind of assistant with **Microsoft Agent Framework**, showing .NET and Python side by side. The series uses a personal finance and investing helper as its running example. It looks up stock prices, reads a portfolio, drafts reports, and runs analyses, while sensitive actions require approval.

## A claw is a harness

The model is only one component. The harness gives it the boundaries and capabilities needed to become a useful application:

- **Tools** let the agent interact with data and services.
- **Plans** let it organize and adapt multi-step work.
- **Memory** carries useful information across turns and sessions.
- **Approvals** require a human decision before risky actions.
- **Observability** makes the agent’s activity visible.
- **Deployment** turns the loop into a service rather than a local experiment.

Agent Framework provides composable building blocks for these concerns. That means a team can focus on the behavior and boundaries of the assistant instead of hand-rolling every loop, approval callback, and persistence mechanism.

The distinction matters for .NET developers building internal agents. A chat completion can answer a question, but a production assistant needs explicit choices about which tools exist, which actions are reversible, what information persists, and how a team can inspect a failed run.

## The series progression

The series builds one assistant incrementally:

1. **Meet your agent harness and claw.** Start with a minimal harness, a custom `get_stock_price` tool, web search, and planning through todos plus plan/execute modes.
2. **Working with your data, safely.** Add file access for reading a portfolio CSV and writing reports, approvals for risky actions, and durable memory using a file or Foundry.
3. **Scaling its capabilities.** The planned next stage covers skills, including Foundry-managed skills, background agents for concurrent work, shell access, and CodeAct.
4. **Production-ready.** The final planned stage covers OpenTelemetry observability, Purview governance, deployment to Foundry Hosted Agents, and evaluation.

The samples are runnable and live in the accompanying repository, so the series is intended to be followed as an implementation path rather than read only as a conceptual overview.

## The model still sets the ceiling

The harness can multiply what a model can do, but it cannot make an unreliable model reliably follow layered instructions. Every turn requires the model to choose the right tool, follow the harness instructions, adapt its plan, reason over tool output, and ask for approval when the action is sensitive.

The source recommends a current, high-capability model for this kind of loop. An older or smaller model can run the harness, but teams should expect more hand-holding and less complete instruction following. That is a design input, not merely a model-picking detail: the harness and model form one operating system for the agent’s behavior.

For a .NET team, the right evaluation question is not “Can the model answer a prompt?” It is “Can the model complete this multi-step workflow while respecting tool boundaries, approval gates, and the information it has been given?”

## Why the finance example works

The personal finance assistant is deliberately concrete. It has benign actions such as looking up a stock price, analytical actions such as reading a portfolio and drafting a report, and sensitive actions such as placing a trade or sending a report.

That range makes the harness boundaries visible. A tool call can return information, a plan can organize several calls, memory can preserve the user’s context, and an approval can pause an action that should not happen automatically. The sample market data is mock data and the series is illustrative, not financial advice, but the engineering shape applies to many internal .NET assistants.

Replace the portfolio with an incident record, a deployment inventory, or a support queue and the same questions remain: which data can be read, which changes can be proposed, which actions need approval, and what evidence must be retained after the run?

## A practical way to use the series

1. Start with one narrow tool and define its input and output clearly.
2. Add a plan only when the workflow contains multiple meaningful steps.
3. Mark actions that mutate data, contact people, or create operational risk as approval-gated.
4. Choose memory deliberately: distinguish durable user preferences from temporary task context.
5. Capture tool calls, decisions, and failures through observability before calling the agent production-ready.
6. Evaluate the workflow with representative tasks, not only successful demonstrations.

The series’ strongest idea is that an agent is not just a model with a prompt. It is a composed system with capabilities and controls. Microsoft Agent Framework gives .NET and Python developers a starting point for assembling that system, while the harness design makes the boundary between helpful automation and unreviewed action explicit.