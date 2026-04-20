---
title: "الوضع المعزول في Aspire يحل كابوس تعارض المنافذ في التطوير المتوازي"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "يُقدم Aspire 13.2 وضع --isolated: منافذ عشوائية، أسرار منفصلة، وصفر تعارضات عند تشغيل نسخ متعددة من نفس AppHost. مثالي لوكلاء الذكاء الاصطناعي وworktrees وسير العمل المتوازي."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

إذا حاولت يوماً تشغيل نسختين من نفس المشروع في وقت واحد، فأنت تعرف الألم. المنفذ 8080 مُستخدم بالفعل.

يحل Aspire 13.2 هذا بعلامة واحدة. كتب James Newton-King [التفاصيل الكاملة](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/).

## الحل: `--isolated`

```bash
aspire run --isolated
```

كل تشغيل يحصل على:
- **منافذ عشوائية** — لا تعارضات بين النسخ
- **أسرار مستخدم معزولة** — سلاسل الاتصال ومفاتيح API تبقى منفصلة لكل نسخة

## سيناريوهات حقيقية

**عمليات checkout متعددة:**

```bash
# الطرفية 1
cd ~/projects/my-app-feature
aspire run --isolated

# الطرفية 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

كلاهما يعمل دون تعارضات.

**وكلاء الخلفية في VS Code.** عندما ينشئ وكيل الخلفية من Copilot Chat شجرة git للعمل باستقلالية، يضمن الوضع المعزول أن تعمل النسختان دون مشاكل.

## خلاصة

الوضع المعزول ميزة صغيرة تحل مشكلة حقيقية ومتزايدة. احصل على 13.2 بـ `aspire update --self`.
