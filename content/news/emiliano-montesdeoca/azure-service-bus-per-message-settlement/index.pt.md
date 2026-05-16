---
title: "Corrigindo o processamento em lote tudo-ou-nada no Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "O Azure Functions agora suporta liquidação por mensagem para triggers do Service Bus, permitindo completar, abandonar, enviar para a fila de mensagens mortas ou adiar cada mensagem de forma independente em um lote."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[A liquidação por mensagem para Azure Service Bus no Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) resolve o clássico problema de falha de lote tudo-ou-nada: se uma mensagem em um lote de 50 falhar, todas as 50 retornam para a fila.

## O problema do lote

No modelo antigo, o Azure Functions processava mensagens em modo lote com um resultado binário: o lote inteiro era bem-sucedido ou o lote inteiro falhava. Uma mensagem malformada significava que todas as 49 mensagens saudáveis voltavam para a fila, eram reprocessadas e tinham a idempotência verificada novamente — desperdiçando computação, inflando custos e criando loops de repetição difíceis de sair.

## Quatro ações de liquidação por mensagem

A liquidação por mensagem oferece quatro ações independentes em cada mensagem:

- **Completar (Complete)** — remover a mensagem da fila (processamento bem-sucedido)
- **Abandonar (Abandon)** — devolver para nova tentativa, opcionalmente modificando propriedades do aplicativo (útil para erros transitórios)
- **Dead-letter** — mover para a fila de mensagens mortas (mensagem envenenada, irrecuperável)
- **Adiar (Defer)** — manter mas tornar recuperável apenas por número de sequência

Em um lote de 50, agora você pode completar 47, abandonar 2 com erros transitórios e enviar para dead-letter 1 mensagem malformada — tudo em uma única invocação de função.

## Exemplos de código

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

## Backoff exponencial sem infraestrutura adicional

Combinar `abandon` com propriedades de aplicativo modificadas permite backoff exponencial diretamente na fila — sem Durable Functions ou filas adicionais. Armazene um contador de tentativas nas propriedades do aplicativo da mensagem, leia-o na reentrega e calcule o atraso. Este padrão costumava exigir orquestração significativa; agora são algumas linhas no handler de novas tentativas.

## Ganhos de eficiência do lote

O antigo modelo pré-lote enviava cada mensagem como uma invocação de função separada: 50 mensagens significavam 50 conexões, 50 cold starts, 50 teardowns. O novo modelo lida com todos os 50 em uma única invocação, e a liquidação por mensagem significa que você não sacrifica essa eficiência quando ocorrem erros.

Leia o post completo em [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
