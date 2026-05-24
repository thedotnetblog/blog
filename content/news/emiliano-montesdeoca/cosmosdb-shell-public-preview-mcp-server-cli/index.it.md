---
title: "Cosmos DB Shell È in Anteprima Pubblica — E Ha un Server MCP Integrato"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell è una nuova CLI open source che espone i comandi del database come strumenti MCP. I tuoi agenti IA possono navigare nei container, eseguire query e gestire dati usando la stessa interfaccia che usi tu."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Se hai mai dovuto saltare tra una scheda del portale, un esempio di SDK e uno script a metà completato solo per rispondere a una domanda su Cosmos DB, conosci già la frizione che questo progetto è progettato per eliminare.

Azure Cosmos DB Shell è appena entrato in anteprima pubblica. È una CLI open source con sintassi simile a bash e — la parte che lo rende interessante — un server MCP integrato.

## Cosa lo Rende Diverso dalle Altre CLI di Database

La CLI in sé è utile: comandi familiari, supporto agli script, integrazione CI/CD. Quella parte è il minimo atteso per uno strumento di database orientato agli sviluppatori.

La parte interessante è l'integrazione del server MCP. Ogni comando che la CLI espone diventa disponibile come strumento MCP che i tuoi agenti IA possono chiamare. Non c'è nessuno strato API personalizzato, nessun codice di integrazione da scrivere. Il tuo agente può:

- Navigare nelle gerarchie di database con `cd`, `ls`, `pwd`
- Eseguire query SQL con `query` e ottenere risultati strutturati
- Creare e modificare elementi con `create item`, `update`, `rm`
- Gestire database e container con `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Ispezionare il contesto corrente con `endpoint`, `pwd`

Il cambiamento fondamentale: il tuo agente non sta parlando con un'API di Cosmos DB — sta parlando con la stessa interfaccia shell che usi tu. I comandi sono deterministici, verificabili e open source in modo da poter ispezionare esattamente cosa sta succedendo.

## La Base Open Source È Importante

Questo non è un servizio gestito a scatola nera. La shell è open source, il che significa:

- I team di sicurezza possono verificare l'implementazione
- I team di piattaforma possono fare fork e estenderla per i loro standard specifici
- Gli sviluppatori possono contribuire miglioramenti che beneficiano tutti

Per i team aziendali che adottano strumenti IA, "possiamo vedere esattamente come funziona" è sempre meno un requisito opzionale. L'open source qui è un differenziatore significativo.

## Tre Scenari Che Diventano Più Semplici

**Analisi intelligente dei dati** — connetti un agente alla shell, fai domande in linguaggio naturale, ottieni risultati di query strutturati. L'agente gestisce la costruzione della query; la shell gestisce l'esecuzione.

**Gestione autonoma dei dati** — i workflow che devono creare, aggiornare o rimuovere dati in Cosmos DB possono farlo attraverso gli strumenti MCP senza necessitare un'integrazione personalizzata.

**Monitoraggio e avvisi in tempo reale** — un agente può interrogare periodicamente i container, confrontare i risultati e segnalare anomalie tramite qualsiasi canale di notifica abbia senso.

L'interfaccia MCP rende questi scenari componibili con qualsiasi piattaforma IA che parla MCP — non solo gli strumenti Microsoft.

## Per Iniziare

La shell è in anteprima pubblica. Installala, configura la tua connessione Cosmos DB e abilita il server MCP. Da lì, qualsiasi host agente compatibile con MCP può scoprire e utilizzare gli strumenti.

Post originale: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
