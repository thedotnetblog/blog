---
title: "VS Code 1.112: Was .NET-Entwickler wirklich interessieren sollte"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 ist da und vollgepackt mit Agent-Upgrades, einem integrierten Browser-Debugger, MCP-Sandboxing und Monorepo-Support. Hier ist, was wirklich zählt, wenn du mit .NET entwickelst."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 ist gelandet, und ehrlich? Dieses Release fühlt sich anders an, wenn du deine Tage in der .NET-Welt verbringst. Es gibt viel in den [offiziellen Release Notes](https://code.visualstudio.com/updates/v1_112), aber lass mich dir etwas Scrollen ersparen und mich auf das konzentrieren, was für uns wirklich zählt.

## Copilot CLI ist gerade viel nützlicher geworden

Das große Thema dieses Releases ist **Agent-Autonomie** — Copilot mehr Raum geben, sein Ding zu machen, ohne dass du jeden Schritt überwachst.

### Nachrichtensteuerung und Warteschlange

Kennst du den Moment, wenn Copilot CLI mitten in einer Aufgabe ist und dir auffällt, dass du etwas vergessen hast zu erwähnen? Vorher musstest du warten. Jetzt kannst du Nachrichten senden, während eine Anfrage noch läuft — entweder um die aktuelle Antwort zu steuern oder Folgeanweisungen in die Warteschlange zu stellen.

Das ist riesig für die längeren `dotnet`-Scaffolding-Aufgaben, wo du Copilot beim Projekt-Setup zuschaust und denkst "oh warte, ich brauche auch MassTransit da drin."

### Berechtigungsstufen

Das ist die Funktion, die mich am meisten begeistert. Copilot CLI-Sitzungen unterstützen jetzt drei Berechtigungsstufen:

- **Standard-Berechtigungen** — der übliche Flow, bei dem Tools vor dem Ausführen um Bestätigung bitten
- **Genehmigungen umgehen** — genehmigt alles automatisch und wiederholt bei Fehlern
- **Autopilot** — wird voll autonom: genehmigt Tools, beantwortet eigene Fragen und macht weiter, bis die Aufgabe erledigt ist

Wenn du etwas wie das Scaffolding einer neuen ASP.NET Core API mit Entity Framework, Migrationen und Docker-Setup machst — Autopilot-Modus bedeutet, du beschreibst was du willst und holst dir einen Kaffee. Er wird es herausfinden.

Du kannst Autopilot mit der Einstellung `chat.autopilot.enabled` aktivieren.

### Änderungen vor der Delegation vorschauen

Wenn du eine Aufgabe an Copilot CLI delegierst, erstellt er einen Worktree. Vorher, wenn du nicht committete Änderungen hattest, musstest du die Quellcodeverwaltung prüfen, um zu sehen, was betroffen wäre. Jetzt zeigt die Chat-Ansicht ausstehende Änderungen direkt dort an, bevor du entscheidest, ob du sie kopieren, verschieben oder ignorieren willst.

Kleine Sache, aber es erspart dir den "warte, was hatte ich gestaged?"-Moment.

## Web-Apps debuggen ohne VS Code zu verlassen

Der integrierte Browser unterstützt jetzt **vollständiges Debugging**. Du kannst Breakpoints setzen, durch Code steppen und Variablen inspizieren — alles in VS Code. Kein Wechsel mehr zu Edge DevTools.

Es gibt einen neuen `editor-browser` Debug-Typ, und wenn du bereits vorhandene `msedge`- oder `chrome`-Launch-Konfigurationen hast, ist die Migration so einfach wie das Ändern des `type`-Felds in deiner `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Für Blazor-Entwickler ist das ein Game Changer. Du führst bereits `dotnet watch` im Terminal aus — jetzt bleibt dein Debugging auch im selben Fenster.

Der Browser hat auch unabhängige Zoom-Stufen bekommen (endlich), richtige Rechtsklick-Kontextmenüs, und der Zoom wird pro Website gespeichert.

## MCP-Server-Sandboxing

Das ist wichtiger als du vielleicht denkst. Wenn du MCP-Server verwendest — vielleicht hast du einen für deine Azure-Ressourcen oder Datenbankabfragen eingerichtet — liefen sie bisher mit denselben Berechtigungen wie dein VS Code-Prozess. Das bedeutet voller Zugriff auf dein Dateisystem, Netzwerk, alles.

Jetzt kannst du sie sandboxen. In deiner `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Wenn ein gesandboxter Server Zugriff auf etwas braucht, das er nicht hat, fordert VS Code dich auf, die Berechtigung zu erteilen. Viel besser als der "hoffen wir, dass niemand etwas Merkwürdiges macht"-Ansatz.

> **Hinweis:** Sandboxing ist derzeit auf macOS und Linux verfügbar. Windows-Support kommt — Remote-Szenarien wie WSL funktionieren aber bereits.

## Monorepo-Customization-Discovery

Wenn du in einem Monorepo arbeitest (und seien wir ehrlich, viele Enterprise-.NET-Lösungen enden als eines), löst das einen echten Schmerzpunkt.

Zuvor, wenn du einen Unterordner deines Repos geöffnet hast, fand VS Code deine `copilot-instructions.md`, `AGENTS.md` oder benutzerdefinierten Skills nicht, die im Repository-Root lagen. Jetzt mit der Einstellung `chat.useCustomizationsInParentRepositories` geht es bis zum `.git`-Root hoch und entdeckt alles.

Das bedeutet, dein Team kann Agent-Anweisungen, Prompt-Dateien und benutzerdefinierte Tools über alle Projekte in einem Monorepo teilen, ohne dass jeder den Root-Ordner öffnen muss.

## /troubleshoot für Agent-Debugging

Hast du jemals benutzerdefinierte Anweisungen oder Skills eingerichtet und dich gefragt, warum sie nicht erkannt werden? Der neue `/troubleshoot`-Skill liest Agent-Debug-Logs und sagt dir, was passiert ist — welche Tools verwendet oder übersprungen wurden, warum Anweisungen nicht geladen wurden und was langsame Antworten verursacht.

Aktiviere es mit:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Dann tippe einfach `/troubleshoot why is my custom skill not loading?` im Chat.

Du kannst diese Debug-Logs jetzt auch exportieren und importieren, was großartig ist, um sie mit deinem Team zu teilen, wenn etwas nicht wie erwartet funktioniert.

## Bild- und Binärdatei-Unterstützung

Agenten können jetzt Bilddateien von der Festplatte und Binärdateien nativ lesen. Binärdateien werden im Hexdump-Format präsentiert, und Bildausgaben (wie Screenshots vom integrierten Browser) erscheinen in einer Karussell-Ansicht.

Für .NET-Entwickler denke: füge einen Screenshot eines UI-Bugs in den Chat ein und lass den Agenten verstehen, was falsch ist, oder lass ihn die Ausgabe eines Blazor-Komponenten-Renderings analysieren.

## Automatische Symbol-Referenzen

Kleine Qualitäts-Verbesserung: wenn du einen Symbolnamen (eine Klasse, Methode, etc.) kopierst und in den Chat einfügst, konvertiert VS Code ihn jetzt automatisch in eine `#sym:Name`-Referenz. Das gibt dem Agenten vollen Kontext über das Symbol, ohne dass du es manuell hinzufügen musst.

Wenn du stattdessen reinen Text möchtest, verwende `Ctrl+Shift+V`.

## Plugins können jetzt aktiviert/deaktiviert werden

Zuvor bedeutete das Deaktivieren eines MCP-Servers oder Plugins, ihn zu deinstallieren. Jetzt kannst du sie an- und ausschalten — sowohl global als auch pro Workspace. Rechtsklick in der Erweiterungsansicht oder der Customization-Ansicht und fertig.

Plugins von npm und pypi können sich jetzt auch automatisch aktualisieren, obwohl sie zuerst um Genehmigung bitten, da Updates bedeuten, dass neuer Code auf deinem Rechner ausgeführt wird.

## Zusammenfassung

VS Code 1.112 pusht eindeutig hart auf die Agent-Experience — mehr Autonomie, besseres Debugging, engere Sicherheit. Für .NET-Entwickler sind das integrierte Browser-Debugging und die Copilot CLI-Verbesserungen die herausragenden Features.

Wenn du noch keine vollständige Copilot CLI-Sitzung im Autopilot-Modus für ein .NET-Projekt ausprobiert hast, ist dieses Release ein guter Zeitpunkt zum Starten. Denk nur daran, deine Berechtigungen einzustellen und es machen zu lassen.

[VS Code 1.112 herunterladen](https://code.visualstudio.com/updates/v1_112) oder innerhalb von VS Code aktualisieren über **Hilfe > Nach Updates suchen**.
