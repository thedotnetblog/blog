---
title: "From Laptop to Production: Deploying AI Agents to Microsoft Foundry with Two Commands"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "The Azure Developer CLI now has 'azd ai agent' commands that take your AI agent from local dev to a live Foundry endpoint in minutes. Here's the full workflow."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

You know that gap between "it works on my machine" and "it's deployed and serving traffic"? For AI agents, that gap has been painfully wide. You need to provision resources, deploy models, wire up identity, set up monitoring — and that's before anyone can actually call your agent.

The Azure Developer CLI just made this a [two-command affair](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## The new `azd ai agent` workflow

Let me walk through what this actually looks like. You have an AI agent project — let's say a hotel concierge agent. It works locally. You want it running on Microsoft Foundry.

```bash
azd ai agent init
azd up
```

That's it. Two commands. `azd ai agent init` scaffolds the infrastructure-as-code in your repo, and `azd up` provisions everything on Azure and publishes your agent. You get a direct link to your agent in the Foundry portal.

## What happens under the hood

The `init` command generates real, inspectable Bicep templates in your repo:

- A **Foundry Resource** (top-level container)
- A **Foundry Project** (where your agent lives)
- **Model deployment** configuration (GPT-4o, etc.)
- **Managed identity** with proper RBAC role assignments
- `azure.yaml` for the service map
- `agent.yaml` with agent metadata and environment variables

Here's the key part: you own all of this. It's versioned Bicep in your repo. You can inspect it, customize it, and commit it alongside your agent code. No magic black boxes.

## The dev inner loop

What I really like is the local development story. When you're iterating on agent logic, you don't want to redeploy every time you change a prompt:

```bash
azd ai agent run
```

This starts your agent locally. Pair it with `azd ai agent invoke` to send test prompts, and you've got a tight feedback loop. Edit code, restart, invoke, repeat.

The `invoke` command is smart about routing too — when a local agent is running, it targets that automatically. When it's not, it hits the remote endpoint.

## Real-time monitoring

This is the feature that sold me. Once your agent is deployed:

```bash
azd ai agent monitor --follow
```

Every request and response flowing through your agent streams to your terminal in real time. For debugging production issues, this is invaluable. No digging through log analytics, no waiting for metrics to aggregate — you see what's happening right now.

## The full command set

Here's the quick reference:

| Command | What it does |
|---------|-------------|
| `azd ai agent init` | Scaffold a Foundry agent project with IaC |
| `azd up` | Provision Azure resources and deploy the agent |
| `azd ai agent invoke` | Send prompts to the remote or local agent |
| `azd ai agent run` | Run the agent locally for development |
| `azd ai agent monitor` | Stream real-time logs from the published agent |
| `azd ai agent show` | Check agent health and status |
| `azd down` | Clean up all Azure resources |

## Why this matters for .NET developers

Even though the sample in the announcement is Python-based, the infrastructure story is language-agnostic. Your .NET agent gets the same Bicep scaffolding, the same managed identity setup, the same monitoring pipeline. And if you're already using `azd` for your .NET Aspire apps or Azure deployments, this fits right into your existing workflow.

The deployment gap for AI agents has been one of the biggest friction points in the ecosystem. Going from a working prototype to a production endpoint with proper identity, networking, and monitoring shouldn't require a week of DevOps work. Now it requires two commands and a few minutes.

## Wrapping up

`azd ai agent` is available now. If you've been putting off deploying your AI agents because the infrastructure setup felt like too much work, give this a shot. Check out the [full walkthrough](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) for the complete step-by-step including frontend chat app integration.
