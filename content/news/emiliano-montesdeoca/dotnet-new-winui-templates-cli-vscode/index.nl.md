---
title: "dotnet new WinUI: Windows-apps maken zonder Visual Studio aan te raken"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI-projectsjablonen werken nu met dotnet new — lege apps, NavigationView-patronen en meer. VS Code-ondersteuning, geen Visual Studio vereist, met Fluent Design-standaarden ingebakken."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI-ontwikkeling vereiste vroeger Visual Studio. Dat verandert: Microsoft heeft open source project- en itemsjablonen voor WinUI gepubliceerd die werken met `dotnet new`, waardoor Windows-app-ontwikkeling in de standaard CLI-workflow wordt gebracht.

## Aan de slag in drie commando's

```shell
# Sjablonen installeren
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Een NavigationView-app aanmaken
dotnet new winui-navview -n MyApp

# Uitvoeren
cd MyApp
dotnet run
```

Geen Visual Studio, geen handmatige projectinstellingen. De app wordt uitgevoerd met `dotnet run`.

## Wat is inbegrepen

**Leeg sjabloon** (`dotnet new winui`) — een modern startpunt met een al verbonden Fluent-titelbalk, bijgewerkt standaard app-pictogram met `.ico`-asset, en correcte standaardwaarden voor licht/donker modus. Beter dan het oude lege sjabloon waarbij je de basisinstellingen zelf moest configureren.

**NavigationView-sjabloon** (`dotnet new winui-navview`) — het master-detail navigatiepatroon, volledig verbonden met een NavigationView, moderne titelbalk en meerpagina navigatiestructuur. Volgt het standaard Windows app-silhouet voor navigatiegebaseerde apps. Als je iets bouwt met zijnavigatie, begin hier.

Beide sjablonen volgen de [Windows app-silhouetten](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — moderne Fluent Design-patronen voor lay-out, navigatie en visuele structuur — direct uit de doos.

## Waarom het belangrijk is voor ontwikkelaars buiten Visual Studio

WinUI-ontwikkelaars die VS Code, Rider of commandoregeltools gebruiken zijn slecht bediend. De bestaande Visual Studio-sjablonen waren niet bruikbaar buiten VS — je moest de projectstructuur handmatig nabootsen en de basisinstellingen zelf verbinden.

Deze sjablonen zijn open source (zie [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), ontwikkeld op basis van [community-feedback](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), en nu beschikbaar. Visual Studio-ondersteuning is in de maak — deze zelfde sjablonen zullen daar uiteindelijk ook werken.

Voor teams die hun WinUI-projectinstellingen willen scripten, integreren in CI, of simpelweg een andere editor dan Visual Studio willen gebruiken, is dit een betekenisvolle verbetering.

Originele post: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
