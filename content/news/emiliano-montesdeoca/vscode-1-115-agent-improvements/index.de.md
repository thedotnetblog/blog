---
title: "VS Code 1.115 — Hintergrund-Terminal-Benachrichtigungen, SSH-Agent-Modus und Mehr"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 bringt Hintergrund-Terminal-Benachrichtigungen für Agenten, SSH-Remote-Agent-Hosting, Dateieinfügen in Terminals und sitzungsbewusstes Edit-Tracking. Das ist relevant für .NET-Entwickler."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "vscode-1-115-agent-improvements.md" >}}).*

VS Code 1.115 ist gerade [erschienen](https://code.visualstudio.com/updates/v1_115), und obwohl es ein leichteres Release in Bezug auf Hauptfeatures ist, sind die agentenbezogenen Verbesserungen wirklich nützlich, wenn man täglich mit KI-Coding-Assistenten arbeitet.

Lass mich hervorheben, was wirklich wissenswert ist.

## Hintergrund-Terminals kommunizieren mit Agenten

Das ist das herausragende Feature. Hintergrund-Terminals benachrichtigen Agenten jetzt automatisch, wenn Befehle abgeschlossen sind, einschließlich Exit-Code und Terminal-Ausgabe. Eingabeaufforderungen in Hintergrund-Terminals werden ebenfalls erkannt und dem Benutzer angezeigt.

Warum ist das wichtig? Wenn du Copilots Agent-Modus verwendet hast, um Build-Befehle oder Test-Suites im Hintergrund auszuführen, kennst du den Schmerz von "Ist das schon fertig?" — Hintergrund-Terminals waren im Wesentlichen Fire-and-Forget. Jetzt wird der Agent benachrichtigt, wenn dein `dotnet build` oder `dotnet test` abgeschlossen ist, sieht die Ausgabe und kann entsprechend reagieren. Es ist eine kleine Änderung, die agentengesteuerte Workflows deutlich zuverlässiger macht.

Es gibt auch ein neues `send_to_terminal`-Tool, das Agenten ermöglicht, Befehle mit Benutzerbestätigung an Hintergrund-Terminals zu senden. Das behebt das Problem, bei dem `run_in_terminal` mit einem Timeout Terminals in den Hintergrund verschob und sie schreibgeschützt machte.

## SSH-Remote-Agent-Hosting

VS Code unterstützt jetzt die Verbindung zu Remote-Maschinen über SSH, installiert automatisch die CLI und startet sie im Agent-Host-Modus. Das bedeutet, dass deine KI-Agent-Sitzungen direkt auf Remote-Umgebungen zielen können — nützlich für .NET-Entwickler, die auf Linux-Servern oder Cloud-VMs bauen und testen.

## Edit-Tracking in Agent-Sitzungen

Dateiänderungen während Agent-Sitzungen werden jetzt verfolgt und wiederhergestellt, mit Diffs, Undo/Redo und Zustandswiederherstellung. Wenn ein Agent Änderungen an deinem Code vornimmt und etwas schiefgeht, kannst du genau sehen, was sich geändert hat, und es zurückrollen. Beruhigend, wenn man Agenten seine Codebasis ändern lässt.

## Browser-Tab-Erkennung und weitere Verbesserungen

Ein paar weitere Quality-of-Life-Ergänzungen:

- **Browser-Tab-Tracking** — Chat kann jetzt Browser-Tabs verfolgen und verlinken, die während einer Sitzung geöffnet wurden, sodass Agenten auf Webseiten verweisen können, die du gerade anschaust
- **Dateieinfügen im Terminal** — füge Dateien (einschließlich Bilder) mit Strg+V, Drag-and-Drop oder Rechtsklick in das Terminal ein
- **Testabdeckung in der Minimap** — Testabdeckungsindikatoren werden jetzt in der Minimap für einen schnellen visuellen Überblick angezeigt
- **Pinch-to-Zoom auf Mac** — der integrierte Browser unterstützt Pinch-to-Zoom-Gesten
- **Copilot-Berechtigungen in Sitzungen** — die Statusleiste zeigt Nutzungsinformationen in der Sitzungsansicht
- **Favicon in Gehe zu Datei** — geöffnete Webseiten zeigen Favicons in der Schnellauswahlliste

## Fazit

VS Code 1.115 ist ein inkrementelles Release, aber die Agent-Verbesserungen — Hintergrund-Terminal-Benachrichtigungen, SSH-Agent-Hosting und Edit-Tracking — ergeben zusammen eine spürbar flüssigere Erfahrung für KI-unterstützte Entwicklung. Wenn du Copilots Agent-Modus für .NET-Projekte verwendest, sind das genau die Art von Quality-of-Life-Verbesserungen, die den täglichen Reibungsverlust reduzieren.

Schau dir die [vollständigen Release Notes](https://code.visualstudio.com/updates/v1_115) für alle Details an.
