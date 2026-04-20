---
title: "VS Code 1.117: Agenty dostają własne gałęzie Git i jestem za tym wszystkimi czterema"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 dostarcza izolację worktree dla sesji agentów, trwały tryb Autopilot i wsparcie dla subagentów. Agentyczny przepływ pracy kodowania właśnie stał się znacznie bardziej realny."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

Linia między "asystentem AI" a "kolegą AI" nieustannie się zaciera. VS Code 1.117 właśnie wyszedł i [pełne notatki wydania](https://code.visualstudio.com/updates/v1_117) są pełne treści, ale historia jest tu jasna: agenty stają się pierwszoklasowymi obywatelami w twoim przepływie pracy deweloperskiej.

Oto co naprawdę ważne.

## Tryb Autopilot wreszcie pamięta twoje preferencje

Wcześniej musiałeś ponownie włączać Autopilot przy każdej nowej sesji. Irytujące. Teraz twój tryb uprawnień utrzymuje się między sesjami i możesz skonfigurować domyślny.

Host Agenta obsługuje trzy konfiguracje sesji:

- **Domyślny** — narzędzia proszą o potwierdzenie przed uruchomieniem
- **Pomiń** — automatycznie zatwierdza wszystko
- **Autopilot** — pełna autonomia, odpowiada na własne pytania i kontynuuje

Jeśli szkieletujesz nowy projekt .NET z migracjami, Docker i CI — ustaw go na Autopilot raz i zapomnij o tym. Ta preferencja zostaje.

## Izolacja worktree i git dla sesji agentów

To jest ta duża. Sesje agentów obsługują teraz pełną izolację worktree i git. To oznacza, że gdy agent pracuje nad zadaniem, dostaje własną gałąź i katalog roboczy. Twoja gałąź główna pozostaje nienaruszona.

Co więcej — Copilot CLI generuje znaczące nazwy gałęzi dla tych sesji worktree. Koniec z `agent-session-abc123`. Dostajesz coś, co faktycznie opisuje co agent robi.

Dla programistów .NET pracujących na wielu gałęziach funkcji lub naprawiających błędy, gdy długie zadanie szkieletowania działa, to zmiana zasad gry. Możesz mieć agenta budującego kontrolery API w jednym worktree, podczas gdy ty debugujesz warstwę usługową w innym. Żadnych konfliktów. Żadnego stashowania. Żadnego bałaganu.

## Subagenty i zespoły agentów

Protokół Hosta Agenta obsługuje teraz subagenty. Agent może uruchamiać inne agenty do obsługi części zadania. Pomyśl o tym jak o delegowaniu — twój główny agent koordynuje, a wyspecjalizowane agenty obsługują kawałki.

To wczesne, ale potencjał dla przepływów pracy .NET jest oczywisty. Wyobraź sobie jednego agenta obsługującego twoje migracje EF Core podczas gdy inny konfiguruje testy integracyjne. Jeszcze tam nie jesteśmy w pełni, ale wsparcie protokołu lądujące teraz oznacza, że narzędzia pojawią się szybko.

## Wyjście terminala automatycznie włączone gdy agenty wysyłają dane wejściowe

Małe, ale znaczące. Gdy agent wysyła dane wejściowe do terminala, wyjście terminala jest teraz automatycznie dołączane do kontekstu. Wcześniej agent musiał wykonać dodatkową turę tylko by zobaczyć co się stało.

Jeśli kiedykolwiek obserwowałeś agenta uruchamiającego `dotnet build`, niepowodzenie i następnie kolejny przebieg tylko by zobaczyć błąd — to tarcie zniknęło. Widzi wyjście natychmiast i reaguje.

## Samooaktualizacja aplikacji Agents na macOS

Samodzielna aplikacja Agents na macOS teraz się samooaktualizuje. Koniec z ręcznym pobieraniem nowych wersji. Po prostu pozostaje aktualna.

## Mniejsze rzeczy warte wiedzy

- **Podglądy package.json** teraz pokazują zarówno zainstalowaną wersję jak i ostatnio dostępną. Przydatne jeśli zarządzasz narzędziami npm obok projektów .NET.
- **Obrazy w komentarzach JSDoc** renderują się poprawnie w podglądach i uzupełnieniach.
- **Sesje Copilot CLI** teraz wskazują czy zostały utworzone przez VS Code czy zewnętrznie — przydatne gdy przeskakujesz między terminalami.
- **Copilot CLI, Claude Code i Gemini CLI** są rozpoznawane jako typy powłoki. Edytor wie co uruchamiasz.

## Wnioski

VS Code 1.117 nie jest efektownym zrzutem funkcji. To infrastruktura. Izolacja worktree, trwałe uprawnienia, protokoły subagentów — to są cegiełki dla przepływu pracy, gdzie agenty obsługują prawdziwe, równoległe zadania bez nadepnięcia na twój kod.

Jeśli budujesz z .NET i jeszcze nie zanurzyłeś się w agentyczny przepływ pracy, szczerze, teraz jest czas, by zacząć.
