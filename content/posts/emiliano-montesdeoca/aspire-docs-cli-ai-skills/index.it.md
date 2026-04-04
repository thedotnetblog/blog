---
title: "Aspire 13.2 include una CLI per la documentazione — e anche il tuo agente IA può usarla"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 aggiunge aspire docs — una CLI per cercare, esplorare e leggere la documentazione ufficiale senza uscire dal terminale. Funziona anche come strumento per agenti IA. Ecco perché è importante."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-docs-cli-ai-skills.md" >}}).*

Conosci quel momento in cui sei immerso in un Aspire AppHost, stai collegando integrazioni, e devi controllare esattamente quali parametri si aspetta l'integrazione Redis? Fai alt-tab al browser, cerchi su aspire.dev, strizzi gli occhi sulla documentazione delle API, poi torni al tuo editor. Contesto perso. Flusso interrotto.

Aspire 13.2 ha appena [rilasciato una soluzione per questo](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). La CLI `aspire docs` ti permette di cercare, esplorare e leggere la documentazione ufficiale di Aspire direttamente dal tuo terminale. E siccome è supportata da servizi riutilizzabili, gli agenti IA e le skill possono usare gli stessi comandi per consultare la documentazione invece di allucinare API che non esistono.

## Il problema che questo risolve davvero

David Pine lo dice perfettamente nel post originale: gli agenti IA erano *terribili* nell'aiutare gli sviluppatori a costruire app con Aspire. Raccomandavano `dotnet run` invece di `aspire run`, facevano riferimento a learn.microsoft.com per docs che vivono su aspire.dev, suggerivano pacchetti NuGet obsoleti, e — il mio preferito — allucinavano API inesistenti.

Perché? Perché Aspire è stato specifico per .NET molto più a lungo di quanto sia stato poliglotta, e i LLM lavorano con dati di addestramento che precedono le ultime funzionalità. Quando dai a un agente IA la possibilità di consultare la documentazione attuale, smette di tirare a indovinare e inizia a essere utile.

## Tre comandi, zero schede del browser

La CLI è di una semplicità rinfrescante:

### Elencare tutta la documentazione

```bash
aspire docs list
```

Restituisce ogni pagina di documentazione disponibile su aspire.dev. Serve un output leggibile dalle macchine? Aggiungi `--format Json`.

### Cercare un argomento

```bash
aspire docs search "redis"
```

Cerca sia nei titoli che nei contenuti con punteggio di rilevanza ponderato. Lo stesso motore di ricerca che alimenta internamente gli strumenti di documentazione. Ottieni risultati classificati con titoli, slug e punteggi di rilevanza.

### Leggere una pagina intera (o solo una sezione)

```bash
aspire docs get redis-integration
```

Trasmette la pagina completa in markdown nel tuo terminale. Ti serve solo una sezione?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Precisione chirurgica. Niente scrolling su 500 righe. Solo la parte che ti serve.

## L'aspetto agente IA

Ecco dove diventa interessante per noi sviluppatori che costruiamo con strumenti IA. Gli stessi comandi `aspire docs` funzionano come strumenti per agenti IA — tramite skill, server MCP, o semplici wrapper CLI.

Invece di far inventare al tuo assistente IA delle API Aspire basate su dati di addestramento obsoleti, può chiamare `aspire docs search "postgres"`, trovare la documentazione ufficiale dell'integrazione, leggere la pagina giusta, e darti l'approccio documentato. Documentazione in tempo reale e aggiornata — non quello che il modello ha memorizzato sei mesi fa.

L'architettura dietro tutto questo è intenzionale. Il team Aspire ha costruito servizi riutilizzabili (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) anziché un'integrazione una tantum. Questo significa che lo stesso motore di ricerca funziona per gli umani nel terminale, gli agenti IA nel tuo editor, e l'automazione nella tua pipeline CI.

## Scenari reali

**Consultazioni rapide nel terminale:** Sei tre file in profondità e hai bisogno dei parametri di configurazione Redis. Due comandi, novanta secondi, di nuovo al lavoro:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**Sviluppo assistito dall'IA:** La tua skill di VS Code avvolge i comandi CLI. Chiedi "Aggiungi un database PostgreSQL al mio AppHost" e l'agente consulta i docs reali prima di rispondere. Nessuna allucinazione.

**Validazione CI/CD:** La tua pipeline valida le configurazioni AppHost contro la documentazione ufficiale in modo programmatico. L'output `--format Json` si collega in modo pulito a `jq` e altri strumenti.

**Basi di conoscenza personalizzate:** Stai costruendo i tuoi strumenti IA? Invia l'output JSON strutturato direttamente nella tua base di conoscenza:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Niente web scraping. Niente chiavi API. Gli stessi dati strutturati usati internamente dagli strumenti di documentazione.

## La documentazione è sempre aggiornata

Questa è la parte che apprezzo di più. La CLI non scarica uno snapshot — interroga aspire.dev con caching basato su ETag. Nel momento in cui la documentazione viene aggiornata, la tua CLI e qualsiasi skill costruita su di essa lo riflette. Niente copie obsolete, niente momenti "ma il wiki diceva...".

## Per concludere

`aspire docs` è una di quelle piccole funzionalità che risolve un problema reale in modo pulito. Gli umani ottengono accesso alla documentazione nativo nel terminale. Gli agenti IA ottengono un modo per smettere di indovinare e iniziare a fare riferimento a docs reali. E tutto è supportato dalla stessa fonte di verità.

Se stai costruendo con .NET Aspire e non hai ancora provato la CLI, esegui `aspire docs search "il-tuo-argomento-qui"` e vedi come ti sembra. Poi considera di integrare quei comandi nella skill IA o nella configurazione di automazione che stai usando — i tuoi agenti ti ringrazieranno.

Dai un'occhiata all'[approfondimento di David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) su come sono nati gli strumenti di documentazione, e al [riferimento ufficiale della CLI](https://aspire.dev/reference/cli/commands/aspire-docs/) per tutti i dettagli.
