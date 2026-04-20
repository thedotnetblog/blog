---
title: "Przestań Pilnować Terminala: Tryb Odłączony Aspire Zmienia Przepływ Pracy"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 pozwala uruchomić AppHost w tle i odzyskać terminal. W połączeniu z nowymi poleceniami CLI i obsługą agentów, to większa sprawa niż się wydaje."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Za każdym razem gdy uruchamiasz Aspire AppHost, twój terminal znika. Zablokowany. Zajęty do Ctrl+C. Chcesz uruchomić szybkie polecenie? Nowa karta. Sprawdzić logi? Kolejna karta. To małe tarcie szybko się kumuluje.

Aspire 13.2 to naprawia. James Newton-King [opisał wszystkie szczegóły](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), i szczerze, to jedna z tych funkcji, która natychmiast zmienia sposób pracy.

## Tryb odłączony: jedno polecenie, terminal wraca

```bash
aspire start
```

To skrót dla `aspire run --detach`. Twój AppHost uruchamia się w tle i natychmiast odzyskujesz terminal.

## Zarządzanie tym, co działa

Uruchamianie w tle jest przydatne tylko wtedy, gdy możesz faktycznie zarządzać tym, co jest uruchomione. Aspire 13.2 dostarcza pełny zestaw poleceń CLI:

```bash
# Lista wszystkich działających AppHostów
aspire ps

# Sprawdź stan konkretnego AppHosta
aspire describe

# Strumieniuj logi z działającego AppHosta
aspire logs

# Zatrzymaj konkretny AppHost
aspire stop
```

## Połącz z trybem izolowanym

Tryb odłączony naturalnie łączy się z trybem izolowanym:

```bash
aspire start --isolated
aspire start --isolated
```

Każda instancja otrzymuje losowe porty, oddzielne sekrety i własny cykl życia.

## Dlaczego to jest ogromne dla agentów kodowania

Agent kodujący w twoim terminalu może teraz:

1. Uruchomić aplikację z `aspire start`
2. Zapytać o jej stan za pomocą `aspire describe`
3. Sprawdzić logi `aspire logs` w celu diagnozy problemów
4. Zatrzymać ją `aspire stop` po zakończeniu

Uruchomienie `aspire agent init` konfiguruje plik umiejętności Aspire, który uczy agentów tych poleceń.

## Podsumowanie

Tryb odłączony to ulepszenie przepływu pracy ukryte jako prosta flaga. Przeczytaj [pełny post](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) i pobierz Aspire 13.2 z `aspire update --self`.
