---
title: "Fixing All-or-Nothing Batch Processing in Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions now supports per-message settlement for Service Bus triggers, letting you complete, abandon, dead-letter, or defer each message independently in a batch."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

[Per-message settlement for Azure Service Bus in Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) solves the classic all-or-nothing batch failure problem: if one message in a batch of 50 fails, all 50 get returned to the queue.

## The batch problem

In the old model, Azure Functions processed messages in batch mode with a binary outcome: the entire batch succeeded or the entire batch failed. One malformed message meant all 49 healthy messages got re-queued, re-processed, and re-checked for idempotency — wasting compute, inflating costs, and creating retry loops that were hard to escape.

## Four per-message settlement actions

Per-message settlement gives you four independent actions on each message:

- **Complete** — remove the message from the queue (processing succeeded)
- **Abandon** — return it for retry, optionally modifying app properties (useful for transient errors)
- **Dead-letter** — move it to the dead-letter queue (poison message, unrecoverable)
- **Defer** — keep it but make it only retrievable by sequence number

In a batch of 50, you can now complete 47, abandon 2 with transient errors, and dead-letter 1 malformed message — all in a single function invocation.

## Code examples

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

## Exponential backoff without extra infrastructure

Combining `abandon` with modified app properties enables exponential backoff directly on the queue — no Durable Functions, no extra queues. Store a retry count in the message's application properties, read it on redelivery, and calculate your delay. This pattern used to require significant orchestration; now it's a few lines in the retry handler.

## Batch efficiency gains

The old pre-batch model sent each message as a separate function invocation: 50 messages meant 50 connections, 50 cold starts, 50 teardowns. The new model handles all 50 in one invocation, and per-message settlement means you're not forfeiting that efficiency when errors occur.

Read the full post at [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
