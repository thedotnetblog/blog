---
title: "تقييم التحديث في GitHub Copilot هو أفضل أداة هجرة لا تستخدمها بعد"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "ملحق التحديث في GitHub Copilot لا يقترح تغييرات الكود فحسب — بل ينتج تقييماً كاملاً للهجرة مع مشكلات قابلة للتنفيذ ومقارنات أهداف Azure وسير عمل تعاوني."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

ترحيل تطبيق .NET Framework قديم إلى .NET الحديث هو أحد تلك المهام التي يعرف الجميع أنهم يجب القيام بها لكن لا أحد يريد البدء فيها.

نشر Jeffrey Fritz [تعمقاً في تقييم التحديث في GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/).

## هذا ليس مجرد محرك اقتراحات كود

يتبع ملحق VS Code نموذج **تقييم → تخطيط → تنفيذ**. تحلل مرحلة التقييم قاعدة الكود بأكملها وتنتج مستنداً منظماً يلتقط كل شيء.

يُخزَّن التقييم تحت `.github/modernize/assessment/`. كل تشغيل ينتج تقريراً مستقلاً.

## طريقتان للبدء

**التقييم الموصى به** — المسار السريع. اختر من مجالات منسقة (ترقية Java/.NET، جاهزية السحابة، الأمان).

**التقييم المخصص** — المسار الموجه. اضبط بالضبط ما يجب تحليله: الحوسبة المستهدفة (App Service، AKS، Container Apps)، نظام التشغيل المستهدف، تحليل الحاويات.

## تقسيم المشكلات قابل للتنفيذ

كل مشكلة تأتي بمستوى الأهمية:

- **إلزامي** — يجب إصلاحه وإلا ستفشل الهجرة
- **محتمل** — قد يؤثر على الهجرة، يحتاج حكماً بشرياً
- **اختياري** — تحسينات موصى بها، لن تعيق الهجرة

## رأيي

إذا كانت لديك تطبيقات .NET Framework قديمة، فهذه *أفضل* أداة للبدء بها.

اقرأ [الدليل الكامل](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) واحصل على [ملحق VS Code](https://aka.ms/ghcp-appmod/vscode-ext).
