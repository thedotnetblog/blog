---
title: "Aspire 13.2 krijgt Bun, betere containers en minder debugfrictie"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 voegt eersteklas Bun-ondersteuning toe voor Vite-apps, fixt de betrouwbaarheid van Yarn en levert containerverbeteringen die lokaal gedrag eerlijker maken. Dit is wat er echt veranderde en waarom dat telt."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

Als je in Aspire .NET-backends met JavaScript-frontends bouwt, is 13.2 zo'n update die je dag stilletjes beter maakt. Geen opvallende nieuwe paradigma's. Gewoon stevige verbeteringen aan dingen die licht irritant waren.

Laten we bekijken wat er echt is aangekomen.

## Bun is nu eersteklas

De headline-feature: Bun-ondersteuning voor Vite-apps in Aspire. Eén vloeiende call, klaar.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

Als je team al Bun gebruikt — en waarschijnlijk wel, gezien de veel snellere installatietijden en opstartsnelheid — dan dwingt Aspire je niet langer tegen de stroom in te zwemmen. Voorheen ging Aspire uit van npm en moest je daar omheen werken. Nu is `.withBun()` een eersteklas optie naast `.withYarn()` en het standaardgedrag van npm.

Waarom maakt dat uit? Omdat de snelheid van JavaScript-tooling rechtstreeks invloed heeft op je inner dev loop. Als je frontend 30 seconden nodig heeft om dependencies te installeren telkens wanneer je een nieuwe omgeving opzet, tikt dat aan. Bun haalt daar flink wat vanaf.

De C#-equivalenten voor AppHost staan gedocumenteerd op [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) als je liever in C# schrijft — dezelfde patronen gelden gewoon.

## Yarn is betrouwbaarder geworden

Bun pakt de aandacht, maar Yarn-gebruikers krijgen iets dat misschien nog belangrijker is: minder mysterieuze fouten. Aspire 13.2 verbetert de betrouwbaarheid van `withYarn()` met `addViteApp()`.

Dit soort fixes klinkt pas spannend als je 20 minuten hebt zitten uitzoeken waarom een Yarn-gestuurde frontend resource niet wilde starten. Beschouw het als opgelost.

## Containerpublicatie waar je echt iets aan hebt

Twee containerverbeteringen die je moet kennen:

### Expliciet pullbeleid

Docker Compose-publicatie ondersteunt nu `PullPolicy`, inclusief de optie `Never`:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

Dit is de workflow van: "gebruik gewoon het image dat ik al gebouwd heb en laat de registry erbuiten." Superhandig als je lokaal iteratief werkt aan images die je handmatig bouwt en publiceert, of wanneer je CI een image oplevert en je Compose exact dát image wilt laten gebruiken zonder stiekem een remote pull.

### PostgreSQL 18+ volumes werken weer

PostgreSQL 18 veranderde de interne indeling van de datadirectory. Daardoor brak volume-mapping in Aspire stilletjes — je datavolume werd wel opgezet, maar persistentie werkte niet goed. 13.2 fixt dat.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

Als je PostgreSQL 18 of later met een datavolume draait, update dan naar Aspire 13.2 en denk er niet meer over na.

## Debugging die net wat fijner voelt

Een paar dingen die het doorstappen van een AppHost-sessie minder frustrerend maken:

- **`DebuggerDisplayAttribute` op core types** — `DistributedApplication`, resources en endpoint-expressions tonen nu nuttige waarden in de debugger in plaats van dat je door object trees moet graven
- **Betere `WaitFor`-foutmeldingen** — als resources niet starten, is de foutcontext nu echt bruikbaar
- **`BeforeResourceStartedEvent` triggert op het juiste moment** — alleen wanneer een resource daadwerkelijk begint te starten, niet bij losse statusovergangen
- **`launchSettings.json` is robuuster** — minder kans dat een foutieve instelling je dev-startup kapotmaakt

Geen van deze verbeteringen is losstaand wereldschokkend, maar samen halen ze frictie uit de debugervaring. Als je ooit drie lagen diep in een Aspire-resource-object hebt moeten duiken om te achterhalen welk endpoint het gebruikte, is die debugger-displayverbetering alleen al de update waard.

## Afsluitend

Aspire 13.2 is een release die op kwaliteit focust. Bun-ondersteuning is de headline, maar de container- en debugverbeteringen zijn wat je dagelijkse werk soepeler maken. Zeker de moeite waard om te updaten — vooral als je PostgreSQL 18 met datavolumes gebruikt.

De volledige details staan in het [oorspronkelijke bericht van David Pine](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) en de [Aspire 13.2 what's new-documentatie](https://aspire.dev/whats-new/aspire-13-2/).