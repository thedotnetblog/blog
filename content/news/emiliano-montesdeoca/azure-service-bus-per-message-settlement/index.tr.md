---
title: "Azure Service Bus'ta Toplu İşlemedeki Hepsini-veya-Hiçbirini Sorununu Çözme"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions artık Service Bus tetikleyicileri için mesaj başına uzlaşmayı destekliyor; bir toplu işlemdeki her mesajı bağımsız olarak tamamlayabilir, bırakabilir, sahipsiz mesaj kuyruğuna gönderebilir veya erteleyebilirsiniz."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[Azure Functions'ta Azure Service Bus için mesaj başına uzlaşma](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/), klasik hepsini-veya-hiçbirini toplu işleme hatası sorununu çözüyor: 50 mesajlık bir toplu işlemde bir mesaj başarısız olursa, tüm 50 mesaj kuyruğa geri dönüyor.

## Toplu işleme sorunu

Eski modelde Azure Functions, mesajları toplu işleme modunda ikili sonuçla işliyordu: tüm toplu işlem başarılı oluyordu ya da tüm toplu işlem başarısız oluyordu. Hatalı biçimlendirilmiş tek bir mesaj, 49 sağlıklı mesajın hepsinin kuyruğa geri dönmesi, yeniden işlenmesi ve idempotentlik açısından yeniden kontrol edilmesi anlamına geliyordu — hesaplama kaynakları boşa gidiyor, maliyetler artıyor ve çıkması zor yeniden deneme döngüleri oluşuyordu.

## Dört mesaj başına uzlaşma eylemi

Mesaj başına uzlaşma, her mesaj için dört bağımsız eylem sunar:

- **Tamamla (Complete)** — mesajı kuyruktan kaldır (işleme başarılı)
- **Bırak (Abandon)** — yeniden deneme için geri gönder, isteğe bağlı olarak uygulama özelliklerini değiştirerek (geçici hatalar için yararlı)
- **Sahipsiz mesaj (Dead-letter)** — sahipsiz mesaj kuyruğuna taşı (zehirli mesaj, kurtarılamaz)
- **Ertele (Defer)** — sakla ancak yalnızca sıra numarasıyla alınabilir hale getir

50 mesajlık bir toplu işlemde artık 47'sini tamamlayabilir, 2'sini geçici hatalarla bırakabilir ve 1 hatalı biçimlendirilmiş mesajı sahipsiz mesaj kuyruğuna gönderebilirsiniz — hepsi tek bir işlev çağrısında.

## Kod örnekleri

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

## Ek altyapı olmadan üstel geri çekilme

`abandon`'ı değiştirilmiş uygulama özellikleriyle birleştirmek, Durable Functions veya ek kuyruklar olmadan doğrudan kuyruk üzerinde üstel geri çekilmeyi mümkün kılar. Mesajın uygulama özelliklerinde yeniden deneme sayacını saklayın, yeniden teslimde okuyun ve gecikmenizi hesaplayın. Bu kalıp eskiden önemli miktarda düzenleme gerektiriyordu; artık yeniden deneme işleyicisinde birkaç satır kod.

## Toplu işleme verimliliği kazanımları

Eski ön-toplu işleme modeli her mesajı ayrı bir işlev çağrısı olarak gönderiyordu: 50 mesaj, 50 bağlantı, 50 soğuk başlatma ve 50 sonlandırma anlamına geliyordu. Yeni model tüm 50'yi tek bir çağrıda işler ve mesaj başına uzlaşma, hatalar meydana geldiğinde bu verimliliği feda etmediğiniz anlamına gelir.

Tam gönderiyi [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) adresinde okuyun.
