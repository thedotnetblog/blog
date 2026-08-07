---
title: "VS Code 1.109 Makes Multi-Agent Workflows Practical"
description: "VS Code 1.109 brings multiple coding agents, session management, parallel subagents, and better steering into one developer workflow."
date: 2026-08-20
author: "Emiliano Montesdeoca"
tags: [vscode, agents, release]
slug: vscode-1-109-agent-workflows
---

Original source: [January 2026 (version 1.109)](https://code.visualstudio.com/updates/v1_109)

## The Agent Choice Becomes a Workflow Choice

For a while, using an AI coding assistant meant choosing the model or subscription attached to your editor and staying with it. VS Code 1.109 moves the decision to the task level. Claude, Codex, and Copilot can take different roles, while the Agent Sessions view gives you one place to see the work.

That matters for .NET teams because the best agent depends on the boundary of the problem. A codebase-specific change benefits from repository context and established conventions. An architectural question may benefit from a second model's perspective. A long-running refactor may be better delegated to a background or cloud session while the developer continues working locally.

The release does not remove the need for judgment. It makes the judgment visible and easier to manage.

## Agent Sessions Are the Operational Layer

The important feature is not simply that more agents are available. It is that their sessions are represented together. A developer can start a local task, inspect a background task, and return to a cloud session without keeping a separate mental checklist of terminals, browser tabs, and chat windows.

For a .NET repository, imagine splitting a modernization task into three pieces: one session inventories target frameworks and packages, another examines test coverage, and a third proposes the implementation plan. The value comes from keeping those activities distinct while retaining a shared place to review their status.

This also creates a better stopping rule. A session that is waiting on a tool call, has failed a test, or needs a decision should be visible as such. That is more useful than treating every agent as an opaque request-and-response interaction.

## Parallel Subagents Change Decomposition

The release also makes parallel subagent work more practical. Instead of asking one agent to research authentication, scan project conventions, and review documentation sequentially, a parent workflow can delegate focused investigations and combine the results.

The pattern works well when the tasks are genuinely independent. A .NET microservice change might need a scan of dependency injection patterns, an inventory of database migrations, and a review of CI configuration. Those investigations can run in parallel, then feed a plan that a human reviews before implementation begins.

The caveat is that parallelism increases the need for clear boundaries. Each subagent needs a narrow question, a defined output, and an explicit instruction about what it may change. Otherwise, the main agent receives several plausible but incompatible recommendations. Parallel work is a coordination tool, not a substitute for task design.

## Thinking and Steering Need Calibration

The release exposes more of the reasoning experience for supported Claude workflows and adds ways to steer or queue messages while an agent is working. Both features address a real supervision problem: developers often realize halfway through a task that the agent has misunderstood the goal.

Steering is useful when the current tool call should finish but the next step needs to change. Queueing is useful when the direction is right and you want to add a follow-up without interrupting the current operation. Cancellation remains the correct choice when the agent is acting on the wrong target or the next mutation would be unsafe.

More visible reasoning can help during an architecture or security review, but it is not proof that a conclusion is correct. For quick edits, the extra detail may add noise and consume context. Choose the level of visibility based on the risk of the task.

## What This Means for .NET Teams

Start with a small, repeatable workflow. Use a local Copilot session for a bounded change, ask a second agent to review the plan, and use a background session only for work that has clear acceptance criteria. Keep source control and tests as the final authority.

Document which tasks may run in parallel and which require a single reviewer. A good default is to allow parallel read-only investigation, but require approval before an agent edits project files, changes package versions, or runs deployment commands.

VS Code 1.109 makes multi-agent development easier to operate, not magically reliable. The teams that benefit most will be the ones that pair session visibility with clear issue descriptions, reproducible builds, and a review boundary that does not disappear just because several agents can work at once.