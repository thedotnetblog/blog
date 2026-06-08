---
title: "Wtyczka Agenta WinUI dla GitHub Copilot i Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft wydał umiejętności agenta dla rozwoju WinUI: scaffold, kompilacja, uruchomienie, testy, iteracja — wszystko z GitHub Copilot CLI lub Claude Code. Kluczowa innowacja: dedykowane narzędzia zakotwiczające agenta w faktach specyficznych dla WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft opublikował zestaw open-source umiejętności agenta dla tworzenia aplikacji WinUI, dostępny pod adresem [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Instalacja i Konfiguracja

Zainstaluj wtyczkę za pomocą `/plugin install winui@awesome-copilot`, a następnie uruchom wstępną konfigurację za pomocą `/winui:winui-setup`. Proces konfiguracji weryfikuje wymagania wstępne, instaluje niezbędne zależności i konfiguruje środowisko do tworzenia aplikacji WinUI.

## Pętla Tworzenia End-to-End

Umiejętności obejmują pełny cykl tworzenia:

- **Scaffold:** Generuje właściwy szablon projektu używając `dotnet new WinUI` z odpowiednimi parametrami — agent zna właściwe szablony i domyślne wartości konfiguracji.
- **Kompilacja:** Zarządza spakowanym modelem wykonywania wymaganym przez aplikacje WinUI, w tym podpisywaniem pakietów i konfiguracjami manifestu.
- **Interakcja i walidacja:** Uruchamia aplikację, wchodzi z nią w interakcję i weryfikuje zachowanie.
- **Naprawianie błędów kompilacji:** Agent rozumie komunikaty błędów specyficzne dla WinUI i wie, jak je naprawić.

## Wydajność Tokenów przez Dedykowane Narzędzia

Kluczową innowacją jest to, że umiejętności zawierają dedykowane narzędzia, które pobierają konkretne dane referencyjne na żądanie:

- Szczegóły API WinUI i Fluent Design
- Wzorce MVVM i najlepsze praktyki
- Pakowanie MSIX, podpisywanie kodu i przesyłanie do Store
- Dostępność, motywy i automatyzacja UI

Zamiast wstrzykiwać całą dokumentację WinUI do kontekstu, narzędzia pobierają dokładnie to, czego agent potrzebuje w danej chwili. Utrzymuje to wydajne wykorzystanie kontekstu i poprawia precyzję w wyspecjalizowanych domenach.

## Dlaczego Dedykowane Umiejętności Są Ważne

Modele języka ogólnego przeznaczenia mają ograniczoną wiedzę o niuansach specyficznych dla WinUI: spakowany model wykonywania, API Fluent Design, integracja MSIX lub specyficzny sposób, w jaki Windows App SDK opakowuje funkcjonalność Win32. Dedykowane narzędzia rozwiązują to przez zakotwiczenie agenta w zweryfikowanych faktach WinUI zamiast potencjalnie przestarzałej lub błędnej wiedzy modelu.

Ten sam wzorzec dotyczy każdego wyspecjalizowanego frameworka lub SDK z własnymi konwencjami i wymaganiami, które różnią się od ogólnych wzorców tworzenia.

Oryginalny post: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
