---
title: "من الحاسوب المحمول إلى الإنتاج: نشر وكلاء الذكاء الاصطناعي على Microsoft Foundry بأمرين فقط"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "يمتلك Azure Developer CLI الآن أوامر 'azd ai agent' تنقل وكيل الذكاء الاصطناعي من التطوير المحلي إلى نقطة نهاية Foundry المباشرة في دقائق."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

تعرف تلك الفجوة بين "يعمل على جهازي" و"تم نشره ويخدم حركة المرور"؟ بالنسبة لوكلاء الذكاء الاصطناعي، كانت تلك الفجوة واسعة بشكل مؤلم.

جعل Azure Developer CLI هذا [أمراً من أمرين](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## سير عمل `azd ai agent` الجديد

```bash
azd ai agent init
azd up
```

هذا كل شيء. `azd ai agent init` يُنشئ هيكل البنية التحتية كـ كود في مستودعك، و`azd up` يوفّر كل شيء على Azure وينشر وكيلك.

## ما يحدث تحت الغطاء

أمر `init` يولّد قوالب Bicep حقيقية وقابلة للفحص في مستودعك — Foundry Resource وFoundry Project وتهيئة نشر النموذج والهوية المُدارة مع RBAC.

## حلقة المطوّر الداخلية

```bash
azd ai agent run    # تشغيل الوكيل محلياً
azd ai agent invoke # إرسال مطالبات اختبار
azd ai agent monitor --follow  # بث السجلات في الوقت الفعلي
```

## مجموعة الأوامر الكاملة

| الأمر | ما يفعله |
|---------|-------------|
| `azd ai agent init` | إنشاء هيكل مشروع وكيل Foundry مع IaC |
| `azd up` | توفير الموارد ونشر الوكيل |
| `azd ai agent invoke` | إرسال مطالبات للوكيل البعيد أو المحلي |
| `azd ai agent run` | تشغيل الوكيل محلياً للتطوير |
| `azd ai agent monitor` | بث السجلات في الوقت الفعلي |
| `azd down` | تنظيف جميع موارد Azure |

راجع [التعليمات الكاملة](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).
