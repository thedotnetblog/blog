---
title: "All-oder-Nichts-Batchverarbeitung in Azure Service Bus beheben"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions unterstützt jetzt die nachrichtenweise Abwicklung für Service Bus-Trigger und ermöglicht es, jede Nachricht in einem Batch unabhängig abzuschließen, aufzugeben, in die Dead-Letter-Queue zu verschieben oder zurückzustellen."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Die nachrichtenweise Abwicklung für Azure Service Bus in Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) löst das klassische All-oder-Nichts-Batch-Fehlerproblem: Schlägt eine Nachricht in einem Batch von 50 fehl, werden alle 50 in die Queue zurückgelegt.

## Das Batch-Problem

Im alten Modell verarbeitete Azure Functions Nachrichten im Batch-Modus mit einem binären Ergebnis: Entweder der gesamte Batch war erfolgreich oder der gesamte Batch schlug fehl. Eine fehlerhafte Nachricht bedeutete, dass alle 49 gesunden Nachrichten wieder in die Queue gestellt, erneut verarbeitet und erneut auf Idempotenz geprüft wurden — Rechenleistung verschwendend, Kosten erhöhend und Wiederholungsschleifen erzeugend, aus denen man kaum entkam.

## Vier nachrichtenweise Abwicklungsaktionen

Die nachrichtenweise Abwicklung bietet vier unabhängige Aktionen pro Nachricht:

- **Abschließen (Complete)** — Nachricht aus der Queue entfernen (Verarbeitung erfolgreich)
- **Aufgeben (Abandon)** — zur Wiederholung zurückgeben, optional mit geänderten App-Eigenschaften (nützlich bei vorübergehenden Fehlern)
- **Dead-Letter** — in die Dead-Letter-Queue verschieben (vergiftete Nachricht, nicht wiederherstellbar)
- **Zurückstellen (Defer)** — behalten, aber nur über die Sequenznummer abrufbar machen

In einem Batch von 50 können jetzt 47 abgeschlossen, 2 mit vorübergehenden Fehlern aufgegeben und 1 fehlerhafte Nachricht in die Dead-Letter-Queue verschoben werden — alles in einer einzigen Funktionsaufruf.

## Code-Beispiele

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

## Exponentielles Backoff ohne zusätzliche Infrastruktur

Die Kombination von `abandon` mit geänderten App-Eigenschaften ermöglicht exponentielles Backoff direkt auf der Queue — ohne Durable Functions oder zusätzliche Queues. Speichere einen Wiederholungszähler in den Anwendungseigenschaften der Nachricht, lies ihn bei der erneuten Zustellung und berechne die Verzögerung. Dieses Muster erforderte früher erheblichen Orchestrierungsaufwand; jetzt sind es ein paar Zeilen im Wiederholungs-Handler.

## Effizienzgewinne durch Batching

Das alte Modell sendete jede Nachricht als separate Funktionsaufruf: 50 Nachrichten bedeuteten 50 Verbindungen, 50 Cold Starts, 50 Teardowns. Das neue Modell verarbeitet alle 50 in einem Aufruf, und die nachrichtenweise Abwicklung bedeutet, dass diese Effizienz bei Fehlern nicht verloren geht.

Den vollständigen Beitrag lesen auf [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
