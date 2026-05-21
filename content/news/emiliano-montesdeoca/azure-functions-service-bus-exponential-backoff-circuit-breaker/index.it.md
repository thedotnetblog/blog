---
title: "Smetti di Martellare una Dipendenza in Difficoltà: Pattern di Retry per Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "I pattern di exponential backoff e circuit breaker sono ora supportati nativamente per le Azure Functions attivate da Service Bus — ecco come funzionano e perché li vuoi entrambi."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Ecco come un guasto recuperabile diventa un'interruzione in un'applicazione Functions: una dipendenza inizia a generare timeout, ogni istanza Function riprova immediatamente e indefinitamente, la dipendenza viene martellata con centinaia di richieste fallite concorrenti, e quello che è iniziato come un piccolo problema transitorio diventa un evento di contropressione a livello di sistema.

Probabilmente conosci questa storia. Azure Functions scala velocemente — questo è tutto il punto. Ma "scalare velocemente" e "riprovare immediatamente" insieme possono peggiorare drammaticamente i guasti.

Due pattern aiutano. Exponential backoff e circuit breaker. Entrambi sono ora supportati nativamente per le Azure Functions attivate da Service Bus.

## Due Pattern, Ruoli Diversi

Questi pattern sono complementari, non alternative:

**L'exponential backoff** risponde a: *quando dovrei riprovare?*
Aumenta il ritardo tra i tentativi in modo che una dipendenza abbia il tempo di recuperare. A livello di messaggio, regolando il ritmo dei retry.

**Il circuit breaker** risponde a: *dovrei chiamare questa dipendenza adesso?*
Interrompe le chiamate ripetute a una dipendenza non sana dopo che viene raggiunta una soglia di errore, poi sonda con cautela dopo un periodo di raffreddamento. A livello di sistema, prevenendo le tempeste di retry.

Li vuoi entrambi. Il backoff gestisce il ritmo dei retry per messaggio. Il circuit breaker gestisce le decisioni di salute aggregate.

## Perché è Importante Specialmente per Service Bus

La coda assorbe il traffico a burst, il che è positivo. Ma senza controlli, la coda può crescere mentre i worker continuano a sprecare risorse di calcolo su chiamate che falliranno. I messaggi avvelenati rimangono attivi più a lungo di quanto dovrebbero. Le partizioni calde o la capacità downstream limitata creano problemi a cascata.

Il design più sicuro:

1. Rilevare il guasto transitorio
2. Ritardare il prossimo tentativo con exponential backoff
3. Interrompere le chiamate alla dipendenza quando viene raggiunta una soglia di guasto (circuito aperto)
4. Riprendere con cautela dopo un periodo di raffreddamento (sonda del circuito)
5. Spostare il lavoro irrecuperabile in dead-letter o in un percorso di quarantena

## Come Appare il Supporto Nativo

Il nuovo supporto si integra con il modello di host Azure Functions esistente — nessuna libreria aggiuntiva, nessuna implementazione personalizzata. La configurazione va nel tuo `host.json`:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

La configurazione del circuit breaker imposta la soglia di errore e l'intervallo di reset in modo che le dipendenze non sane non vengano bombardate durante il recupero.

## Linguaggi Coperti

Questo non è solo per .NET. La funzionalità copre dotnet, JavaScript, TypeScript e Python — il set completo di linguaggi supportati dal trigger Service Bus in Azure Functions.

## Conclusione

I pattern di retry non sono emozionanti da configurare fino alla prima volta che un'interruzione downstream fa sì che le tue Functions peggiorino il problema invece di degradarsi gradualmente. Configurarli in modo proattivo è economico. Adattarli durante un incidente non lo è.

Post originale: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
