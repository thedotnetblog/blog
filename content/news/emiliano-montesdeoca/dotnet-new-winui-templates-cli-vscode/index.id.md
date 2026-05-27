---
title: "dotnet new WinUI: Buat Aplikasi Windows Tanpa Menyentuh Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Template proyek WinUI kini berfungsi dengan dotnet new — aplikasi kosong, pola NavigationView, dan lainnya. Dukungan VS Code, tidak perlu Visual Studio, dengan default Fluent Design sudah terintegrasi."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

Pengembangan WinUI dahulu memerlukan Visual Studio. Itu berubah: Microsoft telah menerbitkan template proyek dan item open source untuk WinUI yang berfungsi dengan `dotnet new`, membawa pengembangan aplikasi Windows ke dalam alur kerja CLI standar.

## Mulai dengan Tiga Perintah

```shell
# Instal template
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Buat aplikasi NavigationView
dotnet new winui-navview -n MyApp

# Jalankan
cd MyApp
dotnet run
```

Tanpa Visual Studio, tanpa pengaturan proyek manual. Aplikasi berjalan dengan `dotnet run`.

## Yang Termasuk di Dalamnya

**Template kosong** (`dotnet new winui`) — titik awal modern dengan bilah judul Fluent yang sudah terhubung, ikon aplikasi default yang diperbarui dengan aset `.ico`, dan default mode terang/gelap yang benar. Lebih baik dari template kosong lama yang membuat Anda mengonfigurasi dasar-dasar sendiri.

**Template NavigationView** (`dotnet new winui-navview`) — pola navigasi master-detail, sepenuhnya terhubung dengan NavigationView, bilah judul modern, dan struktur navigasi multi-halaman. Mengikuti siluet aplikasi Windows standar untuk aplikasi berbasis navigasi. Jika Anda membangun sesuatu dengan navigasi samping, mulai dari sini.

Kedua template mengikuti [siluet aplikasi Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — pola Fluent Design modern untuk tata letak, navigasi, dan struktur visual — langsung dari kotak.

## Mengapa Penting bagi Developer yang Tidak Menggunakan Visual Studio

Developer WinUI yang menggunakan VS Code, Rider, atau alat baris perintah selama ini kurang diperhatikan. Template Visual Studio yang ada tidak dapat digunakan di luar VS — harus membuat ulang struktur proyek secara manual dan menghubungkan dasar-dasarnya.

Template ini bersumber terbuka (lihat [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), dikembangkan dari [umpan balik komunitas](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), dan tersedia sekarang. Dukungan Visual Studio sedang dalam pengerjaan — template yang sama ini pada akhirnya akan berfungsi di sana juga.

Untuk tim yang ingin mengotomatiskan pengaturan proyek WinUI mereka, mengintegrasikannya ke dalam CI, atau sekadar menggunakan editor selain Visual Studio, ini adalah peningkatan yang berarti.

Posting asli: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
