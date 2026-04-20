---
title: "Penilaian Modernisasi GitHub Copilot Adalah Alat Migrasi Terbaik yang Belum Anda Gunakan"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Ekstensi modernisasi GitHub Copilot tidak hanya menyarankan perubahan kode — melainkan menghasilkan penilaian migrasi lengkap dengan masalah yang dapat ditindaklanjuti, perbandingan target Azure, dan alur kerja kolaboratif."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

Memigrasikan aplikasi .NET Framework lama ke .NET modern adalah salah satu tugas yang semua orang tahu harus dilakukan tapi tidak ada yang ingin memulainya.

Jeffrey Fritz baru saja menerbitkan [analisis mendalam tentang penilaian modernisasi GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/).

## Ini bukan sekadar mesin saran kode

Ekstensi VS Code mengikuti model **Nilai → Rencanakan → Eksekusi**. Fase penilaian menganalisis seluruh basis kode dan menghasilkan dokumen terstruktur yang menangkap semuanya.

Penilaian disimpan di bawah `.github/modernize/assessment/`. Setiap run menghasilkan laporan independen.

## Dua cara untuk memulai

**Penilaian yang Direkomendasikan** — jalur cepat. Pilih dari domain yang dikurasi (Peningkatan Java/.NET, Kesiapan Cloud, Keamanan).

**Penilaian Kustom** — jalur terarah. Konfigurasikan apa yang akan dianalisis: komputasi target (App Service, AKS, Container Apps), OS target, analisis kontainerisasi.

## Rincian masalah dapat ditindaklanjuti

Setiap masalah dilengkapi level kritis:

- **Wajib** — harus diperbaiki atau migrasi akan gagal
- **Potensial** — mungkin berdampak pada migrasi, memerlukan penilaian manusia
- **Opsional** — perbaikan yang direkomendasikan, tidak akan memblokir migrasi

## Pendapat saya

Jika Anda memiliki aplikasi .NET Framework lama, ini adalah alat *terbaik* untuk memulai. Dokumen penilaian saja sudah sepadan dengan waktunya.

Baca [panduan lengkap](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) dan unduh [ekstensi VS Code](https://aka.ms/ghcp-appmod/vscode-ext).
