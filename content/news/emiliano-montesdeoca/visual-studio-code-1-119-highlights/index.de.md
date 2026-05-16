---
title: "VS Code 1.119: OpenTelemetry für Agent-Sitzungen, Browser-Integration und Sicherheit"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (Mai 2026) fügt OpenTelemetry-Tracing für Agent-Sitzungen, Browser-Tab-Freigabe für Agents, Verbesserungen bei Vertrauen und Sicherheit sowie einen 1.119.1-Sicherheits-Patch hinzu."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) wurde am 6. Mai 2026 veröffentlicht (mit einem 1.119.1-Sicherheits-Patch kurz danach). Das Release konzentriert sich auf Agent-Observability, Browser-Interaktion und die Reduzierung von Unterbrechungen.

## OpenTelemetry-Tracing für Agent-Sitzungen

Dies ist das herausragende Feature für alle, die Agents in der Produktion betreiben oder agentische Workflows debuggen. Aktivieren Sie es mit zwei Einstellungen:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Traces folgen den semantischen GenAI-Konventionen. Jede Agent-Anfrage erzeugt einen `invoke_agent`-Root-Span mit verschachtelten Child-Spans: `chat`, `execute_tool` und `execute_hook`. Token-Nutzung wird pro Anfrage gemeldet — einschließlich Cache-Lese- und Cache-Erstellungszählungen.

Funktioniert mit dem lokalen Agent, dem Copilot CLI Hintergrund-Agent und dem Claude-Agent. Jedes OTLP-kompatible Backend akzeptiert die Traces — das [Aspire Dashboard Standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) eignet sich gut für die lokale Entwicklung.

## Agents können jetzt auf Browser-Tabs zugreifen

Agents können den Zugriff auf Ihre integrierten Browser-Tabs anfordern — aber nicht automatisch. Sie müssen einen Tab explizit über den Kontext-Picker, Drag-and-Drop oder vorgeschlagenen Kontext freigeben. Im Browser gibt es eine Freigabe-Schaltfläche zum Widerrufen des Zugriffs. Wenn ein Agent versucht, einen neuen Tab auf derselben Domain wie ein bereits offener (nicht freigegebener) Tab zu öffnen, fordert VS Code Sie auf, den vorhandenen Tab wiederzuverwenden.

## Optimierte Token-Nutzung

Ein experimentelles leichtgewichtiges Modell übernimmt jetzt die Verwaltung von Agent-Aufgabenlisten und hält diese Verwaltungsarbeit vom teureren Primärmodell fern. Reduziert den Token-Verbrauch für Aufgaben, die keine volle Reasoning-Kapazität benötigen.

## Vertrauen und Sicherheit

Weniger Unterbrechungen: VS Code 1.119 reduziert Aufforderungen für Netzwerkzugriffsanfragen und Schreibvorgänge in temporäre Ordner durch Agents. Der 1.119.1-Patch behebt spezifische Sicherheitsprobleme — ein Update lohnt sich, falls noch nicht geschehen.

## Schneller Wechsel zur Markdown-Vorschau

Klein aber nützlich: Sie können jetzt schnell den aktuellen Editor zur Markdown-Vorschau wechseln, ohne zu navigieren.

## VS Code Agents (Insiders-Vorschau)

Die neu gestaltete Agent-Sitzungs-UI — neuer Repository-Picker (lokal/Repos/remote), Verbesserungen bei Unter-Sitzungen, Web- und Mobile-Polishing, Fortschrittsanimationen — ist in Insiders unter [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents) verfügbar.

Vollständiges Changelog: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
