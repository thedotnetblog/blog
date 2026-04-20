---
title: "VS Code 1.112: Wat .NET-ontwikkelaars Eigenlijk Moeten Weten"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 is net verschenen en zit vol met agentupgrades, een geïntegreerde browserdebugger, MCP-sandboxing en monorepo-ondersteuning. Dit is wat er echt toe doet als je met .NET bouwt."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 is net geland, en eerlijk? Dit treft als je je dagen in .NET-land doorbrengt. Er staat veel in de [officiële releasenotes](https://code.visualstudio.com/updates/v1_112), maar laat me je wat scrollen besparen en focussen op wat er echt toe doet voor ons.

## Copilot CLI is veel nuttiger geworden

Het grote thema van deze release is **agentautonomie** — Copilot meer ruimte geven om zijn werk te doen zonder dat je elke stap bewaakt.

### Berichtsturen en wachtrij

Je kent dat moment waarop Copilot CLI midden in een taak zit en je realiseert dat je iets bent vergeten te vermelden? Eerder moest je wachten. Nu kun je berichten sturen terwijl een verzoek nog loopt — om de huidige respons bij te sturen of vervolgsinstructies in de wachtrij te zetten.

### Machtigingsniveaus

Dit is waar ik het meest enthousiast over ben. Copilot CLI-sessies ondersteunen nu drie machtigingsniveaus:

- **Default Permissions** — de normale stroom waarbij tools om bevestiging vragen voordat ze worden uitgevoerd
- **Bypass Approvals** — keurt alles automatisch goed en probeert bij fouten opnieuw
- **Autopilot** — volledig autonoom: keurt tools goed, beantwoordt zijn eigen vragen en gaat door totdat de taak klaar is

Je kunt Autopilot inschakelen met de instelling `chat.autopilot.enabled`.

## Webapps debuggen zonder VS Code te verlaten

De geïntegreerde browser ondersteunt nu **volledig debuggen**. Je kunt breakpoints instellen, door code stappen en variabelen inspecteren — allemaal in VS Code.

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Voor Blazor-ontwikkelaars is dit een game changer.

## MCP-server sandboxing

Als je MCP-servers gebruikt, kun je ze nu sandboxen:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

## Monorepo-aanpassingen ontdekken

Als je in een monorepo werkt, loopt VS Code met de instelling `chat.useCustomizationsInParentRepositories` omhoog naar de `.git`-root en ontdekt alles.

## /troubleshoot voor agentdebugging

Heb je ooit aangepaste instructies of vaardigheden ingesteld en je afgevraagd waarom ze niet worden opgepikt? Schakel de nieuwe `/troubleshoot`-vaardigheid in met:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

## Afsluiting

VS Code 1.112 pusht hard op de agentervaring — meer autonomie, betere debugging, strakker beveiliging. [Download VS Code 1.112](https://code.visualstudio.com/updates/v1_112) of update vanuit VS Code via **Help > Check for Updates**.
