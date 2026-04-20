---
title: "الاستجابات في الخلفية في Microsoft Agent Framework: لا مزيد من القلق بشأن انتهاء المهلة"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "يتيح لك Microsoft Agent Framework الآن تفريغ مهام الذكاء الاصطناعي طويلة الأمد باستخدام رموز الاستمرارية. إليك كيفية عمل الاستجابات في الخلفية ولماذا تهم لوكلاء .NET الخاصة بك."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

إذا كنت قد بنيت أي شيء باستخدام نماذج التفكير مثل o3 أو GPT-5.2، فأنت تعرف الألم. يبدأ وكيلك في معالجة مهمة معقدة، يجلس العميل ينتظر، وفي مكان ما تنتهي مهلة الاتصال.

شحن Microsoft Agent Framework للتو [الاستجابات في الخلفية](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — وبصراحة، هذه إحدى الميزات التي كان يجب أن توجد منذ البداية.

## كيف تعمل رموز الاستمرارية

بدلاً من الحظر، تُطلق مهمة الوكيل وتستعيد **رمز استمرارية**. فكّر في الأمر كتذكرة مطالبة في متجر إصلاح:

1. أرسل طلبك مع `AllowBackgroundResponses = true`
2. إذا كان الوكيل يدعم المعالجة في الخلفية، ستحصل على رمز استمرارية
3. استعلم وفق جدولك حتى يعود الرمز `null`

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

## متى تستخدم هذا فعلياً

- **مهام التفكير المعقدة** — التحليل متعدد الخطوات، البحث العميق
- **توليد محتوى طويل** — تقارير تفصيلية، مستندات متعددة الأجزاء
- **الشبكات غير الموثوقة** — عملاء الهاتف المحمول، النشر على الحافة
- **أنماط UX غير متزامنة** — أرسل المهمة، افعل شيئاً آخر، عُد للنتائج

راجع [التوثيق الكامل](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/).
