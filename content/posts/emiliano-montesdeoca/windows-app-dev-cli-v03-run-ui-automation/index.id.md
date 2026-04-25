---
title: "Windows App Dev CLI v0.3: F5 dari Terminal dan UI Automation untuk Agen AI"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 menghadirkan winapp run untuk peluncuran debug dari terminal, winapp ui untuk otomasi antarmuka, dan paket NuGet baru yang membuat dotnet run bekerja dengan aplikasi yang dikemas."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Pengalaman F5 di Visual Studio sangat bagus. Tapi harus membuka VS hanya untuk menjalankan dan men-debug aplikasi Windows yang dikemas — baik di pipeline CI, workflow otomatis, atau saat agen AI menjalankan pengujian — terlalu berlebihan.

Windows App Development CLI v0.3 baru saja [dirilis](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) dan menangani hal ini secara langsung dengan dua fitur utama: `winapp run` dan `winapp ui`.

## winapp run: F5 dari Mana Saja

`winapp run` menerima folder aplikasi yang tidak dikemas dan sebuah manifest, lalu melakukan semua yang VS lakukan saat debug launch: mendaftarkan loose package, menjalankan aplikasi, dan mempertahankan `LocalState` antar re-deploy.

```bash
# Build aplikasi, lalu jalankan sebagai aplikasi yang dikemas
winapp run ./bin/Debug
```

Bekerja untuk WinUI, WPF, WinForms, Console, Avalonia, dan lainnya. Mode dirancang untuk developer maupun workflow otomatis:

- **`--detach`**: Meluncurkan dan segera mengembalikan kontrol ke terminal. Sempurna untuk CI.
- **`--unregister-on-exit`**: Membersihkan package yang terdaftar saat aplikasi ditutup.
- **`--debug-output`**: Menangkap pesan `OutputDebugString` dan exception secara real-time.

## Paket NuGet Baru: dotnet run untuk Aplikasi yang Dikemas

Untuk developer .NET ada paket NuGet baru: `Microsoft.Windows.SDK.BuildTools.WinApp`. Setelah diinstal, `dotnet run` menangani seluruh inner loop: build, menyiapkan loose-layout package, mendaftar di Windows, dan meluncurkan — semuanya dalam satu langkah.

```bash
winapp init
# atau
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation dari Command Line

Inilah fitur yang membuka skenario agentik. `winapp ui` memberikan akses UI Automation penuh ke aplikasi Windows mana pun yang sedang berjalan — WPF, WinForms, Win32, Electron, WinUI3 — langsung dari terminal.

Yang bisa dilakukan:

- Menampilkan semua jendela tingkat teratas
- Menelusuri pohon UI Automation lengkap dari sebuah jendela
- Mencari elemen berdasarkan nama, tipe, atau ID otomasi
- Klik, invoke, dan set nilai
- Mengambil screenshot
- Menunggu elemen muncul — ideal untuk sinkronisasi pengujian

Menggabungkan `winapp ui` dengan `winapp run` menghasilkan workflow build → jalankan → verifikasi yang lengkap dari terminal. Agen dapat menjalankan aplikasi, memeriksa status UI, berinteraksi secara programatik, dan memvalidasi hasilnya.

## Fitur Lainnya

- **`winapp unregister`**: Menghapus package yang sideloaded setelah selesai.
- **`winapp manifest add-alias`**: Menambahkan alias untuk menjalankan aplikasi berdasarkan nama dari terminal.
- **Tab completion**: Satu perintah untuk mengatur tab completion PowerShell.

## Cara Mendapatkannya

```bash
winget install Microsoft.WinAppCli
# atau
npm install -g @microsoft/winappcli
```

CLI dalam public preview. Lihat [repositori GitHub](https://github.com/microsoft/WinAppCli) untuk dokumentasi lengkap dan [pengumuman asli](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) untuk semua detailnya.
