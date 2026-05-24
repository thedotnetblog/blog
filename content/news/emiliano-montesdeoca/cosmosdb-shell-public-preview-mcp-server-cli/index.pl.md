---
title: "Cosmos DB Shell Jest Teraz w Publicznej Wersji Zapoznawczej — i Ma Wbudowany Serwer MCP"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell to nowe CLI o otwartym kodzie źródłowym, które udostępnia polecenia bazy danych jako narzędzia MCP. Twoje agenty AI mogą nawigować po kontenerach, uruchamiać zapytania i zarządzać danymi za pomocą tego samego interfejsu, którego używasz."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Jeśli kiedykolwiek musiałeś przełączać się między zakładką portalu, przykładem SDK i niedokończonym skryptem, żeby odpowiedzieć na jedno pytanie dotyczące Cosmos DB, znasz już tarcie, które ten projekt ma na celu wyeliminować.

Azure Cosmos DB Shell właśnie wszedł do publicznej wersji zapoznawczej. To CLI o otwartym kodzie źródłowym ze składnią podobną do bash i — część, która czyni go interesującym — wbudowanym serwerem MCP.

## Co Odróżnia Go od Innych CLI Baz Danych

Samo CLI jest przydatne: znane polecenia, wsparcie dla skryptów, integracja CI/CD. Ta część to minimum dla narzędzia bazy danych skierowanego do deweloperów.

Interesująca część to integracja serwera MCP. Każde polecenie udostępniane przez CLI staje się dostępne jako narzędzie MCP, które mogą wywoływać Twoje agenty AI. Brak niestandardowej warstwy API, brak kodu integracyjnego do napisania. Twój agent może:

- Nawigować po hierarchiach bazy danych za pomocą `cd`, `ls`, `pwd`
- Wykonywać zapytania SQL za pomocą `query` i uzyskiwać strukturalne wyniki
- Tworzyć i modyfikować elementy za pomocą `create item`, `update`, `rm`
- Zarządzać bazami danych i kontenerami za pomocą `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Sprawdzać bieżący kontekst za pomocą `endpoint`, `pwd`

Kluczowa zmiana: Twój agent nie rozmawia z API Cosmos DB — rozmawia z tym samym interfejsem powłoki, którego Ty używasz. Polecenia są deterministyczne, poddawalne audytowi i mają otwarty kod źródłowy, dzięki czemu możesz dokładnie sprawdzić, co się dzieje.

## Podstawa Open Source Jest Ważna

To nie jest czarnoskrzynkowa usługa zarządzana. Powłoka ma otwarty kod źródłowy, co oznacza:

- Zespoły bezpieczeństwa mogą przeprowadzać audyt implementacji
- Zespoły platformowe mogą ją rozwidlić i rozszerzyć zgodnie ze swoimi specyficznymi standardami
- Deweloperzy mogą wnosić ulepszenia, które przyniosą korzyści wszystkim

Dla zespołów korporacyjnych wdrażających narzędzia AI, "czy możemy dokładnie zobaczyć, jak to działa" coraz rzadziej jest opcjonalnym wymaganiem. Otwarty kod źródłowy jest tutaj znaczącym wyróżnikiem.

## Trzy Scenariusze, Które Stają Się Prostsze

**Inteligentna analiza danych** — połącz agenta z powłoką, zadawaj pytania w języku naturalnym, otrzymuj strukturalne wyniki zapytań. Agent zajmuje się budowaniem zapytania; powłoka zajmuje się wykonaniem.

**Autonomiczne zarządzanie danymi** — przepływy pracy, które muszą tworzyć, aktualizować lub usuwać dane w Cosmos DB, mogą to robić za pomocą narzędzi MCP bez potrzeby niestandardowej integracji.

**Monitorowanie w czasie rzeczywistym i alerty** — agent może okresowo odpytywać kontenery, porównywać wyniki i raportować anomalie przez dowolny sensowny kanał powiadomień.

Interfejs MCP sprawia, że te scenariusze są kompozytywne z dowolną platformą AI obsługującą MCP — nie tylko narzędziami Microsoft.

## Jak Zacząć

Powłoka jest w publicznej wersji zapoznawczej. Zainstaluj ją, skonfiguruj połączenie z Cosmos DB i włącz serwer MCP. Od tego momentu dowolny host agenta zgodny z MCP może wykryć i używać narzędzi.

Oryginalny post: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
