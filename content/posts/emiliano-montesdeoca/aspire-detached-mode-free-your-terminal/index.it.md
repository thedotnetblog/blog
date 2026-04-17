---
title: "Smetti di sorvegliare il tuo terminale: la modalità detached di Aspire cambia il flusso di lavoro"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 ti permette di eseguire il tuo AppHost in background e riprenderti il terminale. Combinato con i nuovi comandi CLI e il supporto per gli agenti, è più importante di quanto sembri."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Ogni volta che esegui un AppHost di Aspire, il tuo terminale sparisce. Bloccato. Occupato finché non premi Ctrl+C. Devi eseguire un comando veloce? Apri un'altra scheda. Vuoi controllare i log? Un'altra scheda. È una piccola frizione che si accumula in fretta.

Aspire 13.2 risolve questo problema. James Newton-King [ha scritto tutti i dettagli](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), e onestamente, questa è una di quelle funzionalità che cambia immediatamente il modo in cui lavori.

## Modalità detached: un comando, terminale recuperato

```bash
aspire start
```

Questa è la scorciatoia per `aspire run --detach`. Il tuo AppHost si avvia in background e riottieni il terminale immediatamente. Niente schede extra. Niente multiplexer di terminale. Solo il tuo prompt, pronto all'uso.

## Gestire ciò che è in esecuzione

Il punto è questo — eseguire in background è utile solo se riesci a gestire ciò che c'è là fuori. Aspire 13.2 include un set completo di comandi CLI proprio per questo:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Questo trasforma il CLI di Aspire in un vero gestore di processi. Puoi avviare più AppHost, controllare il loro stato, seguire i loro log e spegnerli — tutto da un'unica sessione di terminale.

## Combinalo con la modalità isolata

La modalità detached si abbina naturalmente con la modalità isolata. Vuoi eseguire due istanze dello stesso progetto in background senza conflitti di porta?

```bash
aspire start --isolated
aspire start --isolated
```

Ognuna ottiene porte casuali, secret separati e il proprio ciclo di vita. Usa `aspire ps` per vedere entrambe, `aspire stop` per fermare quella di cui non hai più bisogno.

## Perché questo è enorme per gli agenti di codice

Qui diventa davvero interessante. Un agente di codice che lavora nel tuo terminale ora può:

1. Avviare l'app con `aspire start`
2. Interrogare il suo stato con `aspire describe`
3. Controllare i log con `aspire logs` per diagnosticare problemi
4. Fermarla con `aspire stop` quando ha finito

Tutto senza perdere la sessione del terminale. Prima della modalità detached, un agente che eseguiva il tuo AppHost si bloccava nel proprio terminale. Ora può avviare, osservare, iterare e ripulire — esattamente come vorresti che funzionasse un agente autonomo.

Il team di Aspire ha puntato su questo. Eseguire `aspire agent init` configura un file di skill di Aspire che insegna questi comandi agli agenti. Così strumenti come l'agente di codice di Copilot possono gestire i tuoi workload Aspire direttamente.

## Per concludere

La modalità detached è un upgrade del flusso di lavoro mascherato da semplice flag. Smetti di cambiare contesto tra i terminali, gli agenti smettono di bloccarsi da soli, e i nuovi comandi CLI ti danno visibilità reale su ciò che è in esecuzione. È pratico, è pulito, e rende il ciclo di sviluppo quotidiano notevolmente più fluido.

Leggi il [post completo](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) per tutti i dettagli e scarica Aspire 13.2 con `aspire update --self`.
