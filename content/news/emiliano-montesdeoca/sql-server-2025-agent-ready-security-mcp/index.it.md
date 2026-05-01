---
title: "SQL Server 2025 come database pronto per gli agenti: sicurezza, backup e MCP in un solo motore"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "La parte finale della serie Polyglot Tax affronta i problemi di produzione più difficili: una Row-Level Security unificata su dati relazionali, JSON, graph e vector, più i tracciati di audit crittografici e l'integrazione MCP che rendono SQL Server 2025 davvero pronto per gli agenti."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Ho seguito la serie Polyglot Tax di Aditya Badramraju con grande interesse. Le parti 1-3 hanno costruito un caso convincente per SQL Server 2025 come database davvero multi-model — JSON, graph, vector e dati relazionali tutti in un solo motore con un query planner unificato. La parte 4 chiude la serie con le parti che determinano davvero se ti fideresti di questa architettura in produzione.

Spoiler: la storia di produzione è solida.

## Un Solo Modello di Sicurezza per Tutti i Modelli di Dati

Ecco il punto critico degli stack poliglotti: quando un auditor chiede "dimostra che il Tenant A non può vedere i dati del Tenant B", devi rispondere a questa domanda per ogni database separatamente. Cinque database, cinque modelli di sicurezza, cinque prove.

Con SQL Server 2025, definisci una sola policy di Row-Level Security e copre tutti i modelli di dati:

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

Da quel momento, ogni query — join relazionali, query su path JSON, traversali graph, ricerche di similarità vector — viene filtrata automaticamente per tenant. Il motore inserisce il predicate nel piano di esecuzione prima che qualsiasi dato lasci lo storage. Il tuo codice chiamante non deve scrivere `WHERE TenantID = @id` ovunque. Testi la policy una sola volta.

I livelli si compongono ulteriormente: Dynamic Data Masking per le colonne che non dovrebbero mostrare i valori completi a certi ruoli, Always Encrypted per la crittografia end-to-end (perfino i DBA non possono leggerla), e le stored procedure come confine di autorizzazione così che gli agenti chiamino solo ciò che hai esposto esplicitamente.

Questa è la parte dell'architettura che conta di più per un SaaS con forti requisiti di compliance. Una policy, una prova.

## Backup Unificato = Recupero Atomico

Una sola istruzione, tutti i modelli di dati, un punto nel tempo coerente:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

In uno stack poliglotta, il point-in-time recovery su cinque database significa coordinare cinque operazioni di restore e sperare che i timestamp coincidano entro uno o due secondi. Per i dati finanziari, quella differenza di due secondi è inaccettabile. Con un solo database, un solo transaction log, un solo restore — il recovery è atomico per definizione.

## Tabelle Ledger per Tracce di Audit a Prova di Manomissione

Per i settori regolamentati, non basta dire "abbiamo i log". Serve la prova crittografica che quei log non siano stati modificati:

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

Ogni insert, update e delete viene hashato crittograficamente in una struttura in stile blockchain. Puoi dimostrare a un auditor — matematicamente — che una riga non è stata manomessa da quando è stata scritta. In uno stack poliglotta, questa capacità non esiste in modo uniforme in tutti i tuoi database.

## Integrazione MCP: Agenti Senza Middleware Scritto a Mano

La serie stava arrivando proprio qui: SQL Server 2025 supporta direttamente SQL MCP Server, il che significa che i tuoi agenti possono chiamare il database tramite tool call in linguaggio naturale senza che tu scriva middleware per ogni operazione.

Combina questo con le stored procedure come confine di autorizzazione e con la Row-Level Security applicata dal motore, e ottieni un modello in cui:

1. L'agente chiama uno strumento, ad esempio "recupera il contesto cliente per l'account 12345"
2. MCP lo traduce nella stored procedure che hai definito
3. Il motore SQL applica automaticamente isolamento tenant e mascheramento delle colonne
4. L'agente riceve esattamente i dati che è autorizzato a vedere

Nessun livello middleware. Nessun rischio di injection di query ad hoc. L'autorizzazione la gestisce il motore, non l'agente.

## Perché Questo Conta per gli Sviluppatori .NET

Se stai costruendo servizi .NET con SQL Server come archivio primario, il messaggio di questa serie è: non hai bisogno di aggiungere Redis per la cache, un database graph per le relazioni o un vector store per le embeddings. SQL Server 2025 gestisce tutto questo — con una consistenza operativa migliore di uno stack poliglotta e una sicurezza unificata che è davvero auditabile.

L'integrazione MCP significa che i tuoi agenti Semantic Kernel o i workflow di Microsoft Agent Framework possono interagire con il livello dati attraverso lo stesso SQL MCP Server, con le stesse garanzie di sicurezza che imporresti alle query umane.

## Conclusione

La serie Polyglot Tax merita di essere letta dall'inizio alla fine. Le parti 1-3 dimostrano la storia del query planner. La parte 4 dimostra la storia di produzione. Per gli sviluppatori .NET che costruiscono applicazioni agent-first o AI-augmented su Azure SQL, questa architettura merita seria considerazione.

Post originale di Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).