---
title: "Pembaruan Maret Visual Studio Memungkinkan Kamu Membangun Agen Copilot Kustom — dan Alat find_symbol Adalah Hal Besar"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Pembaruan Maret 2026 Visual Studio menghadirkan agen Copilot kustom, skill agen yang dapat digunakan ulang, alat find_symbol yang sadar bahasa, dan profiling bertenaga Copilot dari Test Explorer. Inilah yang penting."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "visual-studio-march-2026-custom-copilot-agents" >}}).*

Visual Studio baru saja mendapatkan pembaruan Copilot paling signifikan hingga saat ini. Mark Downie [mengumumkan rilis Maret](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), dan judul utamanya adalah agen kustom — tapi jujur saja, alat `find_symbol` yang tersembunyi lebih jauh mungkin adalah fitur yang paling mengubah alur kerjamu.

Mari saya uraikan apa yang sebenarnya ada di sini.

## Agen Copilot kustom di repo kamu

Ingin Copilot mengikuti standar pengkodean timmu, menjalankan pipeline build, atau mengquery dokumen internal? Sekarang kamu bisa membangun persis itu.

Agen kustom didefinisikan sebagai file `.agent.md` yang kamu letakkan di `.github/agents/` di repositorimu. Setiap agen mendapatkan akses penuh ke kesadaran workspace, pemahaman kode, alat, model pilihanmu, dan koneksi MCP ke layanan eksternal.

Ini adalah pola yang sama yang sudah didukung VS Code — dan sangat menyenangkan melihat Visual Studio menyusul.

## Skill agen: paket instruksi yang dapat digunakan ulang

Skill secara otomatis diambil dari `.github/skills/` di repositorimu atau `~/.copilot/skills/` di profilmu.

## find_symbol: navigasi sadar bahasa untuk agen

Di sinilah hal-hal menjadi sangat menarik. Alat `find_symbol` baru memberikan mode agen Copilot navigasi simbol yang benar-benar didukung oleh layanan bahasa. Alih-alih mencari kode sebagai teks, agen dapat:

- Menemukan semua referensi ke simbol di seluruh proyekmu
- Mengakses informasi tipe, deklarasi, dan metadata cakupan
- Menavigasi situs panggilan dengan kesadaran bahasa penuh

Artinya dalam praktik: ketika kamu meminta Copilot untuk refaktor metode atau memperbarui tanda tangan parameter di seluruh situs panggilan, ia benar-benar dapat melihat struktur kodemu.

## Profil tes dengan Copilot

Sekarang ada perintah **Profile with Copilot** di menu konteks Test Explorer. Pilih tes, klik profil, dan Profiling Agent secara otomatis menjalankannya dan menganalisis performa.

## Kesimpulan

Agen kustom dan skill adalah judul utama, tapi `find_symbol` adalah pahlawan diam-diam — ini secara fundamental mengubah seberapa akurat Copilot bisa dalam merefaktor kode .NET. Unduh [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) untuk mencoba semuanya.
