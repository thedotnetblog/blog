---
title: "Aspire 13.2 aggiunge MongoDB EF Core e Azure Data Lake — Due integrazioni da provare"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 aggiunge le integrazioni MongoDB Entity Framework Core e Azure Data Lake Storage con health check e service discovery senza configurazione. Ecco come si presentano nella pratica."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 è appena arrivato con [due nuove integrazioni database](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) che meritano la vostra attenzione: MongoDB Entity Framework Core e Azure Data Lake Storage. Se volevate usare EF Core con MongoDB in un'app Aspire, o avevate bisogno di collegare workload data lake con il service discovery, questa release offre entrambe le cose.

## MongoDB incontra EF Core in Aspire

Questa è quella che mi entusiasma di più. Aspire supporta MongoDB da un po', ma è sempre stato il driver grezzo — niente EF Core, niente `DbContext`, niente query LINQ sui vostri documenti. Ora avete l'esperienza completa di EF Core con MongoDB, più gli health check automatici e il service discovery di Aspire.

La configurazione segue il classico pattern di Aspire. Nel vostro AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Poi nel progetto consumatore, aggiungete l'integrazione EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

E registrate il vostro `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Da lì in poi, è EF Core standard. Definite le vostre entità, usate il vostro `DbContext` come fareste con qualsiasi altro provider. L'integrazione gestisce il connection pooling, le trace OpenTelemetry e gli health check dietro le quinte.

Per gli sviluppatori .NET che usavano MongoDB con il driver grezzo e configuravano le connection string manualmente, questo è un bel miglioramento. Ottenete l'astrazione completa di EF Core senza perdere il service discovery di Aspire.

## Azure Data Lake Storage entra in gioco

La seconda grande aggiunta è un'[integrazione Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Se state costruendo pipeline di dati, processi ETL o piattaforme di analisi, ora potete collegare risorse Data Lake allo stesso modo di qualsiasi altra dipendenza Aspire.

Nell'AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Nel progetto consumatore:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Nessuna gestione manuale delle connection string, nessuna caccia alle credenziali. Aspire effettua il provisioning delle risorse e le inietta. Per chi di noi costruisce app .NET cloud-native che toccano sia dati operazionali che workload analitici, questo fa sentire il data lake come un cittadino di prima classe nel modello Aspire.

## Le piccole correzioni che contano

Oltre alle funzionalità principali, ci sono alcuni miglioramenti degni di nota:

- **Fix della connection string MongoDB** — lo slash prima del nome del database ora viene gestito correttamente. Se avevate un workaround, potete rimuoverlo
- **Export SQL Server** — `Aspire.Hosting.SqlServer` ora esporta opzioni di configurazione server aggiuntive per un controllo più granulare
- **Aggiornamenti emulatori** — emulatore ServiceBus 2.0.0, emulatore App Configuration 1.0.2, e l'emulatore preview di CosmosDB ora include un readiness check
- **Azure Managed Redis** — ora usa `rediss://` (Redis Secure) di default, quindi le connessioni sono crittografate fin da subito

L'ultimo punto è sottile ma importante — Redis crittografato di default significa una cosa in meno da configurare in produzione.

## Per concludere

Aspire 13.2 è una release incrementale, ma le integrazioni MongoDB EF Core e Data Lake colmano lacune reali. Se stavate aspettando un supporto EF Core adeguato con MongoDB in Aspire, o avevate bisogno del Data Lake come dipendenza di prima classe, [aggiornate alla 13.2](https://get.aspire.dev) e provatele. Il comando `aspire add` genera tutto il necessario.

Leggete le [note di rilascio complete](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) per maggiori dettagli, e date un'occhiata alla [galleria delle integrazioni](https://aspire.dev/integrations/gallery/) per la lista completa.
