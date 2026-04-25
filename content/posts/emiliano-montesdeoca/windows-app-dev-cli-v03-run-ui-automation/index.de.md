---
title: "Windows App Dev CLI v0.3: F5 aus dem Terminal und UI-Automatisierung für Agenten"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 bringt winapp run für Terminal-basierte Debug-Starts, winapp ui für UI-Automatisierung und ein neues NuGet-Paket, das dotnet run mit gepackten Apps funktioniert."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [hier klicken]({{< ref "index.md" >}}).*

Die F5-Erfahrung von Visual Studio ist großartig. Aber VS nur zum Starten und Debuggen einer gepackten Windows-App öffnen zu müssen, ist zu viel — egal ob man in einer CI-Pipeline ist, einen automatisierten Workflow ausführt oder ein KI-Agent die Tests durchführt.

Windows App Development CLI v0.3 wurde [veröffentlicht](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) und adressiert das direkt mit zwei Hauptfunktionen: `winapp run` und `winapp ui`.

## winapp run: F5 von überall

`winapp run` nimmt einen ungepackten App-Ordner und ein Manifest und erledigt alles, was VS beim Debug-Start tut: registriert ein Loose-Paket, startet die App und bewahrt den `LocalState` zwischen Re-Deploys.

```bash
# App bauen, dann als gepackte App starten
winapp run ./bin/Debug
```

Funktioniert für WinUI, WPF, WinForms, Console, Avalonia und mehr. Die Modi sind für Entwickler und automatisierte Workflows ausgelegt:

- **`--detach`**: Startet und gibt die Kontrolle sofort an das Terminal zurück. Ideal für CI.
- **`--unregister-on-exit`**: Räumt das registrierte Paket beim App-Schließen auf.
- **`--debug-output`**: Erfasst `OutputDebugString`-Meldungen und Ausnahmen in Echtzeit. Mit `--symbols` werden PDBs vom Microsoft Symbol Server geladen.

## Neues NuGet-Paket: dotnet run für gepackte Apps

Für .NET-Entwickler gibt es ein neues NuGet-Paket: `Microsoft.Windows.SDK.BuildTools.WinApp`. Nach der Installation handhabt `dotnet run` den gesamten Inner Loop: Build, Loose-Layout-Paket vorbereiten, bei Windows registrieren und starten — alles in einem Schritt.

```bash
# winapp init erledigt die Einrichtung
winapp init
# Oder direkt installieren
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

Funktioniert mit WinUI, WPF, WinForms, Console, Avalonia. Keine manuellen Schritte, nur `dotnet run`.

## winapp ui: UI-Automatisierung aus der Kommandozeile

Das ist der Feature, der agentische Szenarien ermöglicht. `winapp ui` bietet vollständigen UI-Automatisierungszugriff auf jede laufende Windows-App — WPF, WinForms, Win32, Electron, WinUI3 — direkt aus dem Terminal.

Was möglich ist:

- Alle Fenster der obersten Ebene auflisten
- Den vollständigen UI-Automatisierungsbaum eines Fensters traversieren
- Elemente nach Name, Typ oder Automatisierungs-ID suchen
- Klicken, aufrufen und Werte setzen
- Screenshots aufnehmen
- Auf das Erscheinen von Elementen warten — ideal für Testsynchronisierung

`winapp ui` und `winapp run` kombiniert ergeben einen vollständigen Build → Start → Verifikation-Workflow aus dem Terminal. Ein Agent kann die App ausführen, den UI-Zustand prüfen, programmatisch interagieren und das Ergebnis validieren.

## Weitere Neuerungen

- **`winapp unregister`**: Entfernt ein sidegeladenes Dev-Paket nach dem Test.
- **`winapp manifest add-alias`**: Fügt einen `uap5:AppExecutionAlias` hinzu, damit die App per Name aus dem Terminal gestartet werden kann.
- **Tab-Vervollständigung**: Ein Befehl für die vollständige PowerShell-Vervollständigung.
- **`Package.appxmanifest` als Standard**: `winapp init` erzeugt jetzt `Package.appxmanifest` (VS-Konvention) statt `appxmanifest.xml`.

## Installation

```bash
winget install Microsoft.WinAppCli
# oder
npm install -g @microsoft/winappcli
```

Die CLI ist in Public Preview. Das [GitHub-Repository](https://github.com/microsoft/WinAppCli) enthält vollständige Dokumentation, und die [ursprüngliche Ankündigung](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) hat alle Details.
