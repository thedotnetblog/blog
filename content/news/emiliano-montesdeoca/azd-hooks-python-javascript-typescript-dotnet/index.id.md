---
title: "Hooks azd dengan Python, TypeScript, dan .NET: Selamat Tinggal Shell Script"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI kini mendukung hooks dalam Python, JavaScript, TypeScript, dan .NET. Tidak perlu lagi beralih ke Bash hanya untuk menjalankan script migrasi."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Jika pernah memiliki proyek yang sepenuhnya ditulis dalam .NET namun tetap harus menulis script Bash untuk hooks azd, rasa frustrasi itu sudah pasti familiar. Mengapa harus beralih ke sintaks shell di langkah pre-provisioning ketika seluruh proyek menggunakan C#?

Masalah ini kini memiliki solusi resmi. Azure Developer CLI [baru saja meluncurkan dukungan multi-bahasa untuk hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), dan hasilnya sesuai ekspektasi.

## Apa itu hooks

Hooks adalah script yang berjalan di titik-titik penting dalam siklus hidup `azd` — sebelum provisioning, setelah deployment, dan lainnya. Didefinisikan di `azure.yaml`, mereka memungkinkan injeksi logika kustom tanpa memodifikasi CLI.

Sebelumnya hanya Bash dan PowerShell yang didukung. Kini bisa menggunakan **Python, JavaScript, TypeScript, atau .NET** — dan `azd` menangani sisanya secara otomatis.

## Cara kerja deteksi bahasa

Cukup arahkan hook ke sebuah file dan `azd` akan menyimpulkan bahasa dari ekstensinya:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Tanpa konfigurasi tambahan. Jika ekstensinya ambigu, bisa menambahkan `kind: python` (atau bahasa yang sesuai) secara eksplisit.

## Detail penting per bahasa

### Python

Letakkan `requirements.txt` atau `pyproject.toml` di samping script (atau direktori induknya). `azd` akan otomatis membuat virtual environment, menginstal dependensi, dan menjalankan script.

### JavaScript dan TypeScript

Pola yang sama — letakkan `package.json` dekat script dan `azd` akan menjalankan `npm install` terlebih dahulu. Untuk TypeScript, menggunakan `npx tsx` tanpa langkah kompilasi dan tanpa `tsconfig.json`.

### .NET

Dua mode tersedia:

- **Mode project**: Jika ada `.csproj` di samping script, `azd` otomatis menjalankan `dotnet restore` dan `dotnet build`.
- **Mode single-file**: Di .NET 10+, file `.cs` mandiri dapat dijalankan langsung via `dotnet run script.cs`. Tidak perlu file project.

## Konfigurasi per executor

Setiap bahasa mendukung blok `config` opsional:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## Mengapa ini penting bagi developer .NET

Hooks adalah tempat terakhir dalam proyek berbasis azd yang memaksa pergantian bahasa. Sekarang seluruh deployment pipeline — dari kode aplikasi hingga lifecycle hooks — bisa hidup dalam satu bahasa. Utility .NET yang sudah ada bisa digunakan kembali di hooks, shared library bisa direferensikan, dan pemeliharaan shell script pun berakhir.

## Penutup

Salah satu perubahan yang terlihat kecil namun benar-benar mengurangi gesekan dalam workflow azd sehari-hari. Dukungan multi-bahasa untuk hooks sudah tersedia sekarang — cek [post resmi](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) untuk dokumentasi lengkap.
