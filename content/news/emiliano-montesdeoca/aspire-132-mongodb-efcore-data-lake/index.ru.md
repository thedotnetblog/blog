---
title: "Aspire 13.2 получает MongoDB EF Core и Azure Data Lake — Две интеграции, которые стоит попробовать"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 добавляет интеграции MongoDB Entity Framework Core и Azure Data Lake Storage с автоматическими проверками работоспособности и обнаружением сервисов без настройки. Вот как они выглядят на практике."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Этот пост был переведён автоматически. Оригинальная версия доступна [здесь]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}}).*

Aspire 13.2 вышел с [двумя новыми интеграциями баз данных](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/), которые заслуживают внимания: MongoDB Entity Framework Core и Azure Data Lake Storage. Если вы хотели использовать EF Core с MongoDB в приложении Aspire или вам нужно было подключить рабочие нагрузки Data Lake с обнаружением сервисов, этот релиз предоставляет и то, и другое.

## MongoDB встречает EF Core в Aspire

Это интеграция, которая радует меня больше всего. Aspire поддерживал MongoDB уже давно, но это всегда был сырой драйвер — никакого EF Core, никакого `DbContext`, никаких LINQ-запросов к документам. Теперь вы получаете полноценный EF Core с MongoDB, плюс автоматические проверки работоспособности и обнаружение сервисов от Aspire.

Настройка следует типичному паттерну Aspire. В вашем AppHost:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Затем в потребляющем проекте добавьте интеграцию EF Core:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

И зарегистрируйте свой `DbContext`:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Дальше — стандартный EF Core. Определяйте сущности, используйте `DbContext` как с любым другим провайдером. Интеграция берёт на себя пул соединений, трассировки OpenTelemetry и проверки работоспособности за кулисами.

Для .NET-разработчиков, которые использовали MongoDB с сырым драйвером и вручную настраивали строки подключения, это приятное улучшение качества жизни. Вы получаете полную абстракцию EF Core, не теряя обнаружение сервисов Aspire.

## Azure Data Lake Storage присоединяется

Второе крупное дополнение — [интеграция Azure Data Lake Storage (ADLS)](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Если вы строите конвейеры данных, ETL-процессы или аналитические платформы, теперь можно подключать ресурсы Data Lake так же, как любую другую зависимость Aspire.

В AppHost:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

В потребляющем проекте:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Никакого ручного управления строками подключения, никакой охоты за учётными данными. Aspire выделяет ресурсы и внедряет их. Для тех из нас, кто строит облачно-нативные .NET-приложения, работающие как с операционными данными, так и с аналитическими нагрузками, Data Lake теперь ощущается как полноценный участник модели Aspire.

## Маленькие исправления, которые важны

Помимо основных функций, есть несколько улучшений, которые стоит отметить:

- **Исправление строки подключения MongoDB** — косая черта перед именем базы данных теперь обрабатывается корректно. Если у вас был обходной путь, можете его убрать
- **Экспорт SQL Server** — `Aspire.Hosting.SqlServer` теперь экспортирует дополнительные параметры конфигурации сервера для более тонкого контроля
- **Обновления эмуляторов** — эмулятор ServiceBus 2.0.0, эмулятор App Configuration 1.0.2, предварительный эмулятор CosmosDB теперь включает проверку готовности
- **Azure Managed Redis** — теперь по умолчанию использует `rediss://` (Redis Secure), так что соединения шифруются из коробки

Последний пункт тонкий, но важный — шифрованный Redis по умолчанию означает на одну настройку меньше в продакшене.

## Подводя итоги

Aspire 13.2 — инкрементальный релиз, но интеграции MongoDB EF Core и Data Lake заполняют реальные пробелы. Если вы ждали нормальную поддержку EF Core для MongoDB в Aspire или вам нужен Data Lake как полноценная зависимость, [обновитесь до 13.2](https://get.aspire.dev) и попробуйте. Команда `aspire add` создаст всё необходимое.

Читайте [полные примечания к релизу](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) для подробностей и загляните в [галерею интеграций](https://aspire.dev/integrations/gallery/) для полного списка.
