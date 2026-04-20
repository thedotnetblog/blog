---
title: "VS Code 1.112: ما يجب أن يهتم به مطورو .NET فعلاً"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "وصل VS Code 1.112 للتو ويحتوي على ترقيات الوكيل ومصحح متصفح متكامل وتقييد MCP ودعم monorepo. إليك ما يهم فعلاً إذا كنت تبني مع .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "vscode-1-112-dotnet-developers" >}}).*

وصل VS Code 1.112 للتو، وبصراحة؟ هذا الإصدار مختلف إذا كنت تقضي أيامك في عالم .NET. يوجد الكثير في [ملاحظات الإصدار الرسمية](https://code.visualstudio.com/updates/v1_112)، لكن دعني أوفر عليك التمرير وأركز على ما يهم فعلاً بالنسبة لنا.

## Copilot CLI أصبح أكثر فائدة بكثير

الموضوع الرئيسي لهذا الإصدار هو **استقلالية الوكيل** — إعطاء Copilot مساحة أكبر للعمل دون مراقبة كل خطوة.

### توجيه الرسائل والإضافة للقائمة

هل تعرف تلك اللحظة التي يكون فيها Copilot CLI في منتصف مهمة وتدرك أنك نسيت ذكر شيء ما؟ في السابق، كان عليك الانتظار. الآن يمكنك إرسال رسائل أثناء تشغيل طلب — إما لتوجيه الاستجابة الحالية أو لوضع تعليمات المتابعة في قائمة الانتظار.

### مستويات الأذونات

هذا هو الأكثر إثارةً للاهتمام. تدعم جلسات Copilot CLI الآن ثلاثة مستويات أذونات:

- **Default Permissions** — التدفق المعتاد حيث تطلب الأدوات التأكيد قبل التشغيل
- **Bypass Approvals** — يوافق تلقائيًا على كل شيء ويعيد المحاولة عند الأخطاء
- **Autopilot** — يعمل باستقلالية كاملة: يوافق على الأدوات، ويجيب على أسئلته الخاصة، ويستمر حتى الانتهاء من المهمة

يمكنك تمكين Autopilot بإعداد `chat.autopilot.enabled`.

## تصحيح تطبيقات الويب دون مغادرة VS Code

يدعم المتصفح المدمج الآن **التصحيح الكامل**. يمكنك تعيين نقاط التوقف والتنقل خطوة بخطوة وفحص المتغيرات — كل ذلك داخل VS Code.

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

لمطوري Blazor، هذا تغيير جذري.

## تقييد خادم MCP

إذا كنت تستخدم خوادم MCP، يمكنك الآن تقييدها في صندوق رمل:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

## اكتشاف تخصيصات Monorepo

إذا كنت تعمل في monorepo، مع إعداد `chat.useCustomizationsInParentRepositories`، يصعد VS Code إلى جذر `.git` ويكتشف كل شيء.

## /troubleshoot لتصحيح أخطاء الوكيل

هل سبق أن قمت بإعداد تعليمات مخصصة وتساءلت عن سبب عدم التقاطها؟ قم بتمكين المهارة الجديدة `/troubleshoot` بـ:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

## الخلاصة

يدفع VS Code 1.112 بقوة نحو تجربة الوكيل — استقلالية أكبر وتصحيح أفضل وأمان أكثر إحكامًا. [قم بتنزيل VS Code 1.112](https://code.visualstudio.com/updates/v1_112) أو قم بالتحديث من VS Code عبر **Help > Check for Updates**.
