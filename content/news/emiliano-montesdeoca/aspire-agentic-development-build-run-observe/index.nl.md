---
title: ".NET Aspire 13.2 Wil de Beste Vriend van je AI-Agent Zijn"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 gaat all-in op agentische ontwikkeling — gestructureerde CLI-uitvoer, geïsoleerde runs, zelfherstellende omgevingen en volledige OpenTelemetry-data zodat je AI-agents je apps daadwerkelijk kunnen bouwen, uitvoeren en observeren."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-agentic-development-build-run-observe" >}}).*

Ken je dat moment waarop je AI-codeagent solide code schrijft, je enthousiast wordt, en dan valt alles uit elkaar bij het proberen het *uit te voeren*? Poortconflicten, phantom processes, verkeerde omgevingsvariabelen — plotseling brandt je agent tokens voor het oplossen van opstartproblemen in plaats van het bouwen van functies.

Het Aspire-team heeft een [zeer doordachte post](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) gepubliceerd over precies dit probleem, en hun antwoord is overtuigend: Aspire 13.2 is ontworpen niet alleen voor mensen, maar voor AI-agents.

## Aspire als agentinfrastructuur

Dit is wat Aspire 13.2 meebrengt voor agentische ontwikkeling:

**Je hele stack in getypte code.** De AppHost definieert je volledige topologie — in compileerbare TypeScript of C#:

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

**Één commando voor alles.** In plaats van jongleren met `docker compose up`, `npm run dev` en database-opstartscripts — alles is gewoon `aspire start`.

**Geïsoleerde modus voor parallelle agents.** Met `--isolated` krijgt elke Aspire-run zijn eigen willekeurige poorten en afzonderlijke gebruikersgeheimen.

**Agentogen via telemetrie.** De Aspire CLI stelt tijdens development volledige OpenTelemetry-data bloot — traces, metrics, gestructureerde logs.

## De bowlingbaan-bumper analogie

Het Aspire-team gebruikt een geweldige analogie: denk aan Aspire als bowlingbaanbumpers voor AI-agents. Als de agent niet perfect is (en dat zal hij niet zijn), houden de bumpers hem van het gooien in de goot.

## Samenvatting

Aspire 13.2 is niet alleen een framework voor gedistribueerde apps — het wordt essentiële agentinfrastructuur. Lees de [volledige post](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) van het Aspire-team.
