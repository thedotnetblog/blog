---
title: "Aspire 13.2 يضيف MongoDB EF Core وAzure Data Lake — تكاملان يستحقان التجربة"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يُضيف Aspire 13.2 تكاملَي MongoDB Entity Framework Core وAzure Data Lake Storage مع فحوصات صحة وسرد خدمات بدون إعداد. إليك شكلهما في التطبيق العملي."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

صدر Aspire 13.2 للتو مع [تكاملَين جديدَين لقواعد البيانات](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) يستحقان اهتمامك: MongoDB Entity Framework Core وAzure Data Lake Storage. إذا كنت تريد استخدام EF Core مع MongoDB في تطبيق Aspire، أو تحتاج إلى ربط أعباء عمل data lake مع سرد خدمات صحيح، فهذا الإصدار يقدّم الاثنين.

## MongoDB يلتقي بـ EF Core في Aspire

هذا هو ما أنا أكثر حماساً له. دعمت Aspire MongoDB لفترة، لكنه كان دائماً المشغّل الخام — لا EF Core، ولا `DbContext`، ولا استعلامات LINQ مقابل مستنداتك. الآن تحصل على تجربة EF Core الكاملة مع MongoDB، بالإضافة إلى فحوصات الصحة التلقائية وسرد الخدمات من Aspire.

الإعداد يتبع نمط Aspire المعتاد. في AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

ثم في مشروعك المُستهلِك، أضف تكامل EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

وسجّل `DbContext` الخاص بك:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

من هنا، الأمر EF Core قياسي. عرّف كياناتك، استخدم `DbContext` كما تفعل مع أي مزوّد آخر. يعالج التكامل تجميع الاتصالات وتتبعات OpenTelemetry وفحوصات الصحة خلف الكواليس.

لمطوّري .NET الذين استخدموا MongoDB مع المشغّل الخام وربطوا سلاسل الاتصال يدوياً، هذا تحسين ملموس في جودة الحياة. تحصل على تجريد EF Core الكامل دون فقدان سرد خدمات Aspire.

## Azure Data Lake Storage ينضم إلى الحفلة

الإضافة الكبيرة الثانية هي [تكامل Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). إذا كنت تبني مسارات بيانات أو عمليات ETL أو منصات تحليلات، يمكنك الآن ربط موارد Data Lake بنفس الطريقة التي تربط بها أي تبعية Aspire أخرى.

في AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

في المشروع المُستهلِك:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

لا إدارة يدوية لسلاسل الاتصال، ولا بحث عن بيانات الاعتماد. تُوفّر Aspire الموارد وتحقنها. لمن يبنون تطبيقات .NET سحابية أصلية تلمس كلاً من البيانات التشغيلية وأعباء عمل التحليلات، يجعل هذا data lake مواطناً من الدرجة الأولى في نموذج Aspire.

## الإصلاحات الصغيرة التي تهمّ

بعيداً عن الميزات الرئيسية، هناك بعض تحسينات جودة الحياة التي تستحق الذكر:

- **إصلاح سلسلة اتصال MongoDB** — الشرطة المائلة للأمام قبل اسم قاعدة البيانات تُعالَج الآن بشكل صحيح. إذا كنت تعمل حول هذه المشكلة، يمكنك إزالة الحل البديل
- **تصدير SQL Server** — يُصدّر `Aspire.Hosting.SqlServer` الآن خيارات إعداد خادم إضافية للتحكم الدقيق
- **تحديثات المحاكيات** — محاكي ServiceBus 2.0.0، ومحاكي App Configuration 1.0.2، والمحاكي التجريبي لـ CosmosDB يتضمن الآن فحص الجاهزية
- **Azure Managed Redis** — يُعيَّن الآن افتراضياً إلى `rediss://` (Redis Secure)، لذا الاتصالات مشفّرة بشكل افتراضي

ذلك الأخير دقيق لكن مهمّ — Redis المشفّر افتراضياً يعني شيئاً أقل للإعداد في الإنتاج.

## خلاصة القول

Aspire 13.2 إصدار تدريجي، لكن تكاملَي MongoDB EF Core وData Lake يسدّان فجوات حقيقية. إذا كنت تنتظر دعماً صحيحاً لـ EF Core مع MongoDB في Aspire، أو احتجت Data Lake أن يكون تبعية من الدرجة الأولى، [قم بالترقية إلى 13.2](https://get.aspire.dev) وجرّبهما. يُسقّل الأمر `aspire add` كل ما تحتاجه.

اقرأ [ملاحظات الإصدار الكاملة](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) لمزيد من التفاصيل، واطّلع على [معرض التكاملات](https://aspire.dev/integrations/gallery/) للقائمة الكاملة.
