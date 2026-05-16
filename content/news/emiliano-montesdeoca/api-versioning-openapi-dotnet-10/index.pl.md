---
title: "Łączenie wersjonowania API z OpenAPI w .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 to pierwsza wersja z oficjalnym wsparciem dla .NET 10 i Microsoft.AspNetCore.OpenApi, generująca osobne dokumenty OpenAPI dla każdej wersji API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Łączenie wersjonowania API z OpenAPI w .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — artykuł gościnny Microsoft MVP Sandera ten Brinke — omawia nowy pakiet `Asp.Versioning` v10, pierwszą wersję zaprojektowaną specjalnie dla .NET 10 i wbudowanej biblioteki `Microsoft.AspNetCore.OpenApi`, która zastąpiła Swashbuckle jako domyślną opcję w .NET 9.

## Asp.Versioning v10: stworzony dla nowego stosu OpenAPI

Poprzedni `Asp.Versioning` v8.x nadal działa na .NET 10 dzięki niejawnemu roll-forward, ale v10 to pierwsza wersja zaprojektowana specjalnie pod `Microsoft.AspNetCore.OpenApi`. Kluczowa konfiguracja to wywołanie `AddApiVersioning` połączone z `AddApiExplorer` oraz osobne wywołanie `AddOpenApi` dla każdej wersji, którą chcesz udostępnić:

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

Daje to osobne dokumenty pod `/openapi/v1.json` i `/openapi/v2.json`.

## Strategie wersjonowania: ścieżka URL, query string, nagłówek, media type

Pakiet obsługuje cztery strategie. Wersjonowanie przez ścieżkę URL (`/api/v1/resource`) jest najczęstsze dla publicznych API. Query string (`?version=1.0`) i własny nagłówek (`X-API-Version`) są popularne w usługach wewnętrznych. Wersjonowanie przez media type z nagłówkiem `Accept` to podejście stosowane przez GitHub w jego REST API.

## Wsparcie dla Minimal APIs i Controllers

W przypadku Minimal APIs tworzysz zestaw wersji i mapujesz każdą trasę do konkretnej wersji:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Dla Controllers stosuje się atrybuty `[ApiVersion("1.0")]` i `[MapToApiVersion("1.0")]` na poziomie klasy i akcji.

## SwaggerUI i Scalar działają od razu

Zarówno `Swashbuckle.AspNetCore.SwaggerUI`, jak i `Scalar.AspNetCore` integrują się bezproblemowo — wystarczy wskazać im adresy URL dokumentów dla poszczególnych wersji, a otrzymasz UI z obsługą wersji bez dodatkowej konfiguracji.

## Przykłady kodu używają aplikacji plikowych .NET 10

Przykłady w artykule korzystają z nowej funkcji aplikacji plikowych C# 14 / .NET 10: uruchamiasz pojedynczy plik `.cs` poleceniem `dotnet <nazwaPliku>.cs` bez pliku projektu. Sprawia to, że fragmenty kodu są samowystarczalne i łatwe do wypróbowania lokalnie.

## Podsumowanie

Jeśli używasz .NET 10 i chcesz czystych, wersjonowanych kontraktów OpenAPI bez dodawania middleware firm trzecich, `Asp.Versioning` v10 to oficjalna ścieżka.

Przeczytaj pełny artykuł: [Łączenie wersjonowania API z OpenAPI w .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
