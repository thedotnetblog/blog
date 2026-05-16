---
title: "Combinando el versionado de API con OpenAPI en .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 es la primera versión que soporta oficialmente tanto .NET 10 como Microsoft.AspNetCore.OpenApi, generando documentos OpenAPI separados por versión de API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Combinando el versionado de API con OpenAPI en .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — artículo invitado del MVP de Microsoft Sander ten Brinke — explica el nuevo paquete `Asp.Versioning` v10, la primera versión diseñada específicamente para .NET 10 y la biblioteca integrada `Microsoft.AspNetCore.OpenApi` que reemplazó a Swashbuckle como opción predeterminada en .NET 9.

## Asp.Versioning v10: diseñado para el nuevo stack de OpenAPI

La versión anterior `Asp.Versioning` v8.x sigue funcionando en .NET 10 mediante roll-forward implícito, pero v10 es la primera versión diseñada específicamente para `Microsoft.AspNetCore.OpenApi`. La configuración clave es una llamada a `AddApiVersioning` encadenada con `AddApiExplorer`, más una llamada separada a `AddOpenApi` por cada versión que quieras exponer:

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

Esto produce documentos separados en `/openapi/v1.json` y `/openapi/v2.json`.

## Estrategias de versionado: ruta URL, query string, cabecera, media type

El paquete soporta cuatro estrategias. El versionado por ruta URL (`/api/v1/resource`) es el más común en APIs públicas. La query string (`?version=1.0`) y la cabecera personalizada (`X-API-Version`) son populares en servicios internos. El versionado por media type a través de la cabecera `Accept` es el que usa GitHub en su API REST.

## Compatible con Minimal APIs y Controllers

Para Minimal APIs, se construye un conjunto de versiones y se mapea cada ruta a una versión específica:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Para Controllers, se aplican los atributos `[ApiVersion("1.0")]` y `[MapToApiVersion("1.0")]` a nivel de clase y acción.

## SwaggerUI y Scalar funcionan sin configuración adicional

Tanto `Swashbuckle.AspNetCore.SwaggerUI` como `Scalar.AspNetCore` se integran limpiamente — simplemente apuntas las URLs de documentos por versión y obtienes una interfaz con soporte de versiones sin plumbing extra.

## Los ejemplos de código usan apps de archivo de .NET 10

Los ejemplos del artículo usan la nueva funcionalidad de apps de archivo de C# 14 / .NET 10: ejecutas un único archivo `.cs` con `dotnet <nombrearchivo>.cs`, sin necesidad de un archivo de proyecto. Hace que los fragmentos de código sean autocontenidos y fáciles de probar localmente.

## Conclusión

Si usas .NET 10 y quieres contratos OpenAPI versionados y limpios sin añadir middleware de terceros, `Asp.Versioning` v10 es el camino oficial.

Lee el artículo completo: [Combinando el versionado de API con OpenAPI en .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
