---
title: "الجمع بين إدارة إصدارات API وOpenAPI في .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 هو أول إصدار يدعم رسمياً كلاً من .NET 10 وMicrosoft.AspNetCore.OpenApi، مع توليد مستندات OpenAPI منفصلة لكل إصدار من API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
dir: rtl
---

*تمت ترجمة هذا المنشور تلقائيًا. للنسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

[الجمع بين إدارة إصدارات API وOpenAPI في .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — مقال ضيف من مايكروسوفت MVP ساندر تن برينكه — يشرح حزمة `Asp.Versioning` v10 الجديدة، وهي أول إصدار مصمم خصيصاً لـ .NET 10 ومكتبة `Microsoft.AspNetCore.OpenApi` المدمجة التي حلّت محل Swashbuckle كخيار افتراضي في .NET 9.

## Asp.Versioning v10: مصمم للمكدس الجديد من OpenAPI

النسخة السابقة `Asp.Versioning` v8.x لا تزال تعمل على .NET 10 عبر roll-forward الضمني، لكن v10 هو أول إصدار مصمم خصيصاً لـ `Microsoft.AspNetCore.OpenApi`. الإعداد الأساسي هو استدعاء `AddApiVersioning` متسلسلاً مع `AddApiExplorer`، مع استدعاء منفصل لـ `AddOpenApi` لكل إصدار تريد الكشف عنه:

```csharp
builder.Services.AddApiVersioning(options => {
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
})
.AddApiExplorer(options => {
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddOpenApi("v1");
builder.Services.AddOpenApi("v2");
```

ينتج عن ذلك مستندات منفصلة على `/openapi/v1.json` و `/openapi/v2.json`.

## استراتيجيات الإصدار: مسار URL، query string، الترويسة، media type

تدعم الحزمة أربع استراتيجيات. الإصدار عبر مسار URL (`/api/v1/resource`) هو الأكثر شيوعاً للـ APIs العامة. الـ query string (`?version=1.0`) والترويسة المخصصة (`X-API-Version`) شائعتان في الخدمات الداخلية. الإصدار عبر media type من خلال ترويسة `Accept` هو ما تستخدمه GitHub في REST API الخاصة بها.

## دعم كامل لـ Minimal APIs والـ Controllers

لـ Minimal APIs، تبني مجموعة إصدارات وتعيّن كل مسار لإصدار محدد:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

للـ Controllers، تُطبّق سمات `[ApiVersion("1.0")]` و `[MapToApiVersion("1.0")]` على مستوى الفئة والإجراء.

## SwaggerUI وScalar يعملان بشكل فوري

يتكامل كل من `Swashbuckle.AspNetCore.SwaggerUI` و `Scalar.AspNetCore` بسلاسة — فقط وجّههما إلى عناوين URL للمستندات لكل إصدار وستحصل على واجهة تدعم الإصدارات دون إعداد إضافي.

## أمثلة الكود تستخدم تطبيقات الملف الواحد في .NET 10

تستخدم أمثلة المقال ميزة التطبيقات المستندة إلى الملفات الجديدة في C# 14 / .NET 10: تشغيل ملف `.cs` واحد باستخدام `dotnet <اسم_الملف>.cs` دون الحاجة لملف مشروع. هذا يجعل المقتطفات مكتفية بذاتها وسهلة التجربة محلياً.

## خلاصة

إذا كنت تعمل على .NET 10 وتريد عقود OpenAPI نظيفة وذات إصدارات دون إضافة middleware من جهات خارجية، فإن `Asp.Versioning` v10 هو المسار الرسمي.

اقرأ المقال الكامل: [الجمع بين إدارة إصدارات API وOpenAPI في .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
