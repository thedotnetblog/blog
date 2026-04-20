---
title: "Berhenti Mengawasi Terminal: Mode Terpisah Aspire Mengubah Alur Kerja"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 memungkinkan Anda menjalankan AppHost di background dan mengambil kembali terminal Anda. Dikombinasikan dengan perintah CLI baru dan dukungan agen, ini lebih besar dari yang terlihat."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Setiap kali Anda menjalankan Aspire AppHost, terminal Anda hilang. Terkunci. Terpakai hingga Ctrl+C. Perlu menjalankan perintah cepat? Buka tab baru. Ingin memeriksa log? Tab lain. Gesekan kecil ini menumpuk dengan cepat.

Aspire 13.2 memperbaiki ini. James Newton-King [menulis semua detailnya](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), dan jujur, ini adalah salah satu fitur yang segera mengubah cara Anda bekerja.

## Mode terpisah: satu perintah, terminal kembali

```bash
aspire start
```

Ini singkatan dari `aspire run --detach`. AppHost Anda boot di background dan Anda mendapatkan terminal kembali segera.

## Mengelola yang sedang berjalan

Berjalan di background hanya berguna jika Anda bisa mengelola apa yang berjalan. Aspire 13.2 menyertakan set lengkap perintah CLI:

```bash
# Daftar semua AppHost yang berjalan
aspire ps

# Periksa state AppHost tertentu
aspire describe

# Stream log dari AppHost yang berjalan
aspire logs

# Hentikan AppHost tertentu
aspire stop
```

## Gabungkan dengan mode terisolasi

Mode terpisah secara alami berpasangan dengan mode terisolasi:

```bash
aspire start --isolated
aspire start --isolated
```

Setiap instance mendapat port acak, rahasia terpisah, dan siklus hidupnya sendiri.

## Mengapa ini besar untuk agen coding

Agen coding yang bekerja di terminal Anda sekarang dapat:

1. Memulai aplikasi dengan `aspire start`
2. Mengkueri statusnya dengan `aspire describe`
3. Memeriksa log dengan `aspire logs` untuk mendiagnosis masalah
4. Menghentikannya dengan `aspire stop` saat selesai

Menjalankan `aspire agent init` menyiapkan file skill Aspire yang mengajarkan agen perintah-perintah ini.

## Kesimpulan

Mode terpisah adalah peningkatan alur kerja yang menyamar sebagai flag sederhana. Baca [postingan lengkap](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) dan dapatkan Aspire 13.2 dengan `aspire update --self`.
