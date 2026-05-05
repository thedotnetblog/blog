---
title: "SQL MCP Server — De Juiste Manier om AI-agents Databasetoegang te Geven"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server van Data API builder geeft AI-agents veilige, deterministische databasetoegang zonder schema's bloot te stellen of te vertrouwen op NL2SQL."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "sql-mcp-server-data-api-builder" >}}).*

Laten we eerlijk zijn: de meeste database-MCP-servers die vandaag beschikbaar zijn, zijn angstaanjagend. Ze nemen een zoekopdracht in natuurlijke taal, genereren SQL on-the-fly en voeren het uit op je productiegegevens.

Het Azure SQL-team heeft zojuist [SQL MCP Server geïntroduceerd](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), en het neemt een fundamenteel andere aanpak.

## Waarom geen NL2SQL?

Modellen zijn niet deterministisch. SQL MCP Server gebruikt een **NL2DAB**-aanpak. De agent werkt met de entiteitsabstractielaag van Data API builder om nauwkeurige T-SQL deterministisch te produceren.

## Zeven tools, niet zevenhonderd

SQL MCP Server biedt precies zeven DML-tools:

- `describe_entities` — ontdek beschikbare entiteiten
- `create_record` — rijen invoegen
- `read_records` — tabellen en views opvragen
- `update_record` — rijen wijzigen
- `delete_record` — rijen verwijderen
- `execute_entity` — opgeslagen procedures uitvoeren
- `aggregate_records` — aggregatiequery's

## In drie opdrachten aan de slag

```bash
dab init   --database-type mssql   --connection-string "@env('sql_connection_string')"

dab add Customers   --source dbo.Customers   --permissions "anonymous:*"

dab start
```

## Het beveiligingsverhaal is solide

RBAC op elke laag, Azure Key Vault-integratie, Microsoft Entra + aangepaste OAuth.

Bekijk de [volledige post](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) en [documentatie](https://aka.ms/sql/mcp).
