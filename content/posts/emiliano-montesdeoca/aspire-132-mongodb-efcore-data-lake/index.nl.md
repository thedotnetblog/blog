---
title: "Aspire 13.2 Krijgt MongoDB EF Core en Azure Data Lake — Twee Integraties Die het Proberen Waard Zijn"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 voegt MongoDB Entity Framework Core en Azure Data Lake Storage-integraties toe met automatische health checks en service discovery. Zo zien ze eruit in de praktijk."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 is geland met twee nieuwe database-integraties die de moeite waard zijn: MongoDB Entity Framework Core en Azure Data Lake Storage.

## MongoDB ontmoet EF Core in Aspire

Aspire ondersteunde MongoDB al een tijdje, maar het was altijd de ruwe driver — geen EF Core, geen DbContext, geen LINQ-query's. Nu krijg je de volledige EF Core-ervaring met MongoDB, samen met Aspire's automatische health checks en service discovery.

Instellingen in AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

In het verbruikende project:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Registreer je DbContext:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

De integratie regelt connection pooling, OpenTelemetry-traces en health checks achter de schermen.

## Azure Data Lake Storage doet mee

In AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

In het verbruikende project:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Geen handmatig beheer van verbindingsstrings, geen zoektocht naar inloggegevens.

## Samenvatting

Aspire 13.2 is een incrementele release, maar de MongoDB EF Core en Data Lake-integraties vullen echte gaten. [Upgrade naar 13.2](https://get.aspire.dev) en probeer ze uit.
