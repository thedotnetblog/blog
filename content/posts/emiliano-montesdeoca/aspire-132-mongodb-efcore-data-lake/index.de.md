---
title: "Aspire 13.2 bringt MongoDB EF Core und Azure Data Lake — Zwei Integrationen, die einen Blick wert sind"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 fügt MongoDB Entity Framework Core und Azure Data Lake Storage Integrationen mit konfiguationsfreien Health Checks und Service Discovery hinzu. So sehen sie in der Praxis aus."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 ist gerade erschienen mit [zwei neuen Datenbank-Integrationen](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/), die eure Aufmerksamkeit verdienen: MongoDB Entity Framework Core und Azure Data Lake Storage. Wenn ihr EF Core mit MongoDB in einer Aspire-App nutzen wolltet, oder Data-Lake-Workloads mit ordentlichem Service Discovery anbinden müsst, liefert dieses Release beides.

## MongoDB trifft EF Core in Aspire

Das ist die Integration, auf die ich mich am meisten freue. Aspire hat MongoDB schon länger unterstützt, aber es war immer der rohe Treiber — kein EF Core, kein `DbContext`, keine LINQ-Abfragen gegen eure Dokumente. Jetzt bekommt ihr die volle EF-Core-Erfahrung mit MongoDB, plus Aspires automatische Health Checks und Service Discovery.

Die Einrichtung folgt dem typischen Aspire-Muster. Im AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Dann fügt ihr in eurem konsumierenden Projekt die EF Core Integration hinzu:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Und registriert euren `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Ab da ist es Standard-EF-Core. Definiert eure Entities, nutzt euren `DbContext` wie mit jedem anderen Provider. Die Integration übernimmt Connection Pooling, OpenTelemetry-Traces und Health Checks im Hintergrund.

Für .NET-Entwickler, die MongoDB mit dem rohen Treiber genutzt und Connection Strings manuell verdrahtet haben, ist das ein schönes Upgrade. Ihr bekommt die volle EF-Core-Abstraktion, ohne Aspires Service Discovery zu verlieren.

## Azure Data Lake Storage ist mit dabei

Die zweite große Neuerung ist eine [Azure Data Lake Storage (ADLS) Integration](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Wenn ihr Datenpipelines, ETL-Prozesse oder Analyseplattformen baut, könnt ihr Data-Lake-Ressourcen jetzt genauso anbinden wie jede andere Aspire-Abhängigkeit.

Im AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Im konsumierenden Projekt:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Keine manuelle Connection-String-Verwaltung, keine Credential-Suche. Aspire provisioniert Ressourcen und injiziert sie. Für diejenigen von uns, die cloud-native .NET-Apps bauen, die sowohl operative Daten als auch Analyse-Workloads berühren, fühlt sich der Data Lake damit wie ein erstklassiger Bürger im Aspire-Modell an.

## Die kleinen Verbesserungen, die zählen

Neben den Hauptfeatures gibt es ein paar Verbesserungen, die erwähnenswert sind:

- **MongoDB Connection String Fix** — der Schrägstrich vor dem Datenbanknamen wird jetzt korrekt behandelt. Falls ihr einen Workaround dafür hattet, könnt ihr ihn entfernen
- **SQL Server Exports** — `Aspire.Hosting.SqlServer` exportiert jetzt zusätzliche Serverkonfigurationsoptionen für feingranulare Kontrolle
- **Emulator-Updates** — ServiceBus Emulator 2.0.0, App Configuration Emulator 1.0.2, und der Preview-Emulator von CosmosDB enthält jetzt einen Readiness Check
- **Azure Managed Redis** — nutzt jetzt standardmäßig `rediss://` (Redis Secure), sodass Verbindungen von Haus aus verschlüsselt sind

Der letzte Punkt ist subtil, aber wichtig — verschlüsseltes Redis als Standard bedeutet eine Sache weniger, die man in Produktion konfigurieren muss.

## Fazit

Aspire 13.2 ist ein inkrementelles Release, aber die MongoDB EF Core und Data Lake Integrationen füllen echte Lücken. Wenn ihr auf ordentlichen EF-Core-Support mit MongoDB in Aspire gewartet habt, oder Data Lake als erstklassige Abhängigkeit braucht, [upgradet auf 13.2](https://get.aspire.dev) und probiert es aus. Der `aspire add` Befehl erstellt alles, was ihr braucht.

Lest die [vollständigen Release Notes](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) für mehr Details und schaut euch die [Integrationsgalerie](https://aspire.dev/integrations/gallery/) für die komplette Liste an.
