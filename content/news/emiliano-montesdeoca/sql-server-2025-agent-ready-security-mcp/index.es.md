---
title: "SQL Server 2025 como Base de Datos Lista para Agentes: Seguridad, Backup y MCP en un Solo Motor"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "La parte final de la serie Polyglot Tax aborda los problemas difíciles de producción: seguridad unificada de Row-Level Security en datos relacionales, JSON, grafos y vectores, más integración MCP que hace a SQL Server 2025 genuinamente listo para agentes."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

He seguido la serie Polyglot Tax de Aditya Badramraju con mucho interés. Las partes 1-3 construyeron un caso convincente para SQL Server 2025 como una base de datos genuinamente multi-modelo. La parte 4 cierra la serie con las partes que realmente determinan si confiarías en esta arquitectura en producción.

## Un Modelo de Seguridad para Todos los Modelos de Datos

```sql
CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID) ON dbo.Customers,
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID) ON dbo.Events,
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID) ON dbo.Relationships,
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID) ON dbo.Embeddings
WITH (STATE = ON);
```

Una política, una prueba. Para un auditor que pregunta "demuestra que el Tenant A no puede ver los datos del Tenant B", esto es oro.

## Backup Unificado = Recuperación Atómica

```sql
RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

En un stack políglota, coordinar la recuperación de cinco bases de datos es una pesadilla de consistencia. Con una sola base de datos y un log de transacciones, la recuperación es atómica por definición.

## Integración MCP: Agentes Sin Middleware Codificado a Mano

SQL Server 2025 soporta el SQL MCP Server directamente. Los agentes llaman herramientas, el motor impone aislamiento de tenant y enmascaramiento de columnas automáticamente.

## Resumiendo

Para desarrolladores .NET construyendo aplicaciones con agentes en Azure SQL, esta arquitectura merece consideración seria. Post original de Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
