---
title: "Cosmos DB Shell Is in Public Preview — And It Has an MCP Server Built In"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell is a new open-source CLI that exposes database commands as MCP tools. Your AI agents can navigate containers, run queries, and manage data using the same interface you use."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

If you've ever had to bounce between a portal tab, an SDK sample, and a half-finished script just to answer one Cosmos DB question, you already know the friction this project is designed to remove.

Azure Cosmos DB Shell just entered public preview. It's an open-source CLI with bash-like syntax and — the part that makes this interesting — an integrated MCP server.

## What Makes This Different From Other Database CLIs

The CLI itself is useful: familiar commands, scripting support, CI/CD integration. That part is table stakes for a developer-focused database tool.

The interesting part is the MCP server integration. Every command the CLI exposes becomes available as an MCP tool that your AI agents can call. There's no custom API layer, no integration code to write. Your agent can:

- Navigate database hierarchies with `cd`, `ls`, `pwd`
- Run SQL queries with `query` and get structured results back
- Create and modify items with `create item`, `update`, `rm`
- Manage databases and containers with `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Inspect current context with `endpoint`, `pwd`

The key shift: your agent isn't talking to a Cosmos DB API — it's talking to the same shell interface you use. The commands are deterministic, auditable, and open source so you can inspect exactly what's happening.

## The Open-Source Foundation Matters

This isn't a black-box managed service. The shell is open source, which means:

- Security teams can audit the implementation
- Platform teams can fork and extend it for their specific standards
- Developers can contribute improvements that benefit everyone

For enterprise teams adopting AI tooling, "can we see exactly how it works" is increasingly not an optional requirement. Open source here is a meaningful differentiator.

## Three Scenarios That Become Easier

**Intelligent data analysis** — connect an agent to the shell, ask natural language questions, get structured query results. The agent handles the query construction; the shell handles execution.

**Autonomous data management** — workflows that need to create, update, or remove data in Cosmos DB can do so through the MCP tools without needing a custom integration.

**Real-time monitoring and alerts** — an agent can periodically query containers, compare results, and surface anomalies through whatever notification channel makes sense.

The MCP interface makes these scenarios composable with any AI platform that speaks MCP — not just Microsoft's tooling.

## Getting Started

The shell is in public preview. Install it, configure your Cosmos DB connection, and enable the MCP server. From there, any MCP-compatible agent host can discover and use the tools.

Original post: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
