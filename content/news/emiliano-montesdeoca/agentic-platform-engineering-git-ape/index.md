---
title: "Agentic Platform Engineering Is Getting Real — Git-APE Shows How"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft's Git-APE project puts agentic platform engineering into practice — using GitHub Copilot agents and Azure MCP to turn natural-language requests into validated cloud infrastructure."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

Platform engineering has been one of those terms that sounds great in conference talks but usually means "we built an internal portal and a Terraform wrapper." The real promise — self-service infrastructure that's actually safe, governed, and fast — has always been a few steps away.

The Azure team just published [Part 2 of their agentic platform engineering series](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), and this one is all about the hands-on implementation. They call it **Git-APE** (yes, the acronym is intentional), and it's an open-source project that uses GitHub Copilot agents plus Azure MCP servers to turn natural-language requests into validated, deployed infrastructure.

## What Git-APE actually does

The core idea: instead of developers learning Terraform modules, navigating portal UIs, or filing tickets to a platform team, they talk to a Copilot agent. The agent interprets the intent, generates Infrastructure-as-Code, validates it against policies, and deploys — all within VS Code.

Here's the setup:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Open the workspace in VS Code, and the agent configuration files are auto-discovered by GitHub Copilot. You interact with the agent directly:

```
@git-ape deploy a function app with storage in West Europe
```

The agent uses Azure MCP Server under the hood to interact with Azure services. The MCP configuration in VS Code settings enables specific capabilities:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Why this matters

For those of us building on Azure, this shifts the platform engineering conversation from "how do we build a portal" to "how do we describe our guardrails as APIs." When your platform's interface is an AI agent, the quality of your constraints and policies becomes the product.

The Part 1 blog laid out the theory: well-described APIs, control schemas, and explicit guardrails make platforms agent-ready. Part 2 proves it works by shipping actual tooling. The agent doesn't just blindly generate resources — it validates against best practices, respects naming conventions, and applies your organization's policies.

Clean-up is just as easy:

```
@git-ape destroy my-resource-group
```

## My take

I'll be honest — this one is more about the pattern than the specific tool. Git-APE itself is a demo/reference architecture. But the underlying idea — agents as the interface to your platform, MCP as the protocol, GitHub Copilot as the host — is where enterprise developer experience is heading.

If you're a platform team looking at how to make your internal tooling agent-friendly, there's no better starting point. And if you're a .NET developer wondering how this connects to your world: the Azure MCP Server and GitHub Copilot agents work with any Azure workload. Your ASP.NET Core API, your .NET Aspire stack, your containerized microservices — all of it can be the target of an agentic deployment flow.

## Wrapping up

Git-APE is an early but concrete look at agentic platform engineering in practice. Clone the [repo](https://github.com/Azure/git-ape), try the demo, and start thinking about how your platform's APIs and policies would need to look for an agent to safely use them.

Read the [full post](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) for the walkthrough and video demos.
