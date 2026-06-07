---
title: "VS Code 1.121: Lieblingsmodelle Anheften, Terminal-Ausgabe-Komprimierung, Agent SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 fügt Modell-Favoriten hinzu, erweiterte Terminal-Ausgabe-Komprimierung für Test-Runner und Build-Tools, einen Leerlauf-Stille-Timer für Hintergrundterminals und interaktive SSH-Tastatur-Authentifizierung im Agent Host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 setzt die Copilot-Agent-Qualitätsverbesserungen aus 1.120 fort, mit Fokus auf Modellverwaltung und Terminal-Verhalten.

## Lieblingsmodelle Anheften

Der Modell-Picker unterstützt jetzt das Anheften. Wenn du immer dasselbe Modell oder zwei verwendest, hefte sie an die Spitze der Liste. Reduziert das Scrollen, wenn du Zugang zu vielen Modellen verschiedener Anbieter hast.

## Erweiterte Terminal-Ausgabe-Komprimierung

Das Agent-Terminal-Tool komprimierte bereits die Ausgabe für gängige Befehle. 1.121 erweitert dies auf Test-Runner und Build-Tools:

- **Test-Runner:** `pytest`, `jest`, `cargo test`
- **Build-Tools:** `tsc`, `cargo build`, `make`
- **Linter, Docker, Paketmanager**

Lange Build-Ausgaben und Test-Fehlerberichte werden in relevante Ausschnitte komprimiert, bevor sie an das Modell weitergegeben werden. Das hält die Kontextnutzung handhabbar, wenn der Agent Build-Zyklen oder Test-Suites ausführt, die Tausende von Ausgabezeilen produzieren können.

## Leerlauf-Stille-Timer für Hintergrundterminals

Ein neuer Leerlauf-Stille-Timer für das `run_in_terminal`-Tool: Wenn ein synchroner Befehl für einen konfigurierbaren Zeitraum keine Ausgabe produziert, wird er automatisch zur Hintergrundausführung hochgestuft. Das verhindert, dass lang laufende Befehle den Agenten blockieren, wenn sie still verarbeiten. Du erhältst eine Terminal-ID, die du später überprüfen kannst.

## VSCODE_AGENT Umgebungsvariable

Wenn Copilot Chat Befehle im Terminal ausführt, wird jetzt eine Umgebungsvariable `VSCODE_AGENT` gesetzt. Nützlich, wenn du Skripte oder Tools hast, die sich anders verhalten, wenn sie aus einer Agent-Sitzung im Vergleich zu interaktiv aufgerufen werden.

## Zum Chat aus dem Browser Hinzufügen

Ein Rechtsklick im integrierten Browser zeigt jetzt eine Option "Zum Chat hinzufügen". Wähle Inhalt von einer Webseite aus und füge ihn direkt zu deinem Copilot-Chat-Kontext hinzu, ohne Kopieren und Einfügen.

## Behoben: Mehrzeilige Shell-Befehle in Agent Host

Eine überfällige Fehlerkorrektur: Mehrzeilige Shell-Befehle im Terminal-Tool von Agent Host funktionieren jetzt korrekt. Zuvor konnten diese fehlschlagen oder falsches Verhalten erzeugen.

## Interaktive SSH-Tastatur-Authentifizierung

Agent Host SSH-Verbindungen unterstützen jetzt interaktive Tastatur-Authentifizierung — die Fallback-Authentifizierungsmethode, die von einigen SSH-Servern verwendet wird (einschließlich einiger älterer Unternehmenskonfigurationen). Agenten, die auf Remote-SSH-Hosts arbeiten, haben weniger Wahrscheinlichkeit, auf Authentifizierungsfehler zu stoßen.

Originalbeitrag: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
