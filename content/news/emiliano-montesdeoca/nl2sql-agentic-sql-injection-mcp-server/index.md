---
title: "NL2SQL Is the SQL Injection of the Agentic Age"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Before you let an agent query your database with natural language, read this. NL2SQL looks simple until you think through schema completeness, indeterminism, and what SQL MCP Server actually solves."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

There's a version of the NL2SQL pitch that sounds perfect: users ask questions in natural language, agents generate SQL, data comes back. Fewer screens, fewer queries, less code. Simple.

Then you think about it for five more minutes.

## The Problems Nobody Talks About in the Demo

**Schemas weren't designed to explain things.** Cryptic table names, inconsistent column names, technically valid relationships that are semantically invalid without additional predicates — these are normal for enterprise databases. They're not bugs, they're just the accumulated history of business changes. But when you ask a model to infer intent from a schema that wasn't designed to communicate intent, the model will try anyway. It won't give up. It'll generate its best-effort query and return results with confidence.

**Models are not deterministic.** Ask the same question about the same database twice and you might get different SQL. The model is calculating probabilities, and slight variations in context drive different outputs. You cannot test your way to a guarantee that the agent always generates the right query.

**User review doesn't scale.** "Just review every query before execution" sounds safe. But it assumes users are experts in both the data model and SQL — exactly the people who didn't need the natural language interface. It also introduces cognitive overload and a new class of confirmation bias, where users overwhelmed by query complexity approve invalid queries rather than investigate them.

**And then there's injection.** In traditional SQL development, parameterization solved injection because user input filled parameters, not SQL structure. With NL2SQL, the model is generating the SQL itself. The prompt, schema context, conversation history, and retrieved data all influence what gets executed. If someone crafts a prompt that changes what the model generates, that's injection — not at the parameter level, but at the query generation level. And unlike dropping a table (obvious, recoverable), NL2SQL injection produces queries that return incorrect results with no visible error. Business decisions get made on wrong data.

## What SQL MCP Server Actually Solves

This is where the article makes its most useful practical point. Instead of giving an agent arbitrary schema access and hoping for the best, SQL MCP Server exposes a **curated API surface** built on top of [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

The difference matters: the agent doesn't generate SQL. It calls named endpoints that return predefined result shapes. The SQL is written once, by a developer, and is deterministic. The agent's nondeterminism is limited to choosing *which* endpoint to call, not constructing arbitrary queries.

This is analogous to what parameterization did for SQL injection in the traditional app model — you remove the ability to construct arbitrary queries from untrusted input.

## The Right Question

The article doesn't say "never use NL2SQL." It says: be deliberate about *where* you apply it and *what* you expose. For exploratory analysis in a controlled environment, with a scoped schema and read-only access, NL2SQL might be fine. For production systems where business decisions depend on the results, a curated API layer is significantly safer.

Honesty: some problems are genuinely better solved with structured queries behind named endpoints than with natural language to SQL. SQL MCP Server gives you that option without abandoning the agentic interface entirely.

Original post: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
