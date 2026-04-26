---
title: "SQL Server 2025 as Your Agent-Ready Database: Security, Backup, and MCP in One Engine"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "The final part of the Polyglot Tax series tackles the hard production problems: unified Row-Level Security across relational, JSON, graph, and vector data — plus cryptographic audit trails and MCP integration that make SQL Server 2025 genuinely agent-ready."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

I've been following the Polyglot Tax series by Aditya Badramraju with a lot of interest. Parts 1-3 built a compelling case for SQL Server 2025 as a genuinely multi-model database — JSON, graph, vectors, and relational data all in one engine with a unified query planner. Part 4 closes the series with the parts that actually determine whether you'd trust this architecture in production.

Spoiler: the production story is solid.

## One Security Model to Rule All Data Models

Here's the thing with polyglot stacks: when an auditor asks "prove that Tenant A cannot see Tenant B's data," you have to answer that question for each database independently. Five databases, five security models, five proofs.

With SQL Server 2025, you define one Row-Level Security policy and it covers every data model:

```sql
CREATE FUNCTION dbo.fn_TenantFilter(@TenantID INT)
RETURNS TABLE WITH SCHEMABINDING
AS RETURN SELECT 1 AS fn_result
WHERE @TenantID = CAST(SESSION_CONTEXT(N'TenantID') AS INT);

CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Customers,     -- Relational
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Events,        -- JSON data
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Relationships, -- Graph edges
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Embeddings     -- Vector data
WITH (STATE = ON);
```

From that point, every query — relational joins, JSON path queries, graph traversals, vector similarity searches — is automatically filtered by tenant. The engine injects the predicate into the execution plan before any data leaves storage. Your calling code doesn't need `WHERE TenantID = @id` everywhere. You test the policy once.

The layers compose further: Dynamic Data Masking for columns that shouldn't show full values to certain roles, Always Encrypted for end-to-end encryption (even DBAs can't read it), and stored procedures as the permission boundary so agents only call what you explicitly exposed.

This is the part of the architecture that matters most for compliance-heavy SaaS. One policy, one proof.

## Unified Backup = Atomic Recovery

One statement, all data models, consistent point in time:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

In a polyglot stack, point-in-time recovery across five databases means coordinating five restore operations and hoping the timestamps line up within a second or two. For financial data, that two-second inconsistency is unacceptable. With one database, one transaction log, one restore — recovery is atomic by definition.

## Ledger Tables for Tamper-Evident Audit Trails

For regulated industries, you need more than "we have logs." You need cryptographic proof that those logs weren't modified:

```sql
CREATE TABLE FinancialTransactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount MONEY NOT NULL,
    TransactionType NVARCHAR(20),
    TransactionDate DATETIME2 DEFAULT SYSUTCDATETIME()
)
WITH (SYSTEM_VERSIONING = ON, LEDGER = ON);
```

Every insert, update, and delete gets cryptographically hashed into a blockchain-style structure. You can prove to an auditor — mathematically — that a row hasn't been tampered with since it was written. In a polyglot stack, this capability doesn't exist uniformly across all your databases.

## MCP Integration: Agents Without Hand-Coded Middleware

The series built toward this: SQL Server 2025 supports the SQL MCP Server directly, which means your agents can call the database through natural language tool calls without you writing middleware for every operation.

Combine that with stored procedures as the permission boundary and Row-Level Security enforced at the engine, and you have a model where:

1. Agent calls a tool (e.g., "get customer context for account 12345")
2. MCP translates to the stored procedure you defined
3. SQL engine enforces tenant isolation and column masking automatically
4. Agent gets exactly the data it's allowed to see

No middleware layer. No ad-hoc query injection risk. The engine handles authorization, not the agent.

## Why This Matters for .NET Developers

If you're building .NET services with SQL Server as your primary store, the message from this series is: you don't need to add Redis for caching, a graph DB for relationships, or a vector store for embeddings. SQL Server 2025 handles all of that — with better operational consistency than a polyglot stack and unified security that's actually auditable.

The MCP integration means your Semantic Kernel agents or Microsoft Agent Framework workflows can interact with your data tier through the same SQL MCP Server, with the same security guarantees you'd enforce for human queries.

## Wrapping up

The Polyglot Tax series is worth reading end-to-end. Parts 1-3 prove the query planner story. Part 4 proves the production story. For .NET developers building agent-first or AI-augmented applications on Azure SQL, this architecture deserves serious consideration.

Original post by Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
