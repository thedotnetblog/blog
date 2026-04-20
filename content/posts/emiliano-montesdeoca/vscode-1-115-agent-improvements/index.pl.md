---
title: "VS Code 1.115 — powiadomienia terminala w tle, tryb agenta przez SSH i więcej"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 przynosi powiadomienia terminala w tle dla agentów, zdalne hostowanie agentów przez SSH, wklejanie plików do terminali i śledzenie edycji uwzględniające sesje. Oto co ważne dla programistów .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 właśnie [wyszedł](https://code.visualstudio.com/updates/v1_115) i choć jest to lżejsze wydanie pod względem nagłówkowych funkcji, ulepszenia związane z agentami są naprawdę przydatne, jeśli codziennie pracujesz z asystentami AI.

Pozwól, że wyróżnię to, co naprawdę warto wiedzieć.

## Terminale w tle informują agentów

To jest wyróżniająca się funkcja. Terminale w tle teraz automatycznie powiadamiają agentów o zakończeniu poleceń, w tym o kodzie wyjścia i wyjściu terminala. Monity wejściowe w terminalach w tle są również wykrywane i udostępniane użytkownikowi.

Dlaczego to ważne? Jeśli używałeś trybu agenta Copilot do uruchamiania poleceń kompilacji lub zestawów testów w tle, znasz ból "czy to już skończyło?" — terminale w tle były praktycznie na zasadzie "odpal i zapomnij". Teraz agent dostaje powiadomienie, gdy twoje `dotnet build` lub `dotnet test` zakończy się, widzi wyjście i może odpowiednio zareagować. To mała zmiana, która sprawia, że przepływy pracy oparte na agentach są znacznie bardziej niezawodne.

Jest też nowe narzędzie `send_to_terminal`, które pozwala agentom wysyłać polecenia do terminali w tle z potwierdzeniem użytkownika, naprawiając problem gdzie `run_in_terminal` z limitem czasu przenosiło terminale do tła i czyniło je tylko do odczytu.

## Zdalne hostowanie agentów przez SSH

VS Code obsługuje teraz połączenie ze zdalnymi maszynami przez SSH, automatycznie instalując CLI i uruchamiając go w trybie hosta agenta. Oznacza to, że twoje sesje agenta AI mogą bezpośrednio celować w zdalne środowiska — przydatne dla programistów .NET, którzy kompilują i testują na serwerach Linux lub maszynach wirtualnych w chmurze.

## Śledzenie edycji w sesjach agenta

Edycje plików dokonane podczas sesji agenta są teraz śledzone i przywracane, z diff, cofnij/ponów i przywróceniem stanu. Jeśli agent wprowadza zmiany do twojego kodu i coś pójdzie nie tak, możesz zobaczyć dokładnie co się zmieniło i to cofnąć. Spokój ducha przy pozwalaniu agentom modyfikować twoją bazę kodu.

## Świadomość kart przeglądarki i inne ulepszenia

Kilka kolejnych ulepszeń komfortu pracy:

- **Śledzenie kart przeglądarki** — czat może teraz śledzić i linkować do kart przeglądarki otwartych podczas sesji, by agenty mogły odwoływać się do stron internetowych, na które patrzysz
- **Wklejanie plików do terminala** — wklej pliki (w tym obrazy) do terminala przez Ctrl+V, przeciągnij i upuść lub kliknij prawym przyciskiem
- **Pokrycie testów w minimapie** — wskaźniki pokrycia testów są teraz widoczne w minimapie dla szybkiego przeglądu wizualnego
- **Szczypanie do powiększenia na Mac** — zintegrowana przeglądarka obsługuje gesty szczypania do powiększenia
- **Uprawnienia Copilot w sesjach** — pasek stanu pokazuje informacje o użyciu w widoku Sesji
- **Favicon w Przejdź do pliku** — otwarte strony internetowe pokazują favicon na liście szybkiego wyboru

## Podsumowanie

VS Code 1.115 to wydanie przyrostowe, ale ulepszenia agentów — powiadomienia terminala w tle, zdalne hostowanie agentów przez SSH i śledzenie edycji — składają się na zauważalnie płynniejsze doświadczenie przy programowaniu wspomaganym przez AI. Jeśli używasz trybu agenta Copilot dla projektów .NET, to właśnie takie poprawki komfortu pracy redukują codzienne tarcie.

Sprawdź [pełne notatki wydania](https://code.visualstudio.com/updates/v1_115) po każdy szczegół.
