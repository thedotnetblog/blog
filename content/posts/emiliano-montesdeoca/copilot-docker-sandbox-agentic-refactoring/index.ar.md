---
title: "Docker Sandbox يتيح لوكلاء Copilot إعادة هيكلة الكود دون تعريض جهازك للخطر"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "يمنح Docker Sandbox وكلاء GitHub Copilot جهاز microVM آمناً لإعادة الهيكلة — لا مطالبات أذونات، ولا خطر على المضيف. إليك لماذا يغير ذلك كل شيء لتحديث .NET على نطاق واسع."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

إذا استخدمت وضع الوكيل في Copilot لأي شيء يتجاوز التعديلات الصغيرة، فأنت تعرف الألم. كل كتابة ملف، كل أمر طرفية — موجه إذن آخر.

نشر فريق Azure مقالاً عن [Docker Sandbox لوكلاء GitHub Copilot](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/).

## ما الذي يمنحك إياه Docker Sandbox فعلاً

الفكرة الأساسية بسيطة: شغّل جهاز microVM خفيف الوزن ببيئة Linux كاملة، زامن مساحة عملك فيه، ودع وكيل Copilot يعمل بحرية بالداخل.

هذا أكثر من مجرد "تشغيل الأشياء في حاوية":
- **مزامنة مزدوجة الاتجاه** تحافظ على المسارات المطلقة
- **Docker daemon خاص** يعمل داخل microVM
- **وكلاء تصفية HTTP/HTTPS** تتحكم في الوصول إلى الشبكة
- **وضع YOLO** — يعمل الوكيل بدون مطالبات أذونات

## لماذا يجب على مطوري .NET الاهتمام

مع Docker Sandbox، يمكنك توجيه وكيل Copilot إلى مشروع، والسماح له بإعادة الهيكلة بحرية داخل microVM، وتشغيل `dotnet build` و`dotnet test` للتحقق، وقبول التغييرات التي تعمل فعلاً فقط.

## الخلاصة

Docker Sandbox يحل التوتر الجوهري في البرمجة الوكيلية: الوكلاء يحتاجون إلى الحرية ليكونوا مفيدين، لكن الحرية على جهازك المضيف خطيرة. تمنحك microVMs كليهما.
