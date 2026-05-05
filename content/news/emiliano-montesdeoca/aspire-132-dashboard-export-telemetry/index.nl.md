---
title: "Het Dashboard van Aspire 13.2 Heeft Nu een Telemetry API — en Dat Verandert Alles"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 brengt slimmere telemetrie-export, een programmeerbare API voor traces en logs, en GenAI-visualisatieverbeteringen. Dit is waarom het uitmaakt voor je debugging-workflow."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

Als je gedistribueerde apps bouwt met .NET Aspire, weet je al dat het dashboard het beste deel van de hele ervaring is. Aspire 13.2 heeft het aanzienlijk verbeterd.

## Telemetrie exporteren zoals een normaal persoon

Aspire 13.2 voegt een proper **Beheer logs en telemetrie**-dialoogvenster toe waar je kunt:
- Alle telemetrie wissen
- Geselecteerde telemetrie exporteren naar een ZIP-bestand in standaard OTLP/JSON-indeling
- Die ZIP later importeren in een willekeurig Aspire-dashboard

Dat laatste deel is de killer-feature. Reproduceer een bug, exporteer de telemetrie, voeg het toe aan je werkitem, en je teamgenoot kan het importeren in hun eigen dashboard.

## De telemetrie-API is de echte game changer

Het dashboard stelt nu een HTTP API bloot onder `/api/telemetry`:
- `GET /api/telemetry/resources` — lijst van resources met telemetrie
- `GET /api/telemetry/spans` — spans opvragen met filters
- `GET /api/telemetry/logs` — logs opvragen met filters
- `GET /api/telemetry/traces` — traces weergeven

Dit ondersteunt de nieuwe CLI-opdrachten `aspire agent mcp` en `aspire otel`.

## GenAI-telemetrie wordt praktisch

VS Code Copilot chat en Copilot CLI ondersteunen het configureren van een `OTEL_EXPORTER_OTLP_ENDPOINT` — wijs ze naar het Aspire-dashboard en je kunt je AI-agents in real-time zien denken via telemetrie.

## Samenvatting

Aspire 13.2 transformeert het dashboard van "prettige debugging-UI" naar "programmeerbaar observabiliteitsplatform". Ga naar [aspire.dev](https://aspire.dev).
