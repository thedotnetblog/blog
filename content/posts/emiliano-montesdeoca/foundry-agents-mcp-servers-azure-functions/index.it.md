---
title: "Collega i tuoi server MCP su Azure Functions ai Foundry Agents — Ecco come"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Costruisci il tuo server MCP una volta, distribiscilo su Azure Functions e collegalo agli agenti Microsoft Foundry con autenticazione adeguata. I tuoi strumenti funzionano ovunque — VS Code, Cursor, e ora agenti AI aziendali."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}}).*

Ecco cosa adoro dell'ecosistema MCP: costruisci il tuo server una volta e funziona ovunque. VS Code, Visual Studio, Cursor, ChatGPT — ogni client MCP può scoprire e utilizzare i tuoi strumenti. Ora, Microsoft sta aggiungendo un altro consumatore a quella lista: gli agenti Foundry.

Lily Ma del team Azure SDK [ha pubblicato una guida pratica](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) su come collegare server MCP distribuiti su Azure Functions con gli agenti Microsoft Foundry. Se hai già un server MCP, questo è puro valore aggiunto — nessuna ricostruzione necessaria.

## Perché questa combinazione ha senso

Azure Functions ti offre infrastruttura scalabile, autenticazione integrata e fatturazione serverless per ospitare server MCP. Microsoft Foundry ti dà agenti AI che possono ragionare, pianificare e agire. Collegare i due significa che i tuoi strumenti personalizzati — interrogare un database, chiamare un'API aziendale, eseguire logica di validazione — diventano capacità che gli agenti AI aziendali possono scoprire e utilizzare autonomamente.

Il punto chiave: il tuo server MCP resta lo stesso. Stai semplicemente aggiungendo Foundry come un altro consumatore. Gli stessi strumenti che funzionano nel tuo setup VS Code ora alimentano un agente AI con cui il tuo team o i clienti interagiscono.

## Opzioni di autenticazione

È qui che il post offre davvero valore. Quattro metodi di autenticazione a seconda del tuo scenario:

| Metodo | Caso d'uso |
|--------|-----------|
| **Basato su chiave** (predefinito) | Sviluppo o server senza autenticazione Entra |
| **Microsoft Entra** | Produzione con identità gestite |
| **Passthrough identità OAuth** | Produzione dove ogni utente si autentica individualmente |
| **Senza autenticazione** | Dev/test o solo dati pubblici |

Per la produzione, Microsoft Entra con identità dell'agente è il percorso consigliato. Il passthrough identità OAuth è per quando il contesto utente conta — l'agente chiede agli utenti di accedere, e ogni richiesta porta il token personale dell'utente.

## Configurazione

Il flusso generale:

1. **Distribuisci il tuo server MCP su Azure Functions** — esempi disponibili per [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript e Java
2. **Abilita l'autenticazione MCP integrata** sulla tua function app
3. **Ottieni l'URL del tuo endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Aggiungi il server MCP come strumento in Foundry** — naviga al tuo agente nel portale, aggiungi un nuovo strumento MCP, fornisci endpoint e credenziali

Poi testalo nel playground dell'Agent Builder inviando un prompt che attiverebbe uno dei tuoi strumenti.

## La mia opinione

La storia della composabilità qui sta diventando davvero forte. Costruisci il tuo server MCP una volta in .NET (o Python, TypeScript, Java), distribuiscilo su Azure Functions, e ogni client compatibile con MCP può usarlo — strumenti di codifica, app di chat, e ora agenti AI aziendali. È un pattern "scrivi una volta, usa ovunque" che funziona davvero.

Per gli sviluppatori .NET nello specifico, l'[estensione MCP di Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) rende tutto semplice. Definisci i tuoi strumenti come Azure Functions, fai il deploy, e hai un server MCP di livello produzione con tutta la sicurezza e la scalabilità che Azure Functions offre.

## Conclusione

Se hai strumenti MCP in esecuzione su Azure Functions, collegarli agli agenti Foundry è una vittoria rapida — i tuoi strumenti personalizzati diventano capacità AI aziendali con autenticazione adeguata e senza modifiche al codice del server.

Leggi la [guida completa](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) per istruzioni passo passo su ogni metodo di autenticazione, e consulta la [documentazione dettagliata](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) per configurazioni di produzione.
