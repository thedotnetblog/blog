---
title: "Aspire 13.2 incorpora Bun, millora els contenidors i redueix la fricció en la depuració"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 afegeix suport de primera classe per a Bun a les apps Vite, millora la fiabilitat de Yarn i incorpora millores de contenidors que fan que el comportament local sigui més fidel. Aquí tens què ha canviat realment i per què importa."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Si fa temps que construeixes backends .NET amb frontends JavaScript a Aspire, la 13.2 és el tipus d'actualització que et millora el dia sense fer gaire soroll. Res de paradigmes nous cridaners. Només millores sòlides per a coses que eren lleugerament molestes.

Anem a veure què ha arribat realment.

## Bun ja és un ciutadà de primera classe

La gran novetat: suport per a Bun en apps Vite a Aspire. Una crida fluida, i llestos.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

Si el teu equip ja fa servir Bun — i potser sí, tenint en compte uns temps d'instal·lació molt més ràpids i un arrencat molt més àgil — Aspire ja no et fa remar contra corrent. Abans, Aspire assumia npm i havies de fer-ne voltes. Ara `.withBun()` és una opció de primera classe al costat de `.withYarn()` i del comportament predeterminat de npm.

Per què importa? Perquè la velocitat de les eines JavaScript afecta directament el bucle intern de desenvolupament. Si el teu frontend triga 30 segons a instal·lar dependències cada cop que arranques un entorn nou, això s'acumula. Bun retalla això de manera dràstica.

Les equivalències d'AppHost en C# estan documentades a [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) si prefereixes escriure en C# — s'apliquen tots els mateixos patrons.

## Yarn ha guanyat fiabilitat

Bun s'endú els titulars, però els usuaris de Yarn reben una cosa potser més important: menys fallades misterioses. Aspire 13.2 millora la fiabilitat de `withYarn()` amb `addViteApp()`.

Aquestes correccions no semblen emocionants fins que has passat 20 minuts depurant per què un recurs frontal basat en Yarn no arrencava. Dona-ho per arreglat.

## Publicació de contenidors que realment pots entendre

Dues millores de contenidors que val la pena conèixer:

### Política de pull explícita

La publicació amb Docker Compose ara admet `PullPolicy`, inclosa l'opció `Never`:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

Aquest és el flux de treball de «utilitza la imatge que ja he construït i deixa el registre en pau». Molt útil quan iteres localment sobre imatges que construeixes i publiques manualment, o quan el teu CI genera una imatge i vols que Compose faci servir exactament aquella sense descarregar res remot d'amagat.

### Els volums de PostgreSQL 18+ tornen a funcionar

PostgreSQL 18 va canviar la disposició interna del directori de dades. Això va trencar el mapatge de volums a Aspire de manera silenciosa — el volum de dades es configurava però la persistència en realitat no funcionava bé. La 13.2 ho arregla.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

Si estàs executant PostgreSQL 18 o posterior amb un volum de dades, actualitza a Aspire 13.2 i no hi pensis més.

## Millores de qualitat de vida en la depuració

Algunes coses que fan menys frustrant fer pas a pas una sessió d'AppHost:

- **`DebuggerDisplayAttribute` als tipus core** — `DistributedApplication`, els recursos i les expressions d'endpoint ara mostren valors útils al depurador en comptes de fer-te rebuscar entre arbres d'objectes
- **Millors missatges de fallada de `WaitFor`** — quan els recursos no arranquen, el context de l'error ara sí que és útil
- **`BeforeResourceStartedEvent` s'activa en el moment correcte** — només quan un recurs realment comença a arrencar, no en transicions d'estat no relacionades
- **`launchSettings.json` és més robust** — menys possibilitats que una configuració malformada corrompi l'arrencada del teu entorn de desenvolupament

Cap d'aquestes millores no és individualment espectacular, però en conjunt eliminen fricció de l'experiència de depuració. Si alguna vegada has hagut de baixar tres nivells dins d'un objecte de recurs d'Aspire per esbrinar quin endpoint feia servir, la millora del debugger display ja val l'actualització.

## Resumint

Aspire 13.2 és una versió centrada en la qualitat. El suport de Bun és el titular, però les millores de contenidors i depuració són el que farà que la feina diària sigui més fluida. Val la pena actualitzar, sobretot si fas servir PostgreSQL 18 amb volums de dades.

Tots els detalls al [post original de David Pine](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) i a la documentació de [novetats d'Aspire 13.2](https://aspire.dev/whats-new/aspire-13-2/).