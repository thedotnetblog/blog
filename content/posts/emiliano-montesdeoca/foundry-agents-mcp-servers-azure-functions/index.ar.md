---
title: "قم بتوصيل خوادم MCP على Azure Functions بوكلاء Foundry — إليك الطريقة"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "ابنِ خادم MCP مرة واحدة، انشره على Azure Functions، واربطه بوكلاء Microsoft Foundry مع المصادقة المناسبة."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

هناك شيء أحبه في نظام MCP البيئي: تبني خادمك مرة واحدة ويعمل في كل مكان.

نشرت Lily Ma من فريق Azure SDK [دليلاً عملياً](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) حول توصيل خوادم MCP المنشورة على Azure Functions بوكلاء Microsoft Foundry.

## لماذا هذا التركيب منطقي

يمنحك Azure Functions بنية تحتية قابلة للتوسع ومصادقة مدمجة وفوترة بدون خادم. يمنحك Microsoft Foundry وكلاء ذكاء اصطناعي يمكنهم التفكير والتخطيط واتخاذ الإجراءات.

## خيارات المصادقة

| الطريقة | حالة الاستخدام |
|--------|----------|
| **مبني على مفتاح** | التطوير أو الخوادم بدون Entra auth |
| **Microsoft Entra** | الإنتاج مع هويات مُدارة |
| **OAuth identity passthrough** | حيث يهم سياق المستخدم |
| **بدون مصادقة** | التطوير/الاختبار أو البيانات العامة فقط |

## الإعداد

1. **انشر خادم MCP على Azure Functions** — نماذج متاحة لـ [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
2. **فعّل مصادقة MCP المدمجة**
3. **احصل على URL نقطة النهاية** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **أضف خادم MCP كأداة في Foundry**

اقرأ [الدليل الكامل](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/).
