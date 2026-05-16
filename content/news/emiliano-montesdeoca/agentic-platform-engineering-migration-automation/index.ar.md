---
title: "إزالة العمل المتكرر في الهجرة باستخدام Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "يقوم Git-Ape بهجرة مستودع Terraform AWS حقيقي إلى Azure Bicep — باستخراج نية النشر وإعادة رسم المعمارية بدلاً من التحويل الحرفي."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — استعراض لأداة Git-Ape (أداة git للهندسة المنصبية الذكية) لترحيل مستودع Terraform على AWS حقيقي إلى Azure، مع التركيز على استخراج النية بدلاً من التحويل سطراً بسطر.

## المدخل: contoso-migration

المصدر هو مشروع Terraform حقيقي (`contoso-migration`) ينشر تطبيق Next.js على AWS — EC2 للحوسبة، وALB لموازنة التحميل، وS3 للتخزين المؤقت للتوزيع، ومفاتيح IAM للهوية. التكلفة: ~34$/شهرياً. الهدف ليس إعادة إنشاء نفس البنية التحتية على Azure، بل فهم ما تحاول عملية النشر فعله بالفعل، وإعادة بنائه باستخدام الخدمات الأصيلة في Azure.

## الخطوة 1: التحقق والمصادقة

يبدأ Git-Ape بالتحقق من جميع أدوات CLI المطلوبة — `az`، و`aws`، و`gh`، و`jq`، و`git` — والتأكد من جلسات المصادقة النشطة قبل الشروع في أي إجراء. لا تشغيل جزئي.

## الخطوة 2: استخراج النية

يقرأ العامل المستودع المصدر بأكمله عبر GitHub API ويستخرج نية النشر: بيئة التشغيل (Node.js)، ونوع الحوسبة، ونمط الوصول، ومعالجة التوزيع، ونموذج الهوية، والشبكة، والمراقبة. هذه هي الخطوة الأساسية — إنها تبني نموذجاً دلالياً لما يفعله النشر، وليس ما تستخدمه كلمات مفتاح Terraform.

## الخطوة 3: رسم الخدمات

تُعيَن خدمات AWS إلى معادلاتها في Azure:
- EC2 → App Service (Linux، Node 20 LTS)
- ALB → موازنة تحميل App Service المدمجة
- أدوار/مفاتيح IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## الخطوة 4: عامل النقد

قبل توليد المخرجات، يعمل عامل نقد يرصد مشكلتين مانعتين:

1. **نمط مضاد: البناء عند الإقلاع** — كان Terraform الأصلي يشغّل `npm install && npm run build` على EC2 عند الإقلاع. الحل: البناء في CI ونشر توزيع جاهز.
2. **Blob Storage غير ضروري** — كان S3 يُستخدم لتدريج التوزيع وكان يمكن التخلص منه مع CI/CD المناسب. أسقطه عامل النقد كلياً.

## الخطوة 5: المخرجات المُولَّدة

النتيجة هي ~80 سطراً من Bicep بدلاً من أكثر من 200 سطر من Terraform الأصلي. أنشأ العامل مستودع GitHub جديداً يحتوي على `infra/main.bicep` و`.github/workflows/deploy.yml` وأزال جميع الملفات الخاصة بـ AWS.

## مقارنة الوضع الأمني

أنتجت الهجرة أيضاً ترقية أمنية ملموسة:

| AWS الأصلي | مخرجات Azure |
|---|---|
| HTTP فقط | HTTPS فقط، TLS 1.2 |
| SSH مفتوح لـ 0.0.0.0/0 | لا كشف SSH |
| مفاتيح وصول IAM | OIDC + Managed Identity |
| لا مراقبة | Application Insights |

التكلفة: ~13$/شهرياً مقابل 34$ الأصلية.

## ما الذي يميز هذا عن محوّل صياغة

خطوة عامل النقد هي ما يفصل هذا عن الترجمة الآلية. لقد رصد أنماطاً كانت ستعمل على AWS ولكنها ستكون خاطئة على Azure — وأصلحها بدلاً من تكرارها. المخرج ليس "AWS بصياغة Azure"؛ بل هو نشر أصيل على Azure يحقق نفس الهدف بشكل أنظف.

راجع [الاستعراض الكامل](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) للاطلاع على تتبع العامل الكامل والملفات المُولَّدة.
