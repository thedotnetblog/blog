---
title: "Agent Skills in Visual Studio: Lehre Copilot, Wie Dein Team Wirklich Arbeitet"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio unterstützt jetzt Agent Skills — wiederverwendbare Anweisungssets, die Copilot die spezifischen Workflows, Coding-Standards und Konventionen deines Teams beibringen. Einmal definieren, automatisch anwenden."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Eine der anhaltenden Frustrationen mit KI-Coding-Assistenten: Sie kennen allgemeine Programmierung gut, aber sie kennen nicht die spezifischen Konventionen *deines* Teams, deine internen APIs oder deine bevorzugten Muster. In jeder Sitzung erklärst du den Kontext erneut. Agent Skills in Visual Studio ist dafür konzipiert, dieses Problem zu lösen.

## Was Agent Skills Sind

Wiederverwendbare Anweisungssets — definiert in `SKILL.md`-Dateien — die Copilot-Agenten beibringen, wie spezifische Aufgaben zu behandeln sind. Definiere einen Skill für "wie wir unsere Build-Pipeline ausführen", "wie wir Boilerplate für unsere Service-Schicht generieren" oder "unsere Code-Review-Checkliste". Der Agent wendet den Skill automatisch an, wenn er relevant ist.

Dies ist kein neues Konzept (`.github/copilot-instructions.md` gibt es schon eine Weile), aber die Visual Studio-Integration macht sie zu Objekten erster Klasse mit einer Discovery-Benutzeroberfläche.

## Skills in Visual Studio Erstellen

Der integrierte UI-Flow: Klicke auf das Werkzeug-Symbol in Copilot Chat, öffne das Skills-Panel, klicke auf `+`. Du wählst globalen (persönlichen) oder lösungsweiten Geltungsbereich, wählst einen Namen und Visual Studio generiert eine Vorlage. Der Copilot-Agent-Modus kann dir dann helfen, die Vorlage auszufüllen — verwende den Agenten, um den Skill für den Agenten zu schreiben.

Derzeit im Insiders-Kanal, demnächst im Release-Kanal.

Du kannst Skills auch manuell erstellen:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Discovery-Speicherorte

Skills werden automatisch von Standardpfaden entdeckt:

**Lösungsebene (über Repo geteilt):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/persönlich (dein Benutzerprofil, überall verfügbar):** `~/.copilot/skills/`, `~/.agents/skills/`

Die Multi-Speicherort-Unterstützung bedeutet, dass dieselbe Konvention mit GitHub Copilot, Claude Code und anderen Agent-Frameworks funktioniert — definiere deine Skills einmal, verwende sie überall.

## Das Format

Skills folgen dem [agentskills.io/specification](https://agentskills.io/specification)-Format — eine Markdown-basierte Spezifikation, die sowohl für Menschen lesbar als auch maschinenanalysierbar ist. Du kannst Skripte, Vorlagen und Beispiele neben der `SKILL.md` einbeziehen.

## Praktischer Nutzen

Die wahre Stärke liegt nicht in den einzelnen Funktionen — sie liegt in der Kombination von team-geteilten Skills (über `.github/skills/`) und persönlichen Skills (über `~/.agents/skills/`). Team-Skills kodieren, wie deine Organisation Dinge erledigt. Persönliche Skills kodieren, wie du speziell arbeitest. Der Agent erhält automatisch beide Kontexte.

Für Organisationen, die Copilot bereits intensiv nutzen, ist dies ein bedeutender Schritt hin dazu, das Tool wirklich über die spezifischen Codebase-Konventionen bewusst zu machen, anstatt generische Ratschläge zu geben.

Originalbeitrag: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
