---
title: ".NET 11 Preview 4: Template Server MCP, Pustaka Runtime-Async, API Proses"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 telah hadir. Sorotan utama: template server MCP di SDK, pustaka runtime yang dikompilasi dengan runtime-async, dotnet watch untuk mobile, dan perluasan besar API Proses."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 telah tersedia. Setiap rilis preview utama .NET menambahkan daftar panjang item di seluruh runtime, SDK, pustaka, ASP.NET Core, MAUI, C#, dan Entity Framework. Daripada mengulang daftar lengkapnya, berikut hal-hal yang menarik perhatian saya.

## Template Server MCP Hadir di SDK .NET

Item yang paling menarik: template proyek server MCP kini disertakan dalam SDK. Ini berarti `dotnet new mcp-server` (atau apa pun nama akhir perintahnya) berfungsi langsung tanpa konfigurasi tambahan. Bagi siapa saja yang membangun tooling MCP di .NET, ini sangat mengurangi hambatan awal. Integrasi MCP di toolchain platform mengisyaratkan arah yang dituju ekosistem.

## Pustaka Runtime Dikompilasi dengan Runtime-Async

Runtime itu sendiri kini mengompilasi pustaka standarnya menggunakan fitur runtime-async. Ini adalah perubahan internal yang mempengaruhi performa — mesin state async dalam runtime menjadi lebih efisien. Pentingnya di sini bukan pada perubahan API yang terlihat pengguna; melainkan bahwa runtime-async sudah cukup matang untuk digunakan pada BCL itu sendiri, yang merupakan sinyal bermakna tentang kesiapan fitur ini.

## Optimasi JIT dan Intrinsik Hardware

Preview 4 melanjutkan pekerjaan JIT. Peningkatan intrinsik hardware dan pembuatan kode hadir di sini — detailnya ada di catatan rilis runtime. Jenis perubahan ini biasanya meningkatkan throughput pada loop komputasi padat tanpa perubahan kode dari pihak Anda.

## Perluasan API Proses

Pembaruan besar untuk `System.Diagnostics.Process` hadir di Preview 4:

- `Process.RunAndCaptureTextAsync` — memulai proses, menangkap stdout/stderr, menunggu keluar, semuanya dalam satu panggilan tanpa risiko deadlock
- `KillOnParentExit` — penggabungan siklus hidup yang ringan antara proses induk dan anak
- API berbasis `SafeProcessHandle` yang lebih ramah trimmer

Jika Anda pernah menulis kode boilerplate untuk menangkap output proses tanpa memicu deadlock (pembacaan async dari stdout *dan* stderr secara bersamaan), `RunAndCaptureTextAsync` adalah API yang Anda butuhkan.

## dotnet watch untuk Android dan iOS

`dotnet watch` kini mendukung pemilihan perangkat untuk proyek .NET MAUI Android dan iOS. Iterasi lebih cepat di mobile tanpa mengelola koneksi perangkat secara manual dalam loop build.

## API Kompresi Berbasis Span

API encoder/decoder Deflate, ZLib, dan GZip berbasis span baru hadir di pustaka. Alokasi lebih sedikit saat menangani data terkompresi — relevan jika Anda melakukan pemrosesan data throughput tinggi.

## Coba Sekarang

[Unduh .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — ini adalah preview, belum siap produksi, tetapi layak dijalankan pada proyek Anda untuk menemukan masalah lebih awal sebelum siklus RC.

Posting asli: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
