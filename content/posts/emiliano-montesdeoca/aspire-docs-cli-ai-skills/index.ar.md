---
title: "Aspire 13.2 يشحن CLI للوثائق — ويمكن لوكيل الذكاء الاصطناعي استخدامه أيضاً"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 يُضيف aspire docs — واجهة سطر أوامر للبحث والتصفح وقراءة الوثائق الرسمية دون مغادرة الطرفية. تعمل أيضاً كأداة لوكلاء الذكاء الاصطناعي."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "aspire-docs-cli-ai-skills" >}}).*

تعرف تلك اللحظة حين تكون عميقاً في AppHost من Aspire، توصّل التكاملات، وتحتاج إلى التحقق من المعاملات التي يتوقعها تكامل Redis؟ تنتقل إلى المتصفح، تبحث في aspire.dev. السياق ضائع.

أطلق Aspire 13.2 [إصلاحاً لذلك](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). يتيح لك CLI `aspire docs` البحث في الوثائق الرسمية وتصفحها وقراءتها مباشرةً من الطرفية.

## ثلاثة أوامر، صفر تبويبات متصفح

```bash
# قائمة بجميع الوثائق
aspire docs list

# البحث عن موضوع
aspire docs search "redis"

# قراءة صفحة كاملة
aspire docs get redis-integration

# قسم واحد فقط
aspire docs get redis-integration --section "Add Redis resource"
```

## زاوية الوكيل الذكي

نفس أوامر `aspire docs` تعمل كأدوات لوكلاء الذكاء الاصطناعي. بدلاً من اختراع واجهات Aspire البرمجية بناءً على بيانات تدريب قديمة، يمكن للوكيل استدعاء `aspire docs search "postgres"` وإيجاد الوثائق الرسمية.

## خلاصة

`aspire docs` ميزة صغيرة تحل مشكلة حقيقية بشكل نظيف. راجع [التعمق الكامل لـ David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/).
