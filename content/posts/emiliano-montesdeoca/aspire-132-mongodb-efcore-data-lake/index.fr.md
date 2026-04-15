---
title: "Aspire 13.2 accueille MongoDB EF Core et Azure Data Lake — Deux intégrations à essayer"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 ajoute les intégrations MongoDB Entity Framework Core et Azure Data Lake Storage avec des health checks et du service discovery sans configuration. Voici à quoi elles ressemblent en pratique."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 vient d'arriver avec [deux nouvelles intégrations de bases de données](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) qui méritent votre attention : MongoDB Entity Framework Core et Azure Data Lake Storage. Si vous vouliez utiliser EF Core avec MongoDB dans une app Aspire, ou si vous aviez besoin de connecter des workloads data lake avec du service discovery, cette version apporte les deux.

## MongoDB rencontre EF Core dans Aspire

C'est celle qui m'enthousiasme le plus. Aspire supporte MongoDB depuis un moment, mais c'était toujours le driver brut — pas d'EF Core, pas de `DbContext`, pas de requêtes LINQ sur vos documents. Maintenant vous avez l'expérience complète d'EF Core avec MongoDB, plus les health checks automatiques et le service discovery d'Aspire.

La mise en place suit le pattern typique d'Aspire. Dans votre AppHost :

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Puis dans votre projet consommateur, ajoutez l'intégration EF Core :

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Et enregistrez votre `DbContext` :

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

À partir de là, c'est de l'EF Core standard. Définissez vos entités, utilisez votre `DbContext` comme vous le feriez avec n'importe quel autre provider. L'intégration gère le connection pooling, les traces OpenTelemetry et les health checks en arrière-plan.

Pour les développeurs .NET qui utilisaient MongoDB avec le driver brut et configuraient les connection strings manuellement, c'est une belle amélioration. Vous obtenez l'abstraction complète d'EF Core sans perdre le service discovery d'Aspire.

## Azure Data Lake Storage entre dans la danse

Le deuxième ajout majeur est une [intégration Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Si vous construisez des pipelines de données, des processus ETL ou des plateformes d'analytique, vous pouvez maintenant connecter des ressources Data Lake de la même façon que n'importe quelle autre dépendance Aspire.

Dans l'AppHost :

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Dans le projet consommateur :

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Pas de gestion manuelle de connection strings, pas de recherche de credentials. Aspire provisionne les ressources et les injecte. Pour ceux d'entre nous qui construisent des apps .NET cloud-native touchant à la fois aux données opérationnelles et aux workloads analytiques, cela fait du data lake un citoyen de première classe dans le modèle Aspire.

## Les petits correctifs qui comptent

Au-delà des fonctionnalités principales, il y a quelques améliorations à noter :

- **Correction du connection string MongoDB** — le slash avant le nom de la base de données est maintenant géré correctement. Si vous aviez un workaround, vous pouvez le supprimer
- **Exports SQL Server** — `Aspire.Hosting.SqlServer` exporte maintenant des options de configuration serveur supplémentaires pour un contrôle plus fin
- **Mises à jour des émulateurs** — émulateur ServiceBus 2.0.0, émulateur App Configuration 1.0.2, et l'émulateur preview de CosmosDB inclut maintenant une vérification de disponibilité
- **Azure Managed Redis** — utilise maintenant `rediss://` (Redis Secure) par défaut, donc les connexions sont chiffrées d'emblée

Ce dernier point est subtil mais important — un Redis chiffré par défaut signifie une chose de moins à configurer en production.

## Pour conclure

Aspire 13.2 est une version incrémentale, mais les intégrations MongoDB EF Core et Data Lake comblent de vrais manques. Si vous attendiez un support EF Core correct avec MongoDB dans Aspire, ou si vous aviez besoin que Data Lake soit une dépendance de première classe, [passez à la 13.2](https://get.aspire.dev) et essayez-les. La commande `aspire add` génère tout ce dont vous avez besoin.

Lisez les [notes de version complètes](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) pour plus de détails, et consultez la [galerie d'intégrations](https://aspire.dev/integrations/gallery/) pour la liste complète.
