---
title: "Azure DevOps MCP Server Lands in Microsoft Foundry: What This Means for Your AI Agents"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "The Azure DevOps MCP Server is now available in Microsoft Foundry. Connect your AI agents directly to DevOps workflows — work items, repos, pipelines — with a few clicks."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) has been having a moment. If you've been following the AI agent ecosystem, you've probably noticed MCP servers popping up everywhere — giving agents the ability to interact with external tools and services through a standardized protocol.

Now the [Azure DevOps MCP Server is available in Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), and this is one of those integrations that makes you think about the practical possibilities.

## What's actually happening here

Microsoft already released the Azure DevOps MCP Server as a [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — that's the MCP server itself. What's new is the Foundry integration. You can now add the Azure DevOps MCP Server to your Foundry agents directly from the tool catalog.

For those not familiar with Foundry yet: it's Microsoft's unified platform for building and managing AI-powered applications and agents at scale. Model access, orchestration, evaluation, deployment — all in one place.

## Setting it up

The setup is surprisingly straightforward:

1. In your Foundry agent, go to **Add Tools** > **Catalog**
2. Search for "Azure DevOps"
3. Select the Azure DevOps MCP Server (preview) and click **Create**
4. Enter your organization name and connect

That's it. Your agent now has access to Azure DevOps tools.

## Controlling what your agent can access

Here's the part I appreciate: you're not stuck with an all-or-nothing approach. You can specify which tools are available to your agent. So if you only want it to read work items but not touch pipelines, you can configure that. Principle of least privilege, applied to your AI agents.

This matters for enterprise scenarios where you don't want an agent accidentally triggering a deployment pipeline because someone asked it to "help with the release."

## Why this is interesting for .NET teams

Think about what this enables in practice:

- **Sprint planning assistants** — agents that can pull work items, analyze velocity data, and suggest sprint capacity
- **Code review bots** — agents that understand your PR context because they can actually read your repos and linked work items
- **Incident response** — agents that can create work items, query recent deployments, and correlate bugs with recent changes
- **Developer onboarding** — "What should I work on?" gets a real answer backed by actual project data

For .NET teams already using Azure DevOps for their CI/CD pipelines and project management, having an AI agent that can actually interact with those systems directly is a significant step toward useful automation (not just chatbot-as-a-service).

## The bigger MCP picture

This is part of a broader trend: MCP servers are becoming the standard way AI agents interact with the outside world. We're seeing them for GitHub, Azure DevOps, databases, SaaS APIs — and Foundry is becoming the hub where these connections all come together.

If you're building agents in the .NET ecosystem, MCP is worth paying attention to. The protocol is standardized, the tooling is maturing, and the Foundry integration makes it accessible without having to manually wire up server connections.

## Wrapping up

The Azure DevOps MCP Server in Foundry is in preview, so expect it to evolve. But the core workflow is solid: connect, configure tool access, and let your agents work with your DevOps data. If you're already in the Foundry ecosystem, this is a few clicks away. Give it a try and see what workflows you can build.

Check out the [full announcement](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) for the step-by-step setup and more details.
