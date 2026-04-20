---
title: "VS Code 1.115 — Powiadomienia Terminalu w Tle, Tryb Agenta SSH i Więcej"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 przynosi powiadomienia terminalu w tle dla agentów, zdalne hostowanie agentów przez SSH, wklejanie plików w terminalach i śledzenie edycji uwzględniające sesje. Oto co ważne dla programistów .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 właśnie [wylądował](https://code.visualstudio.com/updates/v1_115) i choć jest to lżejsze wydanie pod względem głównych funkcji, ulepszenia związane z agentami są naprawdę użyteczne, jeśli pracujesz z asystentami AI codziennie.

Pozwól, że podkreślę, co naprawdę warto wiedzieć.

## Terminale w tle mówią z powrotem do agentów

To wyróżniająca się funkcja. Terminale w tle teraz automatycznie powiadamiają agentów, gdy polecenia się kończą, łącznie z kodem wyjścia i wynikiem terminalu. Monity wejściowe w terminalach w tle są również wykrywane i prezentowane użytkownikowi.

Dlaczego to ma znaczenie? Jeśli używałeś trybu agenta Copilot do uruchamiania poleceń kompilacji lub pakietów testowych w tle, znasz ból "czy to już się skończyło?" — terminale w tle były w zasadzie strzał i zapomnij. Teraz agent dostaje powiadomienie, gdy Twój `dotnet build` lub `dotnet test` się kończy, widzi wynik i może zareagować.

Jest też nowe narzędzie `send_to_terminal`, które pozwala agentom wysyłać polecenia do terminali w tle z potwierdzeniem użytkownika.

## Zdalne hostowanie agentów przez SSH

VS Code obsługuje teraz połączenie z zdalnymi maszynami przez SSH, automatycznie instalując CLI i uruchamiając go w trybie hosta agenta.

## Śledzenie edycji w sesjach agentów

Edycje plików wykonane podczas sesji agentów są teraz śledzone i przywracane, z różnicami, cofaniem/ponawianiem i przywracaniem stanu.

## Świadomość kart przeglądarki i inne ulepszenia

Kilka dodatkowych ulepszeń jakości życia:

- **Śledzenie kart przeglądarki** — czat może teraz śledzić i linkować do kart przeglądarki otwartych podczas sesji
- **Wklejanie plików w terminalu** — wklejaj pliki (łącznie z obrazami) do terminalu przez Ctrl+V
- **Pokrycie testów w minimapie** — wskaźniki pokrycia testów pojawiają się teraz w minimapie
- **Ściśnięcie palcami do zoomu na Mac** — zintegrowana przeglądarka obsługuje gesty ściśnięcia
- **Favicon w Go to File** — otwarte strony internetowe pokazują favicons na liście szybkiego wyboru

## Podsumowanie

VS Code 1.115 to wydanie przyrostowe, ale ulepszenia agentów — powiadomienia terminalu w tle, hostowanie agentów SSH i śledzenie edycji — sumują się do zauważalnie płynniejszego doświadczenia. Sprawdź [pełne notatki do wydania](https://code.visualstudio.com/updates/v1_115), aby poznać wszystkie szczegóły.
