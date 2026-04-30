---
title: "GPT-5.5 هنا ويأتي إلى Azure Foundry — ما يحتاج مطورو .NET معرفته"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 متاح عمومًا في Microsoft Foundry. التطور من GPT-5 إلى 5.5، ما الذي تحسّن فعلًا وكيف تبدأ باستخدامه في وكلائك اليوم."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*تمت ترجمة هذا المقال تلقائيًا. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

أعلنت Microsoft للتو أن [GPT-5.5 متاح عمومًا في Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). إذا كنت تبني وكلاء على Azure، فهذا هو التحديث الذي كنت تنتظره.

## تطور GPT-5

- **GPT-5**: وحّد التفكير والسرعة في نظام واحد
- **GPT-5.4**: تفكير متعدد الخطوات أقوى، قدرات وكالية مبكرة للمؤسسات
- **GPT-5.5**: تفكير أعمق في السياق الطويل، تنفيذ وكالي أكثر موثوقية، كفاءة أفضل في الرموز

## ما الذي تغيّر فعلًا

**برمجة وكالية محسّنة**: يحتفظ GPT-5.5 بالسياق عبر قواعد الشفرة الكبيرة، ويشخّص الإخفاقات المعمارية، ويتوقع متطلبات الاختبار. يستدل النموذج على *ما يؤثر فيه أيضًا* الإصلاح قبل التصرف.

**كفاءة الرموز**: مخرجات أعلى جودة مع رموز أقل ومحاولات أقل. انخفاض مباشر في التكلفة والكمون في الإنتاج.

## التسعير

| النموذج | المدخلات ($/M رمز) | المدخلات المخزنة | المخرجات ($/M رمز) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## لماذا يهم Foundry

يتيح لك Foundry Agent Service تعريف الوكلاء في YAML أو توصيلهم بـ Microsoft Agent Framework أو GitHub Copilot SDK أو LangGraph أو OpenAI Agents SDK — وتشغيلهم كوكلاء مستضافين معزولين مع نظام ملفات دائم وهوية Microsoft Entra مستقلة وتسعير بمقياس صفري.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "أنت مساعد مفيد.", name: "وكيلي");
```

اطلع على [الإعلان الكامل](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) لجميع التفاصيل.
