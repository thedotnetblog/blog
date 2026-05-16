---
title: "Solucionant el processament per lots tot-o-res a Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions ja admet la liquidació per missatge per als activadors de Service Bus, permetent-te completar, abandonar, enviar a la cua de missatges morts o diferir cada missatge de forma independent dins d'un lot."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[La liquidació per missatge per a Azure Service Bus a Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) resol el problema clàssic de fallada de lots tot-o-res: si un missatge en un lot de 50 falla, els 50 tornen a la cua.

## El problema del lot

En el model antic, Azure Functions processava els missatges en mode lot amb un resultat binari: tot el lot tenia èxit o tot el lot fallava. Un missatge mal format significava que els 49 missatges sans tornaven a la cua, es tornaven a processar i es tornava a verificar la idempotència — malbaratant còmput, inflant costos i creant bucles de reintent difícils d'escapar.

## Quatre accions de liquidació per missatge

La liquidació per missatge t'ofereix quatre accions independents per a cada missatge:

- **Completar (Complete)** — eliminar el missatge de la cua (processament reeixit)
- **Abandonar (Abandon)** — retornar-lo per a reintent, opcionalment modificant propietats de l'aplicació (útil per a errors transitoris)
- **Missatge mort (Dead-letter)** — moure'l a la cua de missatges morts (missatge verinós, irrecuperable)
- **Diferir (Defer)** — conservar-lo però fer-lo recuperable només pel número de seqüència

En un lot de 50, ara pots completar 47, abandonar 2 amb errors transitoris i enviar a la cua de morts 1 missatge mal format — tot en una sola invocació de funció.

## Exemples de codi

**.NET (C#):**
```csharp
[Function("ProcessOrderBatch")]
public async Task Run(
    [ServiceBusTrigger("orders-queue", IsBatched = true)] ServiceBusReceivedMessage[] messages,
    ServiceBusMessageActions messageActions)
{
    foreach (var message in messages)
    {
        try {
            await messageActions.CompleteMessageAsync(message);
        } catch {
            await messageActions.DeadLetterMessageAsync(message);
        }
    }
}
```

**Node.js/TypeScript:**
```typescript
import '@azure/functions-extensions-servicebus';
export async function processOrderBatch(sbContext, context) {
    const { messages, actions } = sbContext;
    for (const message of messages) {
        try {
            await processOrder(messageBodyAsJson(message));
            await actions.complete(message);
        } catch {
            await actions.deadletter(message);
        }
    }
}
app.serviceBusQueue('processOrderBatch', {
    sdkBinding: true,
    autoCompleteMessages: false,
    cardinality: 'many',
    handler: processOrderBatch
});
```

**Python V2:**
```python
@app.service_bus_queue_trigger(auto_complete_messages=False, cardinality="many")
def process_order_batch(messages, message_actions):
    for message in messages:
        try:
            process_order(json.loads(message.body))
            message_actions.complete(message)
        except:
            message_actions.deadletter(message)
```

## Retirada exponencial sense infraestructura addicional

Combinar `abandon` amb propietats d'aplicació modificades permet implementar retirada exponencial directament a la cua — sense Durable Functions ni cues addicionals. Emmagatzema un comptador de reintents a les propietats de l'aplicació del missatge, llegeix-lo en el lliurament nou i calcula el retard. Aquest patró abans requeria una orquestració significativa; ara és unes poques línies al gestor de reintents.

## Guanys d'eficiència del lot

El model antic enviava cada missatge com una invocació de funció separada: 50 missatges significaven 50 connexions, 50 arrencades en fred, 50 tancaments. El nou model gestiona els 50 en una sola invocació, i la liquidació per missatge significa que no perds aquesta eficiència quan es produeixen errors.

Llegeix la publicació completa a [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
