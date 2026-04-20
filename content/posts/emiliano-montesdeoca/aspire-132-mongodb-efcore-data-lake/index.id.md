---
title: "Aspire 13.2 Mendapatkan MongoDB EF Core dan Azure Data Lake — Dua Integrasi yang Patut Dicoba"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 menambahkan integrasi MongoDB Entity Framework Core dan Azure Data Lake Storage dengan health check otomatis dan service discovery. Inilah tampilannya dalam praktik."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 hadir dengan dua integrasi database baru yang patut diperhatikan: MongoDB Entity Framework Core dan Azure Data Lake Storage.

## MongoDB bertemu EF Core di Aspire

Aspire telah mendukung MongoDB untuk sementara, tapi selalu driver mentah — tidak ada EF Core, tidak ada DbContext, tidak ada kueri LINQ. Sekarang Anda mendapatkan pengalaman EF Core penuh dengan MongoDB, beserta health check otomatis dan service discovery dari Aspire.

Pengaturan di AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Di proyek yang menggunakan:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Daftarkan DbContext Anda:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Integrasi menangani connection pooling, trace OpenTelemetry, dan health check di belakang layar.

## Azure Data Lake Storage bergabung

Di AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Di proyek yang menggunakan:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Tidak ada manajemen connection string manual, tidak ada pencarian kredensial.

## Kesimpulan

Aspire 13.2 adalah rilis inkremental, tapi integrasi MongoDB EF Core dan Data Lake mengisi celah nyata. [Upgrade ke 13.2](https://get.aspire.dev) dan coba.
