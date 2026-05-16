---
title: "修复 Azure Service Bus 中的全有或全无批量处理问题"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions 现在支持 Service Bus 触发器的按消息结算，让您可以在批处理中独立地完成、放弃、转入死信队列或推迟每条消息。"
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[Azure Functions 中 Azure Service Bus 的按消息结算](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/)解决了经典的全有或全无批量失败问题：如果 50 条消息的批次中有一条失败，所有 50 条消息都会返回队列。

## 批量处理问题

在旧模型中，Azure Functions 以批处理模式处理消息，结果是二选一的：整个批次成功或整个批次失败。一条格式错误的消息意味着所有 49 条正常消息都会重新入队、重新处理并重新检查幂等性——浪费计算资源、推高成本，并产生难以逃脱的重试循环。

## 四种按消息结算操作

按消息结算为每条消息提供四种独立操作：

- **完成 (Complete)** — 从队列中移除消息（处理成功）
- **放弃 (Abandon)** — 返回以重试，可选择修改应用属性（对临时错误很有用）
- **死信 (Dead-letter)** — 移至死信队列（有毒消息，无法恢复）
- **推迟 (Defer)** — 保留消息但仅允许通过序列号检索

在 50 条消息的批次中，现在可以完成 47 条、放弃 2 条临时错误消息，并对 1 条格式错误消息执行死信操作——全部在单次函数调用中完成。

## 代码示例

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

## 无需额外基础设施的指数退避

将 `abandon` 与修改后的应用属性结合使用，可直接在队列上实现指数退避——无需 Durable Functions 或额外队列。在消息的应用属性中存储重试计数，在重新投递时读取并计算延迟。此模式以前需要大量编排工作；现在只需在重试处理程序中添加几行代码。

## 批处理效率提升

旧的预批处理模型将每条消息作为单独的函数调用发送：50 条消息意味着 50 个连接、50 次冷启动、50 次销毁。新模型在一次调用中处理全部 50 条，而按消息结算意味着在发生错误时不会丢失这种效率。

在 [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) 阅读完整文章。
