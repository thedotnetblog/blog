---
title: "Construint una aplicació de conferències amb IA amb la pila composable de .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft va crear ConferencePulse — una aplicació Blazor per a conferències en directe — combinant Microsoft.Extensions.AI, DataIngestion, VectorData, MCP i Agent Framework. Aquí s'explica com encaixen les peces."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[Construint una aplicació de conferències amb IA amb la pila composable de .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft va crear ConferencePulse, una aplicació Blazor Server per a sessions de conferències en directe, combinant cinc biblioteques d'extensió de .NET. La van utilitzar a la MVP Summit.

## Què fa ConferencePulse

ConferencePulse s'executa durant les sessions en directe i proporciona: enquestes generades per IA a partir del contingut de la sessió, preguntes i respostes del públic amb un pipeline RAG que extreu d'una base de coneixement en viu, informació generada automàticament i resums de sessions produïts per múltiples agents d'IA concurrents. La pila és .NET 10, Blazor Server, Aspire, dividida en cinc projectes: Web, Core, Ingestion, Agents, Mcp i AppHost.

## Microsoft.Extensions.AI: una abstracció per a tot

`IChatClient` és l'abstracció unificada — es configura una vegada i la mateixa interfície funciona per a Azure OpenAI, OpenAI, Anthropic o qualsevol altre proveïdor. Sis línies per obtenir un client totalment configurat amb invocació de funcions, traçat OpenTelemetry i middleware de registre:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

El mateix `IChatClient` es reutilitza més tard per al pas d'enriquiment de la ingesta de dades — no cal cap client separat per a això.

## Pipeline de DataIngestion

El contingut de la sessió flueix a través d'un pipeline: `MarkdownReader` → `HeaderChunker` (500 tokens, 50 tokens de solapament) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Els enriquidors utilitzen el mateix `IChatClient` per generar resums i extreure paraules clau abans de la indexació. Les preguntes del públic, els parells de preguntes i respostes i els resultats de les enquestes s'ingereixen en temps real a mesura que avança la sessió — la base de coneixement creix durant la xerrada.

## VectorData: cerca independent del proveïdor

`VectorStoreCollection.SearchAsync()` funciona igual tant si el magatzem subjacent és Qdrant com Azure AI Search. La cerca híbrida (vector + text complet) és compatible. El pipeline RAG per a preguntes i respostes del públic consulta aquesta col·lecció i obté fragments rellevants per passar com a context al client de xat.

## MCP: contingut de la sessió com a eines

El contingut de la sessió s'exposa via MCP perquè qualsevol client compatible amb MCP hi pugui accedir. Tant el servidor com el client estan implementats — el servidor exposa el coneixement de la sessió com a eines MCP, i el client permet cridar aquestes eines des de dins del pipeline de l'agent.

## Agent Framework: resum multi-agent paral·lel

El resum de la sessió es genera per tres agents que s'executen de manera concurrent — `PollSummaryAgent`, `QuestionSummaryAgent` i `InsightSummaryAgent` — i després es fusionen. Això utilitza el patró de xat en grup o d'execució paral·lela de Microsoft Agent Framework. Cada agent gestiona una preocupació; l'orquestrador fusiona les sortides.

## El principi de disseny

La publicació fa un punt que val la pena recordar: utilitza l'eina més senzilla que s'adapti. Crides directes a `IChatClient` per a tasques de generació simples. Crida d'eines/funcions per a l'extracció de dades estructurades. Agents complets només quan necessites raonament autònom de múltiples passos. La superposició de biblioteques ho enforça — pots agafar `Microsoft.Extensions.AI` sense incloure l'Agent Framework complet.

Consulteu la [publicació completa](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) per a l'estructura completa del projecte i els enllaços al codi font.
