---
title: "Alles-of-niets batchverwerking oplossen in Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions ondersteunt nu per-bericht afhandeling voor Service Bus-triggers, waarmee je elk bericht in een batch onafhankelijk kunt voltooien, opgeven, naar de dead-letter-wachtrij sturen of uitstellen."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[Per-bericht afhandeling voor Azure Service Bus in Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) lost het klassieke alles-of-niets batchfailure probleem op: als één bericht in een batch van 50 mislukt, worden alle 50 teruggestuurd naar de wachtrij.

## Het batchprobleem

In het oude model verwerkte Azure Functions berichten in batchmodus met een binaire uitkomst: de volledige batch slaagde of de volledige batch mislukte. Eén misvormd bericht betekende dat alle 49 gezonde berichten terugkeerden in de wachtrij, opnieuw werden verwerkt en opnieuw op idempotentie werden gecontroleerd — wat compute verspilde, kosten opdreef en retryloops creëerde die moeilijk te doorbreken waren.

## Vier per-bericht afhandelingsacties

Per-bericht afhandeling geeft je vier onafhankelijke acties op elk bericht:

- **Voltooien (Complete)** — verwijder het bericht uit de wachtrij (verwerking geslaagd)
- **Opgeven (Abandon)** — stuur terug voor opnieuw proberen, optioneel app-eigenschappen aanpassen (nuttig voor tijdelijke fouten)
- **Dead-letter** — verplaats naar de dead-letter-wachtrij (giftig bericht, niet te herstellen)
- **Uitstellen (Defer)** — bewaar het maar maak het alleen opvraagbaar via volgnummer

In een batch van 50 kun je nu 47 voltooien, 2 opgeven met tijdelijke fouten en 1 misvormd bericht naar dead-letter sturen — alles in één enkele functieaanroep.

## Codevoorbeelden

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

## Exponentiële backoff zonder extra infrastructuur

Het combineren van `abandon` met gewijzigde app-eigenschappen maakt exponentiële backoff direct op de wachtrij mogelijk — geen Durable Functions of extra wachtrijen nodig. Sla een retrycount op in de applicatie-eigenschappen van het bericht, lees deze bij herlevering en bereken je vertraging. Dit patroon vereiste vroeger aanzienlijke orkestratie; nu zijn het een paar regels in de retry-handler.

## Efficiëntiewinst door batching

Het oude pre-batchmodel stuurde elk bericht als een afzonderlijke functieaanroep: 50 berichten betekenden 50 verbindingen, 50 cold starts, 50 teardowns. Het nieuwe model verwerkt alle 50 in één aanroep, en per-bericht afhandeling betekent dat je die efficiëntie niet opgeeft bij fouten.

Lees het volledige bericht op [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
