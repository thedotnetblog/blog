---
title: "VS Code 1.116 — Aplikacja Agentów Zyskuje Nawigację Klawiaturową i Dopełnienia Kontekstu Pliku"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 skupia się na dopracowaniu aplikacji Agentów — dedykowane skróty klawiszowe, ulepszenia dostępności, dopełnienia kontekstu pliku i rozwiązywanie linków CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-116-agents-app-updates" >}}).*

VS Code 1.116 to wydanie z kwietnia 2026 roku i choć jest lżejsze niż niektóre niedawne aktualizacje, zmiany są skoncentrowane i znaczące — szczególnie jeśli używasz aplikacji Agentów na co dzień.

Oto co wylądowało, na podstawie [oficjalnych notatek do wydania](https://code.visualstudio.com/updates/v1_116).

## Ulepszenia aplikacji Agentów

Aplikacja Agentów nadal dojrzewa z dopracowaniem użyteczności, które robi realną różnicę w codziennych przepływach pracy:

**Dedykowane skróty klawiszowe** — możesz teraz skupiać widok Zmian, drzewo plików w Zmianach i widok Dostosowań Czatu za pomocą dedykowanych poleceń i skrótów klawiszowych. Przynosi to w pełni sterowane klawiaturą przepływy pracy.

**Okno dialogowe pomocy dostępności** — naciśnięcie `Alt+F1` w polu wejściowym czatu otwiera teraz okno dialogowe pomocy dostępności pokazujące dostępne polecenia i skróty. Użytkownicy czytników ekranu mogą również kontrolować szczegółowość ogłoszeń.

**Dopełnienia kontekstu pliku** — wpisz `#` w czacie aplikacji Agentów, aby uruchomić dopełnienia kontekstu pliku w zakresie bieżącej przestrzeni roboczej. Małe ulepszenie jakości życia, które przyspiesza każdą interakcję.

## Rozwiązywanie linków CSS `@import`

Miła wiadomość dla programistów frontend: VS Code teraz rozwiązuje odwołania CSS `@import`, które używają ścieżek node_modules. Możesz `Ctrl+klikać` przez importy takie jak `@import "some-module/style.css"` podczas używania bundlerów.

## Podsumowanie

VS Code 1.116 to wydanie skupione na udoskonaleniu — sprawia, że aplikacja Agentów jest bardziej nawigowalna, bardziej dostępna i bardziej przyjazna dla klawiatury. Sprawdź [pełne notatki do wydania](https://code.visualstudio.com/updates/v1_116), aby zobaczyć pełną listę.
