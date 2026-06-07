---
title: "VS Code 1.121: Przypinanie Ulubionych Modeli, Kompresja Wyjścia Terminala, Agent SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 dodaje ulubione modele, rozszerzoną kompresję wyjścia terminala dla narzędzi testowych i budowania, timer ciszy bezczynności dla terminali w tle i interaktywne uwierzytelnianie SSH via klawiaturę w agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 kontynuuje ulepszenia jakości agenta Copilot z wersji 1.120, skupiając się na zarządzaniu modelami i zachowaniu terminala.

## Przypinanie Ulubionych Modeli

Selektor modeli obsługuje teraz przypinanie. Jeśli zawsze sięgasz po ten sam model lub dwa, przypnij je do górnej części listy. Zmniejsza przewijanie gdy masz dostęp do wielu modeli od wielu dostawców.

## Rozszerzona Kompresja Wyjścia Terminala

Narzędzie terminala agenta już kompresowało wyjście dla typowych poleceń. 1.121 rozszerza to na narzędzia testowe i budowania:

- **Narzędzia testowe:** `pytest`, `jest`, `cargo test`
- **Narzędzia budowania:** `tsc`, `cargo build`, `make`
- **Lintery, Docker, menedżery pakietów**

Długie wyjścia budowania i raporty niepowodzeń testów są kompresowane do odpowiednich fragmentów przed przekazaniem do modelu. Utrzymuje to zużycie kontekstu na zarządzalnym poziomie gdy agent uruchamia cykle budowania lub zestawy testów, które mogą generować tysiące linii wyjścia.

## Timer Ciszy Bezczynności dla Terminali w Tle

Nowy timer ciszy bezczynności dla narzędzia `run_in_terminal`: jeśli polecenie synchroniczne nie generuje wyjścia przez konfigurowalny okres, automatycznie jest promowane do wykonania w tle. Zapobiega to blokowaniu agenta przez długo działające polecenia gdy przetwarzają po cichu. Otrzymujesz ID terminala do późniejszego sprawdzenia.

## Zmienna Środowiskowa VSCODE_AGENT

Gdy Copilot Chat uruchamia polecenia w terminalu, ustawiana jest teraz zmienna środowiskowa `VSCODE_AGENT`. Przydatne jeśli masz skrypty lub narzędzia, które zachowują się inaczej gdy są wywoływane z sesji agenta versus interaktywnie.

## Dodaj do Czatu z Przeglądarki

Kliknięcie prawym przyciskiem w zintegrowanej przeglądarce pokazuje teraz opcję "Dodaj do Czatu". Zaznacz treść ze strony internetowej i dodaj ją bezpośrednio do kontekstu Copilot Chat bez kopiowania i wklejania.

## Naprawiono: Wieloliniowe Polecenia Shell w Agent Host

Długo oczekiwana naprawa błędu: wieloliniowe polecenia shell w narzędziu terminala Agent Host teraz działają poprawnie. Wcześniej mogły one zawodzić lub generować nieprawidłowe zachowanie.

## Interaktywne Uwierzytelnianie SSH via Klawiaturę

Połączenia SSH Agent Host obsługują teraz interaktywne uwierzytelnianie via klawiaturę — awaryjną metodę uwierzytelniania używaną przez niektóre serwery SSH (w tym niektóre starsze konfiguracje korporacyjne). Agenci pracujący na zdalnych hostach SSH są mniej narażeni na błędy uwierzytelniania.

Oryginalny post: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
