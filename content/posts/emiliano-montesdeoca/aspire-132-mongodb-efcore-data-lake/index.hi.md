---
title: "Aspire 13.2 में MongoDB EF Core और Azure Data Lake — दो Integrations जो आज़माने लायक हैं"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 में MongoDB Entity Framework Core और Azure Data Lake Storage integrations जुड़े हैं, जिनमें zero-config health checks और service discovery है। यहाँ देखें ये व्यवहार में कैसे दिखते हैं।"
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 अभी [दो नए database integrations](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) के साथ आया है जो आपका ध्यान आकर्षित करने के लायक हैं: MongoDB Entity Framework Core और Azure Data Lake Storage। अगर आप Aspire app में EF Core के साथ MongoDB उपयोग करना चाहते थे, या proper service discovery के साथ data lake workloads wire up करने की ज़रूरत थी, तो यह release दोनों deliver करती है।

## MongoDB meets EF Core in Aspire

यह वो है जिसके बारे में मैं सबसे ज़्यादा excited हूँ। Aspire ने काफी समय से MongoDB को support किया है, लेकिन यह हमेशा raw driver था — कोई EF Core नहीं, कोई `DbContext` नहीं, documents के खिलाफ कोई LINQ queries नहीं। अब आपको MongoDB के साथ पूरा EF Core experience मिलता है, plus Aspire के automatic health checks और service discovery।

इसे setup करना typical Aspire pattern है। अपने AppHost में:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

फिर अपने consuming project में, EF Core integration जोड़ें:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

और अपना `DbContext` register करें:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

वहाँ से, यह standard EF Core है। अपनी entities define करें, अपने `DbContext` को किसी भी दूसरे provider की तरह उपयोग करें। Integration connection pooling, OpenTelemetry traces और health checks को behind the scenes handle करता है।

.NET developers के लिए जो raw driver के साथ MongoDB उपयोग कर रहे थे और manually connection strings wire up कर रहे थे, यह एक अच्छा quality-of-life upgrade है। आपको Aspire की service discovery खोए बिना पूरा EF Core abstraction मिलता है।

## Azure Data Lake Storage पार्टी में शामिल हुई

दूसरा बड़ा addition एक [Azure Data Lake Storage (ADLS) integration](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/) है। अगर आप data pipelines, ETL processes, या analytics platforms बना रहे हैं, तो अब आप Data Lake resources को उसी तरह wire up कर सकते हैं जैसे आप किसी दूसरी Aspire dependency को करते हैं।

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

कोई manual connection string management नहीं, कोई credential hunting नहीं। Aspire resources provision करता है और उन्हें inject करता है। जो लोग cloud-native .NET apps बना रहे हैं जो operational data और analytics workloads दोनों को handle करती हैं, उनके लिए यह data lake को Aspire model में एक first-class citizen जैसा महसूस कराता है।

## छोटे fixes जो मायने रखते हैं

Headline features के अलावा, कुछ quality-of-life improvements भी हैं जो ध्यान देने योग्य हैं:

- **MongoDB connection string fix** — database name से पहले forward slash अब सही तरीके से handle होता है। अगर आप इसके आसपास काम कर रहे थे, तो आप वह workaround हटा सकते हैं
- **SQL Server exports** — `Aspire.Hosting.SqlServer` अब finer-grained control के लिए additional server configuration options export करता है
- **Emulator updates** — ServiceBus emulator 2.0.0, App Configuration emulator 1.0.2, और CosmosDB का preview emulator अब readiness check शामिल करता है
- **Azure Managed Redis** — अब default रूप से `rediss://` (Redis Secure) है, इसलिए connections out of the box encrypted हैं

वह आखिरी वाला subtle लेकिन important है — default रूप से encrypted Redis का मतलब है production में configure करने के लिए एक कम चीज़।

## अंत में

Aspire 13.2 एक incremental release है, लेकिन MongoDB EF Core और Data Lake integrations real gaps भरते हैं। अगर आप Aspire में MongoDB के साथ proper EF Core support का इंतज़ार कर रहे थे, या Data Lake को first-class dependency बनाने की ज़रूरत थी, तो [13.2 पर upgrade करें](https://get.aspire.dev) और इन्हें आज़माएं। `aspire add` command आपको ज़रूरत की सब कुछ scaffold कर देती है।

अधिक details के लिए [full release notes](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) पढ़ें, और पूरी list के लिए [integration gallery](https://aspire.dev/integrations/gallery/) देखें।
