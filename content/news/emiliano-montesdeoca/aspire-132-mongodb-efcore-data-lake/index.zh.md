---
title: "Aspire 13.2 新增 MongoDB EF Core 和 Azure Data Lake — 两个值得尝试的集成"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 新增了 MongoDB Entity Framework Core 和 Azure Data Lake Storage 集成，支持零配置健康检查和服务发现。来看看它们在实践中是什么样的。"
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}})。*

Aspire 13.2 刚刚发布，带来了[两个新的数据库集成](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/)，值得关注：MongoDB Entity Framework Core 和 Azure Data Lake Storage。如果你一直想在 Aspire 应用中使用 EF Core 操作 MongoDB，或者需要将 Data Lake 工作负载与服务发现连接起来，这个版本同时满足了这两个需求。

## MongoDB 在 Aspire 中遇见 EF Core

这是让我最兴奋的一个。Aspire 支持 MongoDB 已经有一段时间了，但一直是原始驱动程序——没有 EF Core，没有 `DbContext`，没有对文档的 LINQ 查询。现在你可以获得完整的 EF Core 体验配合 MongoDB，加上 Aspire 的自动健康检查和服务发现。

配置遵循典型的 Aspire 模式。在你的 AppHost 中：

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

然后在消费项目中，添加 EF Core 集成：

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

注册你的 `DbContext`：

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

接下来就是标准的 EF Core 了。定义你的实体，像使用其他任何提供程序一样使用 `DbContext`。集成会在后台处理连接池、OpenTelemetry 跟踪和健康检查。

对于那些一直使用原始驱动程序操作 MongoDB 并手动配置连接字符串的 .NET 开发者来说，这是一个很好的体验提升。你可以获得完整的 EF Core 抽象，同时不会失去 Aspire 的服务发现。

## Azure Data Lake Storage 加入阵营

第二个重大新增是 [Azure Data Lake Storage (ADLS) 集成](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/)。如果你正在构建数据管道、ETL 流程或分析平台，现在可以像连接其他 Aspire 依赖项一样连接 Data Lake 资源。

在 AppHost 中：

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

在消费项目中：

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

不需要手动管理连接字符串，不需要四处寻找凭据。Aspire 负责资源的预配和注入。对于我们这些构建同时涉及运营数据和分析工作负载的云原生 .NET 应用的人来说，这让 Data Lake 在 Aspire 模型中真正成为了一等公民。

## 值得关注的小修复

除了主要功能之外，还有一些值得一提的改进：

- **MongoDB 连接字符串修复** — 数据库名称前的斜杠现在可以正确处理了。如果你之前有临时解决方案，现在可以移除了
- **SQL Server 导出** — `Aspire.Hosting.SqlServer` 现在导出额外的服务器配置选项，提供更精细的控制
- **模拟器更新** — ServiceBus 模拟器 2.0.0、App Configuration 模拟器 1.0.2，CosmosDB 的预览模拟器现在包含就绪检查
- **Azure Managed Redis** — 现在默认使用 `rediss://`（Redis Secure），连接开箱即加密

最后一点虽然不起眼但很重要——默认加密的 Redis 意味着生产环境中少了一项需要配置的东西。

## 总结

Aspire 13.2 是一个增量版本，但 MongoDB EF Core 和 Data Lake 集成填补了真实的空白。如果你一直在等待 Aspire 中 MongoDB 的正式 EF Core 支持，或者需要 Data Lake 成为一等依赖项，[升级到 13.2](https://get.aspire.dev) 试试看吧。`aspire add` 命令会为你生成所需的一切。

阅读[完整的发行说明](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates)了解更多详情，查看[集成库](https://aspire.dev/integrations/gallery/)获取完整列表。
