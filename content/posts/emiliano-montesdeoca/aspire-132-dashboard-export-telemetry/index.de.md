---
title: "Das Aspire 13.2 Dashboard hat jetzt eine Telemetrie-API — und das ändert alles"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 bringt smarteren Telemetrie-Export, eine programmierbare API für Traces und Logs sowie Verbesserungen der GenAI-Visualisierung. Hier erfährst du, warum das für deinen Debugging-Workflow wichtig ist."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "aspire-132-dashboard-export-telemetry.md" >}}).*

Wenn du verteilte Apps mit .NET Aspire baust, weißt du bereits, dass das Dashboard das Beste an der ganzen Erfahrung ist. Alle Traces, Logs und Metriken an einem Ort — kein externes Jaeger, kein Seq-Setup, keine „lass mich mal im anderen Terminal schauen"-Momente.

Aspire 13.2 hat es deutlich besser gemacht. James Newton-King [hat das Update angekündigt](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), und ehrlich gesagt? Die Telemetrie-Export- und API-Features allein rechtfertigen das Upgrade.

## Telemetrie exportieren wie ein normaler Mensch

Hier ist das Szenario, das wir alle kennen: Du debuggst ein verteiltes Problem, reproduzierst es endlich nach zwanzig Minuten Setup, und jetzt musst du dem Team zeigen, was passiert ist. Vorher? Screenshots. Trace-IDs kopieren und einfügen. Das übliche Chaos.

Aspire 13.2 fügt einen ordentlichen **Logs und Telemetrie verwalten**-Dialog hinzu, in dem du:

- Alle Telemetrie löschen kannst (nützlich vor einem Reproduktionsversuch)
- Ausgewählte Telemetrie als ZIP-Datei im Standard-OTLP/JSON-Format exportieren kannst
- Diese ZIP-Datei später in jedes Aspire-Dashboard reimportieren kannst

Der letzte Punkt ist das Killer-Feature. Du reproduzierst einen Bug, exportierst die Telemetrie, hängst sie an dein Work Item, und dein Kollege kann sie in sein eigenes Dashboard importieren, um genau das zu sehen, was du gesehen hast. Kein „kannst du das auf deinem Rechner reproduzieren?" mehr.

Einzelne Traces, Spans und Logs haben auch eine „Export JSON"-Option im Kontextmenü. Musst du einen bestimmten Trace teilen? Rechtsklick, JSON kopieren, in die PR-Beschreibung einfügen. Fertig.

## Die Telemetrie-API ist der echte Game Changer

Das begeistert mich am meisten. Das Dashboard bietet jetzt eine HTTP-API unter `/api/telemetry` zum programmatischen Abfragen von Telemetriedaten. Verfügbare Endpunkte:

- `GET /api/telemetry/resources` — Ressourcen mit Telemetrie auflisten
- `GET /api/telemetry/spans` — Spans mit Filtern abfragen
- `GET /api/telemetry/logs` — Logs mit Filtern abfragen
- `GET /api/telemetry/traces` — Traces auflisten
- `GET /api/telemetry/traces/{traceId}` — alle Spans für einen bestimmten Trace abrufen

Alles kommt im OTLP-JSON-Format zurück. Das treibt die neuen CLI-Befehle `aspire agent mcp` und `aspire otel` an, aber die wirkliche Bedeutung ist größer: Du kannst jetzt Tooling, Skripte und KI-Agent-Integrationen bauen, die die Telemetrie deiner App direkt abfragen.

Stell dir einen KI-Coding-Agent vor, der deine tatsächlichen verteilten Traces beim Debuggen sehen kann. Das ist nicht mehr hypothetisch — genau das ermöglicht diese API.

## GenAI-Telemetrie wird praktisch

Wenn du KI-gestützte Apps mit Semantic Kernel oder Microsoft.Extensions.AI baust, wirst du den verbesserten GenAI-Telemetrie-Visualizer zu schätzen wissen. Aspire 13.2 fügt hinzu:

- KI-Toolbeschreibungen als Markdown gerendert
- Einen dedizierten GenAI-Button auf der Traces-Seite für schnellen Zugriff
- Bessere Fehlerbehandlung für abgeschnittenes oder nicht-standardmäßiges GenAI-JSON
- Click-to-Highlight-Navigation zwischen Tool-Definitionen

Der Blogpost erwähnt, dass VS Code Copilot Chat, Copilot CLI und OpenCode alle das Konfigurieren eines `OTEL_EXPORTER_OTLP_ENDPOINT` unterstützen. Richte sie auf das Aspire-Dashboard und du kannst buchstäblich deinen KI-Agents beim Denken in Echtzeit über Telemetrie zusehen. Das ist ein Debugging-Erlebnis, das du nirgendwo anders findest.

## Zusammenfassung

Aspire 13.2 verwandelt das Dashboard von „netter Debugging-UI" zu „programmierbarer Observability-Plattform". Der Export/Import-Workflow allein spart echte Zeit beim verteilten Debugging, und die Telemetrie-API öffnet die Tür zu KI-gestützter Diagnostik.

Wenn du bereits Aspire nutzt, aktualisiere. Wenn nicht — das ist ein guter Grund, [aspire.dev](https://aspire.dev) auszuprobieren.
