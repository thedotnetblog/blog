---
title: "Aspire 13.2 Dostaje MongoDB EF Core i Azure Data Lake — Dwie Integracje Warte Wypróbowania"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 dodaje integracje MongoDB Entity Framework Core i Azure Data Lake Storage z automatycznymi health checks i service discovery. Oto jak wyglądają w praktyce."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 właśnie wylądował z dwiema nowymi integracjami bazodanowymi, które są warte uwagi: MongoDB Entity Framework Core i Azure Data Lake Storage.

## MongoDB spotyka EF Core w Aspire

To ta, z której jestem najbardziej podekscytowany. Aspire obsługiwał MongoDB przez chwilę, ale zawsze był to surowy sterownik — bez EF Core, bez DbContext, bez zapytań LINQ. Teraz otrzymujesz pełne doświadczenie EF Core z MongoDB, wraz z automatycznymi health checks i service discovery Aspire.

Konfiguracja w AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

W projekcie klienckim:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Zarejestruj DbContext:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Integracja obsługuje connection pooling, ślady OpenTelemetry i health checks za kulisami.

## Azure Data Lake Storage dołącza do zabawy

W AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

W projekcie klienckim:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Żadnego ręcznego zarządzania ciągami połączeń, żadnego polowania na poświadczenia.

## Podsumowanie

Aspire 13.2 to wydanie przyrostowe, ale integracje MongoDB EF Core i Data Lake wypełniają rzeczywiste luki. [Zaktualizuj do 13.2](https://get.aspire.dev) i wypróbuj je.
