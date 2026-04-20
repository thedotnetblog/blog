---
title: "Foundry Agent Service is GA: Wat Er Echt Toe Doet voor .NET Agent-bouwers"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsofts Foundry Agent Service is GA gegaan met privénetwerken, Voice Live, productieevaluaties en een open multi-model runtime."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

Laten we eerlijk zijn — het bouwen van een AI-agentprototype is het gemakkelijke deel. Het moeilijke deel is alles erna.

[De Foundry Agent Service is GA gegaan](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), en deze release is precies gericht op die "alles erna"-kloof.

## Gebouwd op de Responses API

De volgende generatie Foundry Agent Service is gebouwd op de OpenAI Responses API. De architectuur is bewust open — je bent niet gebonden aan één modelprovider.

## Privénetwerken: de enterprise-blokkade verwijderd

- **Geen publieke egress** — agentverkeer raakt nooit het openbare internet
- **Container/subnet-injectie** in je netwerk
- **Toolconnectiviteit inbegrepen** — MCP-servers, Azure AI Search via privépaden

## MCP-authenticatie

| Auth-methode | Wanneer te gebruiken |
|-------------|-------------|
| Sleutelgebaseerd | Eenvoudige gedeelde toegang |
| Entra Agent Identity | Service-to-service |
| Entra Managed Identity | Per-project-isolatie |
| OAuth Identity Passthrough | Gebruikersdelegatie |

## Voice Live

Voice Live vouwt STT, LLM en TTS samen in één beheerde API.

## Evaluaties

1. **Kant-en-klare evaluatoren** — coherentie, relevantie, grounding
2. **Aangepaste evaluatoren** — je eigen bedrijfslogica
3. **Continue evaluatie** — steekproeven van live productieverkeer

Bekijk de [quickstart-gids](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) en de [GA-aankondiging](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
