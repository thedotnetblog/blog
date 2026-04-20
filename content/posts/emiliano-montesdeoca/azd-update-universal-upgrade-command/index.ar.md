---
title: "azd update — أمر واحد يتحكّم في جميع مديري الحزم"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يمتلك Azure Developer CLI الآن أمر تحديث عالمياً يعمل بصرف النظر عن طريقة التثبيت — winget أو Homebrew أو Chocolatey أو سكريبت التثبيت."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "azd-update-universal-upgrade-command" >}}).*

هل تعرف رسالة "إصدار جديد من azd متاح" التي تظهر كل أسابيع قليلة؟ تلك التي تتجاهلها لأنك لا تتذكر إن كنت قد ثبّتت `azd` عبر winget أو Homebrew أو ذلك السكريبت curl الذي شغّلته قبل ستة أشهر؟ نعم، تمّ حلّ هذا الأمر أخيراً.

شحنت Microsoft للتو [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — أمر واحد يُحدّث Azure Developer CLI إلى أحدث إصدار بصرف النظر عن طريقة تثبيتك الأصلية. Windows، macOS، Linux — لا يهم. أمر واحد.

## كيف يعمل

```bash
azd update
```

هذا كل شيء. إن أردت الوصول المبكر إلى الميزات الجديدة، يمكنك التبديل إلى بناء الـ insiders اليومي:

```bash
azd update --channel daily
azd update --channel stable
```

يكتشف الأمر طريقة التثبيت الحالية لديك ويستخدم آلية التحديث المناسبة داخلياً. لا مزيد من "انتظر، هل استخدمت winget أم choco على هذا الجهاز؟".

## التحفّظ الصغير

يأتي `azd update` ابتداءً من الإصدار 1.23.x. إن كنت على إصدار أقدم، ستحتاج إلى إجراء تحديث يدوي أخير باستخدام طريقة تثبيتك الأصلية. بعد ذلك، `azd update` يتولى كل شيء من الآن فصاعداً.

تحقق من إصدارك الحالي بـ `azd version`. إن احتجت تثبيتاً جديداً، [وثائق التثبيت](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) ستُرشدك.

## لماذا هذا مهم

هذا تحسين صغير لجودة الحياة، لكن بالنسبة لأولئك منّا الذين يستخدمون `azd` يومياً لنشر وكلاء الذكاء الاصطناعي وتطبيقات Aspire إلى Azure، البقاء محدّثاً يعني حالات أقل من "هذه الخطأ تمّ إصلاحها بالفعل في الإصدار الأخير". شيء واحد أقل يجب التفكير فيه.

اقرأ [الإعلان الكامل](https://devblogs.microsoft.com/azure-sdk/azd-update/) والغوص العميق لـ Jon Gallant [هنا](https://blog.jongallant.com/2026/04/azd-update) لمزيد من السياق.
