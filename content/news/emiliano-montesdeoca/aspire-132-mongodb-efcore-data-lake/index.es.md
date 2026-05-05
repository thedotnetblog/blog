---
title: "Aspire 13.2 incorpora MongoDB EF Core y Azure Data Lake — Dos integraciones que vale la pena probar"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 añade integraciones de MongoDB Entity Framework Core y Azure Data Lake Storage con health checks y service discovery sin configuración. Así es como se ven en la práctica."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 acaba de llegar con [dos nuevas integraciones de bases de datos](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) que merecen tu atención: MongoDB Entity Framework Core y Azure Data Lake Storage. Si querías usar EF Core con MongoDB en una app de Aspire, o necesitabas conectar cargas de trabajo de data lake con service discovery, esta versión trae ambas cosas.

## MongoDB se encuentra con EF Core en Aspire

Esta es la que más me entusiasma. Aspire ha soportado MongoDB desde hace tiempo, pero siempre fue con el driver directo — sin EF Core, sin `DbContext`, sin consultas LINQ contra tus documentos. Ahora tienes la experiencia completa de EF Core con MongoDB, además de los health checks automáticos y el service discovery de Aspire.

Configurarlo sigue el patrón típico de Aspire. En tu AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Luego en tu proyecto consumidor, añade la integración de EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Y registra tu `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

A partir de ahí, es EF Core estándar. Define tus entidades, usa tu `DbContext` como lo harías con cualquier otro proveedor. La integración se encarga del connection pooling, trazas de OpenTelemetry y health checks en segundo plano.

Para desarrolladores .NET que han estado usando MongoDB con el driver directo y configurando connection strings manualmente, esto es una mejora de calidad de vida muy bienvenida. Obtienes la abstracción completa de EF Core sin perder el service discovery de Aspire.

## Azure Data Lake Storage se une a la fiesta

La segunda gran adición es una [integración de Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Si estás construyendo pipelines de datos, procesos ETL o plataformas de analítica, ahora puedes conectar recursos de Data Lake de la misma forma que conectarías cualquier otra dependencia de Aspire.

En el AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

En el proyecto consumidor:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Sin gestión manual de connection strings, sin buscar credenciales. Aspire aprovisiona los recursos y los inyecta. Para los que construimos apps .NET cloud-native que tocan tanto datos operacionales como cargas de trabajo analíticas, esto hace que el data lake se sienta como un ciudadano de primera clase en el modelo de Aspire.

## Las pequeñas correcciones que importan

Más allá de las funcionalidades principales, hay algunas mejoras de calidad de vida que vale la pena mencionar:

- **Corrección del connection string de MongoDB** — la barra diagonal antes del nombre de la base de datos ahora se maneja correctamente. Si habías implementado un workaround, ya puedes eliminarlo
- **Exports de SQL Server** — `Aspire.Hosting.SqlServer` ahora exporta opciones de configuración adicionales del servidor para un control más granular
- **Actualizaciones de emuladores** — emulador de ServiceBus 2.0.0, emulador de App Configuration 1.0.2, y el emulador preview de CosmosDB ahora incluye una verificación de disponibilidad
- **Azure Managed Redis** — ahora usa `rediss://` (Redis Secure) por defecto, así que las conexiones están cifradas desde el inicio

Esa última es sutil pero importante — Redis cifrado por defecto significa una cosa menos que configurar en producción.

## Para cerrar

Aspire 13.2 es una versión incremental, pero las integraciones de MongoDB EF Core y Data Lake llenan vacíos reales. Si estabas esperando soporte adecuado de EF Core con MongoDB en Aspire, o necesitabas que Data Lake fuera una dependencia de primera clase, [actualiza a 13.2](https://get.aspire.dev) y pruébalas. El comando `aspire add` genera todo lo que necesitas.

Lee las [notas de la versión completas](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) para más detalles, y consulta la [galería de integraciones](https://aspire.dev/integrations/gallery/) para la lista completa.
