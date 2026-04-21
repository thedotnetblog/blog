---
title: "azd + GitHub Copilot: إعداد المشروع بالذكاء الاصطناعي وحل الأخطاء بذكاء"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "يتكامل Azure Developer CLI الآن مع GitHub Copilot لإنشاء بنية المشروع التحتية وحل أخطاء النشر — دون مغادرة الطرفية."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *تُرجِمت هذه المقالة تلقائيًا. للاطلاع على النسخة الأصلية بالإنجليزية، [انقر هنا]({{< ref "index.md" >}}).*

هل تعرف تلك اللحظة التي تريد فيها نشر تطبيق موجود على Azure فتجد نفسك تحدق في ملف `azure.yaml` فارغ، محاولًا تذكر ما إذا كان Express API الخاص بك يجب أن يستخدم Container Apps أم App Service؟ تلك اللحظة أصبحت الآن أقصر بكثير.

يتكامل Azure Developer CLI (`azd`) الآن مع GitHub Copilot بطريقتين عمليتين: سقالة المشروع بمساعدة الذكاء الاصطناعي خلال `azd init`، واستكشاف الأخطاء وإصلاحها بذكاء عند فشل عمليات النشر. كلا الميزتين تعملان بالكامل داخل الطرفية.

## الإعداد مع Copilot أثناء azd init

عند تشغيل `azd init`، يظهر الآن خيار "Set up with GitHub Copilot (Preview)". اختره وسيحلل Copilot قاعدة التعليمات البرمجية الخاصة بك لإنشاء `azure.yaml` وقوالب البنية التحتية ووحدات Bicep — بناءً على الكود الفعلي.

```
azd init
# اختر: "Set up with GitHub Copilot (Preview)"
```

المتطلبات:

- **azd 1.23.11 أو أحدث** — تحقق بـ `azd version` أو حدّث بـ `azd update`
- **اشتراك نشط في GitHub Copilot** (فردي أو للأعمال أو للمؤسسات)
- **GitHub CLI (`gh`)** — سيطلب `azd` تسجيل الدخول إذا لزم الأمر

ما أجده مفيدًا حقًا: يعمل في الاتجاهين. تبني من الصفر؟ يساعدك Copilot على تهيئة خدمات Azure الصحيحة من البداية. لديك تطبيق موجود تريد نشره؟ وجّه Copilot إليه وسيُنشئ التهيئة دون الحاجة إلى إعادة هيكلة أي شيء.

### ما الذي يفعله فعليًا

لنفترض أن لديك Node.js Express API يعتمد على PostgreSQL. بدلًا من اتخاذ قرار يدوي بين Container Apps وApp Service ثم كتابة Bicep من الصفر، يكتشف Copilot تقنياتك ويُنشئ:

- `azure.yaml` بالإعدادات الصحيحة لـ `language` و`host` و`build`
- وحدة Bicep لـ Azure Container Apps
- وحدة Bicep لـ Azure Database for PostgreSQL

ويُجري فحوصات مسبقة قبل تغيير أي شيء — يتحقق من نظافة دليل git، ويطلب موافقتك على أدوات خادم MCP مسبقًا. لا شيء يحدث دون علمك بما سيتغير بالضبط.

## استكشاف الأخطاء وإصلاحها مع Copilot

أخطاء النشر لا مفر منها. معاملات مفقودة، مشكلات في الأذونات، توفر SKU — ونادرًا ما تخبرك رسالة الخطأ بالشيء الوحيد الذي تحتاج معرفته فعلًا: *كيف تُصلحه*.

بدون Copilot، الحلقة تبدو هكذا: انسخ الخطأ ← ابحث في المستندات ← اقرأ ثلاث إجابات Stack Overflow غير ذات صلة ← شغّل بعض أوامر `az` CLI ← أعد المحاولة وتمنَّ. مع Copilot في `azd`، تنهار هذه الحلقة. عند فشل أي أمر `azd`، يعرض فورًا أربعة خيارات:

- **Explain** — شرح بلغة مبسطة لما حدث
- **Guidance** — تعليمات خطوة بخطوة لإصلاح المشكلة
- **Diagnose and Guide** — تحليل كامل + يطبق Copilot الإصلاح (بموافقتك) + إعادة محاولة اختيارية
- **Skip** — التعامل معه بنفسك

النقطة الرئيسية: لدى Copilot بالفعل سياق مشروعك والأمر الفاشل وتفاصيل الخطأ. اقتراحاته خاصة بـ *وضعك*.

### ضبط السلوك الافتراضي

إذا كنت دائمًا تختار نفس الخيار، تجاوز الموجه التفاعلي:

```
azd config set copilot.errorHandling.category troubleshoot
```

القيم: `explain` و`guidance` و`troubleshoot` و`fix` و`skip`. يمكنك أيضًا تمكين الإصلاح التلقائي وإعادة المحاولة:

```
azd config set copilot.errorHandling.fix allow
```

العودة إلى الوضع التفاعلي في أي وقت:

```
azd config unset copilot.errorHandling.category
```

## خاتمة

شغّل `azd update` للحصول على أحدث إصدار وجرّب `azd init` في مشروعك القادم.

اقرأ [الإعلان الأصلي هنا](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
