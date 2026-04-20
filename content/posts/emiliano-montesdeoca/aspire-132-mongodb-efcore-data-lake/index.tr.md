---
title: "Aspire 13.2'ye MongoDB EF Core ve Azure Data Lake Geldi — Denemeye Değer İki Entegrasyon"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, sıfır yapılandırmada health check ve service discovery ile MongoDB Entity Framework Core ve Azure Data Lake Storage entegrasyonları ekliyor. Bunlar pratikte nasıl görünüyor."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2, dikkat etmeye değer iki yeni veritabanı entegrasyonuyla geldi: MongoDB Entity Framework Core ve Azure Data Lake Storage.

## MongoDB, Aspire'de EF Core ile buluşuyor

Aspire bir süredir MongoDB'yi destekliyordu, ancak her zaman ham sürücüydü — EF Core yok, DbContext yok, LINQ sorguları yok. Artık MongoDB ile tam EF Core deneyimini alıyorsunuz; Aspire'nin otomatik health check'leri ve service discovery'si ile birlikte.

AppHost'ta kurulum:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Tüketen projede:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

DbContext'i kaydedin:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Entegrasyon, bağlantı havuzlaması, OpenTelemetry izleri ve health check'leri arka planda yönetir.

## Azure Data Lake Storage partiye katılıyor

AppHost'ta:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Tüketen projede:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Manuel bağlantı dizisi yönetimi yok, kimlik bilgisi avı yok.

## Sonuç

Aspire 13.2 artımlı bir sürüm, ancak MongoDB EF Core ve Data Lake entegrasyonları gerçek boşlukları dolduruyor. [13.2'ye yükseltin](https://get.aspire.dev) ve deneyin.
