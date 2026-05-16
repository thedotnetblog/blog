---
title: "Pembaruan Azure Developer CLI (azd) April 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd merilis lima versi pada April 2026, dengan fitur unggulan dukungan hook multi-bahasa untuk Python, JavaScript, TypeScript, dan .NET — ditambah pratinjau publik azd update, pemeriksaan kuota AI, dan lainnya."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) merilis lima versi pada April 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 hingga 1.24.2), dengan tema besar berupa hook yang kini berjalan dalam Python, JavaScript, TypeScript, dan .NET — tidak hanya Bash dan PowerShell.

## Hook multi-bahasa di azure.yaml

Hook kini dapat menunjuk ke file `.py`, `.js`, `.ts`, atau `.cs` selain skrip shell. Setiap bahasa mendapat resolusi dependensi otomatis:

- **Python** — mendeteksi `requirements.txt` atau `pyproject.toml`, membuat virtualenv, dan menginstal dependensi sebelum berjalan. Konfigurasikan nama env dengan `virtualEnvName`.
- **JavaScript / TypeScript** — mendeteksi `package.json` dan menjalankan `npm install` secara otomatis. TypeScript dieksekusi via `npx tsx` tanpa langkah kompilasi. Pilih package manager Anda dengan blok konfigurasi `packageManager`.
- **.NET** — menjalankan file `.cs` dengan `dotnet run`. Skrip single-file didukung di .NET 10+. Konfigurasikan framework target melalui blok `configuration/framework`.

Ini berarti tim yang sudah bekerja dengan salah satu bahasa ini tidak perlu lagi memelihara hook Bash atau PowerShell terpisah hanya untuk menghubungkan event lifecycle provisioning.

## azd update masuk pratinjau publik

`azd update` kini dalam pratinjau publik di semua platform. Satu perintah menangani pembaruan terlepas dari bagaimana azd awalnya diinstal — tidak perlu lagi melacak jalur Homebrew, WinGet, atau MSI secara terpisah.

## Mode non-interaktif via AZD_NON_INTERACTIVE

Menyetel `AZD_NON_INTERACTIVE=true` (atau menggunakan `--non-interactive` / `--no-prompt`) kini menghasilkan kegagalan yang konsisten dan deterministik dalam pipeline CI/CD ketika input yang diperlukan tidak dapat diselesaikan secara otomatis. Sebelumnya perilakunya tidak konsisten di berbagai perintah.

## Pemeriksaan kuota model AI

`azd provision` memvalidasi kuota Azure Cognitive Services sebelum mencoba menyediakan sumber daya model AI. Deployment yang akan gagal karena batas kuota kini menampilkan error lebih awal dalam proses daripada di tengah provisioning.

## "Perbaiki error ini" dalam pemecahan masalah Copilot

Integrasi pemecahan masalah Copilot di azd mendapat kemampuan untuk langsung menerapkan perbaikan yang disarankan — bukan hanya mendeskripsikannya. Ketika agen mengidentifikasi masalah yang dapat diperbaiki, agen dapat melakukan perubahan secara langsung.

## Penyedia provisioning kustom dan resolver rahasia Key Vault

Pembuat ekstensi kini dapat mendaftarkan backend infrastruktur alternatif dengan `WithProvisioningProvider()`. Secara terpisah, azd secara otomatis menyelesaikan referensi `@Microsoft.KeyVault(...)` sebelum meneruskan konfigurasi ke ekstensi, menghilangkan kebutuhan resolusi rahasia manual di penyedia kustom.

## Pengecualian template dan mode watch

Dua file ignore baru memberikan kontrol lebih halus atas penanganan file:
- **`.azdignore`** — mengecualikan file khusus kontributor (dokumentasi, konfigurasi CI) dari salinan template agar pengguna akhir mendapat scaffold proyek yang bersih.
- **`.azdxignore`** — mengecualikan direktori dari pemicu rebuild selama `azd x watch`, mengurangi noise selama pengembangan iteratif.

## Preflight nama yang dipesan dan opsi docker.network

azd kini memperingatkan ketika nama sumber daya yang diprediksi mengandung kata-kata yang dipesan Azure (`MICROSOFT`, `WINDOWS`, atau awalan `LOGIN`) sebelum provisioning dimulai. Opsi `docker.network` baru meneruskan `--network` ke `docker build`, berguna di lingkungan proxy perusahaan yang memerlukan jaringan Docker tertentu.

## Perbaikan keamanan

Paket MSI Windows kini menyertakan verifikasi penandatanganan kode. Perbaikan terpisah menutup kebocoran variabel lingkungan yang dapat mengekspos nilai di seluruh batas perintah ekstensi.

---

Bulan yang padat — dukungan hook multi-bahasa khususnya menghilangkan titik gesekan nyata bagi tim yang tidak bekerja terutama dalam Bash. Lihat [catatan rilis lengkap](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) untuk changelog lengkap dari kelima versi.
