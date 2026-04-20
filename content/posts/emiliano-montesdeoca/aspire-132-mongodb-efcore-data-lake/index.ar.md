---
title: "Aspire 13.2 يحصل على MongoDB EF Core وAzure Data Lake — تكاملان يستحقان التجربة"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "يُضيف Aspire 13.2 تكامل MongoDB Entity Framework Core وAzure Data Lake Storage مع فحوصات صحة تلقائية واكتشاف الخدمات. إليك كيف يبدو ذلك عملياً."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

وصل Aspire 13.2 بتكاملين جديدين لقواعد البيانات يستحقان الاهتمام: MongoDB Entity Framework Core وAzure Data Lake Storage.

## MongoDB تلتقي EF Core في Aspire

هذا ما أتحمس له أكثر. دعم Aspire MongoDB منذ فترة، لكنه كان دائماً المشغّل الأصلي — لا EF Core، لا DbContext، لا استعلامات LINQ. الآن تحصل على تجربة EF Core الكاملة مع MongoDB، مع فحوصات الصحة التلقائية واكتشاف الخدمات من Aspire.

الإعداد في AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

في المشروع المستهلك:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

وسجّل DbContext:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

يتعامل التكامل مع connection pooling وتتبعات OpenTelemetry وفحوصات الصحة خلف الكواليس.

## Azure Data Lake Storage ينضم إلى الحفلة

في AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

في المشروع المستهلك:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

لا إدارة يدوية لسلاسل الاتصال، لا بحث عن بيانات الاعتماد.

## خلاصة

Aspire 13.2 إصدار تدريجي، لكن تكاملات MongoDB EF Core وData Lake تملأ فجوات حقيقية. [قم بالترقية إلى 13.2](https://get.aspire.dev) وجرّبها.
