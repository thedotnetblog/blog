---
title: ".NET أبريل 2026 — تحديثات الأمان التي يجب تطبيقها اليوم"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "تُصلح تحديثات خدمة أبريل 2026 ست ثغرات أمنية عبر .NET 10 و.NET 9 و.NET 8 و.NET Framework — بما في ذلك ثغرتان للتنفيذ عن بُعد."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

صدرت [تحديثات الخدمة لأبريل 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) لـ .NET و.NET Framework، وتتضمن هذه الدفعة إصلاحات أمنية تريد تطبيقها في أقرب وقت. ست ثغرات CVE مُصلَحة، بما في ذلك ثغرتان للتنفيذ عن بُعد (RCE).

## ما الذي تمت معالجته

إليك الملخص السريع:

| CVE | النوع | يؤثر على |
|-----|------|---------|
| CVE-2026-26171 | تجاوز ميزة الأمان | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **تنفيذ عن بُعد** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **تنفيذ عن بُعد** | .NET 10, 9, 8 |
| CVE-2026-32203 | حجب الخدمة | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | حجب الخدمة | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | حجب الخدمة | .NET Framework 2.0–4.8.1 |

تؤثر ثغرتا RCE (CVE-2026-32178 وCVE-2026-33116) على أوسع نطاق من إصدارات .NET وينبغي إعطاؤهما الأولوية.

## الإصدارات المحدَّثة

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

جميعها متاحة عبر القنوات المعتادة — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0)، وصور الحاويات على MCR، ومديري حزم Linux.

## ماذا تفعل

حدّث مشاريعك وخطوط CI/CD إلى أحدث إصدارات التصحيح. إذا كنت تشغّل حاويات، اسحب أحدث الصور. إذا كنت على .NET Framework، تحقق من [ملاحظات إصدار .NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) للتصحيحات المقابلة.

بالنسبة لمن يشغّل .NET 10 في الإنتاج (وهو الإصدار الحالي)، فإن 10.0.6 تحديث إلزامي. ينطبق الأمر ذاته على .NET 9.0.15 و.NET 8.0.26 إذا كنت على تلك المسارات طويلة الأمد للدعم (LTS). ثغرتا تنفيذ عن بُعد ليستا مما يمكن تأجيله.
