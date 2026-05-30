---
title: "Your Local MAF Agent Just Got a Production Home"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents gives your Microsoft Agent Framework agent identity, scaling, session persistence, and zero-extra-wiring observability. Here's what that looks like in practice."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Getting an agent to work locally is the fun part. The tricky part is everything that comes after: deploying it without losing your mind, managing sessions, setting up identity, wiring observability. Usually that means a lot of custom infrastructure glue.

Foundry Hosted Agents just removed most of that glue for Microsoft Agent Framework (MAF) users.

## What Foundry Hosted Agents Actually Does

When you deploy a MAF agent to Foundry Hosted Agents, the platform handles a surprisingly long list of things you'd otherwise build yourself:

- **Scale to zero** — your agent costs nothing while idle and spins back up automatically
- **Per-session VM-isolated sandboxes** — every user session gets its own sandbox with filesystem persistence that survives scale-down events
- **Built-in Entra ID** — each agent gets its own identity so it can call Foundry models, Toolbox, and Azure services without secrets baked into the image
- **Versioned deployments** — every deployment is an immutable snapshot, with blue/green and canary rollout support
- **Zero-config observability** — `APPLICATIONINSIGHTS_CONNECTION_STRING` is injected at runtime so MAF's OpenTelemetry traces flow into App Insights automatically

That last one is genuinely nice. No extra wiring, no additional config. Traces just show up.

## The Code Difference Is Tiny

This is what I appreciate most about this integration. You don't rewrite your agent. You just wrap it:

**In .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**In Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

That's it. The same logic you tested locally is what runs in production. The platform wraps it in the session management, identity, and scaling infrastructure.

## Two Protocols, One Agent

Hosted Agents support two endpoint styles:

- **Responses** (`/responses`) — OpenAI-compatible, manages conversation history and streaming. Good default for chat-shaped agents.
- **Invocations** (`/invocations`) — you define the request/response schema. Good for non-conversational workflows.

If you're building something that looks like a conversation, start with Responses. If you're building an API-shaped agent that takes structured input and returns structured output, Invocations gives you the flexibility.

## The Deployment Flow with `azd`

When you run `azd up` with a MAF agent:

1. Optionally creates a Foundry project and deploys a model
2. Packages your code and pushes an image to Azure Container Registry
3. Provisions compute from the ACR image
4. Assigns a dedicated Entra ID to the agent
5. Exposes a stable endpoint (`https://{project_endpoint}/agents/{agent_name}`)
6. Handles everything else from that point on

Sessions persist for up to 30 days. Idle compute is deprovisioned after 15 minutes and restored transparently on the next request. From the agent's perspective, nothing changed.

## Wrapping Up

The distance between "working locally" and "running in production" has historically been long and painful for AI agents. Foundry Hosted Agents + MAF closes that gap significantly. If you already have a local agent built with Agent Framework, this is worth trying today.

The team says GA is coming soon — this is currently in preview. Check the [MAF Hosted Agent Integration docs](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) and the [.NET samples](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) to get started.

Original article: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
