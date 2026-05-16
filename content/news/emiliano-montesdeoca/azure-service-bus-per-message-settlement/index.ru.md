---
title: "Исправление пакетной обработки «всё или ничего» в Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions теперь поддерживает расчёт на уровне отдельных сообщений для триггеров Service Bus, позволяя независимо завершать, отклонять, отправлять в очередь недоставленных сообщений или откладывать каждое сообщение в пакете."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Этот пост был переведён автоматически. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

[Расчёт на уровне отдельных сообщений для Azure Service Bus в Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) решает классическую проблему сбоя пакета «всё или ничего»: если одно сообщение из пакета в 50 сообщений не обрабатывается, все 50 возвращаются в очередь.

## Проблема пакетной обработки

В старой модели Azure Functions обрабатывал сообщения в пакетном режиме с бинарным результатом: либо весь пакет успешно обрабатывался, либо весь пакет завершался сбоем. Одно некорректное сообщение означало, что все 49 исправных сообщений возвращались в очередь, повторно обрабатывались и снова проверялись на идемпотентность — впустую расходуя вычислительные ресурсы, увеличивая расходы и создавая циклы повторных попыток, из которых трудно было выйти.

## Четыре действия при расчёте на уровне сообщения

Расчёт на уровне сообщения даёт вам четыре независимых действия для каждого сообщения:

- **Завершить (Complete)** — удалить сообщение из очереди (обработка успешна)
- **Отклонить (Abandon)** — вернуть для повторной попытки, опционально изменив свойства приложения (полезно при временных ошибках)
- **Dead-letter** — переместить в очередь недоставленных сообщений (отравленное сообщение, невосстановимое)
- **Отложить (Defer)** — сохранить, но сделать доступным только по порядковому номеру

В пакете из 50 сообщений теперь можно завершить 47, отклонить 2 с временными ошибками и отправить 1 некорректное сообщение в dead-letter — всё в рамках одного вызова функции.

## Примеры кода

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

## Экспоненциальная задержка без дополнительной инфраструктуры

Сочетание `abandon` с изменёнными свойствами приложения позволяет реализовать экспоненциальную задержку прямо в очереди — без Durable Functions или дополнительных очередей. Сохраните счётчик повторных попыток в свойствах приложения сообщения, прочитайте его при повторной доставке и вычислите задержку. Раньше этот паттерн требовал значительной оркестровки; теперь это несколько строк в обработчике повторных попыток.

## Прирост эффективности пакетной обработки

Старая модель до пакетной обработки отправляла каждое сообщение как отдельный вызов функции: 50 сообщений означали 50 подключений, 50 холодных запусков, 50 завершений. Новая модель обрабатывает все 50 в одном вызове, а расчёт на уровне сообщения означает, что вы не теряете эту эффективность при возникновении ошибок.

Читайте полный пост на [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
