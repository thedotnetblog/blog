---
title: "Risolvere l'elaborazione batch tutto-o-niente in Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions ora supporta il settlement per messaggio per i trigger Service Bus, permettendoti di completare, abbandonare, inviare al dead-letter o differire ogni messaggio in modo indipendente in un batch."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Il settlement per messaggio per Azure Service Bus in Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) risolve il classico problema di fallimento del batch tutto-o-niente: se un messaggio su 50 fallisce, tutti e 50 tornano in coda.

## Il problema del batch

Nel vecchio modello, Azure Functions elaborava i messaggi in modalità batch con un risultato binario: o l'intero batch aveva successo o l'intero batch falliva. Un messaggio malformato significava che tutti i 49 messaggi sani tornavano in coda, venivano rielaborati e ricontrollati per l'idempotenza — sprecando risorse di calcolo, gonfiando i costi e creando loop di retry difficili da interrompere.

## Quattro azioni di settlement per messaggio

Il settlement per messaggio ti offre quattro azioni indipendenti su ogni messaggio:

- **Completare (Complete)** — rimuovere il messaggio dalla coda (elaborazione riuscita)
- **Abbandonare (Abandon)** — restituirlo per un nuovo tentativo, modificando opzionalmente le proprietà dell'applicazione (utile per errori transitori)
- **Dead-letter** — spostarlo nella coda dead-letter (messaggio velenoso, irrecuperabile)
- **Differire (Defer)** — conservarlo ma renderlo recuperabile solo tramite numero di sequenza

In un batch di 50, puoi ora completare 47, abbandonare 2 con errori transitori e inviare al dead-letter 1 messaggio malformato — tutto in una singola invocazione di funzione.

## Esempi di codice

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

## Backoff esponenziale senza infrastruttura aggiuntiva

Combinare `abandon` con proprietà di applicazione modificate consente il backoff esponenziale direttamente sulla coda — senza Durable Functions o code aggiuntive. Memorizza un contatore di tentativi nelle proprietà di applicazione del messaggio, leggilo alla riconsegna e calcola il ritardo. Questo pattern richiedeva in precedenza un'orchestrazione significativa; ora sono poche righe nel gestore dei retry.

## Guadagni di efficienza del batch

Il vecchio modello pre-batch inviava ogni messaggio come invocazione di funzione separata: 50 messaggi significavano 50 connessioni, 50 cold start, 50 teardown. Il nuovo modello gestisce tutti i 50 in una sola invocazione, e il settlement per messaggio significa che non si perde quell'efficienza quando si verificano errori.

Leggi il post completo su [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
