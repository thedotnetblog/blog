---
title: "dotnet new WinUI: Windows-Apps erstellen ohne Visual Studio anzufassen"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI-Projektvorlagen funktionieren jetzt mit dotnet new — leere Apps, NavigationView-Muster und mehr. VS Code-Unterstützung, kein Visual Studio erforderlich, mit integrierten Fluent-Design-Standardeinstellungen."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI-Entwicklung erforderte früher Visual Studio. Das ändert sich: Microsoft hat Open-Source-Projekt- und Elementvorlagen für WinUI veröffentlicht, die mit `dotnet new` funktionieren und die Windows-App-Entwicklung in den Standard-CLI-Workflow bringen.

## In drei Befehlen loslegen

```shell
# Vorlagen installieren
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Eine NavigationView-App erstellen
dotnet new winui-navview -n MyApp

# Ausführen
cd MyApp
dotnet run
```

Kein Visual Studio, keine manuelle Projekteinrichtung. Die App läuft mit `dotnet run`.

## Was enthalten ist

**Leere Vorlage** (`dotnet new winui`) — ein moderner Ausgangspunkt mit einer bereits konfigurierten Fluent-Titelleiste, aktualisiertem Standard-App-Symbol mit `.ico`-Asset und korrekten Hell-/Dunkel-Modus-Standardwerten. Besser als die alte leere Vorlage, bei der man die Grundlagen selbst konfigurieren musste.

**NavigationView-Vorlage** (`dotnet new winui-navview`) — das Master-Detail-Navigationsmuster, vollständig eingerichtet mit einer NavigationView, moderner Titelleiste und mehrseitiger Navigationsstruktur. Folgt der standardmäßigen Windows-App-Silhouette für navigationsbasierte Apps. Wenn Sie etwas mit Seitennavigation bauen, fangen Sie hier an.

Beide Vorlagen folgen den [Windows-App-Silhouetten](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — moderne Fluent-Design-Muster für Layout, Navigation und visuelle Struktur — direkt aus der Box.

## Warum das für Entwickler außerhalb von Visual Studio wichtig ist

WinUI-Entwickler, die VS Code, Rider oder Befehlszeilenwerkzeuge verwenden, wurden bisher benachteiligt. Die vorhandenen Visual Studio-Vorlagen waren außerhalb von VS nicht nutzbar — man musste die Projektstruktur manuell nachbilden und die Grundlagen selbst einrichten.

Diese Vorlagen sind Open Source (siehe [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), aus [Community-Feedback](https://github.com/microsoft/microsoft-ui-xaml/issues/10388) entwickelt und jetzt verfügbar. Die Visual Studio-Unterstützung befindet sich in Arbeit — diese Vorlagen werden irgendwann auch dort funktionieren.

Für Teams, die ihr WinUI-Projekt-Setup automatisieren, in CI integrieren oder einfach einen anderen Editor als Visual Studio verwenden möchten, ist das eine bedeutsame Verbesserung.

Original-Post: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
