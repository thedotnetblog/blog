---
title: "إصلاح معالجة الدُفعات الكاملة أو لا شيء في Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "يدعم Azure Functions الآن التسوية لكل رسالة على حدة في مشغّلات Service Bus، مما يتيح لك إكمال كل رسالة أو التخلي عنها أو إرسالها إلى قائمة الرسائل الميتة أو تأجيلها باستقلالية تامة ضمن الدفعة."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[التسوية لكل رسالة في Azure Service Bus ضمن Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) تحلّ مشكلة فشل الدفعات الكلي الكلاسيكية: إذا فشلت رسالة واحدة في دفعة من 50 رسالة، تُعاد جميع الـ 50 إلى قائمة الانتظار.

## مشكلة الدفعة

في النموذج القديم، كانت Azure Functions تعالج الرسائل في وضع الدفعة بنتيجة ثنائية: إما تنجح الدفعة بأكملها أو تفشل بأكملها. رسالة واحدة مشوّهة كانت تعني إعادة جميع الرسائل الـ 49 السليمة إلى القائمة، وإعادة معالجتها، والتحقق من الـ idempotency مجدداً — مما يُهدر الحوسبة ويرفع التكاليف ويخلق حلقات إعادة محاولة يصعب الخروج منها.

## أربع إجراءات للتسوية لكل رسالة

تمنحك التسوية لكل رسالة أربعة إجراءات مستقلة على كل رسالة:

- **إكمال (Complete)** — حذف الرسالة من القائمة (نجحت المعالجة)
- **تخلٍّ (Abandon)** — إعادتها لإعادة المحاولة مع إمكانية تعديل خصائص التطبيق (مفيد للأخطاء المؤقتة)
- **قائمة الرسائل الميتة (Dead-letter)** — نقلها إلى قائمة الرسائل الميتة (رسالة سامة غير قابلة للاسترداد)
- **تأجيل (Defer)** — الاحتفاظ بها لكن جعلها قابلة للاسترداد فقط عبر رقم التسلسل

في دفعة من 50، يمكنك الآن إكمال 47، والتخلي عن 2 بأخطاء مؤقتة، وإرسال 1 مشوّهة إلى قائمة الرسائل الميتة — كل ذلك في استدعاء دالة واحد.

## أمثلة على الكود

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

## التراجع الأسي بدون بنية تحتية إضافية

يتيح الجمع بين `abandon` وخصائص التطبيق المعدّلة تطبيق التراجع الأسي مباشرةً على القائمة — دون Durable Functions أو قوائم إضافية. خزّن عدد المحاولات في خصائص تطبيق الرسالة، اقرأه عند إعادة التسليم، واحسب التأخير. كان هذا النمط يتطلب توزيعاً معقداً؛ الآن أصبح بضعة أسطر في معالج إعادة المحاولة.

## مكاسب كفاءة الدفعات

كان النموذج القديم يرسل كل رسالة كاستدعاء دالة منفصل: 50 رسالة تعني 50 اتصالاً و50 بدء تشغيل بارداً و50 إيقافاً. يعالج النموذج الجديد الـ 50 في استدعاء واحد، والتسوية لكل رسالة تعني أنك لن تتنازل عن هذه الكفاءة عند حدوث أخطاء.

اقرأ المقال الكامل على [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
