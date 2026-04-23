---
title: "كتابة Hooks في azd بـ Python وTypeScript و.NET: وداعًا لسكريبتات Shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "تدعم Azure Developer CLI الآن كتابة hooks بـ Python وJavaScript وTypeScript و.NET. لا مزيد من التبديل إلى Bash من أجل سكريبت migration واحد."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

إن كنت قد امتلكت مشروعًا بالكامل بـ .NET واضطررت رغم ذلك إلى كتابة سكريبتات Bash لـ hooks في azd، فأنت تعرف هذا الألم. لماذا التبديل إلى صياخة shell في خطوة pre-provisioning بينما كل شيء آخر في المشروع مكتوب بـ C#؟

هذا الإحباط لديه الآن حل رسمي. أطلقت Azure Developer CLI [دعم متعدد اللغات لـ hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)، وهو بالضبط بقدر ما يبدو جيدًا.

## ما هي الـ Hooks

الـ Hooks هي سكريبتات تعمل في نقاط حيوية من دورة حياة `azd` — قبل provisioning، وبعد deployment، والمزيد. تُعرَّف في `azure.yaml` وتتيح حقن منطق مخصص دون تعديل الـ CLI.

في السابق، دُعم فقط Bash وPowerShell. الآن يمكن استخدام **Python أو JavaScript أو TypeScript أو .NET** — ويتولى `azd` الباقي تلقائيًا.

## كيف يعمل الاستدلال

ما عليك سوى الإشارة إلى ملف وسيستنتج `azd` اللغة من الامتداد:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

لا إعداد إضافي. إذا كان الامتداد غامضًا، يمكنك إضافة `kind: python` (أو اللغة المناسبة) صراحةً.

## تفاصيل مهمة حسب اللغة

### Python

ضع `requirements.txt` أو `pyproject.toml` بجانب السكريبت (أو في أي دليل أعلى). سينشئ `azd` بيئة افتراضية تلقائيًا، ويثبت التبعيات، ويشغل السكريبت.

### JavaScript وTypeScript

نفس النمط — ضع `package.json` بالقرب من السكريبت وسيشغل `azd` أولاً `npm install`. بالنسبة لـ TypeScript يستخدم `npx tsx` دون خطوة تجميع ودون `tsconfig.json`.

### .NET

وضعان متاحان:

- **وضع المشروع**: إذا كان هناك `.csproj` بجانب السكريبت، سيشغل `azd` تلقائيًا `dotnet restore` و`dotnet build`.
- **وضع الملف الواحد**: في .NET 10+ يمكن تشغيل ملفات `.cs` المستقلة مباشرةً عبر `dotnet run script.cs`. لا حاجة لملف مشروع.

## إعداد خاص بكل منفذ

تدعم كل لغة كتلة `config` اختيارية:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## لماذا يهم هذا لمطوري .NET

كانت الـ hooks آخر مكان في مشروع قائم على azd يجبر على تغيير اللغة. الآن يمكن لكامل pipeline النشر — من كود التطبيق إلى lifecycle hooks — أن يعيش في لغة واحدة. يمكنك إعادة استخدام أدوات .NET الموجودة في hooks، والإشارة إلى مكتبات مشتركة، والتخلص من صيانة سكريبتات shell.

## خلاصة

أحد تلك التغييرات التي تبدو صغيرة لكنها تزيل الكثير من الاحتكاك اليومي مع azd. دعم متعدد اللغات لـ hooks متاح الآن — تحقق من [المنشور الرسمي](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) للحصول على التوثيق الكامل.
