---
title: "API-versiebeheer combineren met OpenAPI in .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 is de eerste versie met officiële ondersteuning voor zowel .NET 10 als Microsoft.AspNetCore.OpenApi, met afzonderlijke OpenAPI-documenten per API-versie."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[API-versiebeheer combineren met OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — gastpost van Microsoft MVP Sander ten Brinke — legt het nieuwe pakket `Asp.Versioning` v10 uit, de eerste versie die specifiek is ontworpen voor .NET 10 en de ingebouwde bibliotheek `Microsoft.AspNetCore.OpenApi` die Swashbuckle als standaard verving in .NET 9.

## Asp.Versioning v10: gebouwd voor de nieuwe OpenAPI-stack

De vorige `Asp.Versioning` v8.x werkt nog steeds op .NET 10 via impliciete roll-forward, maar v10 is de eerste versie die specifiek is ontworpen voor `Microsoft.AspNetCore.OpenApi`. De kerninstelling is een aanroep naar `AddApiVersioning` geketend met `AddApiExplorer`, plus een aparte `AddOpenApi`-aanroep voor elke versie die je wilt blootstellen:

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

Dit levert afzonderlijke documenten op bij `/openapi/v1.json` en `/openapi/v2.json`.

## Versiebeheerstrategieën: URL-pad, query string, header, media type

Het pakket ondersteunt vier strategieën. URL-pad-versiebeheer (`/api/v1/resource`) is het meest voorkomend voor publieke API's. Query string (`?version=1.0`) en aangepaste header (`X-API-Version`) zijn populair voor interne services. Versiebeheer via media type met de `Accept`-header is wat GitHub gebruikt voor zijn REST API.

## Ondersteuning voor Minimal APIs en Controllers

Voor Minimal APIs bouw je een versieset en koppel je elke route aan een specifieke versie:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Voor Controllers pas je `[ApiVersion("1.0")]`- en `[MapToApiVersion("1.0")]`-attributen toe op klasse- en actieniveau.

## SwaggerUI en Scalar werken direct

Zowel `Swashbuckle.AspNetCore.SwaggerUI` als `Scalar.AspNetCore` integreren probleemloos — wijs ze naar de versiespecifieke document-URL's en je krijgt een versie-bewuste UI zonder extra configuratie.

## Codevoorbeelden gebruiken .NET 10 bestandsgebaseerde apps

De voorbeelden in het artikel gebruiken de nieuwe bestandsgebaseerde app-functie van C# 14 / .NET 10: je voert één `.cs`-bestand uit met `dotnet <bestandsnaam>.cs`, zonder projectbestand. Hierdoor zijn de snippets op zichzelf staand en gemakkelijk lokaal te proberen.

## Samenvatting

Als je .NET 10 gebruikt en schone, geversioneerde OpenAPI-contracten wilt zonder middleware van derden toe te voegen, is `Asp.Versioning` v10 de officiële weg.

Lees het volledige artikel: [API-versiebeheer combineren met OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
