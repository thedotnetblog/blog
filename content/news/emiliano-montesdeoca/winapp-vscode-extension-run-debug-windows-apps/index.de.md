---
title: "WinApp VS Code Extension: Windows-Apps Ausführen, Debuggen und Verpacken Ohne den Editor Zu Verlassen"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Die WinApp VS Code Extension bringt die vollständige Windows App Development CLI direkt in VS Code — Windows-Apps (WPF, WinUI, .NET, C++) ausführen, mit Paketidentität debuggen, verpacken und signieren ohne Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Wer jemals versucht hat, eine Windows-App in VS Code zu entwickeln, kennt diesen Moment. Man arbeitet konzentriert, bearbeitet Code im bevorzugten Editor — und dann braucht man Paketidentität für eine Windows-API. Oder ein MSIX. Oder man muss ein Paket signieren. Und plötzlich greift man zu Visual Studio oder sucht um 23 Uhr nach "msix packaging without visual studio".

Diese Reibung gehört der Vergangenheit an. Die [WinApp VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) ist in der öffentlichen Preview — und sie bringt die vollständige [Windows App Development CLI](https://github.com/microsoft/WinAppCli) direkt in VS Code. Keine separate Installation, kein Visual Studio erforderlich.

## Paketidentität Per F5

Das Problem mit Windows-APIs — Benachrichtigungen, Hintergrundaufgaben, On-Device-KI-Features, Share Targets — viele davon erfordern, dass die App **Paketidentität** besitzt. Ohne sie funktionieren diese APIs schlicht nicht.

Paketidentität zu bekommen bedeutete traditionell, ein vollständiges MSIX-Installationspaket zu erstellen oder aus Visual Studio heraus zu starten. Die WinApp Extension ändert das vollständig mit einem benutzerdefinierten `winapp`-Debug-Typ.

Das in die `launch.json` einfügen:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

F5 drücken. Die Extension findet den Build-Output und das Manifest, gibt der App über `winapp run` Paketidentität und hängt den Debugger an. Für .NET-Apps ist das `coreclr` (erfordert das C# Dev Kit). C/C++ nutzt `cppvsdbg`. Node/Electron nutzt den eingebauten Debugger.

Ein `preLaunchTask` lässt sich einrichten, damit das Projekt vor jedem F5-Druck automatisch gebaut wird — derselbe Build-and-Launch-Ablauf wie in Visual Studio, nur in VS Code.

## Alles in der Befehlspalette

`Ctrl+Shift+P` öffnen, `WinApp` eingeben — und das vollständige Toolkit steht bereit:

- **Initialize Project** — Projekt mit Windows SDK und/oder Windows App SDK konfigurieren
- **Run Application** — als Loose-Layout-Paket-App mit Paketidentität starten
- **Create MSIX Package** — App mit Zertifikat- und Runtime-Optionen verpacken
- **Update Manifest Assets** — alle erforderlichen App-Icons aus einem einzigen Quellbild generieren
- **Generate / Install Certificate** — Entwicklungszertifikat-Verwaltung
- **Sign Package** — MSIX oder ausführbare Datei signieren
- **Run SDK Tool** — `makeappx`, `signtool`, `mt` oder `makepri` direkt ausführen

Die WinApp CLI muss auch nicht separat installiert werden. Sie ist in der Extension gebündelt.

## Funktioniert Über Viele Frameworks

Das ist nicht nur ein .NET WPF/WinUI-Werkzeug. Die Extension funktioniert mit:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Diese Breite ist beabsichtigt. VS Code ist der Heimathafen von Web- und Cross-Platform-Entwicklern. Wer eine Tauri- oder Electron-App baut, die Windows-Paketierung braucht, wird von dieser Extension abgedeckt — ohne Visual Studio zu übernehmen.

## Warum Das Für .NET-Entwickler Wichtig Ist

Ich arbeite viel in VS Code — dort schreibe ich Markdown, verwalte Konfigurationen, bearbeite kleinere Projekte und führe Terminals aus. Aber für .NET Windows Desktop-Entwicklung war Visual Studio die einzige echte Option, sobald irgendetwas mit Paketierung zu tun hatte.

Diese Extension schließt diese Lücke. Nun ist ein vollständiger Windows .NET Desktop-Entwicklungszyklus in VS Code möglich — bearbeiten, bauen, mit Paketidentität ausführen, debuggen, verpacken, signieren — ohne den Editor zu verlassen. Das ist eine echte Verbesserung der Lebensqualität.

## Erste Schritte

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Oder **WinApp** in der Extensions-Ansicht suchen (`Ctrl+Shift+X`).

Voraussetzungen:
- Windows 10 oder neuer
- VS Code 1.109.0 oder neuer
- Die Debugger-Extension für die App-Sprache

Die vollständige Ankündigung von Chiara Mooney findet sich [hier](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/).

## Fazit

Die WinApp VS Code Extension ist eine willkommene Ergänzung für .NET Windows Desktop-Entwickler, die in VS Code zuhause sind, aber bisher für Paketierungsaufgaben zu Visual Studio wechseln mussten. Paketidentität per F5, MSIX-Paketierung aus der Befehlspalette, integrierte Zertifikatsverwaltung — das ist die richtige Kombination.

Beim nächsten WPF- oder WinUI-Projekt einfach ausprobieren. Die Reibung, die man bisher umgehen musste, ist jetzt deutlich geringer.
