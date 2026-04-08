---
title: "Connect Your MCP Servers on Azure Functions to Foundry Agents — Here's How"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Build your MCP server once, deploy it to Azure Functions, and connect it to Microsoft Foundry agents with proper auth. Your tools work everywhere — VS Code, Cursor, and now enterprise AI agents."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

Here's something I love about the MCP ecosystem: you build your server once, and it works everywhere. VS Code, Visual Studio, Cursor, ChatGPT — every MCP client can discover and use your tools. Now, Microsoft is adding another consumer to that list: Foundry agents.

Lily Ma from the Azure SDK team [published a practical guide](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) on connecting MCP servers deployed to Azure Functions with Microsoft Foundry agents. If you already have an MCP server, this is pure value-add — no rebuilding required.

## Why this combination makes sense

Azure Functions gives you scalable infrastructure, built-in auth, and serverless billing for hosting MCP servers. Microsoft Foundry gives you AI agents that can reason, plan, and take actions. Connecting the two means your custom tools — querying a database, calling a business API, running validation logic — become capabilities that enterprise AI agents can discover and use autonomously.

The key point: your MCP server stays the same. You're just adding Foundry as another consumer. The same tools that work in your VS Code setup now power an AI agent your team or customers interact with.

## Authentication options

This is where the post really adds value. Four auth methods depending on your scenario:

| Method | Use Case |
|--------|----------|
| **Key-based** (default) | Development or servers without Entra auth |
| **Microsoft Entra** | Production with managed identities |
| **OAuth identity passthrough** | Production where each user authenticates individually |
| **Unauthenticated** | Dev/testing or public data only |

For production, Microsoft Entra with agent identity is the recommended path. OAuth identity passthrough is for when user context matters — the agent prompts users to sign in, and each request carries the user's own token.

## Setting it up

The high-level flow:

1. **Deploy your MCP server to Azure Functions** — samples available for [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript, and Java
2. **Enable built-in MCP authentication** on your function app
3. **Get your endpoint URL** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Add the MCP server as a tool in Foundry** — navigate to your agent in the portal, add a new MCP tool, provide endpoint and credentials

Then test it in the Agent Builder playground by sending a prompt that would trigger one of your tools.

## My take

The composability story here is getting really strong. Build your MCP server once in .NET (or Python, TypeScript, Java), deploy to Azure Functions, and every MCP-compatible client can use it — coding tools, chat apps, and now enterprise AI agents. That's a "write once, use everywhere" pattern that actually works.

For .NET developers specifically, the [Azure Functions MCP extension](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) makes this straightforward. You define your tools as Azure Functions, deploy, and you've got a production-grade MCP server with all the security and scaling Azure Functions provides.

## Wrapping up

If you have MCP tools running on Azure Functions, connecting them to Foundry agents is a quick win — your custom tools become enterprise AI capabilities with proper auth and no code changes to the server itself.

Read the [full guide](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) for step-by-step instructions on each authentication method, and check the [detailed docs](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) for production setups.
