---
title: "Bagaimana Copilot Studio Bermigrasi ke .NET 10 WebAssembly dan Menjadi 20% Lebih Cepat"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Peningkatan .NET 10 WASM bukan hanya untuk proyek baru. Inilah yang diukur Copilot Studio setelah mengupgrade dari .NET 8: fingerprinting otomatis, WasmStripILAfterAOT secara default, dan angka performa eksekusi nyata."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Tim Copilot Studio melakukan sesuatu yang membuat semua pengembang Blazor WASM penasaran: mereka benar-benar mengupgrade aplikasi produksi dari .NET 8 ke .NET 10 dan mengukur hasilnya. Postingan ini membagikan angka-angka spesifik, yang jarang terjadi dan benar-benar berguna.

## Upgrade-nya Membosankan (Itu Hal yang Baik)

Update target framework, refresh referensi paket, perbaiki breaking changes. Itu saja. Build .NET 10 sekarang sudah berjalan di produksi. Migrasi itu sendiri bukanlah bagian yang menarik — perubahan di .NET 10 itulah yang menarik.

## Fingerprinting Aset Otomatis

Sebelumnya, mendistribusikan aplikasi WASM berarti menulis skrip kustom untuk mengganti nama aset yang diterbitkan dengan hash SHA256 untuk cache-busting. Copilot Studio memiliki skrip PowerShell yang melakukan persis ini — mengganti nama file, menyuntikkan atribut `integrity` ke dalam JavaScript loader, mengelola semuanya secara manual.

Di .NET 10, semua itu sudah terintegrasi. Aset yang diterbitkan secara otomatis di-fingerprint, diimpor langsung dari `dotnet.js`, dan divalidasi integritasnya tanpa intervensi manual. Tim menghapus skrip penggantian nama.

Perubahan kecil dalam cakupan, pengurangan kompleksitas yang signifikan.

## WasmStripILAfterAOT Kini Aktif Secara Default

Di .NET 8, menghapus IL dari assembly yang dikompilasi AOT bersifat opt-in. Di .NET 10 ini adalah default. Setelah kompilasi AOT, bytecode IL asli dihapus dari output — tidak diperlukan saat runtime, dan menyimpannya akan menggembungkan ukuran paket tanpa alasan.

Copilot Studio menggunakan optimasi spesifik: ia mendistribusikan baik engine JIT (startup cepat) maupun engine AOT (performa steady-state maksimum), memuat keduanya secara paralel dan melakukan handoff dari JIT ke AOT setelah siap. Ini juga mendeduplikasi file yang identik antara kedua engine.

Perilaku stripping IL baru berarti assembly AOT tidak lagi cocok bit-for-bit dengan padanan JIT-nya, sehingga lebih sedikit file yang dideduplikasi:
- .NET 8: 59 file bersama
- .NET 10: 22 file bersama

Hasil bersih: ukuran paket sekitar 15% lebih besar untuk engine AOT. Download AOT ~6% lebih lambat di LAN cepat, ~17% lebih lambat di 4G. Tapi semuanya terjadi di latar belakang setelah aplikasi sudah interaktif.

## Angka Performa

Inilah bagian yang penting:

- **~20% lebih cepat** pada panggilan pertama (cold path)
- **~5% lebih cepat** pada panggilan berikutnya (warm path)

Peningkatan paling terlihat di "bot besar" — agen besar dan kompleks di mana kode yang dikompilasi AOT mendominasi. Untuk alur kerja yang lebih sederhana, keuntungannya lebih kecil.

## Jika Anda Masih di .NET 8

Cerita migrasinya sangat sederhana: update `<TargetFramework>`, refresh referensi paket, hapus skrip fingerprinting kustom apa pun, dan Anda akan otomatis mendapat manfaat dari `WasmStripILAfterAOT`. Jika Anda mengkompilasi AOT, harapkan keuntungan performa serupa.

Catatan dari postingan: jika Anda memuat runtime .NET WASM di dalam `WebWorker`, set `dotnetSidecar = true` saat menginisialisasi.

Post asli: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
