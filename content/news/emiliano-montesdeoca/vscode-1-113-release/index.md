---
title: "VS Code 1.113: Agent Workflows, Chat Customization, and the Thinking Model"
description: "VS Code 1.113 brings unified chat customizations, configurable thinking effort, nested subagents, and MCP support to CLI agent workflows."
date: 2026-08-30
author: "Emiliano Montesdeoca"
tags: [vscode, release, agents, copilot]
slug: vscode-1-113-release
---

Original source: [Visual Studio Code 1.113](https://code.visualstudio.com/updates/v1_113)

VS Code 1.113 represents a meaningful shift in how agents operate inside the editor. This release moves beyond incremental improvements and addresses the friction .NET developers hit when orchestrating multi-step workflows, composing specialized agents, and reasoning through complex problems.

## Chat Customizations: One Place to Manage Agent Guidance

If you've been configuring VS Code agents, you know the pain. Custom instructions here, prompt files there, agent definitions in another folder. VS Code 1.113 introduces the Chat Customizations editor, a unified interface for creating and managing custom instructions, prompt files, custom agents, and agent skills.

For .NET developers, this matters immediately. You can use one interface to inspect the repository's architectural patterns, dependency policies, and testing conventions instead of hunting through several customization types. The editor includes syntax highlighting and validation, which should mean fewer misconfigurations when an agent starts behaving in an unexpected way.

The editor can also use AI to generate initial customization content based on the project. That is useful for getting a first draft of a repository guide, but it should remain a draft. If your .NET repository requires integration tests for database mutations or has strict async naming conventions, review the generated instructions against the actual code and build checks before committing them.

The feature is in preview. Treat it as a consolidation opportunity, not a reason to abandon version control. Keep customization files in the repository, review the diff, and make sure a teammate can understand what guidance an agent will receive.

## Thinking Effort: Spend Reasoning Where It Pays

Models that support reasoning, such as Claude Sonnet 4.6 and GPT-5.4, now expose a Thinking Effort submenu directly in the model picker. The available levels can vary by model, and VS Code retains the selected effort level per model across conversations. The picker label also shows the active level, for example `GPT-5.3-Codex - Medium`.

This is practical for .NET work because not every task deserves the same latency or token budget. A cross-project refactor, an authorization review, or a difficult concurrency bug may justify a higher reasoning level. Repetitive boilerplate, straightforward test scaffolding, or a mechanical rename usually does not.

My recommendation is to treat thinking effort as a workflow setting, not a badge. Run the same kind of task at two levels and compare correctness, elapsed time, token use, and review effort. The most expensive setting is not automatically the most useful one, and the cheapest setting is not a win if it creates another debugging pass.

The release also deprecates older reasoning-effort settings in favor of the model picker. That makes the active choice more visible, which is helpful when comparing results across sessions.

## Nested Subagents: More Composition, More Responsibility

Subagents can now invoke other subagents when `chat.subagents.allowInvocationsFromSubagents` is enabled. Previously, subagents were restricted from making these invocations to prevent infinite recursion. The new setting opens more complex multi-step workflows.

A .NET code-review agent could delegate a focused security question to a security subagent. A migration agent could hand a specific compatibility issue to a specialist while keeping responsibility for the overall plan. This is useful when the task has genuinely different areas of expertise.

It also creates a new failure mode. Without a clear delegation boundary, nested agents can loop, duplicate work, or consume time without producing a better result. Define which agent may delegate, what information it passes, and what completion signal ends the chain. Start with one level of nesting and inspect the debug log before adding more.

Composition works best when each subagent has a narrow contract. A security subagent should report findings and evidence, not silently rewrite the migration. A test subagent should explain what it validated, not declare an architectural decision complete.

## CLI Agents and Shared MCP Tools

MCP servers configured in VS Code can now be bridged to Copilot CLI and Claude agents, including user-defined servers and workspace servers in `mcp.json`. That makes a repository's custom tools more portable across local editor and command-line workflows.

For a .NET team, this could mean sharing a domain-specific validator, an internal API lookup, or a build diagnostic tool across the places where agents run. The portability is valuable, but the permission boundary still matters. Review which MCP servers are safe for automation, what data they can reach, and whether they should be available in CI.

The release also brings forking sessions to Copilot CLI and Claude agents, behind the relevant Copilot CLI setting, and extends the Agent Debug Log panel to those sessions in preview. That gives teams more ways to explore an alternative prompt and inspect the prompts, tool calls, and event history that produced a result.

## What .NET Developers Should Do Now

1. Consolidate chat customizations carefully, keep the files versioned, and review preview behavior.
2. Test thinking effort on representative tasks and measure review quality, not just response speed.
3. Design nested delegation with explicit ownership and a clear stopping condition.
4. Audit MCP servers before sharing them with CLI or CI agents.
5. Use debug logs and forked sessions to investigate behavior instead of relying on a successful-looking final answer.

The important change in 1.113 is composability. Agents, tools, customizations, and reasoning controls are becoming parts of one workflow. That makes the workflow more capable, but it also makes repository guidance and observability more important than ever.