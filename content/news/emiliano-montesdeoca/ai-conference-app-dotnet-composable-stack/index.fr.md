---
title: "Créer une application de conférence IA avec la pile composable de .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft a créé ConferencePulse — une application Blazor pour les conférences en direct — en combinant Microsoft.Extensions.AI, DataIngestion, VectorData, MCP et Agent Framework. Voici comment les pièces s'assemblent."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Créer une application de conférence IA avec la pile composable de .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft a créé ConferencePulse, une application Blazor Server pour les sessions de conférence en direct, en combinant cinq bibliothèques d'extension .NET. Elle a été utilisée au MVP Summit.

## Ce que fait ConferencePulse

ConferencePulse s'exécute pendant les sessions en direct et fournit : des sondages générés par l'IA à partir du contenu de la session, des questions-réponses du public avec un pipeline RAG puisant dans une base de connaissances en direct, des insights générés automatiquement et des résumés de sessions produits par plusieurs agents IA concurrents. La pile est .NET 10, Blazor Server, Aspire, répartie sur cinq projets : Web, Core, Ingestion, Agents, Mcp et AppHost.

## Microsoft.Extensions.AI : une abstraction pour tout

`IChatClient` est l'abstraction unifiée — on la configure une fois et la même interface fonctionne pour Azure OpenAI, OpenAI, Anthropic ou tout autre fournisseur. Six lignes pour obtenir un client entièrement configuré avec l'invocation de fonctions, le traçage OpenTelemetry et le middleware de journalisation :

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Le même `IChatClient` est réutilisé plus tard pour l'étape d'enrichissement de l'ingestion de données — pas besoin d'un client séparé pour cela.

## Pipeline DataIngestion

Le contenu de la session circule dans un pipeline : `MarkdownReader` → `HeaderChunker` (500 tokens, 50 tokens de chevauchement) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Les enrichisseurs utilisent le même `IChatClient` pour générer des résumés et extraire des mots-clés avant l'indexation. Les questions du public, les paires de questions-réponses et les résultats des sondages sont ingérés en temps réel au fur et à mesure de la session — la base de connaissances s'enrichit pendant la conférence.

## VectorData : recherche indépendante du fournisseur

`VectorStoreCollection.SearchAsync()` fonctionne de la même manière que le magasin sous-jacent soit Qdrant ou Azure AI Search. La recherche hybride (vecteur + texte intégral) est prise en charge. Le pipeline RAG pour les questions-réponses du public interroge cette collection et récupère des extraits pertinents à transmettre comme contexte au client de chat.

## MCP : contenu de session comme outils

Le contenu de la session est exposé via MCP afin que tout client compatible MCP puisse y accéder. Le serveur et le client sont tous deux implémentés — le serveur expose les connaissances de la session comme outils MCP, et le client permet d'appeler ces outils depuis le pipeline de l'agent.

## Agent Framework : résumé multi-agents en parallèle

Le résumé de la session est généré par trois agents s'exécutant de manière concurrente — `PollSummaryAgent`, `QuestionSummaryAgent` et `InsightSummaryAgent` — puis fusionnés. Cela utilise le modèle de chat de groupe ou d'exécution parallèle de Microsoft Agent Framework. Chaque agent gère une préoccupation ; l'orchestrateur fusionne les sorties.

## Le principe de conception

L'article soulève un point important : utiliser l'outil le plus simple qui convient. Les appels directs à `IChatClient` pour les tâches de génération simples. L'appel d'outil/fonction pour l'extraction de données structurées. Les agents complets uniquement quand on a besoin d'un raisonnement autonome en plusieurs étapes. La stratification des bibliothèques l'impose — on peut utiliser `Microsoft.Extensions.AI` sans inclure l'Agent Framework complet.

Consultez le [post complet](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) pour la structure complète du projet et les liens vers le code source.
