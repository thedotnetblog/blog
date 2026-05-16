---
title: "تقاعد Azure Data Studio: انقل سير عمل Azure SQL إلى VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "تقاعد Azure Data Studio في 6 فبراير 2025، وينتهي الدعم في 28 فبراير 2026. إليك مسار الترحيل الكامل إلى VS Code مع امتداد MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[تقاعد Azure Data Studio في 6 فبراير 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)، وينتهي الدعم في 28 فبراير 2026 — البديل الموصى به هو VS Code مع امتداد MSSQL.

## ما يجب تثبيته

ثلاثة أشياء للبدء:

- **امتداد MSSQL** — ابحث عن "SQL Server (mssql)" في VS Code Marketplace
- **امتداد SQL Database Projects** — المخطط كرمز، التحقق من صحة البناء، النشر الموجّه
- **.NET 8 SDK** — مطلوب من نظام البناء؛ غياب SDK هو أكثر مشكلة شائعة عند الاستخدام الأول

## ترحيل اتصالاتك وإعدادات ADS

يتضمن امتداد MSSQL **ADS Migration Toolkit**، الذي يتولى الترحيل لمرة واحدة في تدفق موجّه: يتم استيراد الاتصالات المحفوظة، ومجموعات الاتصالات، والإعدادات، واختصارات لوحة المفاتيح تلقائيًا.

## استعادة ذاكرة العضلات للضغط على F5

يعتمد مستخدمو ADS على F5 لتشغيل الاستعلامات. قم بتثبيت امتداد **MSSQL Database Management Keymap** للحصول على اختصارات لوحة المفاتيح بأسلوب ADS، بما في ذلك F5.

## SQL Database Projects: المخطط كرمز

انقر بزر الفأرة الأيمن على المشروع ← **نشر** ← تهيئة الهدف ← مراجعة البرنامج النصي T-SQL المُنشأ ← النشر. معاينة البرنامج النصي قبل النشر هي ميزة الأمان الرئيسية. تُنشئ قوالب العناصر أُطر لجداول، الإجراءات المخزنة، والمشاهدات — نفس سير العمل مثل SSDT.

مشكلة شائعة: **عدم تطابق النظام الأساسي المستهدف** في ملف `.sqlproj` سيتسبب في أخطاء بناء إذا تم إنشاء المشروع مقابل إصدار مختلف من SQL Server.

## Schema Compare وSchema Designer

يتضمن الامتداد أيضًا **Schema Compare** (مقارنة مشروعك بقاعدة البيانات المنشورة) و**Schema Designer** (تحرير المخطط بصريًا دون كتابة DDL يدويًا).

## مطوري Microsoft Fabric

الإعداد متطابق، لكن ابدأ من **بوابة Fabric** وقم بتوصيل قاعدة البيانات بـ Git أولًا قبل فتحها في VS Code. لدى Microsoft دليل مخصص: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## خلاصة

الترحيل هو تدفق موجّه لمرة واحدة، وليس إعادة بناء يدوية. قم بتثبيت الأدوات الثلاث، وشغّل ADS Migration Toolkit، واستعد اختصارات لوحة المفاتيح الخاصة بك، وستعود إلى وضعك الطبيعي في أقل من 10 دقائق.

اطلع على [المقالة الكاملة](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) للحصول على لقطات شاشة خطوة بخطوة والجولة التفصيلية الخاصة بـ Fabric.
