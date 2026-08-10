---
title: "Agent Optimizer Brings an Evaluation Loop to Foundry Agent Service"
description: "Foundry Agent Optimizer evaluates an agent, generates candidate configurations, ranks them, and promotes a winner without retraining the model."
date: 2026-10-14
author: "Emiliano Montesdeoca"
tags: ["Microsoft Foundry", "Agent Optimizer", "Evaluation", "AI Agents", ".NET"]
slug: foundry-agent-optimizer
---

Original source: [Introducing Agent Optimizer in Foundry Agent Service](https://devblogs.microsoft.com/foundry/agent-optimizer-build2026/)

The friction point Agent Optimizer targets is real: an agent works in the happy path and fails on the scenarios that matter. A support agent forgets to ask for an order number, answers a warranty question without checking the purchase date, or gives advice it should refuse. The usual response is to rewrite the system prompt, test by hand, and hope the fix did not create a regression elsewhere.

That loop is manageable for one agent. It becomes a bottleneck when a team operates many agents across different domains. Foundry Agent Optimizer, introduced in private preview with public preview planned in 30 days from the source announcement, automates more of the evaluate-and-improve cycle.

## From Failure Evidence to a Candidate

The optimizer starts with a task set where each task has explicit pass/fail criteria. It evaluates the baseline and produces a composite score from 0.0 to 1.0. It then generates candidate configurations based on what failed, evaluates those candidates against the same task set, ranks the results, and lets the developer deploy the winner.

That sequence is more important than the headline score. A candidate that improves one example while breaking three others is not an improvement. Reusing the same task set and criteria makes the comparison meaningful, while per-task breakdowns and token costs give the developer evidence before promotion.

The source's customer-support example shows a baseline score of 0.60 and a candidate score of 0.92. The result is presented as an improvement driven by synthetic data or historical traces, evaluator signals, and configuration changes, not model retraining or application code changes. Treat that number as the article's example, not as a promise for every workload.

The operational benefit is a shorter feedback loop. Instead of changing a prompt because a single response felt wrong, a team can ask which behavior failed, generate a candidate, and compare it against a defined evaluation suite.

## Four Places to Improve Behavior

The optimizer supports instruction, skill, model, and tool-description targets.

Instruction is the default. The optimizer generates alternative system prompts that address observed gaps. Skill produces named, reusable procedures for behaviors that need more structure than a prompt rewrite can provide, such as an escalation sequence or troubleshooting playbook.

Model compares model deployments against the same evaluator. That makes a quality and cost trade-off visible rather than theoretical. If a smaller deployment handles the workload adequately, the team can choose it based on evidence. If a larger model earns its cost on the dimensions that matter, the evaluation shows why.

Tool Descriptions improves the agent's understanding of its own local function tools by clarifying when to call one tool, tightening parameters, defining fallback behavior, and stating when the agent should answer directly. The source explicitly limits this capability to tools in the agent's own tool set, not external MCP servers. That boundary should shape the design: optimizer candidates improve what is already wired into the agent; they do not discover an entirely new integration.

For a .NET developer, these targets map to familiar engineering choices. Instructions are policy, Skills are reusable application procedures, model selection is a deployment decision, and tool descriptions are part of the API contract. Evaluate them separately before combining them in one optimization run.

## The Cold-Start Problem Is Part of the Product

Many teams do not have an evaluation dataset on day one. The source's `azd ai agent eval init` command addresses that cold start by generating a dataset and evaluation criteria from the agent's existing instructions. The customer-support example creates tasks around orders, returns, warranties, troubleshooting, escalation, and out-of-scope requests.

This is useful, but generated tests need review. An evaluation suite inherits assumptions from the instructions it reads. If the instructions omit an important security boundary, the generated dataset may omit it too. Treat the generated suite as a first draft, then add cases that represent real failures and abuse paths.

The broader Foundry loop is clear: traces capture interactions, evaluation scores behavior against criteria, Agent Optimizer generates candidates, the winning configuration is deployed as a versioned hosted agent, and evaluation runs again to confirm the change.

That is a better production story than prompt editing in isolation. It also gives teams a place to keep a rollback boundary. A candidate is only useful if the current version remains available and the promotion is explainable.

## A Small Configuration Boundary

To prepare an agent, the source uses an `.agent_configs/baseline/` directory with an `instructions.md` file, optional Skills, optional `tools.json`, and metadata. A `load_config()` call reads an optimized configuration when the service injects one during evaluation and falls back to defaults in normal operation.

The integration is designed to avoid separate production code paths. That is a good property for a .NET team: the application can keep one startup shape while evaluation supplies a different configuration. The team still needs to validate that the actual C# agent or service maps cleanly to the configuration format and that the tool descriptions used by the optimizer match the runtime functions.

## What I Would Do First

1. Write a small evaluation suite before optimizing anything.
2. Add failure cases for authorization, unsafe requests, missing inputs, and tool errors.
3. Run instruction optimization first, because it is the lowest-friction target.
4. Compare model candidates using quality, latency, and token cost rather than preference.
5. Review generated Skills and tool descriptions like code changes.
6. Promote only versioned candidates with a rollback path.

Agent Optimizer is valuable because it makes improvement a repeatable engineering loop. It does not remove the need for good criteria. The quality of the result is still bounded by what the team chooses to measure.