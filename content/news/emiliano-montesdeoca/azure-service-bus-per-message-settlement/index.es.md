---
title: "Solucionando el procesamiento por lotes todo-o-nada en Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions ahora admite la liquidación por mensaje para triggers de Service Bus, permitiéndote completar, abandonar, enviar a la cola de mensajes muertos o diferir cada mensaje de forma independiente en un lote."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[La liquidación por mensaje para Azure Service Bus en Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) resuelve el clásico problema de fallo de lotes todo-o-nada: si un mensaje en un lote de 50 falla, los 50 regresan a la cola.

## El problema del lote

En el modelo antiguo, Azure Functions procesaba mensajes en modo lote con un resultado binario: todo el lote tenía éxito o todo el lote fallaba. Un mensaje malformado significaba que los 49 mensajes sanos volvían a la cola, se reprocesaban y se volvía a verificar la idempotencia — desperdiciando cómputo, inflando costos y creando bucles de reintentos difíciles de escapar.

## Cuatro acciones de liquidación por mensaje

La liquidación por mensaje te da cuatro acciones independientes en cada mensaje:

- **Completar (Complete)** — eliminar el mensaje de la cola (procesamiento exitoso)
- **Abandonar (Abandon)** — devolverlo para reintento, opcionalmente modificando propiedades de la aplicación (útil para errores transitorios)
- **Mensaje muerto (Dead-letter)** — moverlo a la cola de mensajes muertos (mensaje envenenado, irrecuperable)
- **Diferir (Defer)** — conservarlo pero hacerlo recuperable solo por número de secuencia

En un lote de 50, ahora puedes completar 47, abandonar 2 con errores transitorios y enviar a la cola de muertos 1 mensaje malformado — todo en una sola invocación de función.

## Ejemplos de código

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

## Retroceso exponencial sin infraestructura adicional

Combinar `abandon` con propiedades de aplicación modificadas permite implementar retroceso exponencial directamente en la cola — sin Durable Functions ni colas adicionales. Almacena un contador de reintentos en las propiedades de la aplicación del mensaje, léelo en la reentrega y calcula el retraso. Este patrón antes requería una orquestración significativa; ahora son unas pocas líneas en el manejador de reintentos.

## Ganancias de eficiencia del lote

El modelo antiguo enviaba cada mensaje como una invocación de función separada: 50 mensajes significaban 50 conexiones, 50 arranques en frío, 50 desmontajes. El nuevo modelo maneja los 50 en una sola invocación, y la liquidación por mensaje significa que no se pierde esa eficiencia cuando ocurren errores.

Lee el post completo en [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
