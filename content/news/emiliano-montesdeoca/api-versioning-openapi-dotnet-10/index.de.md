---
title: "API-Versionierung mit OpenAPI in .NET 10 kombinieren"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 ist die erste Version mit offiziellem Support für .NET 10 und Microsoft.AspNetCore.OpenApi — mit separaten OpenAPI-Dokumenten pro API-Version."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[API-Versionierung mit OpenAPI in .NET 10 kombinieren](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Gastbeitrag von Microsoft MVP Sander ten Brinke — beschreibt das neue Paket `Asp.Versioning` v10, die erste Version, die speziell für .NET 10 und die integrierte Bibliothek `Microsoft.AspNetCore.OpenApi` entwickelt wurde, die Swashbuckle in .NET 9 als Standard abgelöst hat.

## Asp.Versioning v10: gebaut für den neuen OpenAPI-Stack

Die bisherige `Asp.Versioning` v8.x läuft auf .NET 10 noch über implizites Roll-Forward weiter, aber v10 ist die erste Version, die speziell für `Microsoft.AspNetCore.OpenApi` ausgelegt ist. Die entscheidende Konfiguration ist ein Aufruf von `AddApiVersioning`, verkettet mit `AddApiExplorer`, plus ein separater `AddOpenApi`-Aufruf für jede Version:

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

Das erzeugt separate Dokumente unter `/openapi/v1.json` und `/openapi/v2.json`.

## Versionierungsstrategien: URL-Pfad, Query String, Header, Media Type

Das Paket unterstützt vier Strategien. URL-Pfad-Versionierung (`/api/v1/resource`) ist am gebräuchlichsten bei öffentlichen APIs. Query String (`?version=1.0`) und eigene Header (`X-API-Version`) sind bei internen Diensten verbreitet. Media-Type-Versionierung über den `Accept`-Header ist der Ansatz, den GitHub für seine REST API verwendet.

## Unterstützung für Minimal APIs und Controllers

Bei Minimal APIs erstellt man ein Versions-Set und mappt jede Route auf eine bestimmte Version:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Bei Controllers werden `[ApiVersion("1.0")]`- und `[MapToApiVersion("1.0")]`-Attribute auf Klassen- und Methodenebene gesetzt.

## SwaggerUI und Scalar funktionieren sofort

Sowohl `Swashbuckle.AspNetCore.SwaggerUI` als auch `Scalar.AspNetCore` lassen sich problemlos integrieren — einfach auf die versionsspezifischen Dokument-URLs verweisen und man erhält eine versionsbeWusste UI ohne zusätzliche Konfiguration.

## Codebeispiele nutzen .NET 10 dateibasierte Apps

Die Beispiele im Artikel verwenden das neue dateibasierte App-Feature von C# 14 / .NET 10: Eine einzelne `.cs`-Datei wird mit `dotnet <dateiname>.cs` ausgeführt, ohne Projektdatei. Das macht die Snippets in sich geschlossen und lokal leicht ausprobierbar.

## Fazit

Wer auf .NET 10 setzt und saubere, versionierte OpenAPI-Verträge ohne Drittanbieter-Middleware möchte, findet in `Asp.Versioning` v10 den offiziellen Weg.

Zum vollständigen Artikel: [API-Versionierung mit OpenAPI in .NET 10 kombinieren](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
