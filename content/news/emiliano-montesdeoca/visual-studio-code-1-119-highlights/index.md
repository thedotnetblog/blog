---
title: "VS Code 1.119: OpenTelemetry for Agent Sessions, Browser Integration, and Security"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (May 2026) adds OpenTelemetry tracing for agent sessions, browser tab sharing for agents, trust & security improvements, and a 1.119.1 security patch."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) shipped May 6, 2026 (with a 1.119.1 security patch shortly after). The release focuses on agent observability, browser interaction, and reducing interruptions.

## OpenTelemetry tracing for agent sessions

This is the standout feature for anyone running agents in production or debugging agentic workflows. Enable it with two settings:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Traces follow GenAI semantic conventions. Each agent request produces an `invoke_agent` root span with nested child spans: `chat`, `execute_tool`, and `execute_hook`. Token usage is reported per request — including cache read and cache creation counts.

Works with the local agent, Copilot CLI background agent, and the Claude agent. Any OTLP-compatible backend accepts the traces — the [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) works well for local development.

## Agents can now access browser tabs

Agents can request access to your integrated browser tabs — but it's not automatic. You have to explicitly share a tab via the context picker, drag-and-drop, or suggested context. There's a sharing button in the browser to revoke access. When an agent tries to open a new tab on the same domain as an already-open (unshared) tab, VS Code prompts you to reuse the existing tab instead.

## Optimized token usage

An experimental lightweight model now handles agent todo-list management, keeping that housekeeping off the more expensive primary model. Reduces token burn on tasks that don't need full reasoning capacity.

## Trust & security

Fewer interruptions: VS Code 1.119 reduces prompts for network access requests and temp folder writes by agents. The 1.119.1 patch addresses specific security issues — worth updating if you haven't.

## Markdown preview quick-swap

Small but useful: you can now quickly swap the current editor to Markdown preview without navigating away.

## VS Code Agents (Insiders preview)

The redesigned agent session UI — new repo picker (local/repos/remote), sub-session improvements, web + mobile polish, progress animations — is available in Insiders at [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Full changelog: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
