---
title: "VS Code 1.116 — aplikacja Agents otrzymuje nawigację klawiaturową i uzupełnienia kontekstu pliku"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 skupia się na dopracowaniu aplikacji Agents — dedykowane skróty klawiaturowe, ulepszenia dostępności, uzupełnienia kontekstu pliku i rozpoznawanie linków @import CSS."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-116-agents-app-updates" >}}).*

VS Code 1.116 to wydanie z kwietnia 2026, i choć jest lżejsze niż niektóre ostatnie aktualizacje, zmiany są skoncentrowane i znaczące — szczególnie jeśli codziennie używasz aplikacji Agents.

Oto co wylądowało, na podstawie [oficjalnych notatek wydania](https://code.visualstudio.com/updates/v1_116).

## Ulepszenia aplikacji Agents

Aplikacja Agents nadal dojrzewa z dopracowaniem użyteczności, które robi realną różnicę w codziennych przepływach pracy:

**Dedykowane skróty klawiaturowe** — możesz teraz skupić widok Changes, drzewo plików w Changes i widok Chat Customizations za pomocą dedykowanych poleceń i skrótów klawiaturowych. Jeśli klikałeś po aplikacji Agents, by nawigować, to przynosi pełne przepływy pracy oparte na klawiaturze.

**Dialog pomocy dostępności** — naciśnięcie `Alt+F1` w polu wejściowym czatu teraz otwiera dialog pomocy dostępności pokazujący dostępne polecenia i skróty klawiaturowe. Użytkownicy czytników ekranu mogą też kontrolować szczegółowość ogłoszeń. Dobra dostępność przynosi korzyści wszystkim.

**Uzupełnienia kontekstu pliku** — wpisz `#` w czacie aplikacji Agents, by wywołać uzupełnienia kontekstu pliku ograniczone do twojego bieżącego obszaru roboczego. To jedno z tych małych ulepszeń komfortu pracy, które przyspiesza każdą interakcję — nie trzeba już wpisywać pełnych ścieżek pliku przy odwoływaniu się do kodu.

## Rozpoznawanie linków `@import` CSS

Miłe dla programistów frontend: VS Code teraz rozpoznaje odwołania CSS `@import` używające ścieżek node_modules. Możesz `Ctrl+kliknąć` przez importy jak `@import "some-module/style.css"` przy używaniu bundlerów. Mała rzecz, ale eliminuje punkt tarcia w przepływach pracy CSS.

## Podsumowanie

VS Code 1.116 dotyczy dopracowania — sprawia, że aplikacja Agents jest bardziej nawigowalna, bardziej dostępna i bardziej przyjazna dla klawiatury. Jeśli spędzasz znaczny czas w aplikacji Agents (a podejrzewam, że wielu z nas tak), te zmiany sumują się.

Sprawdź [pełne notatki wydania](https://code.visualstudio.com/updates/v1_116) po kompletną listę.
