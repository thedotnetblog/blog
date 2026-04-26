---
title: "Aspire 13.2 Menambahkan Bun, Kontainer yang Lebih Baik, dan Friksi Debugging yang Lebih Rendah"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 menambahkan dukungan kelas utama untuk Bun pada aplikasi Vite, memperbaiki keandalan Yarn, dan menghadirkan peningkatan kontainer yang membuat perilaku development lokal lebih jujur. Berikut apa yang benar-benar berubah dan kenapa itu penting."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Kalau Anda sudah membangun backend .NET dengan frontend JavaScript di Aspire, 13.2 adalah jenis pembaruan yang diam-diam membuat hari Anda lebih baik. Tidak ada paradigma baru yang heboh. Hanya peningkatan solid pada hal-hal yang sedikit mengganggu.

Mari lihat apa yang benar-benar hadir.

## Bun Kini Dukungan Kelas Utama

Fitur utamanya: dukungan Bun untuk aplikasi Vite di Aspire. Satu panggilan fluent, selesai.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

Kalau tim Anda sudah memakai Bun — dan mungkin memang iya, mengingat waktu instalasinya jauh lebih cepat serta startup-nya lebih gesit — Aspire sekarang tidak lagi memaksa Anda berenang melawan arus. Sebelumnya, Aspire mengasumsikan npm dan Anda harus membuat workaround. Sekarang `.withBun()` adalah opsi kelas utama, berdampingan dengan `.withYarn()` dan perilaku default npm.

Kenapa ini penting? Karena kecepatan tooling JavaScript langsung memengaruhi inner dev loop Anda. Kalau frontend Anda butuh 30 detik untuk memasang dependensi setiap kali membuat environment baru, semuanya akan menumpuk. Bun memangkas itu secara drastis.

Padanan AppHost dalam C# didokumentasikan di [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) kalau Anda lebih suka menulis dalam C# — pola yang sama tetap berlaku.

## Yarn Jadi Lebih Andal

Bun memang jadi sorotan, tapi pengguna Yarn mendapat sesuatu yang mungkin lebih penting: lebih sedikit kegagalan misterius. Aspire 13.2 meningkatkan keandalan `withYarn()` bersama `addViteApp()`.

Perbaikan seperti ini tidak terdengar menarik sampai Anda menghabiskan 20 menit mencari tahu kenapa resource frontend berbasis Yarn tidak mau start. Anggap saja sudah beres.

## Penerbitan Kontainer yang Benar-Benar Bisa Anda Pahami

Ada dua peningkatan kontainer yang layak diketahui:

### Kebijakan Pull yang Eksplisit

Penerbitan Docker Compose sekarang mendukung `PullPolicy`, termasuk opsi `Never`:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

Ini adalah alur kerja yang pada dasarnya berkata, "pakai image yang sudah saya build dan jangan bawa registry ke dalamnya." Sangat berguna saat Anda melakukan iterasi lokal pada image yang Anda build dan publish secara manual, atau saat CI menghasilkan image dan Anda ingin Compose memakai image itu persis, tanpa menyelinapkan pull jarak jauh.

### Volume PostgreSQL 18+ Kembali Berfungsi

PostgreSQL 18 mengubah tata letak internal direktori datanya. Itu mematahkan mapping volume di Aspire secara diam-diam — volume data Anda disiapkan, tetapi persistence sebenarnya tidak berjalan dengan benar. 13.2 memperbaikinya.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

Kalau Anda menjalankan PostgreSQL 18 atau lebih baru dengan data volume, perbarui ke Aspire 13.2 dan jangan pikirkan lagi.

## Peningkatan Kualitas Hidup Saat Debugging

Beberapa hal yang membuat sesi AppHost saat step-through jadi tidak terlalu menjengkelkan:

- **`DebuggerDisplayAttribute` pada tipe inti** — `DistributedApplication`, resource, dan ekspresi endpoint sekarang menampilkan nilai yang berguna di debugger, bukan memaksa Anda menyusuri pohon objek
- **Pesan kegagalan `WaitFor` yang lebih baik** — saat resource gagal start, konteks error sekarang benar-benar membantu
- **`BeforeResourceStartedEvent` dipicu pada waktu yang tepat** — hanya saat resource benar-benar mulai, bukan pada transisi state yang tidak relevan
- **`launchSettings.json` lebih tangguh** — lebih kecil kemungkinan konfigurasi yang rusak merusak startup dev Anda

Masing-masing perubahan ini tidak terlalu heboh, tetapi bersama-sama mereka mengurangi friksi dalam pengalaman debugging. Kalau Anda pernah harus menyelam tiga tingkat ke dalam objek resource Aspire hanya untuk mencari tahu endpoint mana yang dipakai, peningkatan debugger display saja sudah layak untuk update.

## Penutup

Aspire 13.2 adalah rilis yang fokus pada kualitas. Dukungan Bun memang jadi headline, tetapi peningkatan kontainer dan debugging-lah yang akan membuat pekerjaan harian terasa lebih mulus. Layak diperbarui — terutama jika Anda memakai PostgreSQL 18 dengan data volume.

Detail lengkap ada di [post asli oleh David Pine](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) dan [dokumen what's new Aspire 13.2](https://aspire.dev/whats-new/aspire-13-2/).