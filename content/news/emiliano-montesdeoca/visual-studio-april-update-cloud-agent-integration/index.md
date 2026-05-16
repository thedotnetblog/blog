---
title: "Visual Studio 2026 April Update: Cloud Agent, Custom Agents, and Debugger Agent"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Visual Studio 2026 (18.5) April update brings cloud agent integration, user-level custom agents, C++ code tools GA, and a Debugger Agent that validates fixes against live runtime behavior."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

[Visual Studio 2026 (18.5) April update](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) ships cloud agent integration, user-level custom agents, C++ tools going GA, and a new Debugger Agent.

## Cloud agent: offload work to a remote Copilot session

From the Chat window's agent picker, selecting **Cloud** lets you hand off a task to a remote Copilot coding agent. You describe the work, the agent creates a GitHub issue in your repo, then opens a PR when done. You get a notification with "View PR" / "Open in browser" — the whole thing runs while you keep coding, or even with the IDE closed.

## Custom agents now travel with you

User-level custom agents stored in `%USERPROFILE%/.github/agents/` are no longer repo-scoped — they follow you across projects. The storage path is configurable under Tools > Options > GitHub > Copilot > Chat. The `+` button in the agent picker lets you create new agents directly. They get the same capabilities as repo-scoped agents: workspace awareness, tools, model selection, and MCP connections.

Built-in agents: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## C++ Code Editing Tools go GA

Two tools — `get_symbol_call_hierarchy` and `get_symbol_class_hierarchy` — are now on by default. They give Copilot language-aware navigation of C++ codebases, covering inheritance hierarchies and function call chains. Enable via the Tools icon in Copilot Chat. Works best with tool-calling models.

## Debugger Agent: fixes validated against real runtime behavior

Start from a GitHub or Azure DevOps issue (or just a natural language description), switch to Debugger mode, and the agent:

1. Creates a minimal reproducer
2. Generates failure hypotheses
3. Instruments the app with tracepoints and conditional breakpoints
4. Runs an actual debug session
5. Analyzes live telemetry
6. Suggests a precise fix

You stay in the loop throughout — it's interactive, not fully autonomous.

## IntelliSense priority fix

VS now suppresses Copilot completions while the IntelliSense list is active. One suggestion at a time. This was a frequent friction point and it's now on by default.

Full release notes and download at [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
