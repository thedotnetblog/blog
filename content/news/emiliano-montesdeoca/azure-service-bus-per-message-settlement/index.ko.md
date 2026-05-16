---
title: "Azure Service Bus의 전부 또는 전무 배치 처리 문제 해결"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions가 이제 Service Bus 트리거에 대한 메시지별 결제를 지원하여 배치에서 각 메시지를 독립적으로 완료, 포기, 데드레터 또는 연기할 수 있습니다."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[Azure Functions의 Azure Service Bus 메시지별 결제](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/)는 고전적인 전부 또는 전무 배치 실패 문제를 해결합니다: 50개 배치 중 하나의 메시지가 실패하면 50개 모두 큐로 반환됩니다.

## 배치 문제

이전 모델에서 Azure Functions는 이진 결과로 배치 모드에서 메시지를 처리했습니다: 전체 배치가 성공하거나 전체 배치가 실패했습니다. 하나의 잘못된 형식 메시지는 49개의 정상 메시지가 모두 다시 큐에 들어가고, 재처리되고, 멱등성을 재확인해야 함을 의미했습니다 — 컴퓨팅을 낭비하고, 비용을 높이고, 탈출하기 어려운 재시도 루프를 만들었습니다.

## 네 가지 메시지별 결제 작업

메시지별 결제는 각 메시지에 대한 네 가지 독립적인 작업을 제공합니다:

- **완료 (Complete)** — 큐에서 메시지 제거 (처리 성공)
- **포기 (Abandon)** — 재시도를 위해 반환, 선택적으로 앱 속성 수정 (일시적 오류에 유용)
- **데드레터 (Dead-letter)** — 데드레터 큐로 이동 (독성 메시지, 복구 불가)
- **연기 (Defer)** — 보관하되 시퀀스 번호로만 검색 가능하게 설정

50개 배치에서 이제 47개를 완료하고, 일시적 오류로 2개를 포기하고, 잘못된 형식 메시지 1개를 데드레터로 보낼 수 있습니다 — 모두 단일 함수 호출로.

## 코드 예시

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

## 추가 인프라 없는 지수 백오프

`abandon`을 수정된 앱 속성과 결합하면 추가 큐나 Durable Functions 없이 큐에서 직접 지수 백오프를 구현할 수 있습니다. 메시지의 애플리케이션 속성에 재시도 횟수를 저장하고, 재전달 시 읽어서 지연 시간을 계산합니다. 이 패턴은 이전에 상당한 오케스트레이션이 필요했습니다; 이제는 재시도 핸들러에 몇 줄이면 됩니다.

## 배치 효율성 향상

이전 사전 배치 모델은 각 메시지를 별도의 함수 호출로 전송했습니다: 50개 메시지는 50개의 연결, 50번의 콜드 스타트, 50번의 해제를 의미했습니다. 새 모델은 단일 호출로 50개를 모두 처리하며, 메시지별 결제는 오류 발생 시에도 그 효율성을 잃지 않음을 의미합니다.

전체 게시물은 [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/)에서 읽어보세요.
