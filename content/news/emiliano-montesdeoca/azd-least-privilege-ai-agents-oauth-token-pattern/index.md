---
title: "Your AI Agent Has an Identity Problem (And Here's the Template That Solves It)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "A new azd template from Curity and Microsoft shows how to build AI agents that use short-lived OAuth tokens with fine-grained scopes — so agents can never see data they shouldn't."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

There's a moment in every AI agent project that goes something like this: the demo works perfectly, the agent interprets natural language, calls the right APIs, returns the right data. Then you start thinking about real users.

What stops one user's agent session from seeing another user's data? What if the agent is tricked through prompt injection? What if it calls a tool in an unexpected way?

These aren't edge cases. They're design decisions you need to make before shipping.

A new `azd` template from Curity and Microsoft gives you a working reference for exactly this problem.

## The Core Problem: Authentication ≠ Authorization

Most agent samples handle user authentication well. They handle authorization poorly. Knowing *who* the user is doesn't tell you *what data* they should see.

A traditional client app makes predictable API calls. An AI agent is nondeterministic — it interprets natural language and decides what to call. It can be creative. It can also be wrong. And if it's manipulated through prompt injection, you need rules that don't depend on the AI being well-behaved.

The solution this template demonstrates: **short-lived tokens that carry exactly the right information for each hop**.

## How the Token Chain Works

The template uses OAuth 2.0 access tokens with token exchange to narrow permissions at each step. A user token gets exchanged twice before it reaches the MCP server:

1. **First exchange** — narrows the scope and converts the opaque token to a JWT
2. **Second exchange** — adds the agent identity and a new audience for the MCP server hop

What the MCP server token looks like:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

The `customer_id` is baked into the token by the authorization server, not passed as a parameter the agent controls. The API checks the token, not the agent's instructions.

This means: even if someone tricks the agent into trying to fetch another customer's data, the token won't authorize it.

## What the Template Deploys

With a few `azd` commands you get:

- A backend agent on Microsoft Foundry (C#, Microsoft A2A and MCP SDKs)
- An MCP server exposing a sample portfolio API
- Curity Identity Server as the authorization server, alongside Entra ID for authentication
- External and internal API gateways handling token exchange and audit logging
- Bicep for all the Azure infrastructure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, storage

The whole pattern is inspectable and customizable.

## The Design Principle Worth Borrowing

Even if you don't use Curity, the pattern is transferable: **agents should never hold permanent API access**. Every action should use a short-lived token with the minimum scope needed for that specific call, issued to the specific agent identity, carrying the claims the API needs to make authorization decisions.

This holds up against creative agents, mistakes, and prompt injection in ways that "just make sure the agent doesn't do bad things" never will.

## Wrapping Up

Security patterns for AI agents are still being worked out across the industry. This template is one of the more complete reference implementations I've seen — it covers the actual authorization flow, not just authentication.

Original post: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
