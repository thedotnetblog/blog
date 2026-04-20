---
title: "هندسة المنصات الوكيلية تصبح حقيقية — Git-APE يُظهر الكيفية"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "يُجسّد مشروع Git-APE من Microsoft هندسة المنصات الوكيلية على أرض الواقع — باستخدام وكلاء GitHub Copilot وAzure MCP لتحويل الطلبات باللغة الطبيعية إلى بنية تحتية سحابية مُتحقق منها."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "agentic-platform-engineering-git-ape" >}}).*

كانت هندسة المنصات دائماً من المصطلحات التي تبدو رائعة في مؤتمرات التكنولوجيا لكنها عادةً تعني "بنينا بوابة داخلية وغلاف Terraform." الوعد الحقيقي — بنية تحتية ذاتية الخدمة آمنة ومُدارة وسريعة فعلاً — كان دائماً على بعد خطوات.

نشر فريق Azure للتو [الجزء الثاني من سلسلة هندسة المنصات الوكيلية](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/). يسمونه **Git-APE** — مشروع مفتوح المصدر يستخدم وكلاء GitHub Copilot وخوادم Azure MCP لتحويل الطلبات باللغة الطبيعية إلى بنية تحتية مُتحقق منها ومنشورة.

## ما يفعله Git-APE فعلاً

الفكرة الأساسية: بدلاً من تعلم وحدات Terraform، يتحدث المطورون مع وكيل Copilot. يفسر الوكيل النية، يُنشئ Infrastructure-as-Code، يتحقق منه وفق السياسات، وينشره — كل ذلك داخل VS Code.

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

افتح مساحة العمل في VS Code وسيكتشف GitHub Copilot ملفات تهيئة الوكيل تلقائياً:

```
@git-ape deploy a function app with storage in West Europe
```

التنظيف بنفس السهولة:

```
@git-ape destroy my-resource-group
```

## لماذا يهم هذا

بالنسبة لمن يبنون على Azure، يُحوّل هذا محادثة هندسة المنصات من "كيف نبني بوابة" إلى "كيف نصف حواجزنا الحمائية كواجهات برمجية."

كمطور .NET: تعمل Azure MCP Server ووكلاء GitHub Copilot مع أي حمل عمل Azure — ASP.NET Core API ومكدس .NET Aspire — يمكن أن يكون كل شيء هدفاً لتدفق النشر الوكيلي.

## خلاصة

Git-APE نظرة مبكرة لكن ملموسة على هندسة المنصات الوكيلية عملياً. استنسخ [المستودع](https://github.com/Azure/git-ape) واقرأ [المقال كاملاً](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/).
