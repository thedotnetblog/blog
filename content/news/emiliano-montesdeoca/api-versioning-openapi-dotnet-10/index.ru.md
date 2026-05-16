---
title: "Совмещение версионирования API с OpenAPI в .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 — первая версия с официальной поддержкой .NET 10 и Microsoft.AspNetCore.OpenApi, генерирующая отдельные документы OpenAPI для каждой версии API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Этот пост был переведён автоматически. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

[Совмещение версионирования API с OpenAPI в .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — гостевой пост Microsoft MVP Сандера тен Бринке — рассказывает о новом пакете `Asp.Versioning` v10, первой версии, специально разработанной для .NET 10 и встроенной библиотеки `Microsoft.AspNetCore.OpenApi`, которая заменила Swashbuckle в качестве значения по умолчанию в .NET 9.

## Asp.Versioning v10: создан для нового стека OpenAPI

Предыдущая `Asp.Versioning` v8.x продолжает работать на .NET 10 через неявный roll-forward, однако v10 — первая версия, разработанная специально для `Microsoft.AspNetCore.OpenApi`. Ключевая настройка — вызов `AddApiVersioning`, связанный с `AddApiExplorer`, плюс отдельный вызов `AddOpenApi` для каждой версии, которую нужно открыть:

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

В результате создаются отдельные документы по адресам `/openapi/v1.json` и `/openapi/v2.json`.

## Стратегии версионирования: URL-путь, query string, заголовок, media type

Пакет поддерживает четыре стратегии. Версионирование через URL-путь (`/api/v1/resource`) наиболее распространено для публичных API. Query string (`?version=1.0`) и пользовательский заголовок (`X-API-Version`) популярны во внутренних сервисах. Версионирование через media type с заголовком `Accept` — это подход, который использует GitHub для своего REST API.

## Поддержка Minimal APIs и Controllers

Для Minimal APIs создаётся набор версий и каждый маршрут сопоставляется с конкретной версией:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Для Controllers применяются атрибуты `[ApiVersion("1.0")]` и `[MapToApiVersion("1.0")]` на уровне класса и действия.

## SwaggerUI и Scalar работают сразу

Как `Swashbuckle.AspNetCore.SwaggerUI`, так и `Scalar.AspNetCore` интегрируются без лишних настроек — достаточно указать URL документов по версиям, и вы получите версионно-осведомлённый UI без дополнительной конфигурации.

## Примеры кода используют файловые приложения .NET 10

Примеры в статье используют новую функцию файловых приложений C# 14 / .NET 10: запуск одного файла `.cs` командой `dotnet <имяФайла>.cs` без файла проекта. Фрагменты кода самодостаточны и легко воспроизводимы локально.

## Итог

Если вы работаете на .NET 10 и хотите чистые, версионированные контракты OpenAPI без сторонних middleware, `Asp.Versioning` v10 — официальный путь.

Читать полностью: [Совмещение версионирования API с OpenAPI в .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
