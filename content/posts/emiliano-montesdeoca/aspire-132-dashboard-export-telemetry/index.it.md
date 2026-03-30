---
title: "La Dashboard di Aspire 13.2 ora ha un'API di telemetria — e cambia tutto"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 porta un'esportazione telemetrica più intelligente, un'API programmabile per trace e log, e miglioramenti alla visualizzazione GenAI. Ecco perché è importante per il tuo flusso di debug."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-132-dashboard-export-telemetry.md" >}}).*

Se hai sviluppato applicazioni distribuite con .NET Aspire, sai già che la dashboard è la cosa migliore dell'intera esperienza. Tutti i tuoi trace, log e metriche in un unico posto — niente Jaeger esterno, niente configurazione di Seq, niente momenti "fammi controllare l'altro terminale".

Aspire 13.2 ha appena migliorato tutto significativamente. James Newton-King [ha annunciato l'aggiornamento](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), e onestamente? Le funzionalità di esportazione telemetria e l'API da sole giustificano l'upgrade.

## Esportare telemetria come una persona normale

Ecco lo scenario che abbiamo vissuto tutti: stai debuggando un problema distribuito, finalmente lo riproduci dopo venti minuti di setup, e ora devi condividere con il team quello che è successo. Prima? Screenshot. Copia e incolla degli ID delle trace. Il solito caos.

Aspire 13.2 aggiunge un dialog **Gestisci log e telemetria** dove puoi:

- Pulire tutta la telemetria (utile prima di un tentativo di riproduzione)
- Esportare telemetria selezionata in un file ZIP nel formato standard OTLP/JSON
- Re-importare quel ZIP in qualsiasi dashboard Aspire successivamente

Quest'ultimo punto è la funzionalità killer. Riproduci un bug, esporti la telemetria, la alleghi al tuo work item, e il tuo collega può importarla nella propria dashboard per vedere esattamente quello che hai visto tu. Niente più "riesci a riprodurlo sulla tua macchina?"

Trace, span e log individuali hanno anche un'opzione "Export JSON" nei menu contestuali. Devi condividere una trace specifica? Click destro, copia JSON, incolla nella descrizione della PR. Fatto.

## L'API di telemetria è il vero punto di svolta

Questo è ciò che mi entusiasma di più. La dashboard ora espone un'API HTTP sotto `/api/telemetry` per interrogare i dati di telemetria programmaticamente. Endpoint disponibili:

- `GET /api/telemetry/resources` — elencare risorse con telemetria
- `GET /api/telemetry/spans` — interrogare span con filtri
- `GET /api/telemetry/logs` — interrogare log con filtri
- `GET /api/telemetry/traces` — elencare trace
- `GET /api/telemetry/traces/{traceId}` — ottenere tutti gli span per una trace specifica

Tutto torna in formato OTLP JSON. Questo alimenta i nuovi comandi CLI `aspire agent mcp` e `aspire otel`, ma l'implicazione reale è più grande: ora puoi costruire strumenti, script e integrazioni con agenti IA che interrogano direttamente la telemetria della tua app.

Immagina un agente IA che può vedere le tue trace distribuite reali durante il debug. Non è più ipotetico — è ciò che questa API rende possibile.

## La telemetria GenAI diventa pratica

Se stai costruendo app con IA usando Semantic Kernel o Microsoft.Extensions.AI, apprezzerai il visualizzatore di telemetria GenAI migliorato. Aspire 13.2 aggiunge:

- Descrizioni degli strumenti IA renderizzate come Markdown
- Un pulsante GenAI dedicato nella pagina delle trace per accesso rapido
- Migliore gestione errori per JSON GenAI troncato o non standard
- Navigazione click-to-highlight tra le definizioni degli strumenti

Il post menziona che VS Code Copilot chat, Copilot CLI e OpenCode supportano tutti la configurazione di un `OTEL_EXPORTER_OTLP_ENDPOINT`. Puntali alla dashboard Aspire e puoi letteralmente guardare i tuoi agenti IA pensare in tempo reale attraverso la telemetria. Questa è un'esperienza di debug che non troverai da nessun'altra parte.

## Per concludere

Aspire 13.2 trasforma la dashboard da "bella UI di debug" a "piattaforma di osservabilità programmabile". Il flusso di esportazione/importazione da solo fa risparmiare tempo reale nel debug distribuito, e l'API di telemetria apre la porta alla diagnostica assistita dall'IA.

Se sei già su Aspire, aggiorna. Se no — questa è una buona ragione per dare un'occhiata a [aspire.dev](https://aspire.dev).
