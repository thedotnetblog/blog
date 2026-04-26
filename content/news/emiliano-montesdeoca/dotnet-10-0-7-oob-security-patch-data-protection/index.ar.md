---
title: "رقّع هذا الآن: تحديث الأمان OOB ‏.NET 10.0.7 لـ ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 هو إصدار خارج النطاق يصلح ثغرة أمنية في Microsoft.AspNetCore.DataProtection — كان التشفير الموثق يحسب HMAC على البايتات الخطأ، ما قد يؤدي إلى تصعيد الامتيازات. حدّث فورًا."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*تمت ترجمة هذه المقالة تلقائيًا. للنسخة الأصلية، [انقر هنا](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

هذا التحديث ليس اختياريًا. إذا كان تطبيقك يستخدم `Microsoft.AspNetCore.DataProtection`، فعليك التحديث إلى 10.0.7.

## ماذا حدث

بعد إصدار Patch Tuesday الخاص بـ `.NET 10.0.6`، بدأ بعض المستخدمين بالإبلاغ عن فشل فك التشفير في تطبيقاتهم. أثناء التحقيق في ذلك الانحدار، اكتشف الفريق أنه كشف أيضًا عن ثغرة أمنية: **CVE-2026-40372**.

في الإصدارات من `10.0.0` إلى `10.0.6` من `Microsoft.AspNetCore.DataProtection`، كان التشفير الموثق يحسب علامة التحقق HMAC الخاصة به على **البايتات الخطأ** من الحمولة ثم يتجاهل التجزئة المحسوبة. وقد يؤدي ذلك إلى تصعيد الامتيازات.

بعبارة أبسط: كان فحص النزاهة لا يقوم بما يفترض أن يقوم به. يستخدم Data Protection التشفير الموثق لمنع العبث — وHMAC هو فحص "هل تم تعديل هذا؟". إذا حُسب HMAC على بيانات خاطئة، فإنك تفقد تلك الضمانة.

## من المتأثر

أي تطبيق .NET 10 يستخدم `Microsoft.AspNetCore.DataProtection` — من الإصدارات 10.0.0 إلى 10.0.6. والخبر الجيد أن هذه الحزمة خاصة بـ .NET 10. إذا كنت ما تزال على .NET 8 أو 9، فأنت غير متأثر بهذه الثغرة تحديدًا.

حالات الاستخدام الشائعة لـ Data Protection: تشفير ملفات تعريف الارتباط، رموز antiforgery، البيانات المؤقتة في MVC، وأي استخدام آخر لـ `IDataProtector` في تطبيقك.

## كيفية الإصلاح

حدّث حزمة NuGet `Microsoft.AspNetCore.DataProtection` إلى **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

أو حدّث SDK/وقت التشغيل لديك: [نزّل .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

تحقق من أنك على الإصدار الصحيح:

```bash
dotnet --info
```

ثم **أعد البناء وأعد النشر** لتطبيقك. لن يصبح الإصلاح ساريًا إلا بعد تشغيل الحزمة المحدّثة.

## الصورة الأكبر

إصدارات الأمان خارج النطاق نادرة — وتحدث عندما تكون الثغرة خطيرة بما يكفي لعدم انتظار Patch Tuesday التالي. هذه الحالة جاءت مباشرة نتيجة انحدار في 10.0.6 خلق فجوة أمنية. وحقيقة أنه تم اكتشافها عبر تقارير خطأ أمر جيد؛ فهذا يعني أن العملية نجحت. الإصلاح سريع والنطاق محدود.

إذا كنت تشغّل .NET 10 في الإنتاج مع أي إطار عمل لتطبيقات الويب، فهذه حالة تحديث في اليوم نفسه.

الإعلان الأصلي بواسطة Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).