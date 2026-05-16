---
title: "Combining API Versioning with OpenAPI in .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 is the first release to officially support both .NET 10 and Microsoft.AspNetCore.OpenApi, generating separate OpenAPI documents per API version out of the box."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

[Combining API Versioning with OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — guest post by Microsoft MVP Sander ten Brinke — walks through the new `Asp.Versioning` v10 package, the first version purpose-built for both .NET 10 and the built-in `Microsoft.AspNetCore.OpenApi` library that replaced Swashbuckle as the default in .NET 9.

## Asp.Versioning v10: purpose-built for the new OpenAPI stack

The previous `Asp.Versioning` v8.x still works on .NET 10 via implicit roll-forward, but v10 is the first release designed specifically for `Microsoft.AspNetCore.OpenApi`. The key wiring is a call to `AddApiVersioning` chained with `AddApiExplorer`, plus a separate `AddOpenApi` call per version you want to expose:

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

This produces separate documents at `/openapi/v1.json` and `/openapi/v2.json`.

## Versioning strategies: URL path, query string, header, media type

The package supports four strategies. URL path versioning (`/api/v1/resource`) is the most common for public APIs. Query string (`?version=1.0`) and custom header (`X-API-Version`) are popular for internal services. Media type versioning via the `Accept` header is what GitHub uses for its REST API.

## Minimal APIs and Controllers both supported

For Minimal APIs, you build a version set and map each route to a specific version:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

For Controllers, you apply `[ApiVersion("1.0")]` and `[MapToApiVersion("1.0")]` attributes at the class and action level.

## SwaggerUI and Scalar work out of the box

Both `Swashbuckle.AspNetCore.SwaggerUI` and `Scalar.AspNetCore` integrate cleanly — you point them at the per-version document URLs and get a version-aware UI without extra plumbing.

## Code samples use .NET 10 file-based apps

The article's examples use C# 14 / .NET 10's new file-based app feature: you run a single `.cs` file with `dotnet <filename>.cs`, no project file required. It makes the snippets self-contained and easy to try locally.

## Wrapping up

If you're running .NET 10 and want clean, versioned OpenAPI contracts without bolting on third-party middleware, `Asp.Versioning` v10 is the official path forward.

Read the full post: [Combining API Versioning with OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
