---
title: "NL2SQL è la SQL Injection dell'Era Agentiva"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Prima di lasciare che un agente interroghi il tuo database con il linguaggio naturale, leggi questo. NL2SQL sembra semplice finché non rifletti sulla completezza dello schema, l'indeterminismo e cosa risolve realmente SQL MCP Server."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

C'è una versione del discorso su NL2SQL che suona perfetta: gli utenti fanno domande in linguaggio naturale, gli agenti generano SQL, i dati tornano. Meno schermate, meno query, meno codice. Semplice.

Poi ci pensi per altri cinque minuti.

## I Problemi di cui Nessuno Parla nella Demo

**Gli schemi non sono stati progettati per spiegare le cose.** Nomi di tabelle criptici, nomi di colonne incoerenti, relazioni tecnicamente valide ma semanticamente invalide senza predicati aggiuntivi — questo è normale per i database aziendali. Non sono bug, sono semplicemente la storia accumulata dei cambiamenti di business. Ma quando chiedi a un modello di inferire l'intento da uno schema che non è stato progettato per comunicare l'intento, il modello ci proverà comunque. Non si arrenderà. Genererà la sua migliore query possibile e restituirà risultati con sicurezza.

**I modelli non sono deterministici.** Fai la stessa domanda sullo stesso database due volte e potresti ottenere SQL diverso. Il modello sta calcolando probabilità, e lievi variazioni nel contesto producono output diversi. Non puoi testare fino ad ottenere la garanzia che l'agente generi sempre la query corretta.

**La revisione dell'utente non scala.** "Basta rivedere ogni query prima dell'esecuzione" sembra sicuro. Ma presuppone che gli utenti siano esperti sia nel modello di dati che in SQL — esattamente le persone che non avevano bisogno dell'interfaccia in linguaggio naturale. Introduce anche sovraccarico cognitivo e una nuova classe di bias di conferma, dove gli utenti sopraffatti dalla complessità della query approvano query non valide invece di investigarle.

**E poi c'è l'injection.** Nello sviluppo SQL tradizionale, la parametrizzazione ha risolto l'injection perché l'input dell'utente riempiva i parametri, non la struttura SQL. Con NL2SQL, il modello genera il SQL stesso. Il prompt, il contesto dello schema, la cronologia della conversazione e i dati recuperati influenzano tutti ciò che viene eseguito. Se qualcuno elabora un prompt che cambia ciò che il modello genera, questa è injection — non a livello di parametro, ma a livello di generazione di query. E a differenza dell'eliminazione di una tabella (ovvio, recuperabile), l'injection NL2SQL produce query che restituiscono risultati errati senza errori visibili. Le decisioni aziendali vengono prese su dati sbagliati.

## Cosa Risolve Realmente SQL MCP Server

È qui che l'articolo fa il suo punto pratico più utile. Invece di dare a un agente accesso arbitrario allo schema e sperare nel meglio, SQL MCP Server espone una **superficie API curata** costruita su [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

La differenza è importante: l'agente non genera SQL. Chiama endpoint denominati che restituiscono forme di risultato predefinite. Il SQL viene scritto una volta, da uno sviluppatore, ed è deterministico. Il non-determinismo dell'agente è limitato alla scelta di *quale* endpoint chiamare, non alla costruzione di query arbitrarie.

Questo è analogo a ciò che la parametrizzazione ha fatto per l'injection SQL nel modello di app tradizionale — rimuovi la capacità di costruire query arbitrarie dall'input non attendibile.

## La Domanda Giusta

L'articolo non dice "non usare mai NL2SQL." Dice: sii deliberato su *dove* lo applichi e *cosa* esponi. Per l'analisi esplorativa in un ambiente controllato, con uno schema limitato e accesso in sola lettura, NL2SQL potrebbe andare bene. Per i sistemi di produzione dove le decisioni aziendali dipendono dai risultati, un livello API curato è significativamente più sicuro.

Onestà: alcuni problemi si risolvono genuinamente meglio con query strutturate dietro endpoint denominati che con il linguaggio naturale verso SQL. SQL MCP Server ti dà questa opzione senza abbandonare completamente l'interfaccia agentiva.

Post originale: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
