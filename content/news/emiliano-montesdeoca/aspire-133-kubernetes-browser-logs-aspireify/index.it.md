---
title: "Aspire 13.3: Supporto Kubernetes, Log del Browser e la Skill Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Cinque settimane dopo il 13.2, Aspire 13.3 arriva con 45 nuove funzionalità tra cui il deployment AKS di prima classe, una skill di onboarding assistita dall'IA, la cattura dei log del browser e i risultati dei comandi strutturati."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Cinque settimane non sono molto per un rilascio, ma Aspire 13.3 non sembra tale. Gli elementi principali sono significativi: deployment di Kubernetes e AKS di prima classe con Helm, una skill di onboarding assistita da agente chiamata Aspireify, cattura dei log del browser direttamente nel dashboard e risultati dei comandi strutturati. In più, 45 nuove funzionalità, 134 miglioramenti e 93 correzioni di bug.

Passiamo ai punti salienti.

## Aspireify: Onboarding Assistito da Agente

Aggiungere Aspire a un progetto esistente sembra semplice — inserisci un AppHost, fatto. In pratica comporta molta archeologia: quali porte contano, quali variabili d'ambiente sono dipendenze reali, quali servizi Docker Compose devono corrispondere alle integrazioni Aspire.

La nuova **skill Aspireify** fornisce al tuo agente di codice un flusso di lavoro guidato esattamente per questo. Quando `aspire init` crea un AppHost scheletro, la skill Aspireify aiuta l'agente a ispezionare il repository, capire come funziona già e collegare l'AppHost per adattarsi all'app — non il contrario.

La postura predefinita è "minimizzare le modifiche al tuo codice." Se la tua app legge già `DATABASE_URL`, l'agente lo mappa con `WithEnvironment()` invece di chiederti di riscrivere la tua configurazione. Se una porta è codificata in modo fisso, la skill indica all'agente quando preservarla.

Questo è il tipo di tooling IA che fa davvero risparmiare tempo invece di generare più lavoro da revisionare.

## Deployment di Kubernetes e AKS di Prima Classe

Questo era nella lista dei desideri da un po'. Aspire 13.3 include il **supporto di deployment di Kubernetes e AKS di prima classe con Helm**. Ora puoi puntare ad AKS come destinazione di deployment direttamente dagli strumenti Aspire.

Per i team che già eseguono carichi di lavoro di produzione su AKS, questo colma una lacuna significativa. Il tuo modello di applicazione Aspire ora ha un percorso pulito dallo sviluppo locale a Kubernetes senza la necessità di scrivere manualmente chart Helm.

## Log del Browser nel Dashboard

Questa è una di quelle funzionalità che sembrano piccole finché non stai facendo debug di un problema frontend.

La nuova API `WithBrowserLogs()` collega una risorsa browser tracciata a qualsiasi risorsa capace di endpoint. Aspire lancia Chromium usando un pipe CDP privato e trasmette log della console, richieste di rete ed errori direttamente nel flusso di log della risorsa:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

L'AppHost TypeScript supporta lo stesso:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Errori della console, richieste di rete fallite, eccezioni lato client — tutto visibile nello stesso dashboard dove stai già guardando trace e metriche. Nessun cambio di tab verso le DevTools del browser per le cose di base.

## Risultati dei Comandi Strutturati

I comandi delle risorse hanno ricevuto un aggiornamento significativo. Fino ad ora, i comandi restituivano successo/fallimento. Ora restituiscono risultati strutturati: testo, JSON o markdown che fluisce attraverso il modello, l'interfaccia del dashboard, la CLI e gli strumenti MCP.

Il dashboard lega tutto questo con un nuovo centro notifiche nell'intestazione. I risultati dei comandi appaiono come notifiche con timestamp con rendering markdown e un'azione "Visualizza risposta".

Questo rende i comandi delle risorse veramente componibili. Un'integrazione ora può esporre un comando che restituisce un output significativo — come un URL di tunnel — invece di cambiare semplicemente lo stato da qualche parte.

## Conclusione

Aspire 13.3 vale l'aggiornamento anche solo per il supporto Kubernetes. I log del browser e i risultati dei comandi strutturati sembrano il tipo di miglioramenti della qualità della vita che si accumulano rapidamente in un flusso di lavoro di sviluppo quotidiano.

Note di rilascio complete: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
