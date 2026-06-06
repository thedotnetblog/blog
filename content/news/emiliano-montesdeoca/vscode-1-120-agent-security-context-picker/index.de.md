---
title: "VS Code 1.120: Passwort-Prompts, Kontextgrößen-Auswahl, GitHub-Metadaten im Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 ist ein fokussiertes Release für Copilot-Nutzer: sichere Passwort-Prompt-Behandlung, Modell-Kontextgrößen-Auswahl, GitHub-PR-Metadaten in Agent-Sitzungen und Sitzungsarchiv-Verwaltung."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 wurde mit einer Reihe von Copilot-Agent-Verbesserungen geliefert, die einzeln klein, aber im täglichen Gebrauch spürbar besser sind.

## Sichere Passwort-Prompt-Erkennung in Agent-Terminals

Wenn ein Copilot-Agent einen Terminal-Befehl ausführt, der einen Passwort- oder Passphrase-Prompt auslöst, erkennt VS Code dies jetzt und zeigt einen Bestätigungsdialog an. Der Dialog fokussiert das Terminal, damit du das Geheimnis direkt eingeben kannst — und entscheidend: Geheimnisse werden niemals durch das Modell geleitet.

Dies ist eine bedeutende Sicherheitsverbesserung. Zuvor konnten Agenten, die Befehle ausführten, die Authentifizierungs-Prompts auslösten, Situationen schaffen, in denen Benutzer versehentlich Anmeldedaten preisgeben könnten. Die Ankündigung durch den Bildschirmleser bedeutet, dass auch Barrierefreiheits-Nutzer die Benachrichtigung erhalten.

## Kontextgrößen-Auswahl im Modell-Picker

Eine neue Kontextgrößen-Auswahl ermöglicht es dir, wie viel Kontext das Modell für eine Sitzung verwendet. Verschiedene Modelle haben unterschiedliche Kontextfenstergrößen, und einige Workflows profitieren davon, ihn einzuschränken (geringere Latenz, geringere Kosten) oder zu maximieren (komplexe Codebasen, lang laufende Sitzungen).

## GitHub-PR-Metadaten in Agent Host-Sitzungen

Für Sitzungen, die durch ein GitHub-Repository unterstützt werden, zeigt VS Code jetzt GitHub-Metadaten — einschließlich eines Pull-Request-Buttons — in der Agent-Host-Benutzeroberfläche an. Weniger Kontextwechsel zum Browser oder der GitHub-Erweiterung, wenn du an einem PR arbeitest.

## Chat-Sitzungsarchiv-Verwaltung

Zwei Verbesserungen für den Sitzungs-Quick Pick:
- Archivierte Sitzungen sind standardmäßig ausgeblendet (weniger visuelle Unordnung)
- Die Suche trifft immer noch auf archivierte Sitzungen zu, sodass du eine nach Titel wiederbeleben kannst

Sitzungen werden auch standardmäßig nach Aktualität gruppiert, wodurch aktuelle Arbeit leichter zu finden ist.

## Copilot CLI Plugin-Erkennung

VS Code erkennt jetzt automatisch Copilot CLI-Benutzer-installierte Plugins aus `~/.copilot/installed-plugins/`. Wenn du WinUI oder andere domänenspezifische Agent-Skills eingerichtet hast, werden sie ohne manuelle Konfiguration erkannt.

## Benutzerdefinierte Diff-Editor-API (Vorschau)

Für Erweiterungsautoren: eine neue vorgeschlagene API `customDiffEditorProvider` ermöglicht es Erweiterungen, ein einheitliches Diff in einer einzelnen Webview mit Zugriff auf beide Originale und modifizierte Dokumente zu rendern, anstatt zwei nebeneinander liegender benutzerdefinierter Editor-Ansichten.

Originalbeitrag: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
