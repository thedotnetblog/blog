---
title: "Foundry Agent Service jest GA: Co Naprawdę Ważne dla Budowniczych Agentów .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Usługa Foundry Agent firmy Microsoft właśnie osiągnęła GA z prywatną siecią, Voice Live, ocenami produkcyjnymi i otwartym środowiskiem uruchomieniowym wielu modeli."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

Bądźmy szczerzy — budowanie prototypu agenta AI to łatwa część. Trudna część to wszystko potem.

[Foundry Agent Service właśnie osiągnął GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), a to wydanie jest skupione na tej luce "wszystko potem".

## Zbudowany na Responses API

Nowej generacji Foundry Agent Service jest zbudowany na OpenAI Responses API. Architektura jest celowo otwarta — nie jesteś przywiązany do jednego dostawcy modeli.

## Prywatna sieć: blokada enterprise usunięta

- **Brak publicznego wyjścia** — ruch agenta nigdy nie dotyka publicznego internetu
- **Iniekcja kontenera/podsieci** do Twojej sieci
- **Łączność narzędzi** — serwery MCP, Azure AI Search działają przez prywatne ścieżki

## Uwierzytelnianie MCP

| Metoda auth | Kiedy używać |
|-------------|-------------|
| Key-based | Prosty wspólny dostęp |
| Entra Agent Identity | Service-to-service |
| Entra Managed Identity | Izolacja per-projekt |
| OAuth Identity Passthrough | Delegowany dostęp użytkownika |

## Voice Live

Voice Live składa STT, LLM i TTS w jedno zarządzane API.

## Oceny

1. **Wbudowane ewaluatory** — spójność, trafność, uziemienie
2. **Niestandardowe ewaluatory** — Twoja własna logika biznesowa
3. **Ciągła ocena** — próbkowanie żywego ruchu produkcyjnego

Sprawdź [przewodnik quickstart](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) i [ogłoszenie GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
