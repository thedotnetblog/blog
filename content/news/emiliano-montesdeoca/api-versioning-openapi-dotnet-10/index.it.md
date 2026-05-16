---
title: "Combinare il versionamento API con OpenAPI in .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 è la prima versione con supporto ufficiale per .NET 10 e Microsoft.AspNetCore.OpenApi, generando documenti OpenAPI separati per versione API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Combinare il versionamento API con OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — articolo ospite del Microsoft MVP Sander ten Brinke — illustra il nuovo pacchetto `Asp.Versioning` v10, la prima versione progettata specificamente per .NET 10 e la libreria integrata `Microsoft.AspNetCore.OpenApi` che ha sostituito Swashbuckle come default in .NET 9.

## Asp.Versioning v10: progettato per il nuovo stack OpenAPI

La precedente `Asp.Versioning` v8.x continua a funzionare su .NET 10 tramite roll-forward implicito, ma v10 è la prima versione pensata appositamente per `Microsoft.AspNetCore.OpenApi`. La configurazione chiave è una chiamata a `AddApiVersioning` concatenata con `AddApiExplorer`, più una chiamata separata a `AddOpenApi` per ogni versione da esporre:

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

Questo produce documenti separati a `/openapi/v1.json` e `/openapi/v2.json`.

## Strategie di versioning: URL path, query string, header, media type

Il pacchetto supporta quattro strategie. Il versioning via URL path (`/api/v1/resource`) è il più comune per le API pubbliche. La query string (`?version=1.0`) e l'header personalizzato (`X-API-Version`) sono diffusi nei servizi interni. Il versioning via media type attraverso l'header `Accept` è quello usato da GitHub per la sua REST API.

## Supporto per Minimal APIs e Controllers

Per le Minimal APIs, si crea un version set e si mappa ogni route a una versione specifica:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Per i Controllers si applicano gli attributi `[ApiVersion("1.0")]` e `[MapToApiVersion("1.0")]` a livello di classe e action.

## SwaggerUI e Scalar funzionano subito

Sia `Swashbuckle.AspNetCore.SwaggerUI` che `Scalar.AspNetCore` si integrano senza problemi — basta puntarli agli URL dei documenti per versione per ottenere una UI version-aware senza configurazione aggiuntiva.

## Gli esempi di codice usano le file-based app di .NET 10

Gli esempi dell'articolo usano la nuova funzionalità file-based app di C# 14 / .NET 10: si esegue un singolo file `.cs` con `dotnet <nomefile>.cs`, senza file di progetto. I frammenti sono autocontenuti e facili da provare in locale.

## Conclusione

Se usi .NET 10 e vuoi contratti OpenAPI versionati e puliti senza aggiungere middleware di terze parti, `Asp.Versioning` v10 è la strada ufficiale.

Leggi l'articolo completo: [Combinare il versionamento API con OpenAPI in .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
