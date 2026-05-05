---
title: "Windows App Dev CLI v0.3: F5 z terminala i UI Automation dla agentów"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 przynosi winapp run do uruchamiania i debugowania z terminala, winapp ui do automatyzacji interfejsu oraz nowy pakiet NuGet umożliwiający działanie dotnet run z zapakowanymi aplikacjami."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Ten artykuł został przetłumaczony automatycznie. Aby zobaczyć oryginał, [kliknij tutaj]({{< ref "index.md" >}}).*

Doświadczenie F5 w Visual Studio jest świetne. Ale otwieranie VS tylko po to, żeby uruchomić i debugować zapakowaną aplikację Windows — czy to w potoku CI, zautomatyzowanym workflowie, czy gdy agent AI wykonuje testy — to zbędny narzut.

Windows App Development CLI v0.3 właśnie [wyszło](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) i rozwiązuje ten problem bezpośrednio dzięki dwóm głównym funkcjom: `winapp run` i `winapp ui`.

## winapp run: F5 z dowolnego miejsca

`winapp run` przyjmuje folder niezapakowanej aplikacji i manifest, wykonując wszystko, co VS robi przy uruchamianiu debugowania: rejestruje luźny pakiet, uruchamia aplikację i zachowuje `LocalState` między ponownymi deploymentami.

```bash
# Zbuduj aplikację, a następnie uruchom ją jako zapakowaną aplikację
winapp run ./bin/Debug
```

Działa dla WinUI, WPF, WinForms, Console, Avalonia i innych. Tryby są zaprojektowane zarówno dla deweloperów, jak i zautomatyzowanych workflowów:

- **`--detach`**: Uruchamia i natychmiast zwraca kontrolę do terminala. Idealny dla CI.
- **`--unregister-on-exit`**: Usuwa zarejestrowany pakiet przy zamknięciu aplikacji.
- **`--debug-output`**: Przechwytuje komunikaty `OutputDebugString` i wyjątki w czasie rzeczywistym.

## Nowy pakiet NuGet: dotnet run dla zapakowanych aplikacji

Dla deweloperów .NET jest nowy pakiet NuGet: `Microsoft.Windows.SDK.BuildTools.WinApp`. Po instalacji `dotnet run` obsługuje cały inner loop: budowanie, przygotowanie pakietu loose-layout, rejestrację w Windows i uruchomienie — wszystko w jednym kroku.

```bash
winapp init
# lub
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation z wiersza poleceń

To funkcja otwierająca scenariusze agentyczne. `winapp ui` zapewnia pełny dostęp UI Automation do dowolnej działającej aplikacji Windows — WPF, WinForms, Win32, Electron, WinUI3 — bezpośrednio z terminala.

Co można robić:

- Wylistować wszystkie okna najwyższego poziomu
- Nawigować po pełnym drzewie UI Automation dowolnego okna
- Wyszukiwać elementy po nazwie, typie lub ID automatyzacji
- Klikać, wywoływać i ustawiać wartości
- Robić zrzuty ekranu
- Czekać na pojawienie się elementów — idealne do synchronizacji testów

Połączenie `winapp ui` z `winapp run` daje kompletny workflow build → uruchomienie → weryfikacja z terminala. Agent może uruchomić aplikację, sprawdzić stan UI, programowo z nią interagować i zwalidować wynik.

## Inne nowości

- **`winapp unregister`**: Usuwa sideloadowany pakiet po zakończeniu pracy.
- **`winapp manifest add-alias`**: Dodaje alias do uruchamiania aplikacji po nazwie z terminala.
- **Uzupełnianie tabulatorem**: Jedno polecenie do skonfigurowania uzupełniania w PowerShell.

## Jak zdobyć

```bash
winget install Microsoft.WinAppCli
# lub
npm install -g @microsoft/winappcli
```

CLI jest w publicznym podglądzie. Pełna dokumentacja dostępna w [repozytorium GitHub](https://github.com/microsoft/WinAppCli), a wszystkie szczegóły w [oryginalnym ogłoszeniu](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/).
