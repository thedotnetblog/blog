---
title: "Foundry Agent Service أصبح GA: ما يهم فعلاً لمطوري وكلاء .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "خدمة Foundry Agent من Microsoft وصلت للإتاحة العامة مع الشبكات الخاصة وVoice Live وتقييمات الإنتاج وبيئة تشغيل متعددة النماذج المفتوحة."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

لنكن صادقين — بناء نموذج أولي لوكيل الذكاء الاصطناعي هو الجزء السهل. الجزء الصعب هو كل ما يأتي بعده.

[Foundry Agent Service وصل للإتاحة العامة](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)، وهذا الإصدار مُركَّز بدقة على فجوة "كل ما يأتي بعده".

## مبني على Responses API

خدمة Foundry Agent من الجيل التالي مبنية على OpenAI Responses API. البنية مفتوحة عن قصد — لست مقيداً بمزود نموذج واحد.

## الشبكات الخاصة: إزالة العائق المؤسسي

- **لا خروج عام** — حركة مرور الوكيل لا تلمس الإنترنت العام أبداً
- **حقن الحاوية/الشبكة الفرعية** في شبكتك
- **اتصال الأدوات مدرج** — خوادم MCP وAzure AI Search عبر مسارات خاصة

## مصادقة MCP

| طريقة المصادقة | متى تُستخدم |
|-------------|-------------|
| مبني على مفتاح | وصول مشترك بسيط |
| هوية وكيل Entra | خدمة لخدمة |
| هوية مُدارة Entra | عزل لكل مشروع |
| تمرير هوية OAuth | وصول مُفوَّض من المستخدم |

## Voice Live

يُدمج Voice Live STT وLLM وTTS في واجهة برمجة تطبيقات مُدارة واحدة.

## التقييمات

1. **مُقيِّمون جاهزون** — التماسك والصلة والاتكاء
2. **مُقيِّمون مخصصون** — منطق عملك الخاص
3. **تقييم مستمر** — أخذ عينات من حركة مرور الإنتاج المباشرة

راجع [دليل البدء السريع](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) و[إعلان GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
