---
title: "T-SQL Regex on 2 MB Blobs: No More Truncation, Less Application Code"
description: "Azure SQL and SQL Server 2025 CU5 extend all seven native T-SQL regex functions to varchar(max) and nvarchar(max) inputs up to 2 MB."
date: 2026-09-11
author: "Emiliano Montesdeoca"
tags: [azure-sql, t-sql, regular-expressions, lob-types, sql-server-2025]
slug: azure-sql-regex-lob-types
---

Original source: [Regex support for LOB types in T-SQL—available in Azure SQL & SQL Server 2025](https://devblogs.microsoft.com/azure-sql/regex-support-for-lob-types-in-t-sql-available-in-azure-sql-sql-server-2025/)

## The Problem This Removes

A table full of logs, HTML documents, or large JSON payloads often leads to an awkward split: the database stores the text, while .NET code exports it for pattern matching, redaction, or extraction. That adds network round-trips and scatters data-processing logic across two layers.

Native T-SQL regex already reduced that need, but large-object support was incomplete. SQL Server 2025 CU5 closes the gap: all seven regex functions accept `varchar(max)` and `nvarchar(max)` inputs up to 2 MB. Azure SQL Database, SQL Database in Fabric, and Azure SQL Managed Instance with the relevant update policy also support the capability.

The practical result is that common logs, HTML pages, and JSON payloads no longer need to be truncated to 8,000 bytes or split merely to run a regex operation.

## What Changed in CU5

At the original SQL Server 2025 general availability release, LOB inputs were supported on `REGEXP_LIKE`, `REGEXP_COUNT`, and `REGEXP_INSTR`. The remaining scalar functions and table-valued functions required non-LOB strings. CU5 brings all seven functions to the same 2 MB input limit:

- `REGEXP_LIKE` filters rows.
- `REGEXP_COUNT` counts occurrences.
- `REGEXP_INSTR` locates a match.
- `REGEXP_REPLACE` redacts or cleanses text.
- `REGEXP_SUBSTR` extracts one value.
- `REGEXP_MATCHES` returns matches and capture groups as rows.
- `REGEXP_SPLIT_TO_TABLE` shreds text into rows by a regex delimiter.

The pattern remains capped at 8,000 bytes. The 2 MB limit applies to the input passed to one function call, not to the maximum size of the `varchar(max)` or `nvarchar(max)` column.

The engine uses RE2, a linear-time, non-backtracking implementation. That matters when patterns run against large or untrusted text because the engine avoids catastrophic backtracking behavior.

## The Set-Based Advantage

The source's examples use a `LogEntries` table with a `RawPayload` `varchar(max)` column. The same payload can be filtered for HTTP 5xx responses, counted for request methods, searched for the first error position, or passed through nested `REGEXP_REPLACE` calls to redact credit-card, SSN, and email-shaped values.

`REGEXP_MATCHES` is especially useful when the output should become relational data. It returns one row per match, including the matched value and JSON describing capture groups. `REGEXP_SPLIT_TO_TABLE` can turn a multi-line payload into one row per line. Those results can feed a CTE, an aggregate, a join, or a staging table without first moving the document into application memory.

For a .NET application, this can simplify the boundary. If the transformation is fundamentally a database filter or cleanse, keep it close to the data and return the smaller result set to the application. That does not mean every regex belongs in SQL. Business rules that depend on domain services, external APIs, or rich application types may still belong in C#.

## Prerequisites to Check

SQL Server requires CU5 or later. The feature is also available in the Azure SQL services described by the source, with Managed Instance availability depending on the update policy and regional rollout.

The two table-valued functions require compatibility level 170 unless the preview database-scoped configuration that enables built-in TVFs at other levels is used. The source also notes that `REGEXP_LIKE` requires compatibility level 170, while the other scalar functions are available at all compatibility levels.

Check the database before changing a query:

```sql
SELECT name, compatibility_level
FROM sys.databases
WHERE name = DB_NAME();
```

The 2 MB ceiling is measured in UTF-8 bytes, not simply characters. ASCII input can approach two million characters, while non-ASCII text consumes more bytes. A value above `2 * 1024 * 1024` bytes is rejected with error 19311 rather than silently truncated. If individual values are larger, split them into logical units at ingestion rather than inventing a query-time workaround.

## A Better .NET Decision Boundary

If the current code reads a large database value into .NET only to run a regex, audit it. A SQL-side implementation may reduce I/O, application CPU, and synchronization risk. Compare query plans and database resource usage; moving work into SQL is not automatically cheaper when the pattern is expensive or the data is poorly indexed.

Keep parameterization and authorization intact. A regex operation can cleanse data, but it does not replace access control or validation. Test multiline flags, capture-group semantics, Unicode behavior, and the exact byte-size boundary with representative payloads.

## Recommendations

1. Inventory application code that exports database text only for regex processing.
2. Test the seven functions on Azure SQL or SQL Server 2025 CU5 with representative LOBs.
3. Verify compatibility level and the 2 MB UTF-8 byte limit.
4. Keep oversized values logically partitioned at ingestion.
5. Compare SQL and .NET performance before moving high-volume transformations.

CU5 completes the native regex story for large objects. The useful change is not merely that a bigger string is accepted; it is that filtering, extraction, redaction, and shredding can remain set-based and close to the data.