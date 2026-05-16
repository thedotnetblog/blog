---
title: "Combiner le versionnement d'API avec OpenAPI dans .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 est la première version avec support officiel pour .NET 10 et Microsoft.AspNetCore.OpenApi, générant des documents OpenAPI séparés par version d'API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Combiner le versionnement d'API avec OpenAPI dans .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — article invité du MVP Microsoft Sander ten Brinke — présente le nouveau package `Asp.Versioning` v10, la première version conçue spécifiquement pour .NET 10 et la bibliothèque intégrée `Microsoft.AspNetCore.OpenApi` qui a remplacé Swashbuckle comme option par défaut dans .NET 9.

## Asp.Versioning v10 : conçu pour le nouveau stack OpenAPI

L'ancienne `Asp.Versioning` v8.x continue de fonctionner sur .NET 10 via le roll-forward implicite, mais v10 est la première version pensée spécifiquement pour `Microsoft.AspNetCore.OpenApi`. La configuration clé est un appel à `AddApiVersioning` enchaîné avec `AddApiExplorer`, plus un appel séparé à `AddOpenApi` pour chaque version que vous souhaitez exposer :

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

Cela produit des documents séparés à `/openapi/v1.json` et `/openapi/v2.json`.

## Stratégies de versionnement : chemin URL, query string, en-tête, media type

Le package supporte quatre stratégies. Le versionnement par chemin URL (`/api/v1/resource`) est le plus courant pour les APIs publiques. La query string (`?version=1.0`) et l'en-tête personnalisé (`X-API-Version`) sont populaires pour les services internes. Le versionnement par media type via l'en-tête `Accept` est celui qu'utilise GitHub pour son API REST.

## Compatible avec les Minimal APIs et les Controllers

Pour les Minimal APIs, on crée un ensemble de versions et on mappe chaque route à une version spécifique :

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Pour les Controllers, on applique les attributs `[ApiVersion("1.0")]` et `[MapToApiVersion("1.0")]` au niveau de la classe et de l'action.

## SwaggerUI et Scalar fonctionnent sans configuration supplémentaire

`Swashbuckle.AspNetCore.SwaggerUI` et `Scalar.AspNetCore` s'intègrent sans friction — il suffit de les pointer vers les URLs de documents par version pour obtenir une interface versionnée sans plumbing additionnel.

## Les exemples de code utilisent les apps fichier de .NET 10

Les exemples de l'article utilisent la nouvelle fonctionnalité d'apps basées sur les fichiers de C# 14 / .NET 10 : on exécute un seul fichier `.cs` avec `dotnet <nomfichier>.cs`, sans fichier de projet. Les snippets sont ainsi autonomes et faciles à essayer en local.

## En résumé

Si vous utilisez .NET 10 et souhaitez des contrats OpenAPI versionnés et propres sans middleware tiers, `Asp.Versioning` v10 est la voie officielle.

Lire l'article complet : [Combiner le versionnement d'API avec OpenAPI dans .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
