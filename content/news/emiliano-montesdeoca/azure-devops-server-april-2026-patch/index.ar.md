---
title: "تصحيح Azure DevOps Server لشهر أبريل 2026 — إصلاح اكتمال طلبات السحب وتحديثات الأمان"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يحصل Azure DevOps Server على التصحيح 3 مع إصلاح فشل اكتمال طلبات السحب، وتحسين التحقق من تسجيل الخروج، واستعادة اتصالات PAT الخاصة بـ GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "azure-devops-server-april-2026-patch" >}}).*

تنبيه سريع للفرق التي تشغل Azure DevOps Server المستضاف ذاتياً: أصدرت Microsoft [التصحيح 3 لشهر أبريل 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) مع ثلاثة إصلاحات محددة.

## ما الذي تم إصلاحه

- **فشل اكتمال طلبات السحب** — كان استثناء مرجع فارغ أثناء الإكمال التلقائي لعناصر العمل يتسبب في فشل دمج طلبات السحب. إذا كنت تواجه أخطاء عشوائية في اكتمال طلبات السحب، فهذا هو السبب على الأرجح
- **التحقق من إعادة توجيه تسجيل الخروج** — تحسين التحقق أثناء تسجيل الخروج لمنع عمليات إعادة التوجيه الخبيثة المحتملة. هذا إصلاح أمني يستحق التطبيق الفوري
- **اتصالات PAT بـ GitHub Enterprise Server** — كان إنشاء اتصالات رمز الوصول الشخصي بـ GitHub Enterprise Server معطوباً، وقد تم استعادته الآن

## كيفية التحديث

نزّل [التصحيح 3](https://aka.ms/devopsserverpatch3) وشغّل المثبت. للتحقق من تطبيق التصحيح:

```bash
<patch-installer>.exe CheckInstall
```

إذا كنت تشغّل Azure DevOps Server محلياً، توصي Microsoft بشدة بالبقاء على آخر تصحيح للأمان والموثوقية معاً. راجع [ملاحظات الإصدار](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) للتفاصيل الكاملة.
