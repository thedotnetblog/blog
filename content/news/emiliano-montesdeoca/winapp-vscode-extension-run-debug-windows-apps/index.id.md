---
title: "Ekstensi WinApp untuk VS Code: Jalankan, Debug, dan Paket Aplikasi Windows Tanpa Meninggalkan Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Ekstensi WinApp untuk VS Code membawa CLI Pengembangan Aplikasi Windows secara penuh langsung ke VS Code — jalankan, debug dengan package identity, paket, dan tandatangani aplikasi Windows tanpa menyentuh Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Postingan ini telah diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Jika kamu pernah mencoba mengembangkan aplikasi Windows di VS Code, kamu pasti tahu momen itu. Kamu sedang bekerja dengan penuh konsentrasi, mengedit kode di editor favorit — dan tiba-tiba kamu butuh package identity untuk Windows API. Atau perlu membuat MSIX. Atau menandatangani paket. Dan tiba-tiba kamu membuka Visual Studio, atau mencari "msix packaging without visual studio" pukul 11 malam.

Gesekan itu kini sudah tiada. [Ekstensi WinApp untuk VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) kini dalam public preview — dan ini adalah [CLI Pengembangan Aplikasi Windows](https://github.com/microsoft/WinAppCli) lengkap yang terintegrasi langsung ke VS Code. Tidak perlu instalasi terpisah, tidak perlu Visual Studio.

## Package Identity dari F5

Masalah dengan Windows API — notifikasi, background task, fitur AI on-device, share target — banyak di antaranya membutuhkan aplikasimu memiliki **package identity**. Tanpanya, API tersebut tidak akan berfungsi.

Secara tradisional, mendapatkan package identity berarti membangun installer MSIX lengkap atau menjalankan dari Visual Studio. Ekstensi WinApp mengubah ini sepenuhnya dengan tipe debug `winapp` kustom.

Tambahkan ini ke `launch.json`-mu:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Tekan F5. Ekstensi menemukan build output dan manifest-mu, memberikan package identity ke aplikasimu melalui `winapp run`, dan melampirkan debugger. Untuk aplikasi .NET, itu `coreclr` (butuh C# Dev Kit). C/C++ menggunakan `cppvsdbg`. Node/Electron menggunakan debugger bawaan.

Kamu bisa mengatur `preLaunchTask` agar proyek otomatis di-build sebelum setiap tekan F5 — alur build-and-launch yang sama seperti Visual Studio, hanya di VS Code.

## Semua Ada di Command Palette

Buka `Ctrl+Shift+P`, ketik `WinApp`, dan kamu mendapatkan toolkit lengkap:

- **Initialize Project** — konfigurasikan proyek dengan Windows SDK dan/atau Windows App SDK
- **Run Application** — jalankan sebagai aplikasi loose-layout packaged dengan package identity
- **Create MSIX Package** — paket aplikasi dengan opsi sertifikat dan runtime
- **Update Manifest Assets** — otomatis generate semua ikon aplikasi yang diperlukan dari satu gambar sumber
- **Generate / Install Certificate** — manajemen sertifikat pengembangan
- **Sign Package** — tandatangani MSIX atau executable
- **Run SDK Tool** — jalankan `makeappx`, `signtool`, `mt`, atau `makepri` langsung

Tidak perlu menginstal WinApp CLI juga. Sudah dibundel dengan ekstensi.

## Bekerja di Berbagai Framework

Ini bukan hanya alat untuk .NET WPF/WinUI. Ekstensi bekerja dengan:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Jangkauan ini disengaja. VS Code adalah tempat para developer web dan cross-platform tinggal. Jika kamu membangun aplikasi Tauri atau Electron yang membutuhkan packaging Windows, ekstensi ini mendukungmu tanpa perlu mengadopsi Visual Studio.

## Mengapa Penting bagi Developer .NET

Saya banyak bekerja di VS Code — di sinilah saya menulis Markdown, mengelola konfigurasi, mengedit proyek kecil, dan menjalankan terminal. Tapi untuk pengembangan desktop Windows di .NET, Visual Studio selalu menjadi satu-satunya pilihan nyata begitu kamu butuh sesuatu yang berhubungan dengan packaging.

Ekstensi ini menutup celah itu. Sekarang kamu bisa memiliki siklus pengembangan desktop Windows .NET yang lengkap — edit, build, jalankan dengan package identity, debug, paket, tanda tangan — tanpa meninggalkan VS Code. Ini adalah peningkatan kualitas kerja yang nyata.

## Memulai

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Atau cari **WinApp** di tampilan Extensions (`Ctrl+Shift+X`).

Persyaratan:
- Windows 10 atau lebih baru
- VS Code 1.109.0 atau lebih baru
- Ekstensi debugger untuk bahasa aplikasimu

Baca [pengumuman lengkap dari Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) untuk detail lebih lanjut.

## Penutup

Ekstensi WinApp untuk VS Code adalah tambahan yang disambut baik oleh developer desktop Windows .NET yang hidup di VS Code tapi harus beralih ke Visual Studio untuk pekerjaan packaging. Package identity dari F5, MSIX packaging dari command palette, manajemen sertifikat bawaan — ini adalah kumpulan fitur yang tepat.

Coba di proyek WPF atau WinUI berikutnya. Gesekan yang selama ini kamu hadapi baru saja jauh berkurang.
