---
title: "SQL MCP Server, Copilot in SSMS, and a Database Hub with AI Agents: What Actually Matters from SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft dropped a stack of database announcements at SQLCon 2026. Here's the stuff that actually matters if you're building AI-powered apps on Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft just kicked off [SQLCon 2026 alongside FabCon in Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/), and there's a lot to unpack. The original announcement covers everything from savings plans to enterprise compliance features. I'm going to skip the enterprise pricing slides and focus on the pieces that matter if you're a developer building things with Azure SQL and AI.

## SQL MCP Server is in public preview

This is the headline for me. Azure SQL Database Hyperscale now has a **SQL MCP Server** in public preview that lets you securely connect your SQL data to AI agents and Copilots using the [Model Context Protocol](https://modelcontextprotocol.io/).

If you've been following the MCP wave — and honestly, it's hard to miss right now — this is a big deal. Instead of building custom data pipelines to feed your AI agents context from your database, you get a standardized protocol to expose SQL data directly. Your agents can query, reason over, and act on live database information.

For those of us building AI agents with Semantic Kernel or the Microsoft Agent Framework, this opens up a clean integration path. Your agent needs to check inventory? Look up a customer record? Validate an order? MCP gives it a structured way to do that without you writing bespoke data-fetching code for every scenario.

## GitHub Copilot in SSMS 22 is now GA

If you spend any time in SQL Server Management Studio — and let's be honest, most of us still do — GitHub Copilot is now generally available in SSMS 22. Same Copilot experience you already use in VS Code and Visual Studio, but for T-SQL.

The practical value here is straightforward: chat-based assistance for writing queries, refactoring stored procedures, troubleshooting performance issues, and handling admin tasks. Nothing revolutionary in concept, but having it right there in SSMS means you don't need to context-switch to another editor just to get AI help with your database work.

## Vector indexes got a serious upgrade

Azure SQL Database now has faster, more capable vector indexes with full insert, update, and delete support. That means your vector data stays current in real time — no batch reindexing needed.

Here's what's new:
- **Quantization** for smaller index sizes without losing too much accuracy
- **Iterative filtering** for more precise results
- **Tighter query optimizer integration** for predictable performance

If you're doing retrieval-augmented generation (RAG) with Azure SQL as your vector store, these improvements are directly useful. You can keep your vectors alongside your relational data in the same database, which simplifies your architecture significantly compared to running a separate vector database.

The same vector enhancements are also available in SQL database in Fabric, since both run on the same SQL engine underneath.

## Database Hub in Fabric: agentic management

This one is more forward-looking, but it's interesting. Microsoft announced the **Database Hub in Microsoft Fabric** (early access), which gives you a single pane of glass across Azure SQL, Cosmos DB, PostgreSQL, MySQL, and SQL Server via Arc.

The interesting angle isn't just the unified view — it's the agentic approach to management. AI agents continuously monitor your database estate, surface what changed, explain why it matters, and suggest what to do next. It's a human-in-the-loop model where the agent does the legwork and you make the calls.

For teams managing more than a handful of databases, this could genuinely reduce the operational noise. Instead of jumping between portals and manually checking metrics, the agent brings the signal to you.

## What this means for .NET developers

The thread connecting all these announcements is clear: Microsoft is embedding AI agents at every layer of the database stack. Not as a gimmick, but as a practical tooling layer.

If you're building .NET apps backed by Azure SQL, here's what I'd actually do:

1. **Try the SQL MCP Server** if you're building AI agents. It's the cleanest way to give your agents database access without custom plumbing.
2. **Enable Copilot in SSMS** if you haven't already — free productivity win for daily SQL work.
3. **Look into vector indexes** if you're doing RAG and currently running a separate vector store. Consolidating to Azure SQL means one less service to manage.

## Wrapping up

The full announcement has more — savings plans, migration assistants, compliance features — but the developer story is in the MCP Server, the vector improvements, and the agentic management layer. These are the pieces that change how you build, not just how you budget.

Check out the [full announcement from Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) for the complete picture, and [sign up for the Database Hub early access](https://aka.ms/database-hub) if you want to try the new management experience.
