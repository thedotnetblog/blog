---
title: "Costruire un'app per conferenze con IA con lo stack componibile di .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft ha costruito ConferencePulse — un'app Blazor per conferenze live — combinando Microsoft.Extensions.AI, DataIngestion, VectorData, MCP e Agent Framework. Ecco come si incastrano i pezzi."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Costruire un'app per conferenze con IA con lo stack componibile di .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft ha costruito ConferencePulse, un'app Blazor Server per sessioni di conferenza live, combinando cinque librerie di estensione .NET. È stata utilizzata all'MVP Summit.

## Cosa fa ConferencePulse

ConferencePulse funziona durante le sessioni live e fornisce: sondaggi generati dall'IA dal contenuto della sessione, Q&A del pubblico con una pipeline RAG che attinge da una knowledge base live, insight generati automaticamente e riepiloghi delle sessioni prodotti da più agenti IA concorrenti. Lo stack è .NET 10, Blazor Server, Aspire, suddiviso in cinque progetti: Web, Core, Ingestion, Agents, Mcp e AppHost.

## Microsoft.Extensions.AI: un'astrazione per tutto

`IChatClient` è l'astrazione unificata — si configura una volta e la stessa interfaccia funziona per Azure OpenAI, OpenAI, Anthropic o qualsiasi altro provider. Sei righe per ottenere un client completamente configurato con invocazione di funzioni, tracciamento OpenTelemetry e middleware di logging:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Lo stesso `IChatClient` viene riutilizzato in seguito per il passaggio di arricchimento dell'ingestion dei dati — nessun client separato necessario per questo.

## Pipeline DataIngestion

Il contenuto della sessione scorre attraverso una pipeline: `MarkdownReader` → `HeaderChunker` (500 token, 50 token di sovrapposizione) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Gli arricchitori usano lo stesso `IChatClient` per generare riepiloghi ed estrarre parole chiave prima dell'indicizzazione. Le domande del pubblico, le coppie Q&A e i risultati dei sondaggi vengono inseriti in tempo reale man mano che la sessione avanza — la knowledge base cresce durante il talk.

## VectorData: ricerca indipendente dal provider

`VectorStoreCollection.SearchAsync()` funziona allo stesso modo sia che il backing store sia Qdrant o Azure AI Search. La ricerca ibrida (vettore + testo completo) è supportata. La pipeline RAG per il Q&A del pubblico interroga questa collezione e riceve i chunk rilevanti da passare come contesto al client di chat.

## MCP: contenuto della sessione come strumenti

Il contenuto della sessione è esposto tramite MCP in modo che qualsiasi client compatibile con MCP possa accedervi. Sia il server che il client sono implementati — il server espone la conoscenza della sessione come strumenti MCP, e il client consente di chiamare questi strumenti dall'interno della pipeline dell'agente.

## Agent Framework: riepilogo multi-agente in parallelo

Il riepilogo della sessione viene generato da tre agenti che eseguono in modo concorrente — `PollSummaryAgent`, `QuestionSummaryAgent` e `InsightSummaryAgent` — poi uniti. Questo utilizza il pattern di group chat o esecuzione parallela di Microsoft Agent Framework. Ogni agente gestisce una preoccupazione; l'orchestratore unisce gli output.

## Il principio di progettazione

Il post fa un punto degno di nota: usa lo strumento più semplice che si adatta. Chiamate dirette a `IChatClient` per semplici attività di generazione. Chiamata di strumento/funzione per l'estrazione di dati strutturati. Agenti completi solo quando si necessita di ragionamento autonomo multi-step. La stratificazione delle librerie lo impone — è possibile usare `Microsoft.Extensions.AI` senza includere l'Agent Framework completo.

Consulta il [post completo](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) per la struttura completa del progetto e i link al codice sorgente.
