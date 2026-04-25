---
title: "Windows App Dev CLI v0.3: تشغيل F5 من الطرفية وأتمتة واجهة المستخدم للوكلاء الذكيين"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "يُقدّم Windows App Development CLI v0.3 أمر winapp run لتشغيل التطبيقات وتنقيحها من الطرفية، وأمر winapp ui لأتمتة الواجهة، وحزمة NuGet جديدة تتيح dotnet run مع التطبيقات المُحزَّمة."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للاطلاع على النص الأصلي، [انقر هنا]({{< ref "index.md" >}}).*

تجربة F5 في Visual Studio رائعة. لكن فتح VS لمجرد تشغيل تطبيق Windows مُحزَّم وتنقيحه — سواء في خط أنابيب CI، أو سير عمل آلي، أو عندما يُجري وكيل ذكاء اصطناعي الاختبارات — يُشكّل عبئًا زائدًا.

صدر الإصدار v0.3 من Windows App Development CLI [للتو](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)، ويعالج هذا الأمر مباشرةً بميزتين رئيسيتين: `winapp run` و`winapp ui`.

## winapp run: F5 من أي مكان

يستقبل `winapp run` مجلد تطبيق غير مُحزَّم وملف manifest، وينفّذ كل ما يفعله VS عند تشغيل التنقيح: تسجيل حزمة loose، وتشغيل التطبيق، والحفاظ على `LocalState` بين عمليات إعادة النشر.

```bash
# قم ببناء التطبيق، ثم شغّله كتطبيق مُحزَّم
winapp run ./bin/Debug
```

يعمل مع WinUI وWPF وWinForms وConsole وAvalonia والمزيد. صُمِّمت الأوضاع للمطورين وسير العمل الآلي على حد سواء:

- **`--detach`**: يُشغَّل التطبيق ويُعاد التحكم فورًا إلى الطرفية. مثالي لـ CI.
- **`--unregister-on-exit`**: يُزيل الحزمة المُسجَّلة عند إغلاق التطبيق.
- **`--debug-output`**: يلتقط رسائل `OutputDebugString` والاستثناءات في الوقت الفعلي.

## حزمة NuGet جديدة: dotnet run للتطبيقات المُحزَّمة

يتوفر للمطورين العاملين بـ .NET حزمة NuGet جديدة: `Microsoft.Windows.SDK.BuildTools.WinApp`. بعد التثبيت، يتولى `dotnet run` إدارة الحلقة الداخلية بأكملها: البناء، وتحضير حزمة loose-layout، والتسجيل في Windows، والتشغيل — كل ذلك في خطوة واحدة.

```bash
winapp init
# أو
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: أتمتة واجهة المستخدم من سطر الأوامر

هذه هي الميزة التي تفتح سيناريوهات الوكلاء الذكيين. يوفر `winapp ui` وصولًا كاملًا عبر UI Automation لأي تطبيق Windows قيد التشغيل — WPF وWinForms وWin32 وElectron وWinUI3 — مباشرةً من الطرفية.

ما يمكن تحقيقه:

- سرد جميع النوافذ على المستوى الأعلى
- التنقل في شجرة UI Automation الكاملة لأي نافذة
- البحث عن عناصر بالاسم أو النوع أو معرّف الأتمتة
- النقر والاستدعاء وتعيين القيم
- التقاط لقطات الشاشة
- انتظار ظهور العناصر — مثالي لمزامنة الاختبارات

يُتيح الجمع بين `winapp ui` و`winapp run` سير عملًا كاملًا من الطرفية: بناء ← تشغيل ← تحقق. يمكن للوكيل تشغيل التطبيق، وفحص حالة الواجهة، والتفاعل برمجيًا، والتحقق من النتيجة.

## مستجدات أخرى

- **`winapp unregister`**: يحذف حزمة sideloaded عند الانتهاء.
- **`winapp manifest add-alias`**: يُضيف اسمًا مستعارًا لتشغيل التطبيق بالاسم من الطرفية.
- **إكمال تلقائي بـ Tab**: تهيئة إكمال PowerShell بأمر واحد.

## كيفية التثبيت

```bash
winget install Microsoft.WinAppCli
# أو
npm install -g @microsoft/winappcli
```

الأداة في معاينة عامة. راجع [مستودع GitHub](https://github.com/microsoft/WinAppCli) للتوثيق الكامل، و[الإعلان الأصلي](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) لجميع التفاصيل.
