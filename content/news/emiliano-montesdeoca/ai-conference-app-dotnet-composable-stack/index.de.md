---
title: "Eine KI-gestützte Konferenz-App mit dem komponierbaren .NET-Stack erstellen"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft hat ConferencePulse — eine Blazor-App für Live-Konferenzen — durch Kombination von Microsoft.Extensions.AI, DataIngestion, VectorData, MCP und Agent Framework erstellt. So passen die Teile zusammen."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Eine KI-gestützte Konferenz-App mit dem komponierbaren .NET-Stack erstellen](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft hat ConferencePulse entwickelt, eine Blazor Server-App für Live-Konferenzsessions, indem fünf .NET-Erweiterungsbibliotheken kombiniert wurden. Sie wurde auf dem MVP Summit eingesetzt.

## Was ConferencePulse leistet

ConferencePulse läuft während Live-Sessions und bietet: KI-generierte Umfragen aus dem Session-Inhalt, Publikums-Q&A mit einer RAG-Pipeline, die aus einer Live-Wissensdatenbank schöpft, automatisch generierte Erkenntnisse und Session-Zusammenfassungen, die von mehreren gleichzeitig laufenden KI-Agenten erstellt werden. Der Stack ist .NET 10, Blazor Server, Aspire, aufgeteilt auf fünf Projekte: Web, Core, Ingestion, Agents, Mcp und AppHost.

## Microsoft.Extensions.AI: eine Abstraktion für alles

`IChatClient` ist die einheitliche Abstraktion — einmal eingerichtet, funktioniert dieselbe Schnittstelle für Azure OpenAI, OpenAI, Anthropic oder jeden anderen Anbieter. Sechs Zeilen für einen vollständig konfigurierten Client mit Funktionsaufruf, OpenTelemetry-Tracing und Logging-Middleware:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Derselbe `IChatClient` wird später für den Anreicherungsschritt der Datenaufnahme wiederverwendet — kein separater Client dafür nötig.

## DataIngestion-Pipeline

Session-Inhalte fließen durch eine Pipeline: `MarkdownReader` → `HeaderChunker` (500 Token, 50 Token Überlappung) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Die Anreicherungskomponenten verwenden denselben `IChatClient`, um Zusammenfassungen zu generieren und Schlüsselwörter vor der Indexierung zu extrahieren. Publikumsfragen, Q&A-Paare und Umfrageergebnisse werden in Echtzeit aufgenommen, während die Session fortschreitet — die Wissensdatenbank wächst während des Vortrags.

## VectorData: anbieterunabhängige Suche

`VectorStoreCollection.SearchAsync()` funktioniert gleich, egal ob der zugrunde liegende Speicher Qdrant oder Azure AI Search ist. Hybridsuche (Vektor + Volltext) wird unterstützt. Die RAG-Pipeline für Publikums-Q&A fragt diese Sammlung ab und erhält relevante Chunks, die als Kontext an den Chat-Client weitergegeben werden.

## MCP: Session-Inhalt als Tools

Der Session-Inhalt wird über MCP bereitgestellt, sodass jeder MCP-kompatible Client darauf zugreifen kann. Sowohl Server als auch Client sind implementiert — der Server stellt Session-Wissen als MCP-Tools bereit, und der Client ermöglicht das Aufrufen dieser Tools innerhalb der Agenten-Pipeline.

## Agent Framework: parallele Multi-Agent-Zusammenfassung

Die Session-Zusammenfassung wird von drei gleichzeitig laufenden Agenten generiert — `PollSummaryAgent`, `QuestionSummaryAgent` und `InsightSummaryAgent` — und dann zusammengeführt. Dies verwendet das Gruppen-Chat- oder parallele Ausführungsmuster aus dem Microsoft Agent Framework. Jeder Agent behandelt einen Aspekt; der Orchestrator fügt die Ausgaben zusammen.

## Das Designprinzip

Der Beitrag macht einen bemerkenswerten Punkt: Verwende das einfachste Tool, das passt. Direkte `IChatClient`-Aufrufe für einfache Generierungsaufgaben. Tool-/Funktionsaufruf für strukturierte Datenextraktion. Vollständige Agenten nur, wenn autonomes mehrstufiges Reasoning benötigt wird. Die Bibliotheksschichtung erzwingt dies — du kannst `Microsoft.Extensions.AI` verwenden, ohne das vollständige Agent Framework einzubinden.

Siehe den [vollständigen Beitrag](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) für die vollständige Projektstruktur und Quellcode-Links.
