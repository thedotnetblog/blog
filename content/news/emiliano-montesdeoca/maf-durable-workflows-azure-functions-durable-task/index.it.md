---
title: "Workflow Durevoli in Microsoft Agent Framework: Da In-Memory ad Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "Il modello di programmazione del workflow di MAF ora supporta l'esecuzione durevole basata su Durable Task — ecco come costruire workflow di agenti componibili che sopravvivono ai riavvii del processo e scalano su Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Uno dei punti dolenti dei primi workflow di agenti IA: sono fragili. Un workflow multi-step a lunga esecuzione legato a un singolo processo significa che il riavvio del processo = stato perso. Per demo semplici va bene. Per carichi di lavoro in produzione non lo è.

Il modello di programmazione del workflow di Microsoft Agent Framework ora supporta l'**esecuzione durevole**, basata sul framework Durable Task, con hosting Azure Functions. Ecco come funziona il modello di programmazione e perché la storia della durabilità conta.

## I Blocchi Fondamentali

Gli **Executor** sono l'unità fondamentale di lavoro. Ognuno è tipizzato — prende un input specifico e produce un output specifico:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // cercare l'ordine, restituirlo
        return new Order(Id: message.OrderId, ...);
    }
}
```

I **Workflow** collegano gli executor in grafi diretti usando un builder fluente. Il framework gestisce l'esecuzione, il flusso di dati tra i passi e la propagazione degli errori.

Puoi modellare:
- Catene sequenziali (passo A → passo B → passo C)
- Fan-out/fan-in parallelo (eseguire gli agenti A, B, C in parallelo, aggregare i risultati)
- Ramificazione condizionale
- Approvazioni umano-nel-ciclo (mettere in pausa il workflow, attendere un segnale esterno)

## Il Runner In-Memory per lo Sviluppo Locale

Iniziare è veloce:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Il pacchetto principale include un runner leggero in-process. Nessuna dipendenza esterna, nessun database, nessuna risorsa Azure. Funziona benissimo per lo sviluppo locale e i test unitari.

## Aggiungere Durabilità con Durable Task

Quando un workflow deve sopravvivere ai riavvii del processo — perché è a lunga esecuzione, perché ha passi umano-nel-ciclo, perché si distribuisce su molte chiamate di agenti in parallelo — il runner in-memory non è sufficiente.

L'integrazione Durable Task di MAF memorizza lo stato del workflow in Azure Storage. Se il processo si riavvia, il workflow riprende da dove si era fermato. Il modello di programmazione rimane lo stesso; basta sostituire il runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Gli stessi executor, lo stesso grafo del workflow — basato su stato durevole.

## Hosting Azure Functions

Il terzo livello è l'hosting Azure Functions. Il tuo workflow diventa un'app Function: attiva il workflow tramite un endpoint HTTP, e il runtime durevole gestisce scalabilità, stato e affidabilità.

Ciò significa che un workflow multi-agente con chiamate parallele, rami condizionali e approvazioni umane può scalare in un ambiente Functions serverless senza gestione dello stato personalizzata.

## Perché Questo È Importante

La combinazione è significativa per i veri sistemi IA:

- **Chiamate di agenti in parallelo** — distribuire a più agenti specializzati simultaneamente senza blocchi, aggregare i risultati quando tutti completano
- **Processi a lunga esecuzione** — i workflow che coinvolgono approvazione umana o eventi esterni possono mettere in pausa e riprendere per ore o giorni
- **Scalabilità** — Azure Functions scala l'esecuzione orizzontalmente; il framework Durable Task gestisce il coordinamento dello stato parallelo

Se stai costruendo workflow MAF oltre semplici demo locali, questo è il percorso verso l'esecuzione di qualità produzione.

Post originale: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
