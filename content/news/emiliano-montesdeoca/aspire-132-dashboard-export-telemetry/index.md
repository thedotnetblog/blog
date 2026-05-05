---
title: "Aspire 13.2's Dashboard Just Got a Telemetry API — and It Changes Everything"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 ships smarter telemetry export, a programmable API for traces and logs, and GenAI visualization improvements. Here's why this matters for your debugging workflow."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

If you've been building distributed apps with .NET Aspire, you already know the dashboard is the single best thing about the whole experience. All your traces, logs, and metrics in one place — no external Jaeger, no Seq setup, no "let me check the other terminal" moments.

Aspire 13.2 just made it significantly better. James Newton-King [announced the update](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), and honestly? The telemetry export and API features alone are worth the upgrade.

## Export telemetry like a sane person

Here's the scenario we've all lived through: you're debugging a distributed issue, you finally reproduce it after twenty minutes of setup, and now you need to share what happened with your team. Before? Screenshots. Copy-pasting trace IDs. The usual mess.

Aspire 13.2 adds a proper **Manage logs and telemetry** dialog where you can:

- Clear all telemetry (useful before a repro attempt)
- Export selected telemetry to a ZIP file in standard OTLP/JSON format
- Re-import that ZIP into any Aspire dashboard later

That last part is the killer feature. You reproduce a bug, export the telemetry, attach it to your work item, and your teammate can import it into their own dashboard to see exactly what you saw. No more "can you reproduce it on your machine?"

Individual traces, spans, and logs also get an "Export JSON" option in their context menus. Need to share one specific trace? Right-click, copy JSON, paste into your PR description. Done.

## The telemetry API is the real game changer

This is what I'm most excited about. The dashboard now exposes an HTTP API under `/api/telemetry` for querying telemetry data programmatically. Available endpoints:

- `GET /api/telemetry/resources` — list resources with telemetry
- `GET /api/telemetry/spans` — query spans with filters
- `GET /api/telemetry/logs` — query logs with filters
- `GET /api/telemetry/traces` — list traces
- `GET /api/telemetry/traces/{traceId}` — get all spans for a specific trace

Everything comes back in OTLP JSON format. This powers the new `aspire agent mcp` and `aspire otel` CLI commands, but the real implication is bigger: you can now build tooling, scripts, and AI agent integrations that query your app's telemetry directly.

Imagine an AI coding agent that can look at your actual distributed traces while debugging. That's not hypothetical anymore — that's what this API enables.

## GenAI telemetry gets practical

If you're building AI-powered apps with Semantic Kernel or Microsoft.Extensions.AI, you'll appreciate the improved GenAI telemetry visualizer. Aspire 13.2 adds:

- AI tool descriptions rendered as Markdown
- A dedicated GenAI button on the traces page for quick AI trace access
- Better error handling for truncated or non-standard GenAI JSON
- Click-to-highlight navigation between tool definitions

The blog post mentions that VS Code Copilot chat, Copilot CLI, and OpenCode all support configuring an `OTEL_EXPORTER_OTLP_ENDPOINT`. Point them at the Aspire dashboard and you can literally watch your AI agents think in real time through telemetry. That's a debugging experience you won't find anywhere else.

## Wrapping up

Aspire 13.2 takes the dashboard from "nice debugging UI" to "programmable observability platform." The export/import workflow alone saves real time on distributed debugging, and the telemetry API opens the door to AI-assisted diagnostics.

If you're already on Aspire, upgrade. If you're not — this is a good reason to check out [aspire.dev](https://aspire.dev) and see what the fuss is about.
