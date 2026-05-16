---
title: "在 .NET 10 中结合 API 版本控制与 OpenAPI"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 是首个正式支持 .NET 10 和 Microsoft.AspNetCore.OpenApi 的版本，可为每个 API 版本生成独立的 OpenAPI 文档。"
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[在 .NET 10 中结合 API 版本控制与 OpenAPI](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Microsoft MVP Sander ten Brinke 的特邀文章 — 介绍了新的 `Asp.Versioning` v10 包，这是专为 .NET 10 和内置库 `Microsoft.AspNetCore.OpenApi` 设计的首个版本，该内置库在 .NET 9 中取代了 Swashbuckle 成为默认选项。

## Asp.Versioning v10：专为新 OpenAPI 栈而设计

旧版 `Asp.Versioning` v8.x 仍可通过隐式 roll-forward 在 .NET 10 上运行，但 v10 是专为 `Microsoft.AspNetCore.OpenApi` 设计的首个版本。核心配置是将 `AddApiVersioning` 与 `AddApiExplorer` 链式调用，并为每个要公开的版本单独调用 `AddOpenApi`：

```csharp
builder.Services.AddApiVersioning(options => {
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
})
.AddApiExplorer(options => {
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddOpenApi("v1");
builder.Services.AddOpenApi("v2");
```

这将在 `/openapi/v1.json` 和 `/openapi/v2.json` 分别生成独立文档。

## 版本控制策略：URL 路径、查询字符串、请求头、媒体类型

该包支持四种策略。URL 路径版本控制（`/api/v1/resource`）是公共 API 最常见的方式。查询字符串（`?version=1.0`）和自定义请求头（`X-API-Version`）在内部服务中很受欢迎。通过 `Accept` 请求头进行媒体类型版本控制是 GitHub 在其 REST API 中采用的方式。

## 同时支持 Minimal API 和 Controller

对于 Minimal API，需要创建版本集并将每个路由映射到特定版本：

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

对于 Controller，在类和操作级别应用 `[ApiVersion("1.0")]` 和 `[MapToApiVersion("1.0")]` 特性。

## SwaggerUI 和 Scalar 开箱即用

`Swashbuckle.AspNetCore.SwaggerUI` 和 `Scalar.AspNetCore` 都能无缝集成 — 只需将它们指向各版本的文档 URL，无需额外配置即可获得支持版本的 UI。

## 代码示例使用 .NET 10 基于文件的应用

文章中的示例使用了 C# 14 / .NET 10 的新基于文件的应用功能：无需项目文件，直接用 `dotnet <文件名>.cs` 运行单个 `.cs` 文件。这使代码片段自成一体，便于本地快速试验。

## 总结

如果您正在使用 .NET 10，并希望在不引入第三方中间件的情况下获得干净、有版本控制的 OpenAPI 契约，`Asp.Versioning` v10 是官方推荐路径。

阅读完整文章：[在 .NET 10 中结合 API 版本控制与 OpenAPI](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
