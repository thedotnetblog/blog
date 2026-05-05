---
title: "Azure MCP Server 2.0 Just Dropped — Self-Hosted Agentic Cloud Automation Is Here"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 goes stable with self-hosted remote deployments, 276 tools across 57 Azure services, and enterprise-grade security — here's what matters for .NET developers building agentic workflows."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

If you've been building anything with MCP and Azure lately, you probably already know the local experience works well. Plug in an MCP server, let your AI agent talk to Azure resources, move on. But the moment you need to share that setup across a team? That's where things got complicated.

Not anymore. Azure MCP Server [just hit 2.0 stable](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), and the headline feature is exactly what enterprise teams have been asking for: **self-hosted remote MCP server support**.

## What's Azure MCP Server?

Quick refresher. Azure MCP Server implements the [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) specification and exposes Azure capabilities as structured, discoverable tools that AI agents can invoke. Think of it as a standardized bridge between your agent and Azure — provisioning, deployment, monitoring, diagnostics, all through one consistent interface.

The numbers speak for themselves: **276 MCP tools across 57 Azure services**. That's serious coverage.

## The big deal: self-hosted remote deployments

Here's the thing. Running MCP locally on your machine is fine for dev and experiments. But in a real team scenario, you need:

- Shared access for developers and internal agent systems
- Centralized configuration (tenant context, subscription defaults, telemetry)
- Enterprise network and policy boundaries
- Integration into CI/CD pipelines

Azure MCP Server 2.0 addresses all of this. You can deploy it as a centrally managed internal service with HTTP-based transport, proper authentication, and consistent governance.

For auth, you get two solid options:

1. **Managed Identity** — when running alongside [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **On-Behalf-Of (OBO) flow** — OpenID Connect delegation that calls Azure APIs using the signed-in user's context

That OBO flow is particularly interesting for us .NET developers. It means your agentic workflows can operate with the user's actual permissions, not some over-privileged service account. Principle of least privilege, built right in.

## Security hardening

This isn't just a feature release — it's a security one too. The 2.0 release adds:

- Stronger endpoint validation
- Protections against injection patterns in query-oriented tools
- Tighter isolation controls for dev environments

If you're going to expose MCP as a shared service, these safeguards matter. A lot.

## Where can you use it?

The client compatibility story is broad. Azure MCP Server 2.0 works with:

- **IDEs**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **CLI agents**: GitHub Copilot CLI, Claude Code
- **Standalone**: local server for simple setups
- **Self-hosted remote**: the new star of 2.0

Plus there's sovereign cloud support for Azure US Government and Azure operated by 21Vianet, which is critical for regulated deployments.

## Why this matters for .NET developers

If you're building agentic applications with .NET — whether that's Semantic Kernel, Microsoft Agent Framework, or your own orchestration — Azure MCP Server 2.0 gives you a production-ready way to let your agents interact with Azure infrastructure. No custom REST wrappers. No service-specific integration patterns. Just MCP.

Combined with the [fluent API for MCP Apps](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) that dropped a few days ago, the .NET MCP ecosystem is maturing fast.

## Getting started

Pick your path:

- **[GitHub Repo](https://aka.ms/azmcp)** — source code, docs, everything
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — containerized deployment
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE integration
- **[Self-hosting guide](https://aka.ms/azmcp/self-host)** — the 2.0 flagship feature

## Wrapping up

Azure MCP Server 2.0 is exactly the kind of infrastructure upgrade that doesn't look flashy in a demo but changes everything in practice. Self-hosted remote MCP with proper auth, security hardening, and sovereign cloud support means MCP is ready for real teams building real agentic workflows on Azure. If you've been waiting for the "enterprise-ready" signal — this is it.
