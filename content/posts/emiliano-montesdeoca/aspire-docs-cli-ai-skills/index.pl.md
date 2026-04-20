---
title: "Aspire 13.2 Dostarcza CLI do Dokumentacji — i Twój Agent AI Też Może Go Używać"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 dodaje aspire docs — CLI do wyszukiwania, przeglądania i czytania oficjalnej dokumentacji bez opuszczania terminala. Działa też jako narzędzie dla agentów AI."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-docs-cli-ai-skills" >}}).*

Znasz ten moment, kiedy siedzisz głęboko w Aspire AppHost, łączysz integracje i musisz sprawdzić dokładnie, jakich parametrów oczekuje integracja Redis? Alt-tab do przeglądarki, szukasz na aspire.dev. Kontekst utracony.

Aspire 13.2 właśnie [dostarczył rozwiązanie](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). CLI `aspire docs` pozwala wyszukiwać, przeglądać i czytać oficjalną dokumentację Aspire bezpośrednio z terminala.

## Trzy polecenia, zero kart przeglądarki

```bash
# Lista wszystkich dokumentów
aspire docs list

# Szukaj tematu
aspire docs search "redis"

# Przeczytaj pełną stronę
aspire docs get redis-integration

# Tylko jedna sekcja
aspire docs get redis-integration --section "Add Redis resource"
```

## Kąt agentów AI

To samo sprawia, że jest to interesujące dla deweloperów budujących z narzędziami AI. Te same polecenia `aspire docs` działają jako narzędzia dla agentów AI.

Zamiast halucynować Aspire API na podstawie przestarzałych danych treningowych, agent może wywołać `aspire docs search "postgres"`, znaleźć oficjalne dokumenty integracji i przeczytać właściwą stronę.

## Podsumowanie

`aspire docs` to mała funkcja, która czysto rozwiązuje prawdziwy problem. Zobacz [deep dive Davida Pine'a](https://davidpine.dev/posts/aspire-docs-mcp-tools/).
