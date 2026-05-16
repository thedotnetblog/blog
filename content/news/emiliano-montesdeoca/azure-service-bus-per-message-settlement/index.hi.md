---
title: "Azure Service Bus में ऑल-ऑर-नथिंग बैच प्रोसेसिंग को ठीक करना"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions अब Service Bus ट्रिगर्स के लिए प्रति-संदेश सेटलमेंट का समर्थन करता है, जिससे आप एक बैच में प्रत्येक संदेश को स्वतंत्र रूप से पूर्ण, छोड़, dead-letter या defer कर सकते हैं।"
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[Azure Functions में Azure Service Bus के लिए प्रति-संदेश सेटलमेंट](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) क्लासिक ऑल-ऑर-नथिंग बैच विफलता समस्या को हल करता है: यदि 50 के एक बैच में एक संदेश विफल होता है, तो सभी 50 कतार में वापस आ जाते हैं।

## बैच की समस्या

पुराने मॉडल में, Azure Functions बैच मोड में संदेशों को बाइनरी परिणाम के साथ प्रोसेस करता था: या तो पूरा बैच सफल होता था या पूरा बैच विफल होता था। एक खराब संदेश का मतलब था कि सभी 49 स्वस्थ संदेश फिर से कतार में डाले जाते, फिर से प्रोसेस होते और idempotency के लिए फिर से जांचे जाते — कंप्यूट बर्बाद करते, लागत बढ़ाते और retry loops बनाते जिनसे निकलना मुश्किल था।

## चार प्रति-संदेश सेटलमेंट क्रियाएं

प्रति-संदेश सेटलमेंट आपको प्रत्येक संदेश पर चार स्वतंत्र क्रियाएं देता है:

- **पूर्ण (Complete)** — संदेश को कतार से हटाएं (प्रोसेसिंग सफल रही)
- **छोड़ें (Abandon)** — retry के लिए वापस करें, वैकल्पिक रूप से app properties संशोधित करते हुए (क्षणिक त्रुटियों के लिए उपयोगी)
- **Dead-letter** — dead-letter कतार में ले जाएं (जहरीला संदेश, अपुनर्प्राप्य)
- **Defer** — इसे रखें लेकिन इसे केवल sequence number द्वारा पुनर्प्राप्त करने योग्य बनाएं

50 के एक बैच में, आप अब 47 को पूर्ण कर सकते हैं, क्षणिक त्रुटियों के साथ 2 को छोड़ सकते हैं, और 1 खराब संदेश को dead-letter कर सकते हैं — सब एक ही function invocation में।

## कोड उदाहरण

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

## अतिरिक्त इन्फ्रास्ट्रक्चर के बिना एक्सपोनेंशियल बैकऑफ

`abandon` को संशोधित app properties के साथ मिलाने से कतार पर सीधे एक्सपोनेंशियल बैकऑफ संभव होता है — बिना Durable Functions या अतिरिक्त कतारों के। संदेश के application properties में retry count स्टोर करें, redelivery पर इसे पढ़ें और अपनी देरी की गणना करें। इस pattern को पहले महत्वपूर्ण orchestration की आवश्यकता थी; अब यह retry handler में कुछ पंक्तियां है।

## बैच दक्षता लाभ

पुराने pre-batch मॉडल ने प्रत्येक संदेश को एक अलग function invocation के रूप में भेजा: 50 संदेशों का मतलब था 50 connections, 50 cold starts, 50 teardowns। नया मॉडल एक invocation में सभी 50 को संभालता है, और प्रति-संदेश सेटलमेंट का मतलब है कि त्रुटियां होने पर आप वह दक्षता नहीं खोते।

पूरी पोस्ट पढ़ें [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) पर।
