---
title: ".NET Aspire 13.2 Vuole Essere il Migliore Amico del Tuo Agente IA"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 punta tutto sullo sviluppo agentico — output CLI strutturato, esecuzioni isolate, ambienti auto-riparanti e dati OpenTelemetry completi perché i tuoi agenti IA possano davvero costruire, eseguire e osservare le tue app."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-agentic-development-build-run-observe" >}}).*

Conosci quel momento in cui il tuo agente IA scrive del codice solido, ti entusiasmi, e poi tutto crolla quando prova a *eseguire* la cosa? Conflitti di porte, processi fantasma, variabili d'ambiente sbagliate — improvvisamente il tuo agente sta bruciando token per risolvere problemi di avvio invece di costruire funzionalità.

Il team di Aspire ha appena pubblicato un [post molto ben pensato](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) su esattamente questo problema, e la loro risposta è convincente: Aspire 13.2 è progettato non solo per gli umani, ma per gli agenti IA.

## Il problema è reale

Gli agenti IA sono incredibili nello scrivere codice. Ma consegnare un'app full-stack funzionante richiede molto di più che generare file. Devi avviare i servizi nell'ordine giusto, gestire le porte, impostare le variabili d'ambiente, connettere i database e ottenere feedback quando qualcosa si rompe. Al momento, la maggior parte degli agenti gestisce tutto questo per tentativi — eseguendo comandi, leggendo output di errore, riprovando.

Aggiungiamo istruzioni Markdown, skill personalizzati e prompt per guidarli, ma sono imprevedibili, non possono essere compilati e costano token solo per essere parsati. Il team di Aspire ha centrato l'insight chiave: gli agenti hanno bisogno di **compilatori e API strutturate**, non di più Markdown.

## Aspire come infrastruttura per agenti

Ecco cosa porta Aspire 13.2 al tavolo dello sviluppo agentico:

**Tutto il tuo stack in codice tipizzato.** L'AppHost definisce la tua topologia completa — API, frontend, database, cache — in TypeScript o C# compilabile:

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

Un agente può leggere questo per capire la topologia dell'app, aggiungere risorse, collegare connessioni e *compilare per verificare*. Il compilatore gli dice immediatamente se qualcosa è sbagliato. Niente congetture, niente tentativi con i file di configurazione.

**Un solo comando per governarli tutti.** Invece di far destreggiate gli agenti tra `docker compose up`, `npm run dev` e script di avvio database, tutto è semplicemente `aspire start`. Tutte le risorse si avviano nell'ordine giusto, sulle porte giuste, con la configurazione giusta. I processi a lunga durata non bloccano l'agente — Aspire li gestisce.

**Modalità isolata per agenti paralleli.** Con `--isolated`, ogni esecuzione di Aspire ottiene le proprie porte casuali e segreti utente separati. Hai più agenti che lavorano su git worktree? Non entreranno in collisione. Questo è enorme per strumenti come gli agenti in background di VS Code che creano ambienti paralleli.

**Occhi da agente attraverso la telemetria.** Qui diventa davvero potente. La CLI di Aspire espone dati OpenTelemetry completi durante lo sviluppo — tracce, metriche, log strutturati. Il tuo agente non sta solo leggendo l'output della console sperando per il meglio. Può tracciare una richiesta fallita tra i servizi, profilare endpoint lenti e individuare esattamente dove le cose si rompono. Questa è osservabilità di livello produzione nel ciclo di sviluppo.

## L'analogia dei parabordi del bowling

Il team di Aspire usa un'ottima analogia: pensa ad Aspire come ai parabordi della pista da bowling per gli agenti IA. Se l'agente non è perfetto (e non lo sarà), i parabordi impediscono che tiri nel canale. La definizione dello stack previene la misconfigurazioni, il compilatore cattura gli errori, la CLI gestisce i processi e la telemetria fornisce il ciclo di feedback.

Combina questo con qualcosa come Playwright CLI, e il tuo agente può davvero *usare* la tua app — cliccando nei flussi, controllando il DOM, vedendo le cose rotte nella telemetria, sistemando il codice, riavviando e testando di nuovo. Costruire, eseguire, osservare, sistemare. Questo è il ciclo di sviluppo autonomo che stavamo inseguendo.

## Per iniziare

Nuovo con Aspire? Installa la CLI da [get.aspire.dev](https://get.aspire.dev) e segui la [guida introduttiva](https://aspire.dev/get-started/first-app).

Già usi Aspire? Esegui `aspire update --self` per ottenere la 13.2, poi punta il tuo agente di coding preferito al tuo repo. Potresti stupirti di quanto va più lontano con i guardrail di Aspire.

## Per concludere

Aspire 13.2 non è più solo un framework per app distribuite — sta diventando infrastruttura essenziale per agenti. Definizioni di stack strutturate, avvio con un comando, esecuzioni parallele isolate e telemetria in tempo reale danno agli agenti IA esattamente ciò di cui hanno bisogno per passare dallo scrivere codice al consegnare app.

Leggi il [post completo](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) dal team di Aspire per tutti i dettagli e i video dimostrativi.
