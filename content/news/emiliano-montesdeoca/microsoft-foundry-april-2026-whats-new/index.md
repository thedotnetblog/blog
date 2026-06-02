---
title: "Microsoft Foundry April 2026: Foundry Local GA, GPT-5.5, CodeAct with Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "April's Foundry recap is heavy: Foundry Local hits GA, GPT-5.5 arrives, Agent Framework gets OpenTelemetry tracing, CodeAct runs Python in Hyperlight micro-VMs, and the Agent Monitoring Dashboard lands."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

A busy month for Microsoft Foundry. Here are the announcements that matter most.

## Foundry Local Is Generally Available

Foundry Local — Microsoft's cross-platform local AI runtime — graduates from preview to GA on Windows, macOS (Apple Silicon), and Linux x64. Production-ready local model inference with a developer-friendly SDK. The 1.1 release (detailed in [a separate post](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)) adds transcription, embeddings, and Responses API support.

## GPT-5.5

The latest GPT-5 family model is now available in Foundry. Default quota for Tier 5 and Tier 6 subscriptions. If you've been working with earlier GPT-5 variants, this is worth evaluating for your use cases.

## Agent Framework Tracing in Foundry

Two tracing features ship in preview this month:

**Microsoft Agent Framework tracing** — MAF agents can now emit OpenTelemetry traces into Foundry. Debug agent behavior, trace multi-step execution, surface latency and errors across tool calls. This fills a real gap: knowing *what your agent actually did* in production, not just what it returned.

**Hosted-agent tracing** — Sessions, tool calls, and run steps from hosted agents also surface in Foundry traces. Same observability story extended to the hosted tier.

## CodeAct with Hyperlight (Alpha)

This is the most technically interesting addition: Agent Framework can now execute Python code inside [Hyperlight](https://github.com/hyperlight-dev/hyperlight) micro-virtual machines.

CodeAct is the pattern where an agent generates and executes Python code as a tool. The obvious concern is security — you're running model-generated code. Hyperlight's micro-VMs provide process-level isolation with near-native startup time, making sandboxed code execution practical without the overhead of full containers or VMs.

For agentic workflows where code execution is necessary, this is a significant safety improvement over running code in the host process.

## Agent Monitoring Dashboard (Preview)

A unified operations dashboard combining token usage, latency, run success rate, and evaluator scores in one view. The distinction from regular observability dashboards: it includes evaluation results alongside operational metrics, so you can correlate "the agent is slower" with "evaluator scores dropped" — or confirm they're unrelated.

## Continuous Evaluation Custom Evaluators (Preview)

You can now bring your own code-based or prompt-based evaluators into continuous evaluation pipelines. Previously, continuous eval was limited to built-in evaluators. Custom evaluators let you enforce team-specific quality criteria in your production monitoring loop.

## Agent Inventory in Control Plane

The Foundry Control Plane Operate view now shows all supported agents across a subscription: Foundry agents, Azure SRE Agent, Logic Apps agent loops, and registered custom agents. One view to understand what's deployed and where.

Original post: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
