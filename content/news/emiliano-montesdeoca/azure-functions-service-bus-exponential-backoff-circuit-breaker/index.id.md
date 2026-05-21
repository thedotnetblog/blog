---
title: "Berhenti Menghantam Dependensi yang Kesulitan: Pola Retry untuk Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Pola exponential backoff dan circuit breaker kini didukung secara native untuk Azure Functions yang dipicu Service Bus — inilah cara kerjanya dan mengapa Anda membutuhkan keduanya."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Inilah cara kegagalan yang dapat dipulihkan menjadi pemadaman di aplikasi Functions: dependensi mulai timeout, setiap instance Functions langsung retry tanpa batas, dependensi dihantam dengan ratusan permintaan gagal secara bersamaan, dan apa yang dimulai sebagai gangguan sementara berubah menjadi peristiwa backpressure di seluruh sistem.

Anda mungkin mengenal cerita ini. Azure Functions scale out dengan cepat — itulah seluruh tujuannya. Namun "scale out cepat" dan "retry segera" bersama-sama dapat membuat kegagalan menjadi jauh lebih buruk.

Dua pola membantu. Exponential backoff dan circuit breaker. Keduanya kini didukung secara native untuk Azure Functions yang dipicu Service Bus.

## Dua Pola, Peran Berbeda

Pola-pola ini saling melengkapi, bukan alternatif:

**Exponential backoff** menjawab: *kapan saya harus mencoba lagi?*
Ini meningkatkan penundaan antara retry sehingga dependensi memiliki waktu untuk pulih. Di tingkat pesan, mengatur waktu retry.

**Circuit breaker** menjawab: *haruskah saya memanggil dependensi ini sekarang?*
Ini menghentikan panggilan berulang ke dependensi yang tidak sehat setelah ambang kegagalan tercapai, kemudian dengan hati-hati menyelidiki setelah periode pendinginan. Di tingkat sistem, mencegah badai retry.

Anda menginginkan keduanya. Backoff menangani pengaturan retry per pesan. Circuit breaker menangani keputusan kesehatan agregat.

## Mengapa Ini Penting Terutama untuk Service Bus

Antrean menyerap lonjakan trafik, yang merupakan hal baik. Namun tanpa kontrol, antrean dapat tumbuh sementara worker terus membuang sumber daya komputasi pada panggilan yang akan gagal. Pesan beracun tetap aktif lebih lama dari seharusnya. Partisi panas atau kapasitas downstream terbatas menciptakan masalah berjenjang.

Desain yang lebih aman:

1. Mendeteksi kegagalan sementara
2. Menunda upaya berikutnya dengan exponential backoff
3. Menghentikan panggilan ke dependensi saat ambang kegagalan tercapai (circuit terbuka)
4. Melanjutkan dengan hati-hati setelah periode pendinginan (circuit probe)
5. Memindahkan pekerjaan yang tidak dapat dipulihkan ke dead-letter atau jalur karantina

## Tampilan Dukungan Native

Dukungan baru terintegrasi dengan model host Azure Functions yang ada — tidak ada library tambahan, tidak ada implementasi kustom. Konfigurasi masuk ke `host.json` Anda:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

Konfigurasi circuit breaker menetapkan ambang kegagalan dan interval reset sehingga dependensi yang tidak sehat tidak dihantam selama pemulihan.

## Bahasa yang Didukung

Ini bukan hanya untuk .NET. Fitur ini mencakup dotnet, JavaScript, TypeScript, dan Python — set lengkap bahasa yang didukung oleh trigger Service Bus di Azure Functions.

## Kesimpulan

Pola retry tidak menarik untuk dikonfigurasi sampai pertama kali pemadaman downstream menyebabkan Functions Anda memperburuk masalah alih-alih menurun dengan baik. Mengaturnya secara proaktif adalah hal yang murah. Merefaktornya saat insiden tidak demikian.

Post asli: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
