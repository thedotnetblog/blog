---
title: "VS Code 1.120: Bezpieczne Monity Hasła, Selektor Rozmiaru Kontekstu, Metadane GitHub w Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 to skoncentrowane wydanie dla użytkowników Copilot: bezpieczna obsługa monitów hasła, selektor rozmiaru kontekstu modelu, metadane PR GitHub w sesjach agenta i zarządzanie archiwum sesji."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 dostarczono z zestawem ulepszeń agenta Copilot, które są małe indywidualnie, ale zauważalnie lepsze w codziennym użytkowaniu.

## Bezpieczne Wykrywanie Monitów Hasła w Terminalach Agenta

Gdy agent Copilot uruchamia polecenie terminala, które wyzwala monit o hasło lub hasło, VS Code teraz to wykrywa i wyświetla okno dialogowe potwierdzenia. Okno dialogowe skupia terminal, dzięki czemu możesz wpisać sekret bezpośrednio — i co ważne, sekrety nigdy nie są kierowane przez model.

To znaczące ulepszenie bezpieczeństwa. Wcześniej agenci uruchamiający polecenia, które wyzwalały monity uwierzytelniania, mogli tworzyć sytuacje, w których użytkownicy mogliby nieumyślnie ujawnić poświadczenia. Ogłoszenie czytnika ekranu oznacza, że użytkownicy ułatwień dostępu również otrzymują powiadomienie.

## Selektor Rozmiaru Kontekstu w Selektorze Modelu

Nowy selektor rozmiaru kontekstu pozwala wybrać, ile kontekstu model używa dla sesji. Różne modele mają różne rozmiary okna kontekstu, a niektóre przepływy pracy korzystają na jego ograniczaniu (mniejsze opóźnienie, mniejszy koszt) lub maksymalizacji (złożone bazy kodu, długo działające sesje).

## Metadane PR GitHub w Sesjach Agent Host

Dla sesji wspieranych przez repozytorium GitHub, VS Code teraz wyświetla metadane GitHub — w tym przycisk pull request — w interfejsie użytkownika agent host. Mniej przełączania kontekstu do przeglądarki lub rozszerzenia GitHub podczas pracy nad PR.

## Zarządzanie Archiwum Sesji Czatu

Dwa ulepszenia dla Quick Pick sesji:
- Zarchiwizowane sesje są domyślnie ukryte (mniej wizualnego bałaganu)
- Wyszukiwanie nadal pasuje do zarchiwizowanych sesji, więc możesz przywrócić jedną według tytułu

Sesje są również domyślnie grupowane według ostatniości, co ułatwia znajdowanie ostatnich prac.

## Wykrywanie Wtyczek CLI Copilot

VS Code teraz automatycznie wykrywa wtyczki Copilot CLI zainstalowane przez użytkownika z `~/.copilot/installed-plugins/`. Jeśli skonfigurowano WinUI lub inne umiejętności agenta specyficzne dla domeny, są one pobierane bez ręcznej konfiguracji.

## Niestandardowy API Edytora Diff (Wersja zapoznawcza)

Dla autorów rozszerzeń: nowy proponowany API `customDiffEditorProvider` pozwala rozszerzeniom renderować zunifikowaną różnicę w jednym widoku webview z dostępem do oryginalnych i zmodyfikowanych dokumentów, zamiast dwóch niestandardowych widoków edytora obok siebie.

Oryginalny post: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
