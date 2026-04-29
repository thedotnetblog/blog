---
title: "SQL Server 2025 als database die klaar is voor agents: beveiliging, back-up en MCP in één engine"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Het laatste deel van de Polyglot Tax-serie behandelt de lastige productieproblemen: een uniforme Row-Level Security over relationele, JSON-, graph- en vectorgegevens, plus cryptografische audittrails en MCP-integratie die SQL Server 2025 echt agent-ready maken."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Ik heb de Polyglot Tax-serie van Aditya Badramraju met veel interesse gevolgd. Delen 1-3 bouwden een overtuigend verhaal voor SQL Server 2025 als een echt multi-model database — JSON, graph, vector en relationele data allemaal in één engine met een uniforme queryplanner. Deel 4 sluit de serie af met de onderdelen die echt bepalen of je deze architectuur in productie zou vertrouwen.

Spoiler: het productieverhaal is sterk.

## Eén Beveiligingsmodel voor Alle Datamodellen

Dat is het lastige aan polyglot stacks: wanneer een auditor vraagt "bewijs dat Tenant A de data van Tenant B niet kan zien", moet je die vraag voor elke database apart beantwoorden. Vijf databases, vijf beveiligingsmodellen, vijf bewijzen.

Met SQL Server 2025 definieer je één Row-Level Security-policy en die dekt alle datamodellen:

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

Vanaf dat moment wordt elke query — relationele joins, JSON-path queries, graph traversals, vector similarity searches — automatisch per tenant gefilterd. De engine injecteert de predicate in het execution plan voordat er data uit storage vertrekt. Je aanroepende code hoeft niet overal `WHERE TenantID = @id` te schrijven. Je test de policy één keer.

De lagen werken ook samen: Dynamic Data Masking voor kolommen die niet de volledige waarde aan bepaalde rollen mogen tonen, Always Encrypted voor end-to-end encryptie (zelfs DBA's kunnen het niet lezen), en stored procedures als permissiegrens zodat agents alleen aanroepen wat je expliciet hebt vrijgegeven.

Dit is het deel van de architectuur dat het belangrijkst is voor compliance-zware SaaS. Eén policy, één bewijs.

## Geconsolideerde Back-up = Atomisch Herstel

Eén statement, alle datamodellen, één consistent punt in de tijd:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

In een polyglot stack betekent point-in-time recovery over vijf databases dat je vijf restore-operaties moet coördineren en maar moet hopen dat de timestamps binnen een seconde of twee overeenkomen. Voor financiële data is die tweeseconden-inconsistentie onacceptabel. Met één database, één transaction log en één restore is recovery per definitie atomisch.

## Ledger-tabellen voor Manipulatiebestendige Audittrails

Voor gereguleerde sectoren heb je meer nodig dan "we hebben logs". Je hebt cryptografisch bewijs nodig dat die logs niet zijn aangepast:

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

Elke insert, update en delete wordt cryptografisch gehashed in een blockchain-achtige structuur. Je kunt een auditor wiskundig aantonen dat een rij niet is gemanipuleerd sinds die is geschreven. In een polyglot stack bestaat die mogelijkheid niet uniform over al je databases.

## MCP-integratie: Agents Zonder Handmatig Geschreven Middleware

De serie werkte hier naartoe: SQL Server 2025 ondersteunt SQL MCP Server direct, wat betekent dat je agents de database kunnen aanroepen via natuurlijke tool calls zonder dat je voor elke operatie middleware hoeft te schrijven.

Combineer dat met stored procedures als permissiegrens en Row-Level Security op engine-niveau, en je krijgt een model waarin:

1. De agent een tool aanroept, bijvoorbeeld "haal de klantcontext op voor account 12345"
2. MCP dat vertaalt naar de stored procedure die jij hebt gedefinieerd
3. De SQL-engine tenant-isolatie en column masking automatisch afdwingt
4. De agent precies de data krijgt die hij mag zien

Geen middlewarelaag. Geen risico op ad-hoc query injection. De engine verzorgt de autorisatie, niet de agent.

## Waarom Dit Belangrijk Is Voor .NET-ontwikkelaars

Als je .NET-services bouwt en SQL Server je primaire opslag is, dan is de boodschap van deze serie: je hoeft geen Redis toe te voegen voor caching, geen graph database voor relaties en geen vector store voor embeddings. SQL Server 2025 doet dat allemaal — met betere operationele consistentie dan een polyglot stack en met uniforme beveiliging die echt auditeerbaar is.

De MCP-integratie betekent dat je Semantic Kernel-agents of Microsoft Agent Framework-workflows via dezelfde SQL MCP Server met je datalaag kunnen communiceren, met dezelfde beveiligingsgaranties die je ook op menselijke queries zou toepassen.

## Afronding

De Polyglot Tax-serie is de moeite waard om van begin tot eind te lezen. Delen 1-3 bewijzen het queryplannerverhaal. Deel 4 bewijst het productieverhaal. Voor .NET-ontwikkelaars die agent-first of AI-augmented applicaties op Azure SQL bouwen, verdient deze architectuur serieuze overweging.

Originele post van Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).