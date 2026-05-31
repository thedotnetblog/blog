---
title: "Flux de Treball Duradors en Microsoft Agent Framework: De In-Memory a Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "El model de programació de flux de treball de MAF ara suporta l'execució duradora respaldada per Durable Task — aquí es mostra com construir fluxos de treball d'agents composables que sobreviuen a reinicis de processos i escalen a Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Un dels punts dolorosos dels primers fluxos de treball d'agents d'IA: són fràgils. Un flux de treball de múltiples passos de llarga durada vinculat a un únic procés significa que el reinici del procés = estat perdut. Per a demostracions simples és correcte. Per a càrregues de treball en producció no ho és.

El model de programació de fluxos de treball de Microsoft Agent Framework ara suporta l'**execució duradora**, respaldada pel framework Durable Task, amb allotjament a Azure Functions. Aquí s'explica com funciona el model de programació i per qué importa la història de la durabilitat.

## Els Blocs de Construcció Bàsics

Els **Executor** són la unitat fonamental de treball. Cada un té tipus — pren una entrada específica i produeix una sortida específica:

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
        // cercar la comanda, retornar-la
        return new Order(Id: message.OrderId, ...);
    }
}
```

Els **Workflow** connecten executors en grafs dirigits usant un constructor fluent. El framework gestiona l'execució, el flux de dades entre passos i la propagació d'errors.

Podeu modelar:
- Cadenes seqüencials (pas A → pas B → pas C)
- Fan-out/fan-in paral·lel (executar agents A, B, C en paral·lel, agregar resultats)
- Ramificació condicional
- Aprovacions de persona en el bucle (pausar flux de treball, esperar senyal extern)

## El Runner In-Memory per al Desenvolupament Local

Començar és ràpid:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

El paquet principal inclou un runner lleuger en procés. Sense dependències externes, sense base de dades, sense recursos Azure. Funciona perfectament per al desenvolupament local i les proves unitàries.

## Afegir Durabilitat amb Durable Task

Quan un flux de treball necessita sobreviure a reinicis de procés — perquè és de llarga durada, perquè té passos de persona en el bucle, perquè es distribueix en moltes crides d'agent en paral·lel — el runner in-memory no és suficient.

La integració de Durable Task de MAF emmagatzema l'estat del flux de treball a Azure Storage. Si el procés es reinicia, el flux de treball reprèn des d'on va quedar. El model de programació roman igual; simplement canvieu el runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Els mateixos executors, el mateix graf de flux de treball — respaldats per estat durador.

## Allotjament a Azure Functions

La tercera capa és l'allotjament a Azure Functions. El vostre flux de treball es converteix en una aplicació Function: activeu el flux de treball via un endpoint HTTP, i el runtime durador gestiona l'escalat, l'estat i la fiabilitat.

Això significa que un flux de treball multi-agent amb crides paral·leles, branques condicionals i aprovacions humanes pot escalar en un entorn Functions sense servidor sense gestió d'estat personalitzada.

## Per Qué Importa Això

La combinació és significant per als sistemes d'IA reals:

- **Crides d'agent en paral·lel** — distribuir a múltiples agents especialitzats simultàniament sense blocatge, agregar resultats quan tots completin
- **Processos de llarga durada** — els fluxos de treball que impliquen aprovació humana o esdeveniments externs poden pausar i reprendre durant hores o dies
- **Escalat** — Azure Functions escala l'execució horitzontalment; el framework Durable Task gestiona la coordinació de l'estat paral·lel

Si esteu construint fluxos de treball MAF més enllà de demostracions locals simples, aquest és el camí cap a l'execució de qualitat producció.

Publicació original: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
