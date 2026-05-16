---
title: "Naprawianie przetwarzania wsadowego „wszystko albo nic" w Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions obsługuje teraz rozliczanie wiadomość po wiadomości dla wyzwalaczy Service Bus, umożliwiając niezależne ukończenie, porzucenie, wysłanie do kolejki utraconych wiadomości lub odroczenie każdej wiadomości w partii."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Rozliczanie wiadomość po wiadomości dla Azure Service Bus w Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) rozwiązuje klasyczny problem awarii całej partii: jeśli jedna wiadomość w partii 50 nie powiedzie się, wszystkie 50 wraca do kolejki.

## Problem z partią

W starym modelu Azure Functions przetwarzał wiadomości w trybie wsadowym z wynikiem binarnym: cała partia kończyła się sukcesem lub cała partia nie powiodła się. Jedna zniekształcona wiadomość oznaczała, że wszystkie 49 zdrowych wiadomości wracało do kolejki, było ponownie przetwarzanych i sprawdzanych pod kątem idempotentności — marnując zasoby obliczeniowe, zwiększając koszty i tworząc pętle ponownych prób, z których trudno było wyjść.

## Cztery akcje rozliczania wiadomość po wiadomości

Rozliczanie wiadomość po wiadomości daje cztery niezależne akcje dla każdej wiadomości:

- **Ukończ (Complete)** — usuń wiadomość z kolejki (przetwarzanie zakończone sukcesem)
- **Porzuć (Abandon)** — zwróć do ponownej próby, opcjonalnie modyfikując właściwości aplikacji (przydatne dla błędów przejściowych)
- **Dead-letter** — przenieś do kolejki utraconych wiadomości (zatruta wiadomość, nie do odzyskania)
- **Odrocz (Defer)** — zachowaj, ale udostępnij tylko przez numer sekwencji

W partii 50 możesz teraz ukończyć 47, porzucić 2 z błędami przejściowymi i wysłać 1 zniekształconą wiadomość do dead-letter — wszystko w jednym wywołaniu funkcji.

## Przykłady kodu

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

## Wykładnicze wycofanie bez dodatkowej infrastruktury

Łączenie `abandon` ze zmodyfikowanymi właściwościami aplikacji umożliwia wykładnicze wycofanie bezpośrednio w kolejce — bez Durable Functions ani dodatkowych kolejek. Przechowaj licznik prób w właściwościach aplikacji wiadomości, odczytaj go przy ponownym dostarczeniu i oblicz opóźnienie. Ten wzorzec wymagał wcześniej znacznej orkiestracji; teraz to kilka linii w obsłudze ponownych prób.

## Wzrost wydajności przy przetwarzaniu wsadowym

Stary model pre-wsadowy wysyłał każdą wiadomość jako osobne wywołanie funkcji: 50 wiadomości oznaczało 50 połączeń, 50 zimnych startów, 50 zakończeń. Nowy model obsługuje wszystkie 50 w jednym wywołaniu, a rozliczanie wiadomość po wiadomości oznacza, że nie tracisz tej wydajności, gdy wystąpią błędy.

Przeczytaj pełny wpis na [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
