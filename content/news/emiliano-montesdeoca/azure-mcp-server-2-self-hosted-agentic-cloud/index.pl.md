---
title: "Azure MCP Server 2.0 Właśnie Wylądował — Samodzielnie Hostowana Agentic Cloud Automation Jest Tutaj"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 osiąga stabilność z samodzielnie hostowanymi zdalnymi wdrożeniami, 276 narzędziami w 57 usługach Azure i zabezpieczeniami klasy enterprise."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

Jeśli ostatnio budowałeś cokolwiek z MCP i Azure, pewnie wiesz, że lokalne doświadczenie działa dobrze. Ale gdy musisz udostępnić tę konfigurację całemu zespołowi? Tam rzeczy się komplikowały.

Już nie. Azure MCP Server [osiągnął stabilną wersję 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), a główna funkcja to dokładnie to, o co prosiły zespoły enterprise: **obsługa samodzielnie hostowanego zdalnego serwera MCP**.

## Co to jest Azure MCP Server?

Azure MCP Server implementuje specyfikację [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) i ujawnia możliwości Azure jako ustrukturyzowane, odkrywalne narzędzia. Liczby mówią same za siebie: **276 narzędzi MCP w 57 usługach Azure**.

## Wielka sprawa: samodzielnie hostowane zdalne wdrożenia

W prawdziwym scenariuszu zespołowym potrzebujesz:
- Wspólny dostęp dla deweloperów i wewnętrznych systemów agentów
- Scentralizowana konfiguracja
- Granice sieci i polityk enterprise
- Integracja z pipeline'ami CI/CD

Azure MCP Server 2.0 rozwiązuje to wszystko. Do autoryzacji masz dwie opcje:
1. **Managed Identity** — przy pracy z [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **Przepływ On-Behalf-Of (OBO)** — delegacja OpenID Connect z rzeczywistymi uprawnieniami użytkownika

## Wzmocnienie bezpieczeństwa

Wersja 2.0 dodaje silniejszą walidację punktów końcowych, ochronę przed wzorcami injection i ściślejsze kontrole izolacji.

## Pierwsze kroki

- **[GitHub Repo](https://aka.ms/azmcp)** — kod źródłowy, dokumenty
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — wdrożenie w kontenerze
- **[Rozszerzenie VS Code](https://aka.ms/azmcp/download/vscode)** — integracja IDE
- **[Przewodnik self-hosting](https://aka.ms/azmcp/self-host)** — flagowa funkcja 2.0
