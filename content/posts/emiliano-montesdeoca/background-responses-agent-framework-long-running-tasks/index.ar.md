---
title: "الاستجابات في الخلفية في Microsoft Agent Framework: لا مزيد من القلق من انتهاء المهلة"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "يتيح لك Microsoft Agent Framework الآن تفريغ مهام الذكاء الاصطناعي طويلة التشغيل باستخدام رموز الاستمرارية. إليك كيفية عمل الاستجابات في الخلفية ولماذا تهم وكلاء .NET الخاصة بك."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

إذا بنيت أي شيء باستخدام نماذج التفكير مثل o3 أو GPT-5.2، فأنت تعرف المعاناة. يبدأ وكيلك في التفكير في مهمة معقدة، يجلس العميل ينتظر، وفي مكان ما بين "كل شيء على ما يرام" و"هل تعطل؟" تنتهي مهلة اتصالك. كل ذلك العمل؟ ضاع.

أصدر Microsoft Agent Framework للتو [الاستجابات في الخلفية](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — وبصراحة، هذه من الميزات التي كان يجب أن تكون موجودة منذ اليوم الأول.

## مشكلة الاستدعاءات الحاجبة

في نمط الطلب-الاستجابة التقليدي، يحجب عميلك حتى ينتهي الوكيل. هذا يعمل بشكل جيد للمهام السريعة. لكن عندما تطلب من نموذج تفكير إجراء بحث معمق أو تحليل متعدد الخطوات أو إنشاء تقرير من 20 صفحة؟ أنت تتطلع إلى دقائق من الوقت الفعلي. خلال تلك الفترة:

- يمكن أن تنتهي مهل اتصالات HTTP
- تقلبات الشبكة تقتل العملية بأكملها
- يحدق مستخدمك في مؤشر تحميل متسائلاً إذا كان أي شيء يحدث

الاستجابات في الخلفية تقلب هذا رأساً على عقب.

## كيفية عمل رموز الاستمرارية

بدلاً من الحجب، تطلق مهمة الوكيل وتحصل على **رمز استمرارية**. فكر فيه كتذكرة مطالبة في ورشة إصلاح — لا تقف عند الكاونتر تنتظر، بل تعود عندما يكون جاهزاً.

سير العمل مباشر:

1. أرسل طلبك مع `AllowBackgroundResponses = true`
2. إذا كان الوكيل يدعم المعالجة في الخلفية، تحصل على رمز استمرارية
3. استعلم حسب جدولك حتى يعود الرمز `null` — هذا يعني أن النتيجة جاهزة

إليك الإصدار بـ .NET:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Poll until complete
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

إذا أكمل الوكيل فوراً (المهام البسيطة، النماذج التي لا تحتاج معالجة في الخلفية)، لا يُعاد رمز استمرارية. كودك يعمل فقط — بدون معالجة خاصة.

## البث مع الاستئناف: السحر الحقيقي

الاستعلام مناسب لسيناريوهات "أطلق وانسَ"، لكن ماذا عن عندما تريد تقدماً في الوقت الفعلي؟ الاستجابات في الخلفية تدعم أيضاً البث مع استئناف مدمج.

كل تحديث مبث يحمل رمز استمراريته الخاص. إذا انقطع اتصالك في منتصف البث، تستأنف من حيث توقفت تماماً:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simulate a network interruption
}

// Resume from exactly where we left off
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

يستمر الوكيل في المعالجة من جانب الخادم بغض النظر عما يحدث مع عميلك. هذا تحمّل للأعطال مدمج دون كتابة منطق إعادة المحاولة أو قواطع الدائرة.

## متى تستخدم هذا فعلاً

ليست كل استدعاءات الوكيل تحتاج إلى استجابات في الخلفية. للإكمالات السريعة، أنت تضيف تعقيداً بدون سبب. لكن إليك أين تتألق:

- **مهام التفكير المعقدة** — تحليل متعدد الخطوات وبحث معمق وأي شيء يجعل نموذج التفكير يفكر فعلاً
- **توليد محتوى طويل** — تقارير تفصيلية ووثائق متعددة الأجزاء وتحليل مستفيض
- **الشبكات غير الموثوقة** — عملاء الجوال ونشرات الحافة وشبكات VPN المؤسسية المتذبذبة
- **أنماط واجهة المستخدم غير المتزامنة** — أرسل مهمة، اذهب افعل شيئاً آخر، عد للنتائج

بالنسبة لنا كمطوري .NET الذين يبنون تطبيقات مؤسسية، النقطة الأخيرة مثيرة للاهتمام بشكل خاص. فكر في تطبيق Blazor حيث يطلب مستخدم تقريراً معقداً — تطلق مهمة الوكيل، تعرض له مؤشر تقدم، وتتركه يستمر في العمل. بدون مشاكل WebSocket، بدون بنية تحتية مخصصة للطوابير، فقط رمز واستعلام دوري.

## خلاصة القول

الاستجابات في الخلفية متاحة الآن في .NET وPython من خلال Microsoft Agent Framework. إذا كنت تبني وكلاء يفعلون أي شيء أكثر تعقيداً من الأسئلة والأجوبة البسيطة، فهذا يستحق إضافته إلى أدواتك. نمط رمز الاستمرارية يبقي الأمور بسيطة مع حل مشكلة إنتاجية حقيقية جداً.

اطلع على [الوثائق الكاملة](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) للرجوع الكامل إلى واجهة برمجية والمزيد من الأمثلة.
