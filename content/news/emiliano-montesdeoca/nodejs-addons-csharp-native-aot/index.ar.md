---
title: "كتابة إضافات Node.js الأصلية بلغة C# مع .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "استبدل فريق C# Dev Kit إضافات Node.js المكتوبة بـ C++ بـ .NET Native AOT — النتيجة أنظف وأكثر أمانًا وتحتاج فقط إلى .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *تُرجِمت هذه المقالة تلقائيًا. للاطلاع على النسخة الأصلية بالإنجليزية، [انقر هنا]({{< ref "index.md" >}}).*

إليك سيناريو أحبه: فريق يعمل على أدوات .NET كان لديه إضافات Node.js أصلية مكتوبة بـ C++ ومُجمَّعة عبر `node-gyp`. كانت تعمل. لكنها كانت تتطلب تثبيت Python على كل جهاز مطوّر — إصدارًا قديمًا من Python — فقط لتجميع حزمة لن يمسّها أحد في الفريق مباشرةً.

فطرحوا سؤالًا معقولًا جدًا: لدينا .NET SDK مثبّت بالفعل، لماذا نكتب C++ أصلًا؟

كانت الإجابة هي Native AOT، والنتيجة أنيقة حقًا. كتب Drew Noakes من فريق C# Dev Kit كيفية القيام بذلك.

## الفكرة الأساسية

إضافة Node.js الأصلية هي مكتبة مشتركة (`.dll` على Windows، `.so` على Linux، `.dylib` على macOS) يمكن لـ Node.js تحميلها في وقت التشغيل. الواجهة تُسمى [N-API](https://nodejs.org/api/n-api.html) — واجهة برمجة تطبيقات C مستقرة ومتوافقة مع ABI. لا يهتم N-API بالغة التي أنتجت المكتبة، فقط أن تُصدِّر الرموز الصحيحة.

يمكن لـ .NET Native AOT تحقيق ذلك تمامًا. يُجمِّع كود C# مسبقًا إلى مكتبة مشتركة أصلية بنقاط دخول اختيارية.

## إعداد المشروع

ملف المشروع في أدنى حد:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` يُخبر SDK بإنتاج مكتبة مشتركة عند `dotnet publish`.

## تصدير نقطة الدخول

يتوقع Node.js أن تُصدِّر مكتبتك `napi_register_module_v1`. في C#، `[UnmanagedCallersOnly]` يفعل ذلك تمامًا:

```csharp
[UnmanagedCallersOnly(
    EntryPoint = "napi_register_module_v1",
    CallConvs = [typeof(CallConvCdecl)])]
public static nint Init(nint env, nint exports)
{
    Initialize();
    RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
    return exports;
}
```

اللاحقة `u8` تُنتج `ReadOnlySpan<byte>` مع قيمة حرفية للسلسلة UTF-8، مُمرَّرة مباشرةً إلى N-API دون أي تخصيص ترميز.

## حل N-API مقابل العملية المضيفة

تُصدَّر دوال N-API من `node.exe` نفسه، وليس من مكتبة منفصلة. لذا بدلًا من الربط بشيء ما، تحلّها مقابل العملية الجارية عند بدء التشغيل:

```csharp
NativeLibrary.SetDllImportResolver(
    System.Reflection.Assembly.GetExecutingAssembly(),
    ResolveDllImport);
```

مع ذلك، تعمل إعلانات P/Invoke بشكل نظيف:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

## استدعاؤه من TypeScript

يُنتج `dotnet publish` مكتبتك الأصلية الخاصة بالمنصة. غيّر اسمها إلى `.node` واستخدمها مع `require()` القياسي:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

هذا كل شيء. من TypeScript إلى C#، بدون Python، بدون C++.

## خلاصة

استبدل فريق C# Dev Kit عبء Python/C++ بكود C# نظيف يعرف كل شخص في الفريق كيفية كتابته وتصحيحه. النمط ليس معقدًا بمجرد رؤيته، وهو مثال رائع على Native AOT يحل مشكلة حقيقية لا تُناقش بما فيه الكفاية.

اقرأ [المقالة الأصلية على مدونة .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
