---
title: "Foundry Toolboxes: Jeden endpoint dla wszystkich narzędzi agentów AI"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry uruchomił Toolboxes w publicznym podglądzie — sposób na zarządzanie narzędziami agentów AI i ich udostępnianie przez jeden endpoint zgodny z MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Ten artykuł został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Jest problem, który wydaje się błahy — dopóki się na niego nie natrafi. Organizacja buduje wiele agentów AI, każdy wymaga narzędzi, a każdy zespół konfiguruje je od zera. Ta sama integracja wyszukiwania, ta sama konfiguracja Azure AI Search, to samo połączenie z serwerem GitHub MCP — ale w innym repozytorium, przez inny zespół, z innymi danymi uwierzytelniającymi i bez wspólnego zarządzania.

Microsoft Foundry właśnie uruchomił [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) w publicznym podglądzie — bezpośrednia odpowiedź na ten problem.

## Czym jest Toolbox?

Toolbox to nazwany, wielokrotnie używalny zestaw narzędzi, który definiuje się raz w Foundry i udostępnia przez jeden endpoint zgodny z MCP. Każde środowisko uruchomieniowe agenta obsługujące MCP może je konsumować — bez uzależnienia od Foundry Agents.

Obietnica jest prosta: **build once, consume anywhere**. Zdefiniuj narzędzia, skonfiguruj uwierzytelnianie centralnie (OAuth passthrough, tożsamość zarządzana Entra), opublikuj endpoint. Każdy agent potrzebujący tych narzędzi łączy się raz i dostaje je wszystkie.

## Cztery filary (dwa dostępne dziś)

| Filar | Status | Co robi |
|-------|--------|---------|
| **Discover** | Wkrótce | Znajdowanie zatwierdzonych narzędzi bez ręcznego szukania |
| **Build** | Dostępny | Grupowanie narzędzi w wielokrotnie używalny bundle |
| **Consume** | Dostępny | Jeden endpoint MCP udostępnia wszystkie narzędzia |
| **Govern** | Wkrótce | Centralne uwierzytelnianie + obserwowalność wszystkich wywołań |

## Przykład praktyczny

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
    description="Przeszukaj dokumentację i odpowiedz na issues GitHub.",
    tools=[
        {"type": "web_search", "description": "Szukaj publicznej dokumentacji"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Po opublikowaniu Foundry udostępnia ujednolicony endpoint. Jedno połączenie — wszystkie narzędzia.

## Brak uzależnienia od Foundry Agents

Toolboxes są **tworzone i zarządzane** w Foundry, ale powierzchnią konsumpcji jest otwarty protokół MCP. Można ich używać z niestandardowych agentów (Microsoft Agent Framework, LangGraph), GitHub Copilot i innych środowisk IDE zgodnych z MCP.

## Dlaczego to ważne teraz

Fala wielu agentów dociera do produkcji. Każdy nowy agent to nowa powierzchnia zduplikowanej konfiguracji, przestarzałych danych uwierzytelniających i niespójnego zachowania. Podstawa Build + Consume wystarczy, by zacząć centralizować. Gdy pojawi się filar Govern, będzie dostępna w pełni obserwowalna, centralnie kontrolowana warstwa narzędzi dla całej floty agentów.

## Podsumowanie

To jeszcze wczesny etap — publiczny podgląd, Python SDK na początku, Discover i Govern jeszcze przed nami. Ale model jest solidny, a natywny design MCP oznacza, że działa z narzędziami, które już się buduje. Szczegóły w [oficjalnym ogłoszeniu](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
