---
title: "Aspire 13.2 में MongoDB EF Core और Azure Data Lake — दो Integration जो आज़माने लायक हैं"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 में zero-config health checks और service discovery के साथ MongoDB Entity Framework Core और Azure Data Lake Storage integrations आए हैं। व्यवहार में यह कैसा दिखता है।"
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 दो नए database integrations के साथ आया है जो ध्यान देने योग्य हैं: MongoDB Entity Framework Core और Azure Data Lake Storage।

## MongoDB EF Core के साथ मिलता है Aspire में

यह सबसे exciting है। Aspire ने MongoDB को काफी समय से support किया है, लेकिन हमेशा raw driver था — EF Core नहीं, DbContext नहीं, LINQ queries नहीं। अब आपको MongoDB के साथ पूरा EF Core experience मिलता है, Aspire के automatic health checks और service discovery के साथ।

AppHost में:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Consuming project में:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

DbContext register करें:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Integration connection pooling, OpenTelemetry traces और health checks behind the scenes संभालता है।

## Azure Data Lake Storage पार्टी में शामिल हुआ

AppHost में:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Consuming project में:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

कोई manual connection string management नहीं, कोई credential hunting नहीं।

## समापन

Aspire 13.2 एक incremental release है, लेकिन MongoDB EF Core और Data Lake integrations असली gaps भरते हैं। [13.2 में upgrade करें](https://get.aspire.dev) और इन्हें आज़माएं।
