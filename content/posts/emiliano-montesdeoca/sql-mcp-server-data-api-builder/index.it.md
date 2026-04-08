---
title: "SQL MCP Server — Il modo giusto per dare accesso ai database agli agenti AI"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server di Data API builder offre agli agenti AI un accesso sicuro e deterministico ai database senza esporre schemi o affidarsi a NL2SQL. RBAC, cache, supporto multi-database — tutto integrato."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "sql-mcp-server-data-api-builder.md" >}}).*

Siamo onesti: la maggior parte dei server MCP per database disponibili oggi sono spaventosi. Prendono una query in linguaggio naturale, generano SQL al volo e lo eseguono contro i tuoi dati di produzione. Cosa potrebbe andare storto? (Tutto. Tutto potrebbe andare storto.)

Il team di Azure SQL ha appena [presentato SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), e adotta un approccio fondamentalmente diverso. Costruito come funzionalità di Data API builder (DAB) 2.0, dà agli agenti AI un accesso strutturato e deterministico alle operazioni sul database — senza NL2SQL, senza esporre il tuo schema, e con RBAC completo ad ogni passaggio.

## Perché non NL2SQL?

Questa è la decisione di design più interessante. I modelli non sono deterministici, e le query complesse sono le più propense a produrre errori sottili. Le query esatte che gli utenti sperano che l'AI possa generare sono anche quelle che richiedono più scrutinio quando prodotte in modo non deterministico.

Invece, SQL MCP Server usa un approccio **NL2DAB**. L'agente lavora con il livello di astrazione delle entità di Data API builder e il suo query builder integrato per produrre T-SQL accurato e ben formato in modo deterministico. Stesso risultato per l'utente, ma senza il rischio di JOIN allucinati o esposizione accidentale di dati.

## Sette strumenti, non settecento

SQL MCP Server espone esattamente sette strumenti DML, indipendentemente dalle dimensioni del database:

- `describe_entities` — scoprire entità e operazioni disponibili
- `create_record` — inserire righe
- `read_records` — interrogare tabelle e viste
- `update_record` — modificare righe
- `delete_record` — rimuovere righe
- `execute_entity` — eseguire stored procedure
- `aggregate_records` — query di aggregazione

Questo è intelligente perché le finestre di contesto sono lo spazio di pensiero dell'agente. Inondarle con centinaia di definizioni di strumenti lascia meno spazio per il ragionamento. Sette strumenti fissi mantengono l'agente concentrato sul *pensare* piuttosto che sul *navigare*.

Ogni strumento può essere abilitato o disabilitato individualmente:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Iniziare in tre comandi

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Ecco un SQL MCP Server funzionante che espone la tua tabella Customers. Il livello di astrazione delle entità significa che puoi creare alias per nomi e colonne, limitare i campi per ruolo e controllare esattamente cosa vedono gli agenti — senza esporre dettagli interni dello schema.

## La storia della sicurezza è solida

Qui è dove la maturità di Data API builder ripaga:

- **RBAC ad ogni livello** — ogni entità definisce quali ruoli possono leggere, creare, aggiornare o eliminare, e quali campi sono visibili
- **Integrazione con Azure Key Vault** — stringhe di connessione e segreti gestiti in modo sicuro
- **Microsoft Entra + OAuth personalizzato** — autenticazione di livello produzione
- **Content Security Policy** — gli agenti interagiscono attraverso un contratto controllato, non SQL grezzo

L'astrazione dello schema è particolarmente importante. I nomi interni delle tue tabelle e colonne non vengono mai esposti all'agente. Definisci entità, alias e descrizioni che hanno senso per l'interazione AI — non il tuo diagramma ERD del database.

## Multi-database e multi-protocollo

SQL MCP Server supporta Microsoft SQL, PostgreSQL, Azure Cosmos DB e MySQL. E poiché è una funzionalità di DAB, ottieni endpoint REST, GraphQL e MCP simultaneamente dalla stessa configurazione. Stesse definizioni di entità, stesse regole RBAC, stessa sicurezza — su tutti e tre i protocolli.

L'auto-configurazione in DAB 2.0 può persino ispezionare il tuo database e costruire la configurazione dinamicamente, se sei a tuo agio con meno astrazione per la prototipazione rapida.

## La mia opinione

Ecco come dovrebbe funzionare l'accesso aziendale ai database per gli agenti AI. Non "hey LLM, scrivimi un po' di SQL e YOLO sulla produzione." Invece: un livello di entità ben definito, generazione deterministica delle query, RBAC ad ogni passaggio, caching, monitoraggio e telemetria. È noioso nel miglior modo possibile.

Per gli sviluppatori .NET, la storia dell'integrazione è pulita — DAB è uno strumento .NET, l'MCP Server gira come container, e funziona con Azure SQL, che la maggior parte di noi sta già usando. Se stai costruendo agenti AI che hanno bisogno di accesso ai dati, inizia qui.

## Conclusione

SQL MCP Server è gratuito, open-source e gira ovunque. È l'approccio prescrittivo di Microsoft per dare agli agenti AI un accesso sicuro ai database. Consulta il [post completo](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) e la [documentazione](https://aka.ms/sql/mcp) per iniziare.
