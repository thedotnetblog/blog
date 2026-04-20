---
title: ".NET April 2026 Servicing — Patch Keamanan yang Harus Anda Terapkan Hari Ini"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Rilis servicing April 2026 menambal 6 CVE di .NET 10, .NET 9, .NET 8, dan .NET Framework — termasuk dua kerentanan eksekusi kode jarak jauh."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

[Pembaruan servicing April 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) untuk .NET dan .NET Framework sudah tersedia, dan versi ini mencakup perbaikan keamanan yang ingin Anda terapkan segera. Enam CVE ditambal, termasuk dua kerentanan eksekusi kode jarak jauh (RCE).

## Yang ditambal

| CVE | Tipe | Mempengaruhi |
|-----|------|---------|
| CVE-2026-26171 | Bypass Fitur Keamanan | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Eksekusi Kode Jarak Jauh** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Eksekusi Kode Jarak Jauh** | .NET 10, 9, 8 |
| CVE-2026-32203 | Penolakan Layanan | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Penolakan Layanan | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Penolakan Layanan | .NET Framework 2.0–4.8.1 |

## Versi yang diperbarui

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

## Yang harus dilakukan

Perbarui proyek dan pipeline CI/CD Anda ke versi patch terbaru. Dua kerentanan RCE bukan sesuatu yang Anda tunda.
