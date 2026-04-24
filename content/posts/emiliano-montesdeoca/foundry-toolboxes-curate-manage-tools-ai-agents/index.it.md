---
title: "Foundry Toolboxes: Un unico endpoint per tutti i tool degli agenti"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry ha lanciato Toolboxes in public preview — un modo per curare, gestire ed esporre i tool degli agenti IA tramite un unico endpoint compatibile MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

C'è un problema che sembra noioso finché non lo si vive in prima persona: l'organizzazione sta costruendo più agenti IA, ognuno ha bisogno di tool, e ogni team li riconfigura da zero. La stessa integrazione di ricerca web, la stessa config di Azure AI Search, la stessa connessione al server MCP di GitHub — ma in un altro repository, da un altro team, con altre credenziali e senza governance condivisa.

Microsoft Foundry ha appena lanciato [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) in public preview, ed è una risposta diretta a questo problema.

## Cos'è una Toolbox?

Una Toolbox è un bundle di tool con nome, riutilizzabile, che si definisce una volta in Foundry e si espone tramite un unico endpoint compatibile MCP. Qualsiasi runtime di agente che parla MCP può consumarlo — nessun lock-in con Foundry Agents.

La promessa è semplice: **build once, consume anywhere**. Definisci i tool, configura l'autenticazione centralmente (OAuth passthrough, identità gestita di Entra), pubblica l'endpoint. Ogni agente che ha bisogno di quei tool si connette all'endpoint e li ottiene tutti.

## I quattro pilastri (due disponibili oggi)

| Pilastro | Stato | Cosa fa |
|----------|-------|---------|
| **Discover** | In arrivo | Trova tool approvati senza ricerca manuale |
| **Build** | Disponibile | Raggruppa tool in un bundle riutilizzabile |
| **Consume** | Disponibile | Un endpoint MCP unico espone tutti i tool |
| **Govern** | In arrivo | Auth centralizzata + observability per tutte le chiamate |

## Esempio pratico

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Cerca documentazione e rispondi alle issue di GitHub.",
    tools=[
        {"type": "web_search", "description": "Cerca documentazione pubblica"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Una volta pubblicato, Foundry fornisce un endpoint unificato. Una connessione, tutti i tool.

## Nessun lock-in con Foundry Agents

Le Toolbox vengono **create e gestite** in Foundry, ma la superficie di consumo è il protocollo MCP aperto. Si possono usare da agenti personalizzati (Microsoft Agent Framework, LangGraph), GitHub Copilot e altri IDE compatibili MCP.

## Perché è importante adesso

L'ondata multi-agente sta arrivando in produzione. Ogni nuovo agente è una nuova superficie per configurazione duplicata, credenziali scadute e comportamento inconsistente. La base Build + Consume è sufficiente per iniziare a centralizzare. Quando arriverà il pilastro Govern, si avrà uno strato di tool completamente osservabile e controllato centralmente per tutta la flotta di agenti.

## Conclusione

È ancora presto — public preview, SDK Python prima, con Discover e Govern ancora in arrivo. Ma il modello è solido e il design nativo MCP significa che funziona con i tool che si stanno già costruendo. Dai un'occhiata all'[annuncio ufficiale](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) per iniziare.
