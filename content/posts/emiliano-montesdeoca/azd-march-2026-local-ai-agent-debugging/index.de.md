---
title: "azd ermöglicht jetzt lokales Ausführen und Debuggen von KI-Agenten — Das hat sich im März 2026 geändert"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Das Azure Developer CLI hat im März 2026 sieben Releases veröffentlicht. Die Highlights: ein lokaler Run-and-Debug-Loop für KI-Agenten, GitHub Copilot-Integration beim Projekt-Setup und Container App Jobs-Unterstützung."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}}).*

Sieben Releases in einem Monat. Das hat das Azure Developer CLI (`azd`)-Team im März 2026 veröffentlicht, und das Hauptfeature ist genau das, worauf ich gewartet habe: **ein lokaler Run-and-Debug-Loop für KI-Agenten**.

PC Chan [hat die vollständige Zusammenfassung veröffentlicht](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), und obwohl es viel gibt, lass mich das auf das filtern, was für .NET-Entwickler, die KI-gestützte Apps bauen, wirklich wichtig ist.

## KI-Agenten ausführen und debuggen ohne Deployment

Das ist das große Ding. Die neue `azure.ai.agents`-Extension fügt Befehle hinzu, die dir eine ordentliche Inner-Loop-Erfahrung für KI-Agenten geben:

- `azd ai agent run` — startet deinen Agenten lokal
- `azd ai agent invoke` — sendet Nachrichten (lokal oder deployed)
- `azd ai agent show` — zeigt Container-Status und Health
- `azd ai agent monitor` — streamt Container-Logs in Echtzeit

Vorher bedeutete das Testen eines KI-Agenten jedes Mal ein Deployment zu Microsoft Foundry. Jetzt kannst du lokal iterieren, das Verhalten testen und erst deployen, wenn du bereit bist. Wenn du Agenten mit dem Microsoft Agent Framework oder Semantic Kernel baust, ändert das deinen täglichen Workflow.

Der invoke-Befehl funktioniert sowohl gegen lokale als auch deployed Agenten, was bedeutet, dass du den gleichen Test-Workflow verwenden kannst, egal wo der Agent läuft.

## GitHub Copilot richtet dein azd-Projekt ein

`azd init` bietet jetzt eine "Set up with GitHub Copilot (Preview)"-Option. Statt manuell Prompts über deine Projektstruktur zu beantworten, scaffoldet ein Copilot-Agent die Konfiguration für dich. Wenn ein Befehl fehlschlägt, bietet `azd` jetzt KI-gestützte Fehlerbehebung: Kategorie wählen, den Agenten einen Fix vorschlagen lassen und wiederholen — alles ohne das Terminal zu verlassen.

## Container App Jobs und Deployment-Verbesserungen

- **Container App Jobs**: `azd` deployed jetzt `Microsoft.App/jobs` über die bestehende `host: containerapp`-Konfiguration.
- **Konfigurierbare Deployment-Timeouts**: Neues `--timeout`-Flag und `deployTimeout`-Feld in `azure.yaml`.
- **Remote-Build-Fallback**: Bei fehlgeschlagenem ACR-Build fällt `azd` automatisch auf lokalen Docker/Podman-Build zurück.
- **Lokale Preflight-Validierung**: Bicep-Parameter werden lokal validiert, bevor deployed wird.

## DX-Verbesserungen

- **Automatische pnpm/yarn-Erkennung** für JS/TS-Projekte
- **pyproject.toml-Unterstützung** für Python
- **Lokale Template-Verzeichnisse** — `azd init --template` akzeptiert jetzt Dateisystem-Pfade
- **Bessere Fehlermeldungen** im `--no-prompt`-Modus
- **Build-Umgebungsvariablen** in alle Framework-Build-Subprozesse injiziert (.NET, Node.js, Java, Python)

## Zusammenfassung

Der lokale KI-Agenten-Debug-Loop ist der Star dieses Releases, aber die Gesamtheit an Deployment-Verbesserungen und DX-Polish macht `azd` reifer als je zuvor. Wenn du .NET-Apps auf Azure deployst — besonders KI-Agenten — lohnt sich dieses Update.

Schau dir die [vollständigen Release Notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) für alle Details an.
