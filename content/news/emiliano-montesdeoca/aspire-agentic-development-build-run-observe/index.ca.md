---
title: ".NET Aspire 13.2 vol ser el millor amic del vostre agent d'IA"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 s'inclou tot en el desenvolupament agent: sortida CLI estructurada, execucions aïllades, entorns de curació automàtica i dades completes d'OpenTelemetry perquè els vostres agents d'IA puguin crear, executar i observar les vostres aplicacions."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

Coneixeu aquell moment en què el vostre agent de codificació d'IA escriu un codi sòlid, us emocioneu i després es desfà completament intentant *executar* la cosa? Conflictes de ports, processos fantasma, variables d'entorn incorrectes: de sobte, el vostre agent està cremant fitxes per resoldre problemes d'inici en lloc de crear funcions.

L'equip d'Aspire acaba de publicar una [publicació molt atenta](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) sobre exactament aquest problema, i la seva resposta és convincent: Aspire 13.2 està dissenyat no només per a humans, sinó per a agents d'IA.

## El problema és real

Els agents d'IA són increïbles per escriure codi. Però enviar una aplicació de pila completa que funcioni implica molt més que generar fitxers. Heu d'iniciar els serveis en l'ordre correcte, gestionar ports, establir variables d'entorn, connectar bases de dades i obtenir comentaris quan les coses es trenquin. Ara mateix, la majoria d'agents gestionen tot això mitjançant prova i error: executant ordres, llegint la sortida d'error, tornant-ho a provar.

Superposem instruccions de Markdown, habilitats personalitzades i indicacions per intentar guiar-les, però són imprevisibles, no es poden compilar i costen fitxes només per analitzar-les. L'equip d'Aspire va clavar la visió bàsica: els agents necessiten **compiladors i API estructurades**, no més Markdown.

## Aspira com a infraestructura d'agents

Això és el que aporta Aspire 13.2 a la taula de desenvolupament agent:

**La vostra pila sencera en codi escrit.** L'AppHost defineix la vostra topologia completa: API, frontend, base de dades, memòria cau, en TypeScript o C# compilable:

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

Un agent pot llegir-ho per entendre la topologia de l'aplicació, afegir recursos, connectar connexions i *crear per verificar*. El compilador li indica immediatament si alguna cosa no funciona. Sense endevinar, sense prova i error amb fitxers de configuració.

**Una comanda per governar-los tots.** En lloc d'agents que fan malabars amb `docker compose up`, `npm run dev` i scripts d'inici de bases de dades, tot és només `aspire start`. Tots els recursos s'inicien en l'ordre correcte, als ports adequats, amb la configuració correcta. Els processos de llarga durada tampoc pengen l'agent: Aspire els gestiona.

**Mode aïllat per a agents paral·lels.** Amb `--isolated`, cada execució d'Aspire té els seus propis ports aleatoris i secrets d'usuari separats. Hi ha diversos agents treballant en els arbres de treball de git? No xocaran. Això és enorme per a eines com els agents de fons de VS Code que fan girar entorns paral·lels.

**Ulls d'agent a través de la telemetria.** Aquí és on es fa realment potent. L'Aspire CLI exposa dades completes d'OpenTelemetry durant el desenvolupament: traces, mètriques, registres estructurats. El vostre agent no només llegeix la sortida de la consola i espera el millor. Pot rastrejar una sol·licitud fallida entre serveis, perfilar punts finals lents i identificar exactament on es trenquen les coses. Això és observabilitat de grau de producció en el bucle de desenvolupament.

## L'analogia del para-xocs de bitlles

L'equip d'Aspire utilitza una gran analogia: penseu en Aspire com a para-xocs de la pista de bitlles per als agents d'IA. Si l'agent no és perfecte (i no ho serà), els para-xocs eviten que llanci boles de canaló. La definició de pila evita la configuració incorrecta, el compilador detecta errors, la CLI gestiona la gestió del procés i la telemetria proporciona el bucle de retroalimentació.

Combineu-ho amb alguna cosa com Playwright CLI i el vostre agent pot *utilitzar* la vostra aplicació: fent clic a través dels fluxos, comprovant el DOM, veient coses trencades a la telemetria, arreglant el codi, reiniciant i provant de nou. Construir, executar, observar, arreglar. Aquest és el bucle de desenvolupament autònom que hem estat perseguint.

## Primers passos

Nou a Aspire? Instal·leu la CLI des de [get.aspire.dev](https://get.aspire.dev) i seguiu la [guia d'inici](https://aspire.dev/get-started/first-app).

Ja fas servir Aspire? Executeu `aspire update --self` per obtenir 13.2 i, a continuació, indiqueu el vostre agent de codificació preferit al vostre repositori. Potser us sorprendrà quant s'avança amb les baranes d'Aspire al seu lloc.

## Tancant

Aspire 13.2 ja no és només un marc d'aplicacions distribuïdes, sinó que s'està convertint en una infraestructura d'agent essencial. Les definicions de pila estructurades, l'inici d'un sol comandament, les execucions paral·leles aïllades i la telemetria en temps real ofereixen als agents d'IA exactament el que necessiten per passar d'escriure codi a enviar aplicacions.

Llegiu la [publicació completa](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) de l'equip d'Aspire per veure tots els detalls i vídeos de demostració.
