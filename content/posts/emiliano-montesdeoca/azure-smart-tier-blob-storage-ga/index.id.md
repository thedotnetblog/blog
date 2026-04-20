---
title: "Azure Smart Tier Kini GA — Optimasi Biaya Blob Storage Otomatis Tanpa Aturan Siklus Hidup"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Tingkat cerdas Azure Blob Storage kini tersedia secara umum, secara otomatis memindahkan objek antara tingkat hot, cool, dan cold berdasarkan pola akses aktual."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-smart-tier-blob-storage-ga" >}}).*

Jika Anda pernah menghabiskan waktu menyetel kebijakan siklus hidup Azure Blob Storage dan kemudian menyaksikannya runtuh ketika pola akses berubah, ini untuk Anda. Microsoft baru saja mengumumkan [ketersediaan umum smart tier](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) untuk Azure Blob dan Data Lake Storage.

## Yang sebenarnya dilakukan smart tier

Smart tier terus mengevaluasi waktu akses terakhir setiap objek di akun penyimpanan Anda. Data yang sering diakses tetap di hot, data tidak aktif pindah ke cool setelah 30 hari, lalu ke cold setelah 60 hari lagi. Saat data diakses lagi, langsung dipromosikan kembali ke hot.

Tidak ada aturan siklus hidup yang perlu dikonfigurasi. Tidak ada penyesuaian manual.

Selama pratinjau, Microsoft melaporkan bahwa **lebih dari 50% kapasitas yang dikelola smart tier secara otomatis berpindah ke tingkat lebih dingin**.

## Mengapa ini penting untuk developer .NET

Skenario praktis:
- **Telemetri dan log aplikasi** — panas saat debugging, jarang diakses setelah beberapa minggu
- **Pipeline data dan output ETL** — akses intensif saat pemrosesan, lalu sebagian besar dingin
- **Konten yang dibuat pengguna** — unggahan terbaru panas, konten lama mendingin secara bertahap

## Pertukaran yang perlu diketahui

Aturan peringkatan smart tier bersifat statis (30 hari → cool, 90 hari → cold). Jika Anda membutuhkan ambang batas kustom, aturan siklus hidup masih berlaku.
