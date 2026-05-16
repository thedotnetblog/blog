---
title: "Menggabungkan API Versioning dengan OpenAPI di .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 adalah versi pertama yang secara resmi mendukung .NET 10 dan Microsoft.AspNetCore.OpenApi, menghasilkan dokumen OpenAPI terpisah per versi API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Menggabungkan API Versioning dengan OpenAPI di .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — artikel tamu dari Microsoft MVP Sander ten Brinke — menjelaskan paket `Asp.Versioning` v10 baru, versi pertama yang dirancang khusus untuk .NET 10 dan library bawaan `Microsoft.AspNetCore.OpenApi` yang menggantikan Swashbuckle sebagai default di .NET 9.

## Asp.Versioning v10: dibangun untuk stack OpenAPI baru

`Asp.Versioning` v8.x sebelumnya masih berjalan di .NET 10 melalui implicit roll-forward, namun v10 adalah versi pertama yang dirancang khusus untuk `Microsoft.AspNetCore.OpenApi`. Konfigurasi utamanya adalah panggilan `AddApiVersioning` yang dirantai dengan `AddApiExplorer`, ditambah panggilan `AddOpenApi` terpisah untuk setiap versi yang ingin diekspos:

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

Ini menghasilkan dokumen terpisah di `/openapi/v1.json` dan `/openapi/v2.json`.

## Strategi versioning: URL path, query string, header, media type

Paket ini mendukung empat strategi. Versioning URL path (`/api/v1/resource`) paling umum untuk API publik. Query string (`?version=1.0`) dan header kustom (`X-API-Version`) populer untuk layanan internal. Versioning media type melalui header `Accept` adalah yang digunakan GitHub untuk REST API-nya.

## Mendukung Minimal APIs dan Controllers

Untuk Minimal APIs, buat version set dan petakan setiap route ke versi tertentu:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Untuk Controllers, gunakan atribut `[ApiVersion("1.0")]` dan `[MapToApiVersion("1.0")]` di level class dan action.

## SwaggerUI dan Scalar langsung berfungsi

Baik `Swashbuckle.AspNetCore.SwaggerUI` maupun `Scalar.AspNetCore` terintegrasi dengan mulus — cukup arahkan ke URL dokumen per versi dan Anda mendapatkan UI yang sadar versi tanpa konfigurasi tambahan.

## Contoh kode menggunakan file-based apps .NET 10

Contoh-contoh dalam artikel menggunakan fitur file-based app baru dari C# 14 / .NET 10: jalankan satu file `.cs` dengan `dotnet <namafile>.cs`, tanpa perlu file project. Ini membuat snippet mandiri dan mudah dicoba secara lokal.

## Kesimpulan

Jika Anda menggunakan .NET 10 dan menginginkan kontrak OpenAPI yang bersih dan terversi tanpa menambahkan middleware pihak ketiga, `Asp.Versioning` v10 adalah jalur resminya.

Baca artikel lengkapnya: [Menggabungkan API Versioning dengan OpenAPI di .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
