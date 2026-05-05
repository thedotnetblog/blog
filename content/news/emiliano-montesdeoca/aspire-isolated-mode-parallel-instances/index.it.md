---
title: "La Modalità Isolata di Aspire Risolve l'Incubo dei Conflitti di Porta per lo Sviluppo Parallelo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduce la modalità --isolated: porte random, segreti separati e zero collisioni quando si eseguono più istanze dello stesso AppHost. Perfetto per agenti IA, worktree e workflow paralleli."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Se hai mai provato a eseguire due istanze dello stesso progetto contemporaneamente, conosci il dolore. La porta 8080 è già in uso. La porta 17370 è occupata. Uccidi qualcosa, riavvia, destreggiati tra le variabili d'ambiente — è un killer della produttività.

Questo problema sta peggiorando, non migliorando. Gli agenti IA creano git worktree per lavorare in modo indipendente. Gli agenti in background avviano ambienti separati. Gli sviluppatori fanno checkout dello stesso repo due volte per i feature branch. Ognuno di questi scenari sbatte contro lo stesso muro: due istanze della stessa app che lottano per le stesse porte.

Aspire 13.2 risolve questo con un singolo flag. James Newton-King del team Aspire ha [scritto tutti i dettagli](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), ed è una di quelle feature "perché non l'avevamo già?"

## La soluzione: `--isolated`

```bash
aspire run --isolated
```

Questo è tutto. Ogni esecuzione ottiene:

- **Porte random** — niente più collisioni tra istanze
- **Segreti utente isolati** — connection string e chiavi API restano separate per istanza

Nessuna riassegnazione manuale delle porte. Nessun giocoleria con le variabili d'ambiente. Ogni esecuzione ottiene un ambiente pulito e privo di collisioni automaticamente.

## Scenari reali dove questo brilla

**Checkout multipli.** Hai un feature branch in una directory e un bugfix in un'altra:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Entrambi girano senza conflitti. La dashboard mostra cosa sta girando e dove.

**Agenti in background in VS Code.** Quando l'agente in background di Copilot Chat crea un git worktree per lavorare sul tuo codice in modo indipendente, potrebbe aver bisogno di eseguire il tuo AppHost Aspire. Senza `--isolated`, c'è un conflitto di porte con il tuo worktree principale. Con esso, entrambe le istanze funzionano e basta.

Lo skill Aspire distribuito con `aspire agent init` istruisce automaticamente gli agenti a usare `--isolated` quando lavorano nei worktree. Quindi l'agente in background di Copilot dovrebbe gestire tutto nativamente.

**Test di integrazione in parallelo allo sviluppo.** Hai bisogno di eseguire test contro un AppHost live mentre continui a sviluppare funzionalità? La modalità isolata dà a ogni contesto le sue porte e la sua configurazione.

## Come funziona sotto il cofano

Quando passi `--isolated`, la CLI genera un ID di istanza unico per l'esecuzione. Questo guida due comportamenti:

1. **Randomizzazione delle porte** — invece di legarsi a porte prevedibili definite nella configurazione del tuo AppHost, la modalità isolata sceglie porte casuali disponibili per tutto — la dashboard, gli endpoint dei servizi, tutto. Il service discovery si adatta automaticamente, così i servizi si trovano a vicenda indipendentemente da quali porte ottengono.

2. **Isolamento dei segreti** — ogni esecuzione isolata ottiene il proprio store di segreti utente, identificato dall'ID dell'istanza. Connection string e chiavi API di un'esecuzione non trapelano in un'altra.

Il tuo codice non ha bisogno di modifiche. Il service discovery di Aspire risolve gli endpoint a runtime, quindi tutto si connette correttamente indipendentemente dall'assegnazione delle porte.

## Quando usarlo

Usa `--isolated` quando esegui più istanze dello stesso AppHost contemporaneamente — che si tratti di sviluppo parallelo, test automatizzati, agenti IA o git worktree. Per lo sviluppo a singola istanza dove preferisci porte prevedibili, il normale `aspire run` funziona ancora benissimo.

## Per concludere

La modalità isolata è una piccola feature che risolve un problema reale e sempre più comune. Man mano che lo sviluppo assistito da IA ci spinge verso più workflow paralleli — agenti multipli, worktree multipli, contesti multipli — la capacità di semplicemente avviare un'altra istanza senza lottare per le porte è essenziale.

Leggi il [post completo](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) per tutti i dettagli tecnici e provalo con `aspire update --self` per ottenere la 13.2.
