---
title: "dotnet new WinUI: Crea aplicacions Windows sense tocar Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Les plantilles de projecte WinUI ara funcionen amb dotnet new — aplicacions en blanc, patrons NavigationView i més. Suport per a VS Code, sense necessitat de Visual Studio, amb valors predeterminats de Fluent Design integrats."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

El desenvolupament de WinUI requeria Visual Studio. Això està canviant: Microsoft ha publicat plantilles de projectes i elements de codi obert per a WinUI que funcionen amb `dotnet new`, integrant el desenvolupament d'aplicacions Windows al flux de treball estàndard de la CLI.

## Comença en tres ordres

```shell
# Instal·la les plantilles
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Crea una aplicació NavigationView
dotnet new winui-navview -n MyApp

# Executa-la
cd MyApp
dotnet run
```

Sense Visual Studio, sense configuració manual del projecte. L'aplicació s'executa amb `dotnet run`.

## Què s'inclou

**Plantilla en blanc** (`dotnet new winui`) — un punt de partida modern amb una barra de títol Fluent ja connectada, una icona d'aplicació predeterminada actualitzada amb un recurs `.ico`, i valors predeterminats correctes per al mode clar/fosc. Millor que l'antiga plantilla en blanc que et deixava configurar les bases tu mateix.

**Plantilla NavigationView** (`dotnet new winui-navview`) — el patró de navegació mestre-detall, completament connectat amb un NavigationView, barra de títol moderna i estructura de navegació multipàgina. Segueix la silueta estàndard de les aplicacions Windows per a aplicacions basades en navegació. Si estàs construint alguna cosa amb navegació lateral, comença aquí.

Les dues plantilles segueixen les [siluetes d'aplicacions Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — patrons moderns de Fluent Design per al disseny, la navegació i l'estructura visual — directament.

## Per què importa per als desenvolupadors fora de Visual Studio

Els desenvolupadors de WinUI que usen VS Code, Rider o eines de línia d'ordres han estat desatesos. Les plantilles existents de Visual Studio no eren utilitzables fora de VS — calia recrear manualment l'estructura del projecte i configurar les bases.

Aquestes plantilles són de codi obert (veure [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), desenvolupades a partir dels [comentaris de la comunitat](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), i disponibles ara. El suport de Visual Studio està en procés — aquestes mateixes plantilles funcionaran allà eventualment.

Per a equips que volen automatitzar la configuració dels seus projectes WinUI, integrar-la a la CI, o simplement usar un editor diferent de Visual Studio, això és una millora significativa.

Post original: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
