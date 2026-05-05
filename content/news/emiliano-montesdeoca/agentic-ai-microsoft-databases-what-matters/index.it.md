---
title: "SQL MCP Server, Copilot in SSMS e un Database Hub con agenti IA: Cosa conta davvero dalla SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft ha rilasciato una serie di annunci sui database alla SQLCon 2026. Ecco cosa conta davvero se stai costruendo app basate su IA con Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft ha appena inaugurato [SQLCon 2026 insieme a FabCon ad Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/), e c'è un sacco di roba da analizzare. L'annuncio originale copre tutto, dai piani di risparmio alle funzionalità di conformità enterprise. Io salterò le slide sui prezzi enterprise e mi concentrerò sugli elementi che contano se sei uno sviluppatore che costruisce cose con Azure SQL e IA.

## SQL MCP Server è in public preview

Questa è la notizia principale per me. Azure SQL Database Hyperscale ora ha un **SQL MCP Server** in public preview che ti permette di connettere in modo sicuro i tuoi dati SQL ad agenti IA e Copilot usando il [Model Context Protocol](https://modelcontextprotocol.io/).

Se hai seguito l'onda MCP — e onestamente, è difficile non notarla in questo momento — questa è una grande novità. Invece di costruire pipeline di dati personalizzate per alimentare i tuoi agenti IA con il contesto dal tuo database, ottieni un protocollo standardizzato per esporre i dati SQL direttamente. I tuoi agenti possono interrogare, ragionare e agire su informazioni del database in tempo reale.

Per quelli di noi che costruiscono agenti IA con Semantic Kernel o il Microsoft Agent Framework, questo apre un percorso di integrazione pulito. Il tuo agente deve controllare l'inventario? Cercare un record cliente? Validare un ordine? MCP gli dà un modo strutturato per farlo senza che tu debba scrivere codice di recupero dati su misura per ogni scenario.

## GitHub Copilot in SSMS 22 è ora GA

Se passi del tempo in SQL Server Management Studio — e siamo onesti, la maggior parte di noi lo fa ancora — GitHub Copilot è ora disponibile in versione generale in SSMS 22. La stessa esperienza Copilot che già usi in VS Code e Visual Studio, ma per T-SQL.

Il valore pratico è semplice: assistenza via chat per scrivere query, refactoring di stored procedure, risoluzione di problemi di performance e gestione di task amministrativi. Niente di rivoluzionario come concetto, ma averlo direttamente in SSMS significa che non devi cambiare contesto verso un altro editor solo per ottenere aiuto IA sul tuo lavoro coi database.

## Gli indici vettoriali hanno avuto un serio upgrade

Azure SQL Database ora ha indici vettoriali più veloci e più capaci con supporto completo per insert, update e delete. Questo significa che i tuoi dati vettoriali restano aggiornati in tempo reale — niente reindicizzazione batch necessaria.

Ecco le novità:
- **Quantizzazione** per dimensioni degli indici più piccole senza perdere troppa accuratezza
- **Filtro iterativo** per risultati più precisi
- **Integrazione più stretta con il query optimizer** per performance prevedibili

Se stai facendo Retrieval-Augmented Generation (RAG) con Azure SQL come vector store, questi miglioramenti sono direttamente utili. Puoi tenere i tuoi vettori insieme ai dati relazionali nello stesso database, il che semplifica notevolmente la tua architettura rispetto a gestire un database vettoriale separato.

Gli stessi miglioramenti vettoriali sono disponibili anche in SQL Database in Fabric, dato che entrambi girano sullo stesso motore SQL sotto il cofano.

## Database Hub in Fabric: gestione agentica

Questo punto è più orientato al futuro, ma è interessante. Microsoft ha annunciato il **Database Hub in Microsoft Fabric** (accesso anticipato), che ti dà un pannello unico su Azure SQL, Cosmos DB, PostgreSQL, MySQL e SQL Server via Arc.

L'aspetto interessante non è solo la vista unificata — è l'approccio agentico alla gestione. Agenti IA monitorano continuamente il tuo parco database, evidenziano cosa è cambiato, spiegano perché è importante e suggeriscono cosa fare dopo. È un modello human-in-the-loop dove l'agente fa il lavoro pesante e tu prendi le decisioni.

Per i team che gestiscono più di una manciata di database, questo potrebbe davvero ridurre il rumore operativo. Invece di saltare tra portali e controllare manualmente le metriche, l'agente porta il segnale a te.

## Cosa significa questo per gli sviluppatori .NET

Il filo conduttore di tutti questi annunci è chiaro: Microsoft sta integrando agenti IA in ogni livello dello stack database. Non come un espediente, ma come un livello pratico di strumenti.

Se stai costruendo app .NET supportate da Azure SQL, ecco cosa farei concretamente:

1. **Prova il SQL MCP Server** se stai costruendo agenti IA. È il modo più pulito per dare ai tuoi agenti accesso al database senza plumbing personalizzato.
2. **Attiva Copilot in SSMS** se non l'hai già fatto — un guadagno di produttività gratuito per il lavoro SQL quotidiano.
3. **Dai un'occhiata agli indici vettoriali** se stai facendo RAG e attualmente usi un vector store separato. Consolidare su Azure SQL significa un servizio in meno da gestire.

## Per concludere

L'annuncio completo contiene di più — piani di risparmio, assistenti per la migrazione, funzionalità di conformità — ma la storia per gli sviluppatori è nel MCP Server, nei miglioramenti vettoriali e nel livello di gestione agentica. Questi sono gli elementi che cambiano come costruisci, non solo come fai il budget.

Dai un'occhiata all'[annuncio completo di Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) per il quadro completo, e [iscriviti per l'accesso anticipato al Database Hub](https://aka.ms/database-hub) se vuoi provare la nuova esperienza di gestione.
