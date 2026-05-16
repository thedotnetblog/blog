---
title: ".NET 10'da API Sürüm Yönetimini OpenAPI ile Birleştirme"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10, hem .NET 10'u hem de Microsoft.AspNetCore.OpenApi'yi resmi olarak destekleyen ilk sürümdür ve her API sürümü için ayrı OpenAPI belgeleri oluşturur."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[.NET 10'da API Sürüm Yönetimini OpenAPI ile Birleştirme](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Microsoft MVP Sander ten Brinke'nin konuk yazısı — hem .NET 10 hem de .NET 9'da Swashbuckle'ın yerini alan yerleşik kütüphane `Microsoft.AspNetCore.OpenApi` için özel olarak tasarlanmış ilk sürüm olan `Asp.Versioning` v10'u ele alıyor.

## Asp.Versioning v10: yeni OpenAPI yığını için tasarlandı

Önceki `Asp.Versioning` v8.x, örtük roll-forward aracılığıyla .NET 10'da çalışmaya devam ediyor; ancak v10, `Microsoft.AspNetCore.OpenApi` için özel olarak tasarlanmış ilk sürümdür. Temel yapılandırma, `AddApiVersioning`'i `AddApiExplorer` ile zincirlemek ve açmak istediğiniz her sürüm için ayrı bir `AddOpenApi` çağrısı yapmaktır:

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

Bu, `/openapi/v1.json` ve `/openapi/v2.json` adreslerinde ayrı belgeler üretir.

## Sürüm yönetimi stratejileri: URL yolu, sorgu dizisi, başlık, medya türü

Paket dört stratejiyi destekler. URL yolu sürüm yönetimi (`/api/v1/resource`) genel API'ler için en yaygın olanıdır. Sorgu dizisi (`?version=1.0`) ve özel başlık (`X-API-Version`) dahili hizmetlerde popülerdir. `Accept` başlığı aracılığıyla medya türü sürüm yönetimi, GitHub'ın REST API'si için kullandığı yaklaşımdır.

## Minimal API'ler ve Controller'lar için destek

Minimal API'ler için bir sürüm seti oluşturur ve her rotayı belirli bir sürüme eşlersiniz:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Controller'lar için sınıf ve eylem düzeyinde `[ApiVersion("1.0")]` ve `[MapToApiVersion("1.0")]` öznitelikleri uygulanır.

## SwaggerUI ve Scalar hemen çalışır

Hem `Swashbuckle.AspNetCore.SwaggerUI` hem de `Scalar.AspNetCore` sorunsuz entegre olur — sadece sürüme özel belge URL'lerine yönlendirin ve ekstra yapılandırma olmadan sürüm bilincine sahip bir UI elde edin.

## Kod örnekleri .NET 10 dosya tabanlı uygulamaları kullanıyor

Makaledeki örnekler C# 14 / .NET 10'un yeni dosya tabanlı uygulama özelliğini kullanıyor: proje dosyası olmadan tek bir `.cs` dosyasını `dotnet <dosyaadı>.cs` ile çalıştırıyorsunuz. Bu, kod parçacıklarını bağımsız ve yerel olarak kolayca denenebilir hale getiriyor.

## Sonuç

.NET 10 kullanıyorsanız ve üçüncü taraf ara yazılım eklemeden temiz, sürümlü OpenAPI sözleşmeleri istiyorsanız, `Asp.Versioning` v10 resmi yoldur.

Makalenin tamamını okuyun: [.NET 10'da API Sürüm Yönetimini OpenAPI ile Birleştirme](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
