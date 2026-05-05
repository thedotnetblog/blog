---
title: "SQL MCP Server — Właściwy Sposób na Danie Agentom AI Dostępu do Bazy Danych"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server z Data API builder daje agentom AI bezpieczny, deterministyczny dostęp do bazy danych bez ujawniania schematów lub polegania na NL2SQL."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "sql-mcp-server-data-api-builder" >}}).*

Będąc szczerym: większość dostępnych dziś serwerów MCP dla baz danych jest przerażająca. Biorą zapytanie w języku naturalnym, generują SQL w locie i uruchamiają go na twoich danych produkcyjnych.

Zespół Azure SQL właśnie [przedstawił SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), i przyjmuje fundamentalnie inne podejście.

## Dlaczego nie NL2SQL?

Modele nie są deterministyczne. SQL MCP Server używa podejścia **NL2DAB**. Agent pracuje z warstwą abstrakcji encji Data API builder, aby deterministycznie produkować dokładne T-SQL.

## Siedem narzędzi, nie siedemset

SQL MCP Server udostępnia dokładnie siedem narzędzi DML:

- `describe_entities` — odkryj dostępne encje
- `create_record` — wstawiaj wiersze
- `read_records` — zapytuj tabele i widoki
- `update_record` — modyfikuj wiersze
- `delete_record` — usuń wiersze
- `execute_entity` — uruchamiaj procedury składowane
- `aggregate_records` — zapytania agregujące

## Pierwsze kroki w trzech poleceniach

```bash
dab init   --database-type mssql   --connection-string "@env('sql_connection_string')"

dab add Customers   --source dbo.Customers   --permissions "anonymous:*"

dab start
```

## Historia bezpieczeństwa jest solidna

RBAC na każdej warstwie, integracja Azure Key Vault, Microsoft Entra + niestandardowy OAuth.

Sprawdź [pełny post](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) i [dokumentację](https://aka.ms/sql/mcp).
