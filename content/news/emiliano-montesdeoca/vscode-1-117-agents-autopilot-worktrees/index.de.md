---
title: "VS Code 1.117: Agents Bekommen Eigene Git-Branches und Ich Bin Voll Dabei"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 bringt Worktree-Isolation für Agent-Sessions, persistenten Autopilot-Modus und Subagent-Support. Der agentische Coding-Workflow wird jetzt richtig real."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

Die Grenze zwischen „KI-Assistent" und „KI-Teamkollege" wird immer dünner. VS Code 1.117 ist gerade erschienen und die [vollständigen Release Notes](https://code.visualstudio.com/updates/v1_117) sind vollgepackt, aber die Geschichte ist klar: Agents werden zu erstklassigen Bürgern in deinem Entwicklungs-Workflow.

Hier ist, was wirklich zählt.

## Autopilot-Modus merkt sich endlich deine Einstellung

Bisher musstest du Autopilot bei jeder neuen Session neu aktivieren. Nervig. Jetzt bleibt dein Berechtigungsmodus über Sessions hinweg bestehen, und du kannst den Standard konfigurieren.

Der Agent Host unterstützt drei Session-Konfigurationen:

- **Default** — Tools fragen vor der Ausführung nach Bestätigung
- **Bypass** — genehmigt alles automatisch
- **Autopilot** — vollständig autonom, beantwortet eigene Fragen und macht weiter

Wenn du ein neues .NET-Projekt mit Migrationen, Docker und CI aufbaust — stell es einmal auf Autopilot und vergiss es. Diese Einstellung bleibt.

## Worktree- und Git-Isolation für Agent-Sessions

Das ist der große Wurf. Agent-Sessions unterstützen jetzt volle Worktree- und Git-Isolation. Das bedeutet: Wenn ein Agent an einer Aufgabe arbeitet, bekommt er seinen eigenen Branch und sein eigenes Arbeitsverzeichnis. Dein Hauptbranch bleibt unangetastet.

Noch besser — Copilot CLI generiert aussagekräftige Branch-Namen für diese Worktree-Sessions. Kein `agent-session-abc123` mehr. Du bekommst etwas, das tatsächlich beschreibt, was der Agent tut.

Für .NET-Entwickler, die mehrere Feature-Branches verwalten oder Bugs fixen, während eine lange Scaffolding-Aufgabe läuft, ist das ein Game Changer. Du kannst einen Agent deine API-Controller in einem Worktree aufbauen lassen, während du ein Problem in der Service-Schicht in einem anderen debuggst. Keine Konflikte. Kein Stashing. Kein Chaos.

## Subagents und Agent-Teams

Das Agent Host Protocol unterstützt jetzt Subagents. Ein Agent kann andere Agents starten, um Teile einer Aufgabe zu übernehmen. Stell dir das als Delegieren vor — dein Haupt-Agent koordiniert, und spezialisierte Agents kümmern sich um die einzelnen Teile.

Das ist noch früh, aber das Potenzial für .NET-Workflows ist offensichtlich. Stell dir vor, ein Agent kümmert sich um deine EF Core-Migrationen, während ein anderer deine Integrationstests einrichtet. Wir sind noch nicht ganz da, aber dass der Protokoll-Support jetzt landet, bedeutet, dass die Tools schnell folgen werden.

## Terminal-Output wird automatisch mitgeliefert, wenn Agents Input senden

Klein aber bedeutsam. Wenn ein Agent Input an das Terminal sendet, wird der Terminal-Output jetzt automatisch in den Kontext einbezogen. Vorher musste der Agent eine extra Runde drehen, nur um zu lesen, was passiert ist.

Wenn du jemals einem Agent zugesehen hast, wie er `dotnet build` ausführt, scheitert und dann noch einen Roundtrip braucht, nur um den Fehler zu sehen — diese Reibung ist weg. Er sieht den Output sofort und reagiert.

## Die Agents-App auf macOS aktualisiert sich selbst

Die eigenständige Agents-App auf macOS aktualisiert sich jetzt selbst. Kein manuelles Herunterladen neuer Versionen mehr. Sie bleibt einfach aktuell.

## Die kleineren Dinge, die es wert sind zu wissen

- **package.json-Hovers** zeigen jetzt sowohl die installierte Version als auch die neueste verfügbare. Nützlich, wenn du npm-Tooling neben deinen .NET-Projekten verwaltest.
- **Bilder in JSDoc-Kommentaren** werden in Hovers und Completions korrekt gerendert.
- **Copilot CLI-Sessions** zeigen jetzt an, ob sie von VS Code oder extern erstellt wurden — praktisch, wenn du zwischen Terminals springst.
- **Copilot CLI, Claude Code und Gemini CLI** werden als Shell-Typen erkannt. Der Editor weiß, was du ausführst.

## Das Fazit

VS Code 1.117 ist kein auffälliger Feature-Dump. Es ist Infrastruktur. Worktree-Isolation, persistente Berechtigungen, Subagent-Protokolle — das sind die Bausteine für einen Workflow, in dem Agents echte, parallele Aufgaben erledigen, ohne deinen Code zu beeinträchtigen.

Wenn du mit .NET baust und dich noch nicht auf den agentischen Workflow eingelassen hast, ehrlich gesagt, jetzt ist der richtige Zeitpunkt.
