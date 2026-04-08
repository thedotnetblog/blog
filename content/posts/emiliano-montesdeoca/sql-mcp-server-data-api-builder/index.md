---
title: "SQL MCP Server — The Right Way to Give AI Agents Database Access"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server from Data API builder gives AI agents secure, deterministic database access without exposing schemas or relying on NL2SQL. RBAC, caching, multi-database support — all built in."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

Let's be honest: most database MCP servers available today are terrifying. They take a natural language query, generate SQL on the fly, and run it against your production data. What could go wrong? (Everything. Everything could go wrong.)

The Azure SQL team just [introduced SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), and it takes a fundamentally different approach. Built as a feature of Data API builder (DAB) 2.0, it gives AI agents structured, deterministic access to database operations — without NL2SQL, without exposing your schema, and with full RBAC at every step.

## Why no NL2SQL?

This is the most interesting design decision. Models aren't deterministic, and complex queries are the most likely to produce subtle errors. The exact queries users hope AI can generate are also the ones that need the most scrutiny when produced non-deterministically.

Instead, SQL MCP Server uses an **NL2DAB** approach. The agent works with Data API builder's entity abstraction layer and built-in query builder to produce accurate, well-formed T-SQL deterministically. Same result for the user, but without the risk of hallucinated JOINs or accidental data exposure.

## Seven tools, not seven hundred

SQL MCP Server exposes exactly seven DML tools, regardless of database size:

- `describe_entities` — discover available entities and operations
- `create_record` — insert rows
- `read_records` — query tables and views
- `update_record` — modify rows
- `delete_record` — remove rows
- `execute_entity` — run stored procedures
- `aggregate_records` — aggregation queries

This is smart because context windows are the agent's thinking space. Flooding them with hundreds of tool definitions leaves less room for reasoning. Seven fixed tools keep the agent focused on *thinking* rather than *navigating*.

Each tool can be individually enabled or disabled:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Getting started in three commands

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

That's a running SQL MCP Server exposing your Customers table. The entity abstraction layer means you can alias names and columns, limit fields per role, and control exactly what agents see — without exposing internal schema details.

## The security story is solid

This is where Data API builder's maturity pays off:

- **RBAC at every layer** — each entity defines which roles can read, create, update, or delete, and which fields are visible
- **Azure Key Vault integration** — connection strings and secrets managed securely
- **Microsoft Entra + custom OAuth** — production-grade authentication
- **Content Security Policy** — agents interact through a controlled contract, not raw SQL

The schema abstraction is particularly important. Your internal table and column names never get exposed to the agent. You define entities, aliases, and descriptions that make sense for the AI interaction — not your database ERD.

## Multi-database and multi-protocol

SQL MCP Server supports Microsoft SQL, PostgreSQL, Azure Cosmos DB, and MySQL. And because it's a DAB feature, you get REST, GraphQL, and MCP endpoints simultaneously from the same configuration. Same entity definitions, same RBAC rules, same security — across all three protocols.

Auto-configuration in DAB 2.0 can even inspect your database and build the configuration dynamically, if you're comfortable with less abstraction for rapid prototyping.

## My take

This is how enterprise database access for AI agents should work. Not "hey LLM, write me some SQL and YOLO it against production." Instead: a well-defined entity layer, deterministic query generation, RBAC at every step, caching, monitoring, and telemetry. It's boring in the best possible way.

For .NET developers, the integration story is clean — DAB is a .NET tool, the MCP Server runs as a container, and it works with Azure SQL, which most of us are already using. If you're building AI agents that need data access, start here.

## Wrapping up

SQL MCP Server is free, open-source, and runs anywhere. It's the prescriptive approach from Microsoft for giving AI agents secure database access. Check out the [full post](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) and the [documentation](https://aka.ms/sql/mcp) to get started.
