---
title: "Combinar el versionat d'API amb OpenAPI a .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 és la primera versió amb suport oficial per a .NET 10 i Microsoft.AspNetCore.OpenApi, generant documents OpenAPI separats per versió d'API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[Combinar el versionat d'API amb OpenAPI a .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — article convidat del Microsoft MVP Sander ten Brinke — explica el nou paquet `Asp.Versioning` v10, la primera versió dissenyada específicament per a .NET 10 i la biblioteca integrada `Microsoft.AspNetCore.OpenApi` que va substituir Swashbuckle com a opció predeterminada a .NET 9.

## Asp.Versioning v10: dissenyat per al nou stack d'OpenAPI

La versió anterior `Asp.Versioning` v8.x continua funcionant a .NET 10 mitjançant roll-forward implícit, però v10 és la primera versió dissenyada específicament per a `Microsoft.AspNetCore.OpenApi`. La configuració clau és una crida a `AddApiVersioning` encadenada amb `AddApiExplorer`, més una crida separada a `AddOpenApi` per a cada versió que vols exposar:

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

Això genera documents separats a `/openapi/v1.json` i `/openapi/v2.json`.

## Estratègies de versionat: ruta URL, query string, capçalera, media type

El paquet suporta quatre estratègies. El versionat per ruta URL (`/api/v1/resource`) és el més comú per a APIs públiques. La query string (`?version=1.0`) i la capçalera personalitzada (`X-API-Version`) són populars en serveis interns. El versionat per media type a través de la capçalera `Accept` és el que fa servir GitHub a la seva REST API.

## Compatible amb Minimal APIs i Controllers

Per a Minimal APIs, construeixes un conjunt de versions i mappes cada ruta a una versió específica:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Per a Controllers, s'apliquen els atributs `[ApiVersion("1.0")]` i `[MapToApiVersion("1.0")]` a nivell de classe i acció.

## SwaggerUI i Scalar funcionen sense configuració addicional

Tant `Swashbuckle.AspNetCore.SwaggerUI` com `Scalar.AspNetCore` s'integren sense problemes — simplement apuntes a les URLs dels documents per versió i obtens una interfície amb suport de versions sense cap plumbing extra.

## Els exemples de codi usen apps d'arxiu de .NET 10

Els exemples de l'article fan servir la nova funcionalitat d'apps basades en arxius de C# 14 / .NET 10: s'executa un únic arxiu `.cs` amb `dotnet <nomarxiu>.cs`, sense necessitat d'un arxiu de projecte. Això fa que els fragments siguin autocontinguts i fàcils de provar localment.

## Conclusió

Si uses .NET 10 i vols contractes OpenAPI versionats i nets sense afegir middleware de tercers, `Asp.Versioning` v10 és el camí oficial.

Llegeix l'article complet: [Combinar el versionat d'API amb OpenAPI a .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
