---
title: "Een AI-aangedreven conferentie-app bouwen met de composable stack van .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft bouwde ConferencePulse — een Blazor-app voor live conferenties — door Microsoft.Extensions.AI, DataIngestion, VectorData, MCP en Agent Framework samen te voegen. Zo passen de stukken in elkaar."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[Een AI-aangedreven conferentie-app bouwen met de composable stack van .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft bouwde ConferencePulse, een Blazor Server-app voor live conferentiesessies, door vijf .NET-extensiebibliotheken samen te voegen. Het werd gebruikt op de MVP Summit.

## Wat ConferencePulse doet

ConferencePulse draait tijdens live sessies en biedt: AI-gegenereerde polls op basis van sessie-inhoud, publieksvragen en -antwoorden met een RAG-pipeline die put uit een live kennisbase, automatisch gegenereerde inzichten en sessiesamenvattingen geproduceerd door meerdere gelijktijdige AI-agenten. De stack is .NET 10, Blazor Server, Aspire, verdeeld over vijf projecten: Web, Core, Ingestion, Agents, Mcp en AppHost.

## Microsoft.Extensions.AI: één abstractie voor alles

`IChatClient` is de geünificeerde abstractie — éénmalig geconfigureerd en dezelfde interface werkt voor Azure OpenAI, OpenAI, Anthropic of elke andere provider. Zes regels voor een volledig geconfigureerde client met functie-aanroep, OpenTelemetry-tracing en logging-middleware:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Dezelfde `IChatClient` wordt later hergebruikt voor de verrijkingsstap van de data-ingestie — geen aparte client nodig daarvoor.

## DataIngestion-pipeline

Sessie-inhoud stroomt door een pipeline: `MarkdownReader` → `HeaderChunker` (500 tokens, 50 tokens overlapping) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). De verrijkers gebruiken dezelfde `IChatClient` om samenvattingen te genereren en trefwoorden te extraheren vóór indexering. Publieksvragen, Q&A-paren en pollresultaten worden in real-time ingevoerd naarmate de sessie vordert — de kennisbase groeit tijdens de talk.

## VectorData: provideronafhankelijk zoeken

`VectorStoreCollection.SearchAsync()` werkt hetzelfde of de onderliggende opslag Qdrant of Azure AI Search is. Hybride zoeken (vector + volledige tekst) wordt ondersteund. De RAG-pipeline voor publieksvragen bevraagt deze collectie en krijgt relevante stukken terug om als context aan de chatclient door te geven.

## MCP: sessie-inhoud als tools

De sessie-inhoud wordt via MCP beschikbaar gesteld zodat elke MCP-compatibele client er toegang toe heeft. Zowel de server als de client zijn geïmplementeerd — de server stelt sessiekennis beschikbaar als MCP-tools, en de client maakt het mogelijk die tools aan te roepen vanuit de agentpipeline.

## Agent Framework: parallelle multi-agent samenvatting

De sessiesamenvatting wordt gegenereerd door drie agenten die gelijktijdig draaien — `PollSummaryAgent`, `QuestionSummaryAgent` en `InsightSummaryAgent` — en daarna samengevoegd. Dit maakt gebruik van het groepschat- of parallel uitvoeringspatroon van Microsoft Agent Framework. Elke agent behandelt één aspect; de orchestrator voegt de outputs samen.

## Het ontwerpprincipe

Het bericht maakt een punt dat het onthouden waard is: gebruik het eenvoudigste tool dat past. Directe `IChatClient`-aanroepen voor eenvoudige generatietaken. Tool-/functieaanroep voor gestructureerde data-extractie. Volledige agenten alleen wanneer je autonoom redeneren in meerdere stappen nodig hebt. De bibliotheekgelaagdheid dwingt dit af — je kunt `Microsoft.Extensions.AI` gebruiken zonder het volledige Agent Framework mee te trekken.

Zie het [volledige bericht](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) voor de volledige projectstructuur en bronlinks.
