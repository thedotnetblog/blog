---
title: "Foundry Toolboxes: One Endpoint for All Your Agent Tools"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry just launched Toolboxes in public preview — a way to curate, manage, and expose AI agent tools through a single MCP-compatible endpoint without re-wiring everything per agent."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

Here's a problem that sounds boring until you've actually hit it: your organization is building multiple AI agents, each one needs tools, and every team is wiring those tools up from scratch. Same Web Search integration, same Azure AI Search config, same GitHub MCP server connection — just in a different repo, by a different team, with different credentials and no shared governance.

Microsoft Foundry just shipped [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) in public preview, and it's a direct answer to that problem.

## What's a Toolbox?

A Toolbox is a named, reusable bundle of tools that you define once in Foundry and expose through a single MCP-compatible endpoint. Any agent runtime that speaks MCP can consume it — you're not locked to Foundry Agents.

The pitch is simple: **build once, consume anywhere**. Define the tools, configure auth centrally (OAuth passthrough, Entra managed identity), publish the endpoint. Every agent that needs those tools connects to the endpoint and gets them all.

No per-tool wiring. No per-agent credential management.

## The four pillars (two of which ship today)

The Toolbox feature is organized around four ideas:

| Pillar | Status | What it does |
|--------|--------|--------------|
| **Discover** | Coming soon | Find existing approved tools without hunting |
| **Build** | Available now | Curate tools into a named, reusable bundle |
| **Consume** | Available now | Single MCP endpoint exposes all tools |
| **Govern** | Coming soon | Centralized auth + observability across all tool calls |

Today the focus is on Build and Consume. That's enough to remove the most immediate friction.

## Getting started in practice

The SDK is Python-first for now. You start by creating an `AIProjectClient` and then build a toolbox:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

Then you create a toolbox version with the tools you want to bundle:

```python
toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Search public and internal docs, then respond to GitHub issues.",
    tools=[
        {"type": "web_search", "description": "Search approved public documentation"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Once published, Foundry gives you a unified endpoint:

```
https://zava.services.ai.azure.com/api/projects/<project>/toolbox/<toolbox-name>/mcp?api-version=v1
```

Point any MCP-compatible agent runtime at that URL and it discovers all the tools in the bundle dynamically. One connection. All tools.

## Not locked to Foundry Agents

This is worth spelling out because it's a common concern when Microsoft ships something under the Foundry brand.

Toolboxes are **created and governed** in Foundry, but the consumption surface is the open MCP protocol. That means you can use them from:

- **Custom agents** built with Microsoft Agent Framework, LangGraph, or your own code
- **GitHub Copilot** and other MCP-enabled IDEs
- Any other runtime that speaks MCP

You're not locked in. The toolbox is Foundry-homed (that's where you manage it) but not Foundry-bound (you can consume it from anywhere).

## Why it matters now

The multi-agent wave is hitting production. Teams are building 5, 10, 20 agents — and the tool-wiring problem compounds fast. Every new agent is a new surface for duplicated config, stale credentials, and inconsistent behavior.

Toolboxes don't solve governance and discovery yet (those are "coming soon"), but the Build + Consume foundation is enough to start centralizing. Once the Govern pillar ships, you'll have a proper observable, centrally-controlled tool layer for your entire agent fleet.

## Wrapping up

This is early — public preview, Python SDK first, with Discover and Govern still coming. But the model is sound, and the MCP-native design means it works with the tools you're already building on. Take a look at the [official announcement](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) to get started.
