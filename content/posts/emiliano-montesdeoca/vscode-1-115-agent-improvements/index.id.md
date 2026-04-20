---
title: "VS Code 1.115 — Notifikasi Terminal Latar Belakang, Mode Agen SSH, dan Lainnya"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 menghadirkan notifikasi terminal latar belakang untuk agen, hosting agen jarak jauh SSH, tempel file di terminal, dan pelacakan edit sadar sesi. Inilah yang penting untuk developer .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 baru saja [rilis](https://code.visualstudio.com/updates/v1_115), dan meskipun ini adalah rilis yang lebih ringan dalam hal fitur utama, peningkatan terkait agen benar-benar berguna jika kamu bekerja dengan asisten coding AI setiap hari.

Biarkan aku menyoroti apa yang sebenarnya layak diketahui.

## Terminal latar belakang berkomunikasi kembali ke agen

Ini adalah fitur unggulan. Terminal latar belakang sekarang secara otomatis memberi tahu agen ketika perintah selesai, termasuk kode keluar dan output terminal.

Mengapa ini penting? Jika kamu menggunakan mode agen Copilot untuk menjalankan perintah build atau suite test di latar belakang, kamu tahu rasa sakit "apakah itu sudah selesai?" — terminal latar belakang pada dasarnya adalah tembak dan lupakan. Sekarang agen mendapat pemberitahuan ketika `dotnet build` atau `dotnet test`mu selesai, melihat output, dan dapat bereaksi sesuai. Ini adalah perubahan kecil yang membuat alur kerja yang digerakkan agen jauh lebih andal.

Ada juga alat `send_to_terminal` baru yang memungkinkan agen mengirim perintah ke terminal latar belakang dengan konfirmasi pengguna.

## Hosting agen jarak jauh SSH

VS Code sekarang mendukung koneksi ke mesin jarak jauh melalui SSH, secara otomatis menginstal CLI dan memulainya dalam mode host agen.

## Pelacakan edit dalam sesi agen

Edit file yang dibuat selama sesi agen sekarang dilacak dan dipulihkan, dengan diff, undo/redo, dan pemulihan state.

## Kesadaran tab browser dan peningkatan lainnya

Beberapa tambahan kualitas hidup lainnya:

- **Pelacakan tab browser** — chat sekarang bisa melacak dan menautkan ke tab browser yang dibuka selama sesi
- **Tempel file di terminal** — tempel file (termasuk gambar) ke terminal dengan Ctrl+V
- **Cakupan tes di minimap** — indikator cakupan tes sekarang muncul di minimap
- **Pinch-to-zoom di Mac** — browser terintegrasi mendukung gestur pinch-to-zoom

## Kesimpulan

VS Code 1.115 adalah rilis inkremental, tapi peningkatan agen — notifikasi terminal latar belakang, hosting agen SSH, dan pelacakan edit — menambah pengalaman yang terasa lebih lancar secara keseluruhan. Lihat [catatan rilis lengkapnya](https://code.visualstudio.com/updates/v1_115) untuk setiap detail.
