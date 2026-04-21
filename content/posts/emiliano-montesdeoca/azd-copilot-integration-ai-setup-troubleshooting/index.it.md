---
title: "azd + GitHub Copilot: Configurazione del progetto con IA e risoluzione intelligente degli errori"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI si integra ora con GitHub Copilot per generare l'infrastruttura del tuo progetto e risolvere errori di deployment — senza uscire dal terminale."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale in inglese, [clicca qui]({{< ref "index.md" >}}).*

Conosci quel momento in cui vuoi fare il deploy di un'app esistente su Azure e ti ritrovi a fissare un `azure.yaml` vuoto, cercando di ricordare se la tua API Express dovrebbe usare Container Apps o App Service? Quel momento è appena diventato molto più breve.

L'Azure Developer CLI (`azd`) si integra ora con GitHub Copilot in due modi concreti: scaffolding assistito dall'IA durante `azd init`, e risoluzione intelligente degli errori quando i deployment falliscono. Entrambe le funzionalità rimangono completamente nel terminale — esattamente dove voglio che siano.

## Configurazione con Copilot durante azd init

Quando esegui `azd init`, ora compare l'opzione "Set up with GitHub Copilot (Preview)". Selezionala e Copilot analizza la tua codebase per generare `azure.yaml`, i template di infrastruttura e i moduli Bicep — basandosi sul tuo codice reale.

```
azd init
# Seleziona: "Set up with GitHub Copilot (Preview)"
```

Prerequisiti:

- **azd 1.23.11 o superiore** — verifica con `azd version` o aggiorna con `azd update`
- **Abbonamento attivo a GitHub Copilot** (Individual, Business o Enterprise)
- **GitHub CLI (`gh`)** — `azd` chiederà il login se necessario

Quello che trovo genuinamente utile: funziona in entrambi i sensi. Stai costruendo da zero? Copilot ti aiuta a configurare i servizi Azure giusti sin dall'inizio. Hai un'app esistente che volevi deployare da tempo? Punta Copilot su di essa e genera la configurazione senza che tu debba ristrutturare nulla.

### Cosa fa davvero

Diciamo che hai un'API Express Node.js con dipendenza da PostgreSQL. Invece di decidere manualmente tra Container Apps e App Service, e poi scrivere Bicep da zero, Copilot rileva il tuo stack e genera:

- Un `azure.yaml` con le impostazioni corrette di `language`, `host` e `build`
- Un modulo Bicep per Azure Container Apps
- Un modulo Bicep per Azure Database for PostgreSQL

E prima di toccare qualsiasi cosa esegue verifiche preventive — controlla che la tua directory git sia pulita, chiede il consenso per gli strumenti del server MCP. Niente accade senza che tu sappia esattamente cosa sta per cambiare.

## Risoluzione degli errori con Copilot

Gli errori di deployment sono inevitabili. Parametri mancanti, problemi di permessi, disponibilità degli SKU — e il messaggio d'errore raramente ti dice l'unica cosa che hai davvero bisogno di sapere: *come risolverlo*.

Senza Copilot, il ciclo è: copiare l'errore → cercare nella documentazione → leggere tre risposte irrilevanti su Stack Overflow → eseguire alcuni comandi `az` CLI → riprovare sperando. Con Copilot integrato in `azd`, questo ciclo collassa. Quando qualsiasi comando `azd` fallisce, offre immediatamente quattro opzioni:

- **Explain** — spiegazione in linguaggio naturale di cosa è andato storto
- **Guidance** — istruzioni passo dopo passo per correggere il problema
- **Diagnose and Guide** — analisi completa + Copilot applica la correzione (con la tua approvazione) + retry opzionale
- **Skip** — gestire da soli

Il punto cruciale: Copilot ha già il contesto del tuo progetto, il comando che ha fallito e l'output dell'errore. I suoi suggerimenti sono specifici per *la tua situazione*, non documentazione generica.

### Configurare il comportamento predefinito

Se scegli sempre la stessa opzione, salta il prompt interattivo:

```
azd config set copilot.errorHandling.category troubleshoot
```

Valori: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Puoi anche abilitare auto-fix e retry:

```
azd config set copilot.errorHandling.fix allow
```

Ritorno alla modalità interattiva in qualsiasi momento:

```
azd config unset copilot.errorHandling.category
```

## Conclusione

Questo è esattamente il tipo di integrazione di Copilot che porta valore reale. Provalo eseguendo `azd update` per ottenere l'ultima versione e usa `azd init` nel tuo prossimo progetto.

Leggi l'[annuncio originale qui](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
