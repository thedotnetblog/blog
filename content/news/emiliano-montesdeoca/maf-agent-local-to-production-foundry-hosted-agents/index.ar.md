---
title: "وكيل MAF المحلي الخاص بك وجد الآن موطناً في الإنتاج"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "يمنح Foundry Hosted Agents وكيل Microsoft Agent Framework هويةً وتوسعاً وثباتاً للجلسات وقابلية للملاحظة دون إعداد إضافي. إليك كيف يبدو ذلك عملياً."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

جعل الوكيل يعمل محلياً هو الجزء الممتع. الجزء الصعب هو كل ما يأتي بعد ذلك: نشره دون فقدان العقل، وإدارة الجلسات، وإعداد الهوية، وتوصيل قابلية الملاحظة. عادةً ما يعني ذلك الكثير من البنية التحتية المخصصة.

Foundry Hosted Agents أزال للتو معظم تلك البنية التحتية لمستخدمي Microsoft Agent Framework (MAF).

## ما الذي يفعله Foundry Hosted Agents فعلياً

عندما تنشر وكيل MAF على Foundry Hosted Agents، تتولى المنصة قائمة طويلة بشكل مدهش من الأشياء التي كان عليك بناؤها بنفسك:

- **التوسع إلى الصفر** — وكيلك لا يكلف شيئاً عند الخمول ويعود للعمل تلقائياً
- **بيئات معزولة بـ VM لكل جلسة** — كل جلسة مستخدم تحصل على بيئتها المعزولة مع استمرارية نظام الملفات التي تصمد أمام أحداث التقليص
- **Entra ID مدمج** — كل وكيل يحصل على هويته الخاصة لاستدعاء نماذج Foundry وToolbox وخدمات Azure دون أسرار مضمّنة في الصورة
- **نشر ذو إصدارات** — كل نشر هو لقطة ثابتة مع دعم نشر blue/green والنشر التدريجي
- **قابلية ملاحظة دون إعداد** — يُحقن `APPLICATIONINSIGHTS_CONNECTION_STRING` وقت التشغيل لتتدفق تتبعات OpenTelemetry الخاصة بـ MAF إلى App Insights تلقائياً

هذه الأخيرة مريحة فعلاً. لا توصيل إضافي، لا إعداد إضافي. التتبعات تظهر ببساطة.

## الفرق في الكود ضئيل

هذا ما أقدّره أكثر في هذا التكامل. لا تعيد كتابة وكيلك. فقط تغلّفه:

**في .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**في Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

هذا كل شيء. نفس المنطق الذي اختبرته محلياً هو ما يعمل في الإنتاج. تغلّف المنصة ذلك في بنية تحتية لإدارة الجلسات والهوية والتوسع.

## بروتوكولان، وكيل واحد

يدعم Hosted Agents نمطين من نقاط النهاية:

- **Responses** (`/responses`) — متوافق مع OpenAI، يدير تاريخ المحادثة والبث. خيار افتراضي جيد للوكلاء ذوي طابع المحادثة.
- **Invocations** (`/invocations`) — تحدد أنت مخطط الطلب/الاستجابة. جيد لسير العمل غير المحادثاتي.

إذا كنت تبني شيئاً يشبه المحادثة، ابدأ بـ Responses. إذا كنت تبني وكيلاً بصيغة API يأخذ مدخلات منظمة ويرجع مخرجات منظمة، فإن Invocations تمنحك المرونة.

## تدفق النشر مع `azd`

عند تشغيل `azd up` مع وكيل MAF:

1. يُنشئ اختيارياً مشروع Foundry وينشر نموذجاً
2. يحزم كودك ويدفع صورة إلى Azure Container Registry
3. يوفّر الحوسبة من صورة ACR
4. يعيّن Entra ID مخصصاً للوكيل
5. يعرض نقطة نهاية مستقرة (`https://{project_endpoint}/agents/{agent_name}`)
6. يتعامل مع كل شيء آخر من تلك النقطة

تستمر الجلسات حتى 30 يوماً. تُلغى توفير الحوسبة الخاملة بعد 15 دقيقة وتُستعاد بشفافية عند الطلب التالي. من منظور الوكيل، لم يتغير شيء.

## خلاصة

المسافة بين "يعمل محلياً" و"يعمل في الإنتاج" كانت تاريخياً طويلة ومؤلمة لوكلاء الذكاء الاصطناعي. Foundry Hosted Agents + MAF يُغلق هذه الفجوة بشكل كبير. إذا كان لديك بالفعل وكيل محلي مبني بـ Agent Framework، فالأمر يستحق التجربة اليوم.

يقول الفريق إن GA قادم قريباً — وهو حالياً في المعاينة. تحقق من [وثائق تكامل MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) و[أمثلة .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) للبدء.

المقال الأصلي: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
