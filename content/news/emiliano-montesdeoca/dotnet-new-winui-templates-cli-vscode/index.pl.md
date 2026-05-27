---
title: "dotnet new WinUI: Tworzenie aplikacji Windows bez dotykania Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Szablony projektów WinUI działają teraz z dotnet new — puste aplikacje, wzorce NavigationView i więcej. Wsparcie dla VS Code, bez Visual Studio, z wbudowanymi domyślnymi ustawieniami Fluent Design."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

Tworzenie aplikacji WinUI wymagało kiedyś Visual Studio. To się zmienia: Microsoft opublikował open-source szablony projektów i elementów dla WinUI, które działają z `dotnet new`, wprowadzając tworzenie aplikacji Windows do standardowego przepływu pracy CLI.

## Zacznij w trzech poleceniach

```shell
# Zainstaluj szablony
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Utwórz aplikację NavigationView
dotnet new winui-navview -n MyApp

# Uruchom
cd MyApp
dotnet run
```

Bez Visual Studio, bez ręcznej konfiguracji projektu. Aplikacja działa z `dotnet run`.

## Co jest zawarte

**Pusty szablon** (`dotnet new winui`) — nowoczesny punkt startowy z już podłączonym paskiem tytułu Fluent, zaktualizowaną domyślną ikoną aplikacji z zasobem `.ico`, i poprawnymi domyślnymi ustawieniami trybu jasnego/ciemnego. Lepszy niż stary pusty szablon, który pozostawiał konfigurację podstaw tobie.

**Szablon NavigationView** (`dotnet new winui-navview`) — wzorzec nawigacji master-detail, w pełni podłączony z NavigationView, nowoczesnym paskiem tytułu i wielostronicową strukturą nawigacji. Podąża za standardową sylwetką aplikacji Windows dla aplikacji opartych na nawigacji. Jeśli budujesz coś z nawigacją boczną, zacznij tutaj.

Oba szablony przestrzegają [sylwetek aplikacji Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — nowoczesnych wzorców Fluent Design dla układu, nawigacji i struktury wizualnej — od razu.

## Dlaczego to ważne dla deweloperów poza Visual Studio

Deweloperzy WinUI używający VS Code, Rider lub narzędzi wiersza poleceń byli zaniedbani. Istniejące szablony Visual Studio nie były użyteczne poza VS — trzeba było ręcznie odtworzyć strukturę projektu i podłączyć podstawy.

Te szablony są open source (patrz [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), opracowane na podstawie [opinii społeczności](https://github.com/microsoft/microsoft-ui-xaml/issues/10388) i dostępne teraz. Wsparcie Visual Studio jest w trakcie opracowywania — te same szablony będą ostatecznie działać również tam.

Dla zespołów, które chcą zautomatyzować konfigurację projektów WinUI, zintegrować ją z CI lub po prostu używać edytora innego niż Visual Studio, to znaczące ulepszenie.

Oryginalny wpis: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
