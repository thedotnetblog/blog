---
title: "VS Code 1.117: Agents Are Getting Their Own Git Branches and I'm Here For It"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 ships worktree isolation for agent sessions, persistent Autopilot mode, and subagent support. The agentic coding workflow just got way more real."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

The line between "AI assistant" and "AI teammate" keeps getting thinner. VS Code 1.117 just dropped and the [full release notes](https://code.visualstudio.com/updates/v1_117) are packed, but the story here is clear: agents are becoming first-class citizens in your dev workflow.

Here's what actually matters.

## Autopilot mode finally remembers your preference

Previously, you had to re-enable Autopilot every time you started a new session. Annoying. Now your permission mode persists across sessions, and you can configure the default.

The Agent Host supports three session configs:

- **Default** — tools ask for confirmation before running
- **Bypass** — auto-approves everything
- **Autopilot** — fully autonomous, answers its own questions and keeps going

If you're scaffolding a new .NET project with migrations, Docker, and CI — set it to Autopilot once and forget about it. That preference sticks.

## Worktree and git isolation for agent sessions

This is the big one. Agent sessions now support full worktree and git isolation. That means when an agent works on a task, it gets its own branch and working directory. Your main branch stays untouched.

Even better — Copilot CLI generates meaningful branch names for these worktree sessions. No more `agent-session-abc123`. You get something that actually describes what the agent is doing.

For .NET developers running multiple feature branches or fixing bugs while a long scaffolding task runs, this is a game changer. You can have an agent building out your API controllers in one worktree while you're debugging a service layer issue in another. No conflicts. No stashing. No mess.

## Subagents and agent teams

The Agent Host Protocol now supports subagents. An agent can spin up other agents to handle parts of a task. Think of it as delegating — your main agent coordinates, and specialized agents handle the pieces.

This is early, but the potential for .NET workflows is obvious. Imagine one agent handling your EF Core migrations while another sets up your integration tests. We're not fully there yet, but the protocol support landing now means tooling will follow fast.

## Terminal output auto-included when agents send input

Small but meaningful. When an agent sends input to the terminal, the terminal output is now automatically included in the context. Before, the agent had to make an extra turn just to read what happened.

If you've ever watched an agent run `dotnet build`, fail, and then take another round-trip just to see the error — that friction is gone. It sees the output immediately and reacts.

## Self-updating Agents app on macOS

The standalone Agents app on macOS now self-updates. No more manually downloading new versions. It just stays current.

## The smaller stuff worth knowing

- **package.json hovers** now show both the installed version and the latest available. Useful if you manage npm tooling alongside your .NET projects.
- **Images in JSDoc** comments render correctly in hovers and completions.
- **Copilot CLI sessions** now indicate whether they were created by VS Code or externally — handy when you're jumping between terminals.
- **Copilot CLI, Claude Code, and Gemini CLI** are recognized as shell types. The editor knows what you're running.

## The takeaway

VS Code 1.117 isn't a flashy feature dump. It's infrastructure. Worktree isolation, persistent permissions, subagent protocols — these are the building blocks for a workflow where agents handle real, parallel tasks without stepping on your code.

If you're building with .NET and haven't leaned into the agentic workflow yet, honestly, now's the time to start.
