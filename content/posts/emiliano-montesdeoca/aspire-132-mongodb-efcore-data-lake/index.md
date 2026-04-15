---
title: "Aspire 13.2 Gets MongoDB EF Core and Azure Data Lake — Two Integrations Worth Trying"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 adds MongoDB Entity Framework Core and Azure Data Lake Storage integrations with zero-config health checks and service discovery. Here's what they look like in practice."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

Aspire 13.2 just landed with [two new database integrations](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) that are worth your attention: MongoDB Entity Framework Core and Azure Data Lake Storage. If you've been wanting to use EF Core with MongoDB in an Aspire app, or need to wire up data lake workloads with proper service discovery, this release delivers both.

## MongoDB meets EF Core in Aspire

This is the one I'm most excited about. Aspire has supported MongoDB for a while, but it was always the raw driver — no EF Core, no `DbContext`, no LINQ queries against your documents. Now you get the full EF Core experience with MongoDB, plus Aspire's automatic health checks and service discovery.

Setting it up is the typical Aspire pattern. In your AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Then in your consuming project, add the EF Core integration:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

And register your `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

From there, it's standard EF Core. Define your entities, use your `DbContext` like you would with any other provider. The integration handles connection pooling, OpenTelemetry traces, and health checks behind the scenes.

For .NET developers who've been using MongoDB with the raw driver and manually wiring up connection strings, this is a nice quality-of-life upgrade. You get the full EF Core abstraction without losing Aspire's service discovery.

## Azure Data Lake Storage joins the party

The second big addition is an [Azure Data Lake Storage (ADLS) integration](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). If you're building data pipelines, ETL processes, or analytics platforms, you can now wire up Data Lake resources the same way you'd wire up any other Aspire dependency.

In the AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

In the consuming project:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

No manual connection string management, no credential hunting. Aspire provisions resources and injects them. For those of us building cloud-native .NET apps that touch both operational data and analytics workloads, this makes the data lake feel like a first-class citizen in the Aspire model.

## The small fixes that matter

Beyond the headline features, there are a few quality-of-life improvements worth noting:

- **MongoDB connection string fix** — the forward slash before the database name is now handled correctly. If you've been working around this, you can remove that workaround
- **SQL Server exports** — `Aspire.Hosting.SqlServer` now exports additional server configuration options for finer-grained control
- **Emulator updates** — ServiceBus emulator 2.0.0, App Configuration emulator 1.0.2, and CosmosDB's preview emulator now includes a readiness check
- **Azure Managed Redis** — now defaults to `rediss://` (Redis Secure), so connections are encrypted out of the box

That last one is subtle but important — encrypted Redis by default means one less thing to configure in production.

## Wrapping up

Aspire 13.2 is an incremental release, but the MongoDB EF Core and Data Lake integrations fill real gaps. If you've been waiting for proper EF Core support with MongoDB in Aspire, or needed Data Lake to be a first-class dependency, [upgrade to 13.2](https://get.aspire.dev) and give them a spin. The `aspire add` command scaffolds everything you need.

Read the [full release notes](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) for more details, and check out the [integration gallery](https://aspire.dev/integrations/gallery/) for the complete list.
