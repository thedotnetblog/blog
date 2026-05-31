---
title: "Alur Kerja yang Tahan Lama di Microsoft Agent Framework: Dari In-Memory ke Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "Model pemrograman alur kerja MAF kini mendukung eksekusi tahan lama yang didukung oleh Durable Task — berikut cara membangun alur kerja agen yang dapat dikomposisi yang bertahan dari restart proses dan diskalakan di Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Salah satu titik nyeri dengan alur kerja agen AI awal: mereka rapuh. Alur kerja multi-langkah yang berjalan lama dan terikat pada satu proses berarti restart proses = status hilang. Untuk demo sederhana ini tidak masalah. Untuk beban kerja produksi tidak.

Model pemrograman alur kerja Microsoft Agent Framework kini mendukung **eksekusi tahan lama**, didukung oleh framework Durable Task, dengan hosting Azure Functions. Berikut cara kerja model pemrograman dan mengapa cerita ketahanan itu penting.

## Blok Pembangun Inti

**Executor** adalah unit kerja yang mendasar. Setiap executor memiliki tipe — menerima input tertentu dan menghasilkan output tertentu:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // cari pesanan, kembalikan
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflow** menghubungkan executor ke dalam grafik terarah menggunakan fluent builder. Framework menangani eksekusi, aliran data antar langkah, dan propagasi kesalahan.

Anda dapat memodelkan:
- Rantai sekuensial (langkah A → langkah B → langkah C)
- Fan-out/fan-in paralel (jalankan agen A, B, C secara paralel, agregasi hasil)
- Percabangan kondisional
- Persetujuan human-in-the-loop (jeda alur kerja, tunggu sinyal eksternal)

## Runner In-Memory untuk Pengembangan Lokal

Memulai itu cepat:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Paket inti mencakup runner in-process yang ringan. Tidak ada dependensi eksternal, tidak ada database, tidak ada sumber daya Azure. Bekerja sangat baik untuk pengembangan lokal dan pengujian unit.

## Menambahkan Ketahanan dengan Durable Task

Ketika alur kerja perlu bertahan dari restart proses — karena berjalan lama, karena memiliki langkah human-in-the-loop, karena tersebar di banyak panggilan agen paralel — runner in-memory tidak cukup.

Integrasi Durable Task MAF menyimpan status alur kerja di Azure Storage. Jika proses dimulai ulang, alur kerja dilanjutkan dari tempat berhenti. Model pemrograman tetap sama; Anda hanya mengganti runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Executor yang sama, grafik alur kerja yang sama — didukung oleh status tahan lama.

## Hosting Azure Functions

Lapisan ketiga adalah hosting Azure Functions. Alur kerja Anda menjadi aplikasi Function: picu alur kerja melalui endpoint HTTP, dan runtime tahan lama menangani penskalaan, status, dan keandalan.

Ini berarti alur kerja multi-agen dengan panggilan paralel, percabangan kondisional, dan persetujuan manusia dapat diskalakan di seluruh lingkungan Functions serverless tanpa manajemen status kustom.

## Mengapa Ini Penting

Kombinasi ini signifikan untuk sistem AI nyata:

- **Panggilan agen paralel** — distribusikan ke beberapa agen khusus secara bersamaan tanpa memblokir, agregasi hasil saat semua selesai
- **Proses yang berjalan lama** — alur kerja yang melibatkan persetujuan manusia atau peristiwa eksternal dapat menjeda dan melanjutkan selama berjam-jam atau berhari-hari
- **Penskalaan** — Azure Functions menskalakan eksekusi secara horizontal; framework Durable Task mengelola koordinasi status paralel

Jika Anda membangun alur kerja MAF di luar demo lokal sederhana, ini adalah jalan menuju eksekusi berkualitas produksi.

Posting asli: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
