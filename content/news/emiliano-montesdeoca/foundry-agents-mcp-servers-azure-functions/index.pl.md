---
title: "Połącz Swoje Serwery MCP na Azure Functions z Agentami Foundry — Oto Jak"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Zbuduj swój serwer MCP raz, wdróż go na Azure Functions i połącz z agentami Microsoft Foundry z właściwym uwierzytelnianiem."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

Jest jedna rzecz, którą kocham w ekosystemie MCP: budujesz swój serwer raz i działa wszędzie.

Lily Ma z Azure SDK team [opublikowała praktyczny przewodnik](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) dotyczący łączenia serwerów MCP wdrożonych na Azure Functions z agentami Microsoft Foundry.

## Dlaczego ta kombinacja ma sens

Azure Functions daje ci skalowalną infrastrukturę, wbudowane uwierzytelnianie i bezserwerowe rozliczenia. Microsoft Foundry daje ci agentów AI, którzy mogą rozumować i działać. Połączenie obu oznacza, że twoje narzędzia stają się możliwościami agentów AI.

## Opcje uwierzytelniania

| Metoda | Przypadek użycia |
|--------|----------|
| **Key-based** | Programowanie lub serwery bez Entra auth |
| **Microsoft Entra** | Produkcja z zarządzanymi tożsamościami |
| **OAuth identity passthrough** | Produkcja z kontekstem użytkownika |
| **Nieuwierzytelnione** | Dev/testowanie lub dane publiczne |

## Konfiguracja

1. **Wdróż serwer MCP na Azure Functions** — próbki dla [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
2. **Włącz wbudowane uwierzytelnianie MCP**
3. **Pobierz URL endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Dodaj serwer MCP jako narzędzie w Foundry**

Przeczytaj [pełny przewodnik](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/).
