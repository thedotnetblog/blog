---
title: "Aktualizacja Visual Studio 2026 z kwietnia: agent chmurowy, agenty niestandardowe i agent debuggera"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Aktualizacja Visual Studio 2026 (18.5) z kwietnia przynosi integrację agenta chmurowego, niestandardowe agenty na poziomie użytkownika, narzędzia C++ w GA i Agenta Debuggera, który weryfikuje poprawki pod kątem rzeczywistego zachowania środowiska uruchomieniowego."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Aktualizacja Visual Studio 2026 (18.5) z kwietnia](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) dostarcza integrację agenta chmurowego, niestandardowe agenty na poziomie użytkownika, narzędzia C++ osiągające GA i nowego Agenta Debuggera.

## Agent chmurowy: delegowanie pracy do zdalnej sesji Copilot

Z selektora agentów w oknie Chat, wybranie **Cloud** umożliwia delegowanie zadania do zdalnego agenta kodowania Copilot. Opisujesz pracę, agent tworzy issue GitHub w repozytorium, a następnie otwiera PR po zakończeniu. Otrzymujesz powiadomienie z "View PR" / "Open in browser" — wszystko działa, gdy kontynuujesz kodowanie, a nawet gdy IDE jest zamknięte.

## Niestandardowe agenty teraz podążają za Tobą

Niestandardowe agenty na poziomie użytkownika przechowywane w `%USERPROFILE%/.github/agents/` nie są już ograniczone do repozytorium — podążają za Tobą między projektami. Ścieżkę przechowywania można skonfigurować w Tools > Opcje > GitHub > Copilot > Chat. Przycisk `+` w selektorze agentów umożliwia bezpośrednie tworzenie nowych agentów. Mają te same możliwości co agenty w zakresie repozytorium: świadomość obszaru roboczego, narzędzia, wybór modelu i połączenia MCP.

Wbudowane agenty: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Narzędzia do edycji kodu C++ osiągają GA

Dwa narzędzia — `get_symbol_call_hierarchy` i `get_symbol_class_hierarchy` — są teraz domyślnie włączone. Zapewniają Copilotowi nawigację uwzględniającą język w bazach kodu C++, obejmującą hierarchie dziedziczenia i łańcuchy wywołań funkcji. Włącz przez ikonę Tools w Copilot Chat. Najlepiej działa z modelami obsługującymi wywołania narzędzi.

## Agent Debuggera: poprawki weryfikowane pod kątem rzeczywistego zachowania środowiska uruchomieniowego

Zacznij od issue GitHub lub Azure DevOps (lub opisu w języku naturalnym), przełącz się w tryb Debugger, a agent:

1. Tworzy minimalny reproduktor
2. Generuje hipotezy awarii
3. Instrumentuje aplikację tracepoints i warunkowymi breakpoints
4. Uruchamia prawdziwą sesję debugowania
5. Analizuje dane telemetryczne na żywo
6. Sugeruje precyzyjną poprawkę

Pozostajesz w pętli przez cały proces — jest interaktywny, nie w pełni autonomiczny.

## Poprawka priorytetu IntelliSense

VS teraz wycisza uzupełnienia Copilota, gdy lista IntelliSense jest aktywna. Tylko jedna sugestia na raz. Był to częsty punkt tarcia i jest teraz domyślnie włączony.

Pełne informacje o wydaniu i pobieranie na [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
