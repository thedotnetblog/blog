---
title: "Visual Studio Code 1.125: Better visibility for agent work"
description: "VS Code 1.125 adds the Chronicle command set, clearer Agent Host paths, richer Cache Explorer details, and qualified tool names for multi-agent workflows."
date: 2026-11-07
author: "Emiliano Montesdeoca"
tags: ["Visual Studio Code", "Copilot", "Agents", "Release", ".NET Development"]
slug: vscode-1-125-release
---

Original source: [Visual Studio Code 1.125](https://code.visualstudio.com/updates/v1_125)

Visual Studio Code 1.125 is a small release with a useful theme: agent work should be easier to inspect after it happens. The update adds session-history commands to the Agent Host, improves path readability, gives Cache Explorer more context about multi-agent sessions, and makes qualified tool names available in tool sets.

None of these changes writes application code for you. They improve the surfaces around agent-assisted development, which is where teams need enough evidence to understand what happened, what was expensive, and which session or tool was involved.

## Chronicle brings session history into chat

The Agent Host now includes the `/chronicle` command set. The available commands are:

- `/chronicle standup`
- `/chronicle search`
- `/chronicle tips`
- `/chronicle cost-tips`
- `/chronicle improve`
- `/chronicle reindex`

These commands provide session-history insights directly from chat. That matters when an agent session is no longer just a disposable conversation. A developer may need to search earlier work, understand recent activity, identify cost patterns, or reindex history before asking a follow-up question.

The history commands should complement repository evidence rather than replace it. Keep acceptance criteria, architectural decisions, and production changes in source control or the team’s issue system. Session history is valuable for reconstructing the working process; it is not a substitute for a reviewed change.

## Clearer paths in the Agent Host

The Agent Host now displays file paths more readably. That sounds cosmetic until an agent is working across a solution with similarly named projects, generated files, test fixtures, and multiple repository roots.

For .NET development, readable paths make tool activity easier to audit. When a session edits a project file, test, configuration file, or generated artifact, the path should help the developer understand which part of the repository is involved without decoding a dense or ambiguous display. Better presentation does not alter path resolution, so normal review of the actual diff remains essential.

## Cache Explorer for multi-agent sessions

The Cache Explorer view has been enhanced to make multi-agent sessions easier to understand and navigate. It also surfaces more detailed prompt-signature allocation information.

Prompt signatures are a useful part of the agent cost and latency story: repeated context can be reused when the signature remains stable, while changing context can reduce cache reuse. Seeing more allocation detail gives teams a better way to reason about what each session is carrying and why two apparently similar tasks may have different context behavior.

The view is most useful during investigation. If a long-running refactoring session consumes more context than expected, inspect the session and its prompt-signature allocation before guessing that the model alone is responsible. Cache visibility still does not reveal whether a proposed code change is correct; it helps explain the mechanics around the request.

## Qualified tool names in tool sets

VS Code 1.125 adds support for qualified tool names in tool sets. As the number of built-in tools, extension tools, and MCP tools grows, names can collide or become difficult to identify by themselves. A qualified name can preserve the tool’s provider or namespace context.

This is particularly relevant for .NET teams that connect several MCP servers or extensions. A workspace search tool, a repository search tool, and a service-specific search tool may perform related operations but have different ownership and permissions. Qualified names make the tool set more explicit and reduce the chance that a similarly named capability is selected without enough context.

Treat the name as an aid to clarity, not as a security boundary. Tool permissions, server configuration, and the generated change still need review. A clearer catalog is useful because it makes that review easier.

## A practical 1.125 workflow

1. Use `/chronicle search` to recover the context of an earlier agent investigation.
2. Try `/chronicle cost-tips` when a session’s token or cache behavior needs attention.
3. Inspect the improved paths when reviewing Agent Host tool activity across a large solution.
4. Open Cache Explorer for a multi-agent session and compare prompt-signature allocation before changing the workflow.
5. Review qualified tool names in tool sets that combine extension and MCP capabilities.

VS Code 1.125 is about making agent work legible. Better history access, clearer paths, more useful cache detail, and explicit tool identity give developers more information to supervise the agent loop without turning every investigation into a forensic exercise.