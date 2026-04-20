---
title: "توقف عن حراسة طرفيتك: الوضع المنفصل في Aspire يغير سير العمل"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "يتيح لك Aspire 13.2 تشغيل AppHost في الخلفية واسترداد طرفيتك. مقرون بأوامر CLI الجديدة ودعم الوكلاء، هذا أمر أكبر مما يبدو."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

في كل مرة تشغّل فيها Aspire AppHost، تختفي طرفيتك. مقفلة. مشغولة حتى Ctrl+C. تريد تشغيل أمر سريع؟ افتح تبويبًا جديدًا. تريد التحقق من السجلات؟ تبويب آخر. هذا الاحتكاك الصغير يتراكم بسرعة.

يحل Aspire 13.2 هذا. كتب James Newton-King [تفاصيل كاملة](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/)، وبصراحة، هذه إحدى تلك الميزات التي تُغيّر طريقة عملك فوراً.

## الوضع المنفصل: أمر واحد، الطرفية تعود

```bash
aspire start
```

هذا اختصار لـ `aspire run --detach`. يعمل AppHost الخاص بك في الخلفية وتستعيد طرفيتك فوراً.

## إدارة ما يعمل

التشغيل في الخلفية مفيد فقط إذا كنت تستطيع إدارة ما هو جارٍ. يأتي Aspire 13.2 بمجموعة كاملة من أوامر CLI:

```bash
# قائمة جميع AppHost العاملة
aspire ps

# فحص حالة AppHost محدد
aspire describe

# بث السجلات من AppHost العامل
aspire logs

# إيقاف AppHost محدد
aspire stop
```

## دمجه مع الوضع المعزول

الوضع المنفصل يتزاوج طبيعياً مع الوضع المعزول:

```bash
aspire start --isolated
aspire start --isolated
```

كل مثيل يحصل على منافذ عشوائية وأسرار منفصلة ودورة حياة خاصة به.

## لماذا هذا ضخم لوكلاء البرمجة

وكيل البرمجة الذي يعمل في طرفيتك يمكنه الآن:

1. تشغيل التطبيق بـ `aspire start`
2. الاستعلام عن حالته بـ `aspire describe`
3. التحقق من السجلات بـ `aspire logs` لتشخيص المشكلات
4. إيقافه بـ `aspire stop` عند الانتهاء

تشغيل `aspire agent init` يهيّئ ملف مهارات Aspire الذي يعلّم الوكلاء هذه الأوامر.

## خلاصة

الوضع المنفصل هو ترقية لسير العمل متنكرة كعلامة بسيطة. اقرأ [المقال كاملاً](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) واحصل على Aspire 13.2 مع `aspire update --self`.
