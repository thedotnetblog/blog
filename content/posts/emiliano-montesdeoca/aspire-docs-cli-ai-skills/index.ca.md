---
title: "Aspire 13.2 envia una CLI de Docs, i el vostre agent d'IA també la pot utilitzar"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 afegeix aspire docs: una CLI per cercar, navegar i llegir documentació oficial sense sortir del terminal. També funciona com una eina per als agents d'IA. Heus aquí per què això importa."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

Coneixeu aquell moment en què esteu endinsat en un Aspire AppHost, connectant integracions i heu de comprovar exactament quins paràmetres espera la integració de Redis? Feu una pestanya alternativa al vostre navegador, busqueu aspire.dev, mireu els documents de l'API i torneu al vostre editor. Context perdut. Flux trencat.

Aspire 13.2 només [ha enviat una solució per això](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). La CLI `aspire docs` us permet cercar, navegar i llegir la documentació oficial d'Aspire directament des del vostre terminal. I com que està recolzat per serveis reutilitzables, els agents i les habilitats d'IA poden utilitzar les mateixes ordres per buscar documents en lloc d'al·lucinar API que no existeixen.

## El problema que això resol realment

David Pine ho clava a la publicació original: els agents d'IA van ser *terribles* per ajudar els desenvolupadors a crear aplicacions Aspire. Recomanarien `dotnet run` en lloc de `aspire run`, fer referència a learn.microsoft.com per als documents que viuen a aspire.dev, suggerir paquets NuGet obsolets i, el meu favorit personal, al·lucinar API que no existeixen.

Per què? Com que Aspire era específic de.NET molt més temps del que ha estat políglot, i els LLM treballen amb dades de formació anteriors a les últimes funcions. Quan doneu a un agent d'IA la possibilitat de buscar realment els documents actuals, deixa d'endevinar i comença a ser útil.

## Tres ordres, zero pestanyes del navegador

La CLI és molt senzilla:

### Llista tots els documents

```bash
aspire docs list
```

Retorna totes les pàgines de documentació disponibles a aspire.dev. Necessites una sortida llegible per màquina? Afegeix `--format Json`.

### Cerca un tema

```bash
aspire docs search "redis"
```

Cerca tant títols com contingut amb una puntuació de rellevància ponderada. El mateix motor de cerca que impulsa l'eina de documentació internament. Obteniu resultats classificats amb títols, slugs i puntuacions de rellevància.

### Llegeix una pàgina sencera (o només una secció)

```bash
aspire docs get redis-integration
```

Transmet la pàgina completa com a reducció al terminal. Necessites només una secció?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Precisió quirúrgica. Sense desplaçament per 500 línies. Només la part que necessiteu.

## L'angle de l'agent d'IA

Aquí és on és interessant per als desenvolupadors que construïm amb eines d'IA. Les mateixes ordres `aspire docs` funcionen com a eines per als agents d'IA, mitjançant habilitats, servidors MCP o embolcalls CLI senzills.

En comptes que el vostre assistent d'IA creï les API d'Aspire basades en dades d'entrenament obsoletes, pot trucar a `aspire docs search "postgres"`, trobar els documents oficials d'integració, llegir la pàgina adequada i oferir-vos l'enfocament documentat. Documentació actual en temps real, no la que el model va memoritzar fa sis mesos.

L'arquitectura darrere d'això és intencionada. L'equip d'Aspire va crear serveis reutilitzables (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) en lloc d'una integració única. Això vol dir que el mateix motor de cerca funciona per a humans al terminal, agents d'IA al vostre editor i automatització al vostre pipeline CI.

## Escenaris del món real

**Cerques ràpides del terminal:** Teniu tres fitxers de profunditat i necessiteu paràmetres de configuració de Redis. Dues ordres, noranta segons, tornen a treballar:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**Desenvolupament assistit per IA:** la vostra habilitat VS Code inclou les ordres CLI. Demaneu "Afegeix una base de dades PostgreSQL al meu AppHost" i l'agent cerca els documents reals abans de respondre. Sense al·lucinacions.

**Validació CI/CD:** el vostre pipeline valida les configuracions d'AppHost amb la documentació oficial mitjançant programació. `--format Json` emet les canonades netament a `jq` i altres eines.

**Bases de coneixement personalitzades:** crear la teva pròpia eina d'IA? Introduïu la sortida JSON estructurada directament a la vostra base de coneixement:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Sense raspat web. No hi ha claus API. Les mateixes dades estructurades que les eines de documents utilitza internament.

## La documentació sempre està en directe

Aquesta és la part que més agraeixo. La CLI no baixa cap instantània: consulta aspire.dev amb la memòria cau basada en ETag. En el moment en què s'actualitzen els documents, la vostra CLI i qualsevol habilitat incorporada al damunt ho reflecteixen. No hi ha còpies obsoletes, no "però el wiki va dir..." moments.

## Tancant

`aspire docs` és una d'aquestes petites característiques que resol un problema real de manera neta. Els humans tenen accés a la documentació nativa del terminal. Els agents d'IA tenen una manera de deixar d'endevinar i començar a fer referència a documents reals. I tot està recolzat per la mateixa font de veritat.

Si esteu creant amb.NET Aspire i encara no heu provat la CLI, executeu `aspire docs search "your-topic-here"` i mireu com us sembla. A continuació, considereu incloure aquestes ordres en qualsevol habilitat d'IA o configuració d'automatització que feu servir; els vostres agents us ho agrairan.

Fes una ullada a [La immersió profunda de David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) sobre com es van reunir les eines de documents i la [referència oficial de la CLI](https://aspire.dev/reference/cli/commands/aspire-docs/) per a tots els detalls.
