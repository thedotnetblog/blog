---
title: "SQL Server 2025 als Agent-Ready Datenbank: Sicherheit, Backup und MCP in einer Engine"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Der letzte Teil der Polyglot Tax Serie tackles die harten Produktionsprobleme: vereinheitlichte Row-Level Security über relationale, JSON-, Graph- und Vektordaten, plus MCP-Integration."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Ich habe die Polyglot Tax Serie von Aditya Badramraju mit großem Interesse verfolgt. Teile 1-3 lieferten den Beweis für SQL Server 2025 als echte Multi-Modell-Datenbank. Teil 4 schließt die Serie mit den Teilen, die wirklich bestimmen, ob du dieser Architektur in Produktion vertrauen würdest.

## Ein Sicherheitsmodell für alle Datenmodelle

Eine Row-Level Security Policy, die alle Datenmodelle abdeckt — relationale Tabellen, JSON-Events, Graph-Edges, Vektoren. Eine Policy, ein Audit, ein Nachweis.

## Einheitliches Backup = Atomare Wiederherstellung

In einem polyglottes Stack bedeutet Point-in-Time Recovery fünf koordinierte Restore-Operationen und die Hoffnung, dass die Timestamps übereinstimmen. Mit einer Datenbank ist die Wiederherstellung per Definition atomar.

## MCP-Integration: Agenten Ohne Hand-codierten Middleware

SQL Server 2025 unterstützt den SQL MCP Server direkt. Agenten rufen Tools auf, die Engine erzwingt Tenant-Isolierung und Column-Masking automatisch.

## Fazit

Für .NET-Entwickler, die agenten-first Anwendungen auf Azure SQL bauen, verdient diese Architektur ernsthafte Überlegung. Originalpost von Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
