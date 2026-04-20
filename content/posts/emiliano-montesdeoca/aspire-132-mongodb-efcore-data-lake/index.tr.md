---
title: "Aspire 13.2, MongoDB EF Core ve Azure Data Lake Desteği Kazandı — Denemeye Değer İki Entegrasyon"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, sıfır yapılandırmalı sağlık kontrolleri ve servis keşfi ile MongoDB Entity Framework Core ve Azure Data Lake Storage entegrasyonları ekliyor. Bunların pratikte nasıl göründüğü."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-132-mongodb-efcore-data-lake" >}}).*

Aspire 13.2 dikkatinizi çekmeye değer [iki yeni veritabanı entegrasyonuyla](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/) yayımlandı: MongoDB Entity Framework Core ve Azure Data Lake Storage. Bir Aspire uygulamasında MongoDB ile EF Core kullanmak istiyorsanız veya uygun servis keşfiyle data lake iş yüklerini bağlamanız gerekiyorsa, bu sürüm her ikisini de sunuyor.

## MongoDB, Aspire'da EF Core ile buluşuyor

En çok heyecanlandığım bu. Aspire bir süredir MongoDB'yi destekliyordu ama her zaman ham sürücüydü — EF Core yok, `DbContext` yok, belgelerinize karşı LINQ sorgusu yok. Artık MongoDB ile tam EF Core deneyimini, ayrıca Aspire'ın otomatik sağlık kontrolleri ve servis keşfini elde ediyorsunuz.

Kurulum, tipik Aspire desenidir. AppHost'unuzda:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

Ardından tüketen projenize EF Core entegrasyonunu ekleyin:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

Ve `DbContext`'inizi kaydedin:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

Oradan itibaren standart EF Core. Varlıklarınızı tanımlayın, `DbContext`'inizi herhangi bir sağlayıcıyla kullandığınız gibi kullanın. Entegrasyon, bağlantı havuzlamasını, OpenTelemetry izlerini ve sağlık kontrollerini arka planda yönetir.

Ham sürücüyle MongoDB kullanan ve bağlantı dizelerini manuel olarak ayarlayan .NET geliştiricileri için bu, güzel bir yaşam kalitesi yükseltmesi. Aspire'ın servis keşfini kaybetmeden tam EF Core soyutlamasını elde ediyorsunuz.

## Azure Data Lake Storage katılıyor

İkinci büyük ekleme, [Azure Data Lake Storage (ADLS) entegrasyonu](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/). Veri pipeline'ları, ETL süreçleri veya analitik platformlar geliştiriyorsanız, artık Data Lake kaynaklarını herhangi bir diğer Aspire bağımlılığını bağladığınız gibi bağlayabilirsiniz.

AppHost'ta:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

Tüketen projede:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

Manuel bağlantı dizesi yönetimi yok, kimlik bilgisi avcılığı yok. Aspire kaynakları sağlar ve enjekte eder. Hem operasyonel veriye hem de analitik iş yüklerine dokunan cloud-native .NET uygulamaları geliştiriyorsanız, bu data lake'i Aspire modelinde birinci sınıf vatandaş gibi hissettiriyor.

## Önemli küçük düzeltmeler

Manşet özelliklerin ötesinde, dikkate değer birkaç yaşam kalitesi iyileştirmesi var:

- **MongoDB bağlantı dizesi düzeltmesi** — veritabanı adından önce eğik çizgi artık doğru şekilde işleniyor. Bunun etrafından dolaşıyorsanız, o geçici çözümü kaldırabilirsiniz
- **SQL Server dışa aktarmaları** — `Aspire.Hosting.SqlServer` artık daha ince ayarlı kontrol için ek sunucu yapılandırma seçenekleri dışa aktarıyor
- **Emülatör güncellemeleri** — ServiceBus emülatörü 2.0.0, App Configuration emülatörü 1.0.2 ve CosmosDB'nin önizleme emülatörü artık bir hazır olma kontrolü içeriyor
- **Azure Managed Redis** — artık varsayılan olarak `rediss://` (Redis Secure) kullanıyor; bağlantılar kutudan çıktığı gibi şifreli

Son madde ince ama önemli — varsayılan olarak şifreli Redis, üretimde yapılandırılacak bir şey daha az demek.

## Sonuç

Aspire 13.2 artımlı bir sürüm, ancak MongoDB EF Core ve Data Lake entegrasyonları gerçek boşlukları dolduruyor. Aspire'da MongoDB için uygun EF Core desteğini bekliyorsanız veya Data Lake'in birinci sınıf bağımlılık olmasına ihtiyacınız varsa, [13.2'ye yükseltin](https://get.aspire.dev) ve bir deneyin. `aspire add` komutu ihtiyacınız olan her şeyi iskelet haline getiriyor.

Daha fazla ayrıntı için [tam sürüm notlarını](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates) okuyun ve tam liste için [entegrasyon galerisine](https://aspire.dev/integrations/gallery/) göz atın.
