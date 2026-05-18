---
title: "Aspire 13.3: Dukungan Kubernetes, Log Browser, dan Skill Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Lima minggu setelah 13.2, Aspire 13.3 hadir dengan 45 fitur baru termasuk deployment AKS kelas satu, skill onboarding berbasis AI, penangkapan log browser, dan hasil perintah terstruktur."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Lima minggu bukanlah waktu yang lama untuk sebuah rilis, tetapi Aspire 13.3 tidak terasa seperti itu. Item-item utamanya signifikan: deployment Kubernetes dan AKS kelas satu dengan Helm, skill onboarding berbasis agen bernama Aspireify, penangkapan log browser langsung di dasbor, dan hasil perintah terstruktur. Ditambah 45 fitur baru, 134 peningkatan, dan 93 perbaikan bug.

Mari kita bahas sorotan-sorotannya.

## Aspireify: Onboarding Berbasis Agen

Menambahkan Aspire ke proyek yang sudah ada terdengar mudah — tambahkan AppHost, selesai. Dalam praktiknya memerlukan banyak penelitian: port mana yang penting, variabel lingkungan mana yang merupakan dependensi nyata, layanan Docker Compose mana yang harus dipetakan ke integrasi Aspire.

**Skill Aspireify** yang baru memberikan agen koding Anda alur kerja terpandu untuk hal tersebut. Ketika `aspire init` membuat AppHost kerangka, skill Aspireify membantu agen memeriksa repositori, memahami cara kerjanya saat ini, dan menghubungkan AppHost agar sesuai dengan aplikasi — bukan sebaliknya.

Sikap defaultnya adalah "meminimalkan perubahan pada kode Anda." Jika aplikasi Anda sudah membaca `DATABASE_URL`, agen memetakannya dengan `WithEnvironment()` alih-alih meminta Anda menulis ulang konfigurasi. Jika sebuah port dikodekan secara keras, skill memberi tahu agen kapan harus mempertahankannya.

Inilah jenis tooling AI yang benar-benar menghemat waktu alih-alih menghasilkan lebih banyak pekerjaan untuk ditinjau.

## Deployment Kubernetes dan AKS Kelas Satu

Ini sudah ada di daftar keinginan sejak lama. Aspire 13.3 menghadirkan **dukungan deployment Kubernetes dan AKS kelas satu dengan Helm**. Anda sekarang dapat menentukan AKS sebagai target deployment langsung dari alat Aspire.

Bagi tim yang sudah menjalankan beban kerja produksi di AKS, ini menutup kesenjangan yang signifikan. Model aplikasi Aspire Anda sekarang memiliki jalur yang bersih dari pengembangan lokal ke Kubernetes tanpa perlu menulis chart Helm secara manual.

## Log Browser di Dasbor

Ini adalah salah satu fitur yang terlihat kecil sampai Anda men-debug masalah frontend.

API `WithBrowserLogs()` yang baru melampirkan sumber daya browser yang dilacak ke sumber daya apa pun yang mampu menggunakan endpoint. Aspire meluncurkan Chromium menggunakan pipe CDP privat dan melakukan streaming log konsol, permintaan jaringan, dan kesalahan langsung ke aliran log sumber daya:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost mendukung hal yang sama:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Kesalahan konsol, permintaan jaringan yang gagal, pengecualian sisi klien — semuanya terlihat di dasbor yang sama tempat Anda sudah memantau trace dan metrik. Tidak perlu lagi beralih tab ke DevTools browser untuk hal-hal dasar.

## Hasil Perintah Terstruktur

Perintah sumber daya telah mendapat peningkatan signifikan. Sebelumnya, perintah mengembalikan berhasil/gagal. Sekarang mereka mengembalikan hasil terstruktur: teks, JSON, atau Markdown yang mengalir melalui model, UI dasbor, CLI, dan alat MCP.

Dasbor mengikat semuanya dengan pusat notifikasi baru di header. Hasil perintah muncul sebagai notifikasi bertanda waktu dengan rendering Markdown dan aksi "Lihat respons".

Ini membuat perintah sumber daya benar-benar dapat dikomposisi. Sebuah integrasi sekarang dapat mengekspos perintah yang mengembalikan output yang bermakna — seperti URL tunnel — alih-alih hanya mengubah status di suatu tempat.

## Kesimpulan

Aspire 13.3 layak untuk diperbarui bahkan hanya untuk dukungan Kubernetes. Log browser dan hasil perintah terstruktur terasa seperti jenis peningkatan kualitas hidup yang cepat terakumulasi dalam alur kerja pengembangan sehari-hari.

Catatan rilis lengkap: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
