---
title: "VS Code 1.117: Agenci Otrzymują Własne Gałęzie Git i Jestem Za"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 dostarcza izolację worktree dla sesji agentów, trwały tryb Autopilot i wsparcie dla subagentów. Agentatyczny przepływ pracy stał się o wiele bardziej realny."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

Granica między "asystentem AI" a "współpracownikiem AI" stale się zaciera. VS Code 1.117 właśnie wylądował i [pełne notatki do wydania](https://code.visualstudio.com/updates/v1_117) są gęste, ale historia jest jasna: agenci stają się obywatelami pierwszej klasy w Twoim przepływie pracy.

Oto co naprawdę ma znaczenie.

## Tryb Autopilot w końcu pamięta Twoje preferencje

Wcześniej musiałeś ponownie włączać Autopilot za każdym razem, gdy zaczynałeś nową sesję. Irytujące. Teraz Twój tryb uprawnień utrzymuje się między sesjami i możesz skonfigurować domyślny.

Host Agenta obsługuje trzy konfiguracje sesji:

- **Default** — narzędzia proszą o potwierdzenie przed uruchomieniem
- **Bypass** — automatycznie zatwierdza wszystko
- **Autopilot** — w pełni autonomiczny, odpowiada na własne pytania i kontynuuje

Jeśli tworzysz nowy projekt .NET z migracjami, Dockerem i CI — ustaw raz na Autopilot i zapomnij. Ta preferencja zostaje.

## Izolacja worktree i git dla sesji agentów

To jest ta wielka. Sesje agentów obsługują teraz pełną izolację worktree i git. Oznacza to, że gdy agent pracuje nad zadaniem, otrzymuje własną gałąź i katalog roboczy. Twoja główna gałąź pozostaje nienaruszony.

Co więcej — Copilot CLI generuje sensowne nazwy gałęzi dla tych sesji worktree. Koniec z `agent-session-abc123`. Dostajesz coś, co naprawdę opisuje, co agent robi.

Dla programistów .NET uruchamiających wiele gałęzi funkcji lub naprawiających błędy, gdy długie zadanie szkieletowania trwa, to rewolucja. Możesz mieć agenta budującego kontrolery API w jednym worktree, gdy Ty debugujesz warstwę serwisu w innym. Żadnych konfliktów. Żadnego stashowania. Żadnego bałaganu.

## Subagenci i zespoły agentów

Agent Host Protocol teraz obsługuje subagentów. Agent może uruchamiać inne agenty do obsługi części zadania. Pomyśl o tym jako delegowaniu — główny agent koordynuje, a wyspecjalizowane agenty obsługują kawałki.

To jest wczesne, ale potencjał dla przepływów pracy .NET jest oczywisty. Wyobraź sobie jednego agenta obsługującego migracje EF Core, gdy inny konfiguruje testy integracyjne.

## Wynik terminalu automatycznie dołączany, gdy agenci wysyłają wejście

Małe, ale znaczące. Gdy agent wysyła wejście do terminalu, wynik terminalu jest teraz automatycznie dołączany do kontekstu. Jeśli kiedykolwiek obserwowałeś agenta uruchamiającego `dotnet build`, który zawiódł, a następnie musiał wykonać kolejną rundę tylko żeby zobaczyć błąd — to tarcie zniknęło.

## Samodzielna aktualizacja aplikacji Agentów na macOS

Samodzielna aplikacja Agentów na macOS teraz aktualizuje się sama. Koniec z ręcznym pobieraniem nowych wersji.

## Podsumowanie

VS Code 1.117 to infrastruktura. Izolacja worktree, trwałe uprawnienia, protokoły subagentów — to są elementy składowe dla przepływu pracy, w którym agenci obsługują prawdziwe, równoległe zadania bez ingerencji w Twój kod. Jeśli budujesz z .NET i jeszcze nie zanurzyłeś się w agentyczny przepływ pracy, szczerze, teraz jest czas, żeby zacząć.
