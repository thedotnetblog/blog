---
title: "The Real Frontier for Agentic SQL: Auditability with OBO in SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "On-Behalf-Of authentication in Data API builder plus SQL MCP Server is a major governance milestone because Azure SQL can finally audit the human behind an agent action."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

There is a painful truth in enterprise AI projects: many teams obsess over model quality and ignore accountability. When an agent writes or reads production data, the first incident review question is not “was the answer good?” It is “who actually did this?”

Original source: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

This is why OBO support in Data API builder 2.0 with SQL MCP Server is a bigger deal than it first appears. Username/password and managed identity approaches still work operationally, but both collapse identity into the service boundary. Logs show the app or middleware, not the human request origin. That is acceptable for simple automation. It is not acceptable for regulated agentic workflows.

With OBO, SQL authenticates the delegated user context, not the tool host identity. That gives you a fundamentally better audit model: user principal, action, statement context, and middle-tier app identifier together. You get traceability without losing the control surface of MCP tools and DAB entity permissions.

My opinion is firm here: if your agent can touch sensitive SQL data, OBO should be your default architecture, not an optional hardening task. The setup is more involved, but identity debt is always paid later, usually during security incidents, compliance audits, or executive escalations.

Practical implementation guidance:

Start by validating identity flow with a minimal “WhoAmI” view and automated checks in integration tests. If the SQL principal does not match the signed-in user, stop and fix before shipping. Next, wire Log Analytics queries for SQLSecurityAuditEvents into your SOC dashboards and alert on high-risk actions initiated through OBO paths. Finally, align RBAC and DAB permissions so user-level identity and action-level authorization stay consistent end to end.

One subtle but important design point in the announcement is cache behavior. DAB explicitly blocks response caching when user-delegated auth is enabled. That tradeoff is correct. Performance tricks that can leak user-scoped outcomes are not worth it in multi-tenant or regulated environments.

SQL MCP Server plus OBO is the beginning of a mature pattern: agents as controlled operators, users as accountable principals, data planes as auditable systems. If your architecture cannot answer “who did this” with confidence, it is not production-ready AI, no matter how polished the demo looks.
