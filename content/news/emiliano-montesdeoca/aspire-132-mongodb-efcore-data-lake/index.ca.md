---
title: "Aspire 13.2 obté MongoDB EF Core i Azure Data Lake: dues integracions que val la pena provar"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 afegeix integracions MongoDB Entity Framework Core i Azure Data Lake Storage amb comprovacions de salut i descobriment de serveis sense configuració. Aquí teniu el que semblen a la pràctica."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

Aspire 13.2 acaba d'aterrar amb [dues noves integracions de bases de dades](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) que mereixen la vostra atenció: MongoDB Entity Framework Core i Azure Data Lake Storage. Si heu volgut utilitzar EF Core amb MongoDB en una aplicació Aspire o necessiteu connectar les càrregues de treball del llac de dades amb un descobriment de serveis adequat, aquesta versió ofereix tots dos.

## MongoDB compleix EF Core a Aspire

Aquest és el que m'emociona més. Aspire ha donat suport a MongoDB durant un temps, però sempre va ser el controlador en brut: sense EF Core, sense `DbContext`, sense consultes LINQ als vostres documents. Ara teniu l'experiència completa d'EF Core amb MongoDB, a més de les comprovacions automàtiques de l'estat i el descobriment de serveis d'Aspire.

Configurar-lo és el patró típic d'Aspire. Al vostre AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

A continuació, al vostre projecte de consum, afegiu la integració d'EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

I registre el teu `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

A partir d'aquí, és EF Core estàndard. Defineix les teves entitats, utilitza el teu `DbContext` com ho faries amb qualsevol altre proveïdor. La integració gestiona l'agrupació de connexions, les traces d'OpenTelemetry i les comprovacions de salut darrere de les escenes.

Per als desenvolupadors de.NET que han estat utilitzant MongoDB amb el controlador en brut i cablejat manualment les cadenes de connexió, aquesta és una bona actualització de qualitat de vida. Obteniu l'abstracció completa d'EF Core sense perdre el descobriment del servei d'Aspire.

## Azure Data Lake Storage s'uneix a la festa

La segona gran incorporació és una [integració d'Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Si esteu creant canalitzacions de dades, processos ETL o plataformes d'anàlisi, ara podeu connectar els recursos de Data Lake de la mateixa manera que connectaríeu qualsevol altra dependència d'Aspire.

A l'AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

En el projecte de consum:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Sense gestió manual de cadenes de connexió, sense recerca de credencials. Aspire proporciona recursos i els injecta. Per a aquells de nosaltres que creem aplicacions.NET natives del núvol que toquen tant dades operatives com càrregues de treball d'anàlisi, això fa que el llac de dades se senti com un ciutadà de primera classe en el model Aspire.

## Les petites solucions que importen

Més enllà de les funcions dels titulars, hi ha algunes millores en la qualitat de vida que cal destacar:

- **Correcció de cadena de connexió MongoDB**: la barra inclinada abans del nom de la base de dades ara es gestiona correctament. Si heu treballat amb això, podeu eliminar aquesta solució
- **Exporta SQL Server** — `Aspire.Hosting.SqlServer` ara exporta opcions addicionals de configuració del servidor per a un control més detallat
- **Actualitzacions de l'emulador**: l'emulador ServiceBus 2.0.0, l'emulador de configuració d'aplicacions 1.0.2 i l'emulador de vista prèvia de CosmosDB ara inclou una comprovació de la preparació
- **Azure Managed Redis**: ara el valor predeterminat és `rediss://` (Redis Secure), de manera que les connexions es xifren de manera immediata

Aquest últim és subtil però important: Redis xifrat per defecte significa una cosa menys per configurar en producció.

## Tancant

Aspire 13.2 és una versió incremental, però les integracions MongoDB EF Core i Data Lake omplen buits reals. Si estàveu esperant el suport adequat d'EF Core amb MongoDB a Aspire, o necessiteu que Data Lake sigui una dependència de primera classe, [actualitzeu a 13.2](https://get.aspire.dev) i feu-los una volta. L'ordre `aspire add` inclou tot el que necessiteu.

Llegiu les [notes completes de la versió](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) per obtenir més detalls i consulteu la [galeria d'integració](https://aspire.dev/integrations/gallery/) per obtenir la llista completa.
