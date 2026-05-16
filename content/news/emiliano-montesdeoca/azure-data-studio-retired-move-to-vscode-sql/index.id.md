---
title: "Azure Data Studio Dihentikan: Pindahkan Alur Kerja Azure SQL Anda ke VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio dihentikan pada 6 Februari 2025, dengan dukungan berakhir pada 28 Februari 2026. Berikut jalur migrasi lengkap ke VS Code menggunakan ekstensi MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Azure Data Studio dihentikan pada 6 Februari 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), dengan dukungan berakhir pada 28 Februari 2026 — pengganti yang direkomendasikan adalah VS Code dengan ekstensi MSSQL.

## Yang Perlu Diinstal

Tiga hal untuk memulai:

- **Ekstensi MSSQL** — cari "SQL Server (mssql)" di VS Code Marketplace
- **Ekstensi SQL Database Projects** — skema sebagai kode, validasi build, penerbitan terpandu
- **.NET 8 SDK** — diperlukan oleh sistem build; SDK yang tidak ditemukan adalah masalah paling umum saat pertama kali digunakan

## Migrasi Koneksi dan Pengaturan ADS

Ekstensi MSSQL menyertakan **ADS Migration Toolkit** yang menangani migrasi satu kali dalam alur terpandu: koneksi tersimpan, grup koneksi, pengaturan, dan key binding semuanya diimpor secara otomatis.

## Memulihkan Kebiasaan F5

Pengguna ADS mengandalkan F5 untuk menjalankan kueri. Instal ekstensi **MSSQL Database Management Keymap** untuk mendapatkan kembali key binding bergaya ADS, termasuk F5.

## SQL Database Projects: Skema sebagai Kode

Klik kanan pada proyek → **Publish** → konfigurasi target → tinjau skrip T-SQL yang dihasilkan → deploy. Pratinjau skrip sebelum deployment adalah fitur keamanan utama. Template item menghasilkan stub untuk tabel, stored procedure, dan view — alur kerja yang sama seperti SSDT.

Masalah umum: **ketidakcocokan platform target** di file `.sqlproj` akan menyebabkan kesalahan build jika proyek dibuat untuk versi SQL Server yang berbeda.

## Schema Compare dan Schema Designer

Ekstensi juga mencakup **Schema Compare** (perbedaan antara proyek Anda dan database yang di-deploy) dan **Schema Designer** (pengeditan skema secara visual tanpa menulis DDL secara manual).

## Pengembang Microsoft Fabric

Pengaturannya identik, tetapi mulailah dari **portal Fabric** dan hubungkan database ke Git terlebih dahulu sebelum membukanya di VS Code. Microsoft memiliki panduan khusus: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Kesimpulan

Migrasi adalah alur terpandu satu kali, bukan pembangunan ulang secara manual. Instal tiga alat, jalankan ADS Migration Toolkit, pulihkan key binding Anda — dan Anda kembali normal dalam waktu kurang dari 10 menit.

Lihat [artikel lengkap](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) untuk tangkapan layar langkah demi langkah dan panduan khusus Fabric.
