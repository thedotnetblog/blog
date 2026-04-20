---
title: "ربط خوادم MCP على Azure Functions بوكلاء Foundry — إليك الطريقة"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "أنشئ خادم MCP مرة واحدة، وانشره على Azure Functions، وربطه بوكلاء Microsoft Foundry مع المصادقة المناسبة. أدواتك تعمل في كل مكان — VS Code وCursor والآن وكلاء الذكاء الاصطناعي المؤسسي."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

ثمة شيء أحبه في منظومة MCP البيئية: تبني خادمك مرة واحدة ويعمل في كل مكان. VS Code وVisual Studio وCursor وChatGPT — كل عميل MCP يستطيع اكتشاف أدواتك واستخدامها. الآن، تضيف Microsoft مستهلكاً جديداً إلى تلك القائمة: وكلاء Foundry.

نشرت Lily Ma من فريق Azure SDK [دليلاً عملياً](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) حول ربط خوادم MCP المنشورة على Azure Functions بوكلاء Microsoft Foundry. إذا كان لديك خادم MCP بالفعل، فهذا إضافة قيمة صافية — لا إعادة بناء مطلوبة.

## لماذا هذا التركيب منطقي

يمنحك Azure Functions بنية تحتية قابلة للتوسع، ومصادقة مدمجة، وفوترة بدون خادم لاستضافة خوادم MCP. يمنحك Microsoft Foundry وكلاء ذكاء اصطناعي يستطيعون التفكير والتخطيط واتخاذ الإجراءات. ربط الاثنين يعني أن أدواتك المخصصة — الاستعلام عن قاعدة بيانات، أو استدعاء واجهة برمجية تجارية، أو تشغيل منطق التحقق — تصبح قدرات يستطيع وكلاء الذكاء الاصطناعي المؤسسي اكتشافها واستخدامها بصورة مستقلة.

النقطة الجوهرية: خادم MCP الخاص بك يبقى كما هو. أنت تضيف Foundry فحسب كمستهلك إضافي. الأدوات ذاتها التي تعمل في إعداد VS Code الخاص بك تشغّل الآن وكيل ذكاء اصطناعي يتفاعل معه فريقك أو عملاؤك.

## خيارات المصادقة

هنا تكمن القيمة الحقيقية للمقال. أربع طرق للمصادقة تبعاً لسيناريوك:

| الطريقة | حالة الاستخدام |
|---------|---------------|
| **مبنية على مفتاح** (افتراضية) | التطوير أو الخوادم التي لا تستخدم Entra auth |
| **Microsoft Entra** | الإنتاج مع الهويات المُدارة |
| **OAuth identity passthrough** | الإنتاج حيث يُصادق كل مستخدم بشكل فردي |
| **بدون مصادقة** | التطوير/الاختبار أو البيانات العامة فقط |

للإنتاج، Entra Microsoft مع هوية الوكيل هي المسار الموصى به. OAuth identity passthrough مخصص للحالات التي يهمّ فيها سياق المستخدم — يطلب الوكيل من المستخدمين تسجيل الدخول، ويحمل كل طلب رمز المستخدم الخاص به.

## الإعداد

التدفق على مستوى عالٍ:

1. **انشر خادم MCP على Azure Functions** — نماذج متاحة لـ [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) وPython وTypeScript وJava
2. **فعّل مصادقة MCP المدمجة** في تطبيق الدالة الخاص بك
3. **احصل على URL نقطة النهاية** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **أضف خادم MCP كأداة في Foundry** — انتقل إلى وكيلك في البوابة، أضف أداة MCP جديدة، وأدخل نقطة النهاية وبيانات الاعتماد

ثم اختبره في ملعب Agent Builder بإرسال موجّه يُشغّل إحدى أدواتك.

## رأيي

قصة إمكانية التركيب هنا تزداد قوةً بشكل حقيقي. أنشئ خادم MCP مرة واحدة بـ .NET (أو Python أو TypeScript أو Java)، وانشره على Azure Functions، وكل عميل متوافق مع MCP يستطيع استخدامه — أدوات البرمجة، وتطبيقات الدردشة، والآن وكلاء الذكاء الاصطناعي المؤسسي. هذا نمط "اكتب مرة واحدة، استخدم في كل مكان" يعمل فعلاً.

لمطوّري .NET تحديداً، [امتداد Azure Functions MCP](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) يجعل هذا أمراً مباشراً. تعرّف على أدواتك كـ Azure Functions، وانشر، وستحصل على خادم MCP جاهز للإنتاج مع كل الأمان والتوسعية التي يوفرها Azure Functions.

## خلاصة

إذا كانت لديك أدوات MCP تعمل على Azure Functions، فإن ربطها بوكلاء Foundry هو مكسب سريع — أدواتك المخصصة تصبح قدرات ذكاء اصطناعي مؤسسية مع مصادقة مناسبة ودون تغييرات في كود الخادم.

اقرأ [الدليل الكامل](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) للحصول على تعليمات خطوة بخطوة لكل طريقة مصادقة، وراجع [الوثائق التفصيلية](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) لإعدادات الإنتاج.
