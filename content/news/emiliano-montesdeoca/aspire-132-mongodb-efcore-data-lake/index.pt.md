---
title: "Aspire 13.2 ganha MongoDB EF Core e Azure Data Lake — Duas integrações que vale a pena experimentar"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 adiciona integrações de MongoDB Entity Framework Core e Azure Data Lake Storage com health checks e service discovery sem configuração. Veja como ficam na prática."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 acabou de chegar com [duas novas integrações de banco de dados](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) que merecem sua atenção: MongoDB Entity Framework Core e Azure Data Lake Storage. Se você queria usar EF Core com MongoDB em uma app Aspire, ou precisava conectar workloads de data lake com service discovery, esta versão entrega as duas coisas.

## MongoDB encontra EF Core no Aspire

Essa é a que mais me empolga. O Aspire já suportava MongoDB há um tempo, mas sempre foi com o driver direto — sem EF Core, sem `DbContext`, sem consultas LINQ nos seus documentos. Agora você tem a experiência completa do EF Core com MongoDB, mais os health checks automáticos e o service discovery do Aspire.

A configuração segue o padrão típico do Aspire. No seu AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Depois no seu projeto consumidor, adicione a integração EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

E registre seu `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

A partir daí, é EF Core padrão. Defina suas entidades, use seu `DbContext` como faria com qualquer outro provider. A integração cuida do connection pooling, traces OpenTelemetry e health checks nos bastidores.

Para desenvolvedores .NET que estavam usando MongoDB com o driver direto e configurando connection strings manualmente, essa é uma ótima melhoria. Você ganha a abstração completa do EF Core sem perder o service discovery do Aspire.

## Azure Data Lake Storage entra na jogada

A segunda grande adição é uma [integração Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Se você está construindo pipelines de dados, processos ETL ou plataformas de analytics, agora pode conectar recursos de Data Lake da mesma forma que conectaria qualquer outra dependência do Aspire.

No AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

No projeto consumidor:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Sem gerenciamento manual de connection strings, sem caçar credenciais. O Aspire provisiona os recursos e os injeta. Para quem constrói apps .NET cloud-native que lidam tanto com dados operacionais quanto com workloads analíticos, isso faz o data lake parecer um cidadão de primeira classe no modelo do Aspire.

## As pequenas correções que importam

Além das funcionalidades principais, há algumas melhorias que valem a menção:

- **Correção do connection string do MongoDB** — a barra antes do nome do banco de dados agora é tratada corretamente. Se você tinha um workaround, pode removê-lo
- **Exports do SQL Server** — `Aspire.Hosting.SqlServer` agora exporta opções adicionais de configuração do servidor para um controle mais granular
- **Atualizações de emuladores** — emulador do ServiceBus 2.0.0, emulador do App Configuration 1.0.2, e o emulador preview do CosmosDB agora inclui uma verificação de disponibilidade
- **Azure Managed Redis** — agora usa `rediss://` (Redis Secure) por padrão, então as conexões são criptografadas desde o início

Essa última é sutil mas importante — Redis criptografado por padrão significa uma coisa a menos para configurar em produção.

## Concluindo

Aspire 13.2 é uma versão incremental, mas as integrações de MongoDB EF Core e Data Lake preenchem lacunas reais. Se você estava esperando suporte adequado de EF Core com MongoDB no Aspire, ou precisava do Data Lake como dependência de primeira classe, [atualize para a 13.2](https://get.aspire.dev) e teste. O comando `aspire add` gera tudo o que você precisa.

Leia as [notas de versão completas](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) para mais detalhes, e confira a [galeria de integrações](https://aspire.dev/integrations/gallery/) para a lista completa.
