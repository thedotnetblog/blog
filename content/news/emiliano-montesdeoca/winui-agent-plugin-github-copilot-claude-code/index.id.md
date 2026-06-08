---
title: "Plugin Agen WinUI untuk GitHub Copilot dan Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft merilis keterampilan agen untuk pengembangan WinUI: scaffold, build, jalankan, uji, iterasi - semuanya dengan GitHub Copilot CLI atau Claude Code. Inovasi kunci: alat bertujuan khusus yang mendasarkan agen pada fakta spesifik WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft menerbitkan set keterampilan agen sumber terbuka untuk pengembangan aplikasi WinUI, tersedia di [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Instalasi dan Pengaturan

Instal plugin dengan `/plugin install winui@awesome-copilot`, lalu jalankan pengaturan awal dengan `/winui:winui-setup`. Proses pengaturan memverifikasi prasyarat, menginstal dependensi yang diperlukan, dan mengonfigurasi lingkungan untuk pengembangan aplikasi WinUI.

## Loop Pengembangan End-to-End

Keterampilan mencakup siklus pengembangan lengkap:

- **Scaffold:** Menghasilkan template proyek yang benar menggunakan `dotnet new WinUI` dengan parameter yang sesuai — agen mengetahui template yang benar dan nilai konfigurasi default.
- **Build:** Mengelola model eksekusi yang dikemas yang diperlukan aplikasi WinUI, termasuk penandatanganan paket dan konfigurasi manifes.
- **Interaksi dan validasi:** Meluncurkan aplikasi, berinteraksi dengannya, dan memvalidasi perilaku.
- **Memperbaiki kesalahan kompilasi:** Agen memahami pesan kesalahan spesifik WinUI dan mengetahui cara menyelesaikannya.

## Efisiensi Token melalui Alat Bertujuan Khusus

Inovasi kunci adalah bahwa keterampilan mencakup alat bertujuan khusus yang mengambil data referensi konkret sesuai permintaan:

- Detail API WinUI dan Fluent Design
- Pola MVVM dan praktik terbaik
- Pengemasan MSIX, penandatanganan kode, dan pengiriman Store
- Aksesibilitas, tema, dan otomasi UI

Alih-alih menyuntikkan seluruh dokumentasi WinUI ke dalam konteks, alat mengambil tepat apa yang dibutuhkan agen pada saat dibutuhkan. Ini menjaga penggunaan konteks tetap efisien dan meningkatkan presisi dalam domain khusus.

## Mengapa Keterampilan Bertujuan Khusus Penting

Model bahasa serba guna memiliki pengetahuan terbatas tentang nuansa spesifik WinUI: model eksekusi yang dikemas, API Fluent Design, integrasi MSIX, atau cara spesifik Windows App SDK membungkus fungsionalitas Win32. Alat bertujuan khusus menyelesaikan ini dengan mendasarkan agen pada fakta WinUI yang terverifikasi daripada pengetahuan model yang berpotensi usang atau salah.

Pola yang sama berlaku untuk kerangka kerja atau SDK khusus apa pun dengan konvensi dan persyaratannya sendiri yang berbeda dari pola pengembangan umum.

Post asli: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
