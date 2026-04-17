---
title: "Stop Babysitting Your Terminal: Aspire's Detached Mode Changes the Workflow"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 lets you run your AppHost in the background and take your terminal back. Combined with new CLI commands and agent support, this is a bigger deal than it sounds."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

Every time you run an Aspire AppHost, your terminal is gone. Locked. Occupied until you Ctrl+C out of it. Need to run a quick command? Open another tab. Want to check logs? Another tab. It's a small friction that adds up fast.

Aspire 13.2 fixes this. James Newton-King [wrote up the full details](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), and honestly, this is one of those features that immediately changes how you work.

## Detached mode: one command, terminal back

```bash
aspire start
```

That's the shorthand for `aspire run --detach`. Your AppHost boots up in the background and you get your terminal back immediately. No extra tabs. No terminal multiplexer. Just your prompt, ready to go.

## Managing what's running

Here's the thing — running in the background is only useful if you can actually manage what's out there. Aspire 13.2 ships a full set of CLI commands for exactly that:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

This turns the Aspire CLI into a proper process manager. You can start multiple AppHosts, check their status, tail their logs, and shut them down — all from a single terminal session.

## Combine it with isolated mode

Detached mode pairs naturally with isolated mode. Want to run two instances of the same project in the background without port conflicts?

```bash
aspire start --isolated
aspire start --isolated
```

Each gets random ports, separate secrets, and its own lifecycle. Use `aspire ps` to see both, `aspire stop` to kill whichever you're done with.

## Why this is huge for coding agents

This is where it gets really interesting. A coding agent working in your terminal can now:

1. Start the app with `aspire start`
2. Query its state with `aspire describe`
3. Check logs with `aspire logs` to diagnose issues
4. Stop it with `aspire stop` when done

All without losing the terminal session. Before detached mode, an agent that ran your AppHost would lock itself out of its own terminal. Now it can start, observe, iterate, and clean up — exactly how you'd want an autonomous agent to work.

The Aspire team leaned into this. Running `aspire agent init` sets up an Aspire skill file that teaches agents these commands. So tools like Copilot's coding agent can manage your Aspire workloads out of the box.

## Wrapping up

Detached mode is a workflow upgrade disguised as a simple flag. You stop context-switching between terminals, agents stop blocking themselves, and the new CLI commands give you real visibility into what's running. It's practical, it's clean, and it makes the daily development loop noticeably smoother.

Read the [full post](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) for all the details and grab Aspire 13.2 with `aspire update --self`.
