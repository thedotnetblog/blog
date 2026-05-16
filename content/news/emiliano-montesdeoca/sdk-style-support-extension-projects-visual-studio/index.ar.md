---
title: "دعم أسلوب SDK لمشاريع الإضافات في Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "يجلب Visual Studio 18.5 دعماً رسمياً لتنسيق مشروع SDK-style لإضافات VSSDK، مما يقلل وقت البناء بنسبة تصل إلى 75% ويختصر ملفات المشروع إلى ~20 سطراً."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[دعم أسلوب SDK لمشاريع الإضافات في Visual Studio](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) أصبح رسمياً في Visual Studio 18.5 — يمكن لمشاريع إضافات VSIX الكلاسيكية الآن التخلص من تنسيق `.csproj` القديم.

## ما الذي يتغير في ملف المشروع

أبرز تغيير مرئي هو مدى صغر ملف المشروع. تبدو إضافة VSSDK النموذجية الآن هكذا:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net472</TargetFramework>
    <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
    <VsixDeployOnDebug>true</VsixDeployOnDebug>
    <GeneratePkgDefFile>true</GeneratePkgDefFile>
  </PropertyGroup>
  <ItemGroup><ProjectCapability Include="CreateVsixContainer" /></ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
    <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
  </ItemGroup>
</Project>
```

`VSSDKBuildToolsAutoSetup=true` يطبّق الإعدادات الافتراضية المناسبة: `CreateVsixContainer=true` و`DeployExtension=false` القديمة. هذه الخاصية الواحدة تستبدل قدراً كبيراً مما كان يجب كتابته صراحةً من قبل.

## تحسينات وقت البناء

تم تضمين Fast Up-To-Date Check ودعم البناء التزايدي. بالنسبة للحلول الكبيرة مع تغييرات صغيرة، يتحول هذا إلى **تخفيض بنسبة تصل إلى 75% في وقت البناء** — مهم إذا كنت تكرر تطوير إضافة داخل حل ضخم.

## المشاريع الجديدة مقابل الموجودة

المشاريع الجديدة التي تُنشأ في 18.5 تستخدم أسلوب SDK تلقائياً. الإضافات بأسلوب MPF الموجودة تستمر في العمل — الترحيل اختياري. شيء يجب الانتباه إليه أثناء الترحيل: أضف `<UseWpf>true</UseWpf>` إذا كانت إضافتك تستخدم XAML. تحتاج أيضاً إلى وضع علامة على الإضافة كقابلة للنشر في ملف `.sln` أو `.slnx`.

محرر vsixmanifest تم استبداله بمحرر XML كالافتراضي — انقر بزر الماوس الأيمن → Open With إذا أردت المصمم القديم.

## مسار الترحيل الآلي

يمكن لوكيل Modernize في [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) أتمتة الترحيل. عدة إضافات حقيقية تم تحويلها بهذه الطريقة: Smart Screen وCommand Explorer وPostfix Templates وWhitespace Visualizer لـ Mads Kristensen.

## جدير بالملاحظة

VisualStudio.Extensibility (إطار الإضافات الأحدث) كان يدعم أسلوب SDK مسبقاً. هذا التحديث يحقق التكافؤ مع مسار VSSDK الكلاسيكي. المتطلب الوحيد هو حزمة عمل تطوير إضافات Visual Studio.

التفاصيل الكاملة في [المنشور الرسمي](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
