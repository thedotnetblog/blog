---
title: "VS Code 1.119: OpenTelemetry voor agentsessies, browserintegratie en beveiliging"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (mei 2026) voegt OpenTelemetry-tracering voor agentsessies toe, browsertab-deling voor agenten, verbeteringen in vertrouwen en beveiliging, en een beveiligingspatch 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) verscheen op 6 mei 2026 (met een beveiligingspatch 1.119.1 kort daarna). De release richt zich op agentobserveerbaarheid, browserinteractie en minder onderbrekingen.

## OpenTelemetry-tracering voor agentsessies

Dit is de uitgelichte functie voor iedereen die agenten in productie draait of agentische workflows debugt. Activeer het met twee instellingen:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Traces volgen de semantische GenAI-conventies. Elk agentverzoek genereert een `invoke_agent` root span met geneste child spans: `chat`, `execute_tool` en `execute_hook`. Tokengebruik wordt per verzoek gerapporteerd — inclusief cache-lees- en aanmaakaantallen.

Werkt met de lokale agent, de Copilot CLI-achtergrondagent en de Claude-agent. Elk OTLP-compatibel backend accepteert de traces — het [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) werkt goed voor lokale ontwikkeling.

## Agenten hebben nu toegang tot browsertabbladen

Agenten kunnen toegang vragen tot uw geïntegreerde browsertabbladen — maar niet automatisch. U moet een tabblad expliciet delen via de contextselection, slepen en neerzetten of voorgestelde context. Er is een deelknop in de browser om toegang in te trekken. Wanneer een agent een nieuw tabblad probeert te openen op hetzelfde domein als een al openstaand (niet-gedeeld) tabblad, vraagt VS Code u het bestaande tabblad te hergebruiken.

## Geoptimaliseerd tokengebruik

Een experimenteel lichtgewicht model beheert nu takenlijsten van agenten, waardoor dit beheerswerk van het duurdere primaire model wordt gescheiden. Vermindert tokenverbruik voor taken die geen volledige redenercapaciteit vereisen.

## Vertrouwen en beveiliging

Minder onderbrekingen: VS Code 1.119 vermindert prompts voor netwerktoegangsverzoeken en schrijfacties naar tijdelijke mappen door agenten. De 1.119.1-patch pakt specifieke beveiligingsproblemen aan — de moeite waard om bij te werken als u dat nog niet heeft gedaan.

## Snel wisselen naar Markdown-voorbeeld

Klein maar handig: u kunt nu snel de huidige editor wisselen naar het Markdown-voorbeeld zonder te navigeren.

## VS Code Agents (Insiders-voorbeeld)

De opnieuw ontworpen agentsessie-UI — nieuwe repositoryselectie (lokaal/repos/remote), verbeteringen aan subsessies, web- en mobiele verfijning, voortgangsanimaties — is beschikbaar in Insiders op [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Volledig changelog: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
