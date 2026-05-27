---
title: "dotnet new WinUI: إنشاء تطبيقات Windows دون الحاجة إلى Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "قوالب مشاريع WinUI تعمل الآن مع dotnet new — تطبيقات فارغة، أنماط NavigationView والمزيد. دعم VS Code، لا يلزم Visual Studio، مع إعدادات Fluent Design الافتراضية مدمجة."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

كان تطوير WinUI يتطلب Visual Studio في السابق. هذا يتغير الآن: نشرت Microsoft قوالب مشاريع وعناصر مفتوحة المصدر لـ WinUI تعمل مع `dotnet new`، مما يجلب تطوير تطبيقات Windows إلى سير عمل CLI القياسي.

## البدء بثلاثة أوامر

```shell
# تثبيت القوالب
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# إنشاء تطبيق NavigationView
dotnet new winui-navview -n MyApp

# التشغيل
cd MyApp
dotnet run
```

لا Visual Studio، لا إعداد يدوي للمشروع. يعمل التطبيق باستخدام `dotnet run`.

## ما هو متضمن

**القالب الفارغ** (`dotnet new winui`) — نقطة انطلاق حديثة مع شريط عنوان Fluent متصل مسبقًا، أيقونة تطبيق افتراضية محدّثة بأصل `.ico`، وإعدادات افتراضية صحيحة للوضع الفاتح/الداكن. أفضل من القالب الفارغ القديم الذي كان يتركك تضبط الأساسيات بنفسك.

**قالب NavigationView** (`dotnet new winui-navview`) — نمط التنقل الرئيسي-التفصيلي، متصل بالكامل مع NavigationView وشريط عنوان حديث وبنية تنقل متعددة الصفحات. يتبع صورة تطبيق Windows القياسية للتطبيقات المعتمدة على التنقل. إذا كنت تبني شيئًا يحتوي على تنقل جانبي، ابدأ من هنا.

يتبع كلا القالبين [صور تطبيقات Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — أنماط Fluent Design الحديثة للتخطيط والتنقل والبنية المرئية — مباشرةً.

## لماذا يهم هذا للمطورين خارج Visual Studio

كان مطورو WinUI الذين يستخدمون VS Code أو Rider أو أدوات سطر الأوامر في وضع غير مناسب. القوالب الموجودة في Visual Studio لم تكن قابلة للاستخدام خارج VS — كان لا بد من إعادة إنشاء بنية المشروع يدويًا وتوصيل الأساسيات.

هذه القوالب مفتوحة المصدر (انظر [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407))، طُوِّرت من [ملاحظات المجتمع](https://github.com/microsoft/microsoft-ui-xaml/issues/10388)، ومتاحة الآن. دعم Visual Studio قيد التطوير — ستعمل هذه القوالب نفسها هناك أيضًا في نهاية المطاف.

للفرق التي تريد أتمتة إعداد مشاريع WinUI، أو دمجه في CI، أو ببساطة استخدام محرر غير Visual Studio، هذا تحسين ذو معنى.

المنشور الأصلي: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
