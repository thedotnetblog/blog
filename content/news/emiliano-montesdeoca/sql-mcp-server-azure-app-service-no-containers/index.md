---
title: "SQL MCP Server on Azure App Service — No Containers Required"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "The SQL MCP Server can now run on Azure App Service without Docker or Kubernetes. Here's what that means for .NET developers building AI agents that talk to SQL databases."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

Let me be honest with you: every time I see "requires a container" in a tutorial, a little part of me sighs. Containers are great — until your team doesn't have a container strategy, and suddenly a feature that looked simple is blocked behind orchestration overhead you didn't plan for.

That's why this one caught my eye. The SQL MCP Server can now run on Azure App Service — no Docker, no Kubernetes, just the same Data API builder (DAB) configuration that exposes your SQL database through MCP, REST, and GraphQL.

## What's SQL MCP Server, Again?

Quick context if you haven't run into it yet. SQL MCP Server sits between your AI agent and your SQL database. Instead of giving your agent direct database access (which is a terrible idea), it exposes your tables and views as an abstraction layer — entities with defined permissions.

It's built on top of [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/), which means one configuration file drives MCP *and* REST *and* GraphQL simultaneously. Your agent talks to the MCP endpoint. Your traditional app talks to REST or GraphQL. Same config, same runtime, different surfaces.

That's genuinely useful. You're not maintaining two separate API layers.

## The Container Problem (and the Solution)

The original deployment model for SQL MCP Server was containers. That works well in many shops — but not all. Plenty of .NET teams standardize on Azure App Service or VMs. Requiring a container runtime just to expose a SQL endpoint adds friction nobody asked for.

The new walkthrough shows you how to skip the container entirely. The whole thing runs with a `dab start` command, hosted on App Service as a standard .NET 8 web process.

Here's the local setup flow in a nutshell:

```bash
# Install Data API builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Initialize the configuration
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Add an entity
dab add products --source dbo.products --permissions "authenticated:*"

# Configure App Service auth provider
dab configure --runtime.host.authentication.provider AppService

# Start the server
dab start
```

At this point you have MCP at `/mcp`, REST and GraphQL from the same process, and nothing running in a container.

## Authentication That Doesn't Involve Shared API Keys

This is the part I appreciate most. When you deploy to App Service, you configure Microsoft Entra ID as the authentication provider. No shared secrets embedded in config files, no API keys to rotate.

The connection string stays in an App Service environment variable (not in `dab-config.json`), and the MCP endpoint is protected by platform authentication. If you're already aligned to Entra ID across your Azure workloads — which you probably are if you're using Azure AI Foundry agents — this fits naturally.

For local development, you switch to `Simulator` mode and STDIO transport. Flip back to `AppService` mode when deploying. Clean and explicit.

## Deploying to App Service

The actual deployment is straightforward Azure CLI work:

```bash
# Create the App Service plan
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

# Create the web app (.NET 8 runtime)
az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

# Set the startup command
az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Then deploy your DAB project using whatever code deployment path your team already uses — VS Code, GitHub Actions, Zip Deploy. The key detail: it's a **code** deployment, not a container deployment. No image to build, push, or manage.

## Why This Matters for .NET Developers

If you're building AI agents in .NET — whether with the Microsoft Agent Framework, Semantic Kernel, or Azure AI Foundry hosted agents — eventually your agent needs to talk to a database. SQL MCP Server gives you a structured way to do that without exposing raw connection strings or writing a custom API layer.

Running it on App Service closes the gap for teams that aren't running containers. It's the same DAB config, the same Entra auth, the same MCP protocol — just on infrastructure you already know.

Check out the full walkthrough in the [original blog post](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) and the [sample repo on GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Wrapping Up

The SQL MCP Server on App Service is a solid pragmatic option for .NET teams that want to give their agents structured access to SQL data without a container strategy. The combination of DAB's entity model, App Service's built-in Entra auth, and the `dab start` startup command makes for a deployment that's simple to explain and easy to operate.

Give it a try. Your agents will appreciate the clean API surface. Your ops team will appreciate not having to deal with container registries.
