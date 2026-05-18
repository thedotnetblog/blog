---
title: "امتداد WinApp لـ VS Code: تشغيل تطبيقات Windows وتصحيحها وحزمها دون مغادرة المحرر"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "يجلب امتداد WinApp لـ VS Code واجهة سطر الأوامر الكاملة لتطوير تطبيقات Windows مباشرةً إلى VS Code — قم بتشغيل تطبيقات WPF وWinUI و.NET وC++ وتصحيحها بهوية الحزمة وحزمها وتوقيعها دون الحاجة إلى Visual Studio."
dir: rtl
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*تمت ترجمة هذه المقالة تلقائياً. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

إذا سبق لك محاولة بناء تطبيق Windows في VS Code، فأنت تعرف تلك اللحظة. أنت في حالة تدفق كامل، تحرر الكود في محررك المفضل — وفجأة تحتاج إلى هوية الحزمة لـ Windows API. أو تحتاج إلى إنشاء MSIX. أو توقيع حزمة. وبغمضة عين تجد نفسك تفتح Visual Studio، أو تبحث في Google عن "msix packaging without visual studio" في الساعة الحادية عشرة مساءً.

ذلك الاحتكاك لم يعد موجوداً. [امتداد WinApp لـ VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) في المعاينة العامة الآن — وهو يدمج [واجهة سطر الأوامر الكاملة لتطوير تطبيقات Windows](https://github.com/microsoft/WinAppCli) مباشرةً في VS Code. لا تثبيت منفصل، لا حاجة لـ Visual Studio.

## هوية الحزمة بالضغط على F5

المشكلة مع واجهات برمجة تطبيقات Windows — الإشعارات، والمهام في الخلفية، وميزات الذكاء الاصطناعي على الجهاز، وأهداف المشاركة — كثير منها يتطلب أن يمتلك تطبيقك **هوية الحزمة**. بدونها، تلك الواجهات ببساطة لن تعمل.

تقليدياً، الحصول على هوية الحزمة يعني بناء مثبت MSIX كامل أو التشغيل من Visual Studio. يغير امتداد WinApp هذا كلياً من خلال نوع تصحيح أخطاء `winapp` مخصص.

أضف هذا إلى `launch.json` الخاص بك:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

اضغط F5. يحدد الامتداد مخرجات البناء والمانيفست، ويمنح تطبيقك هوية الحزمة عبر `winapp run`، ويرفق مصحح الأخطاء. لتطبيقات .NET يستخدم `coreclr` (يتطلب C# Dev Kit)، وC/C++ يستخدم `cppvsdbg`، وNode/Electron يستخدم مصحح الأخطاء المدمج.

يمكنك تكوين `preLaunchTask` ليُبنى المشروع تلقائياً قبل كل ضغطة F5 — نفس سير بناء وتشغيل Visual Studio، لكن في VS Code.

## كل شيء في لوحة الأوامر

افتح `Ctrl+Shift+P`، اكتب `WinApp`، وستحصل على مجموعة الأدوات الكاملة:

- **Initialize Project** — تهيئة مشروعك مع Windows SDK و/أو Windows App SDK
- **Run Application** — تشغيله كتطبيق محزوم بتخطيط فضفاض مع هوية الحزمة
- **Create MSIX Package** — حزم التطبيق مع خيارات الشهادة وبيئة التشغيل
- **Update Manifest Assets** — توليد جميع أيقونات التطبيق المطلوبة تلقائياً من صورة مصدر واحدة
- **Generate / Install Certificate** — إدارة شهادات التطوير
- **Sign Package** — توقيع MSIX أو ملف تنفيذي
- **Run SDK Tool** — تشغيل `makeappx` أو `signtool` أو `mt` أو `makepri` مباشرةً

لا تحتاج لتثبيت WinApp CLI أيضاً. إنه مدرج مع الامتداد.

## يعمل مع أطر عمل متعددة

هذه ليست مجرد أداة لـ .NET WPF/WinUI. يعمل الامتداد مع:

- **.NET**: WPF، WinForms، Console، WinUI 3
- **C/C++**: Win32، CMake، MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

هذا الاتساع مقصود. VS Code هو حيث يعيش مطورو الويب والمنصات المتعددة. إذا كنت تبني تطبيق Tauri أو Electron يحتاج إلى حزم Windows، فهذا الامتداد يغطيك دون الحاجة إلى اعتماد Visual Studio.

## لماذا يهم مطوري .NET

أعمل كثيراً في VS Code — إنه المكان الذي أكتب فيه Markdown وأدير الإعدادات وأحرر المشاريع الصغيرة وأشغل الطرفيات. لكن لتطوير سطح المكتب .NET على Windows، كان Visual Studio الخيار الوحيد الحقيقي في اللحظة التي تحتاج فيها إلى أي شيء يتعلق بالحزم.

هذا الامتداد يسد تلك الفجوة. يمكنك الآن الحصول على دورة تطوير سطح مكتب Windows .NET كاملة — تحرير، بناء، تشغيل بهوية الحزمة، تصحيح الأخطاء، حزم، توقيع — دون مغادرة VS Code. هذا تحسين حقيقي لجودة العمل.

## البدء

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

أو ابحث عن **WinApp** في عرض الامتدادات (`Ctrl+Shift+X`).

المتطلبات:
- Windows 10 أو أحدث
- VS Code 1.109.0 أو أحدث
- امتداد مصحح الأخطاء للغة تطبيقك

اقرأ [الإعلان الكامل من Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) للمزيد من التفاصيل.

## خلاصة

امتداد WinApp لـ VS Code إضافة مرحب بها لمطوري سطح المكتب .NET على Windows الذين يعيشون في VS Code لكن اضطروا إلى التبديل إلى Visual Studio لأعمال الحزم. هوية الحزمة من F5، حزم MSIX من لوحة الأوامر، إدارة الشهادات مدمجة — هذه هي المجموعة الصحيحة من الميزات.

جربه في مشروع WPF أو WinUI القادم. الاحتكاك الذي كنت تتحايل عليه أصبح الآن أصغر بكثير.
