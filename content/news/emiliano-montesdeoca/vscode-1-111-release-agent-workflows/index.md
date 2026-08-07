---
title: "VS Code 1.111: Agent Workflows Gain Autonomy and Debug Visibility"
description: "VS Code 1.111 adds session-level permission modes, Autopilot preview, agent-scoped hooks, and debug snapshots for safer autonomous workflows."
date: 2026-08-26
author: "Emiliano Montesdeoca"
tags: [vscode, agents, autopilot, release]
slug: vscode-1-111-release-agent-workflows
---

# VS Code 1.111: Agent Workflows Gain Autonomy and Debug Visibility

Original source: [Visual Studio Code 1.111](https://code.visualstudio.com/updates/v1_111)

VS Code 1.111 is the first release in the team's move toward weekly releases, and its agent features explain why that cadence matters. The editor is making autonomous work easier to start while adding the visibility needed to understand it when something goes wrong.

The headline is Autopilot, but the more important story is the boundary around autonomy: permissions, hooks, and debug snapshots give developers ways to scope and inspect the behavior.

## Three Permission Levels, One Important Decision

The Chat view now exposes session-level permission choices. Default approvals keep confirmation behavior in place. Bypass approvals automatically accepts tool calls and retries errors. Autopilot, in preview, goes further by allowing the agent to continue, answer routine questions, retry, and stop when it signals completion.

That is a real change for multi-step work. A well-scoped test update or a bounded refactor can run without a developer approving every intermediate tool call. But bypass and Autopilot also weaken the pause that normally catches a destructive command.

For .NET developers, the prerequisite is not enthusiasm. It is a recovery path. Use a feature branch or isolated worktree, make sure tests and CI gates run, and keep sensitive credentials and deployment targets outside the agent's default reach. Autonomy is only useful when the cost of a wrong decision is contained.

Start with tasks whose acceptance criteria are executable: add tests for a known bug, update a set of mechanical call sites, or implement a small change with an existing pattern. Do not begin with an architectural migration that has no crisp completion signal.

## Agent-Scoped Hooks Keep Policies Local

Hooks can now be attached to a specific agent definition rather than applied globally. This lets a specialized agent carry its own pre- and post-processing behavior without changing every other chat session.

A .NET refactoring agent could run formatting and targeted tests after an edit. A database-review agent could inspect migration output without being allowed to apply it. The key is that the policy travels with the agent's purpose.

Preview syntax and behavior deserve testing in a non-critical repository. Keep hooks fast, make failures visible, and document the commands they run. A hook that quietly changes files or hides a failed validation is worse than no hook at all.

## Debug Snapshots Turn Failures Into Evidence

The Agent Debug panel can provide event snapshots that developers attach to chat for analysis. Instead of saying that an agent "did the wrong thing," you can inspect the tools called, the returned data, and the point where the workflow diverged.

This is particularly useful when an agent misses a project instruction or chooses the wrong configuration file. The snapshot gives the team something concrete to review and improves the next task definition or custom agent.

Debug evidence also helps with reproducibility. Capture the relevant session state, compare it with the repository's instructions, and ask whether the failure came from missing context, an overly broad tool permission, or a flawed assumption. That is a much better feedback loop than simply retrying.

## Small Release Details Matter

The redesigned chat tips help surface commands such as `/init` and `/fork`, while AI-oriented terminal profiles can be grouped for easier access. These are not the main features, but they reduce the friction of discovering and moving between the new workflow pieces.

The weekly release cadence also changes how teams should evaluate the editor. Pin versions for controlled environments, test updates on a representative repository, and keep an eye on preview features before making them part of a standard developer image.

## What .NET Teams Should Do

1. Create a feature-branch workflow for trying Bypass approvals or Autopilot.
2. Use Autopilot only with explicit acceptance criteria and automated checks.
3. Add one narrowly scoped agent hook for formatting or targeted tests.
4. Capture debug snapshots when a session fails instead of relying on memory.
5. Keep preview settings out of production-like automation until their behavior is understood.

VS Code 1.111 does not turn autonomy into a default. It makes autonomy a configurable tool. The teams that benefit will pair that tool with isolation, tests, and a clear human review boundary.