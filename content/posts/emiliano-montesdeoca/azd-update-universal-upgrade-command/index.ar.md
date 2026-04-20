---
title: "azd update — أمر واحد لإدارة كل مديري الحزم"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يمتلك Azure Developer CLI الآن أمر تحديث عالمي يعمل بغض النظر عن طريقة التثبيت — winget أو Homebrew أو Chocolatey أو سكريبت التثبيت."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "azd-update-universal-upgrade-command" >}}).*

تعرف رسالة "إصدار جديد من azd متاح" التي تظهر كل بضعة أسابيع؟ تلك التي تُغلقها لأنك لا تتذكر إن كنت قد ثبّتت `azd` عبر winget أو Homebrew أو سكريبت curl ذاك قبل ستة أشهر؟ هذا قد حُل أخيراً.

شحن Microsoft للتو [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — أمر واحد يُحدّث Azure Developer CLI إلى أحدث إصدار بغض النظر عن طريقة التثبيت الأصلية.

## كيف يعمل

```bash
azd update
```

هذا كل شيء. للوصول المبكر:

```bash
azd update --channel daily
azd update --channel stable
```

يكتشف الأمر طريقة تثبيتك الحالية ويستخدم آلية التحديث المناسبة تلقائياً.

## التحفظ الصغير

`azd update` يشحن بدءاً من الإصدار 1.23.x. إذا كنت على إصدار أقدم، ستحتاج إلى آخر تحديث يدوي. بعد ذلك، يتولى `azd update` كل شيء.

## لماذا يهم

هذا تحسين بسيط لجودة الحياة، لكن لمن يستخدم `azd` يومياً لنشر وكلاء الذكاء الاصطناعي وتطبيقات Aspire على Azure، البقاء محدّثاً يهم.

اقرأ [الإعلان الكامل](https://devblogs.microsoft.com/azure-sdk/azd-update/).
