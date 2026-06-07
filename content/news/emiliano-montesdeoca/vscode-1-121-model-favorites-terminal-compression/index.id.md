---
title: "VS Code 1.121: Pin Model Favorit, Kompresi Output Terminal, Agent SSH"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 menambahkan favorit model, kompresi output terminal yang diperluas untuk test runner dan build tool, timer diam-idle untuk terminal latar belakang, dan autentikasi SSH keyboard-interaktif di agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 melanjutkan peningkatan kualitas agen Copilot dari 1.120, berfokus pada manajemen model dan perilaku terminal.

## Pin Model Favorit

Pemilih model sekarang mendukung penyematan. Jika Anda selalu menggunakan model yang sama atau dua, sematkan ke bagian atas daftar. Mengurangi scroll saat Anda memiliki akses ke banyak model dari beberapa penyedia.

## Kompresi Output Terminal yang Diperluas

Alat terminal agen sudah mengompresi output untuk perintah umum. 1.121 memperluas ini untuk mencakup test runner dan build tool:

- **Test runner:** `pytest`, `jest`, `cargo test`
- **Build tool:** `tsc`, `cargo build`, `make`
- **Linter, Docker, manajer paket**

Output build yang panjang dan laporan kegagalan uji dikompres menjadi kutipan yang relevan sebelum diteruskan ke model. Ini menjaga penggunaan konteks tetap terkelola saat agen menjalankan siklus build atau test suite yang dapat menghasilkan ribuan baris output.

## Timer Diam-Idle untuk Terminal Latar Belakang

Timer diam-idle baru untuk alat `run_in_terminal`: jika perintah sinkron tidak menghasilkan output selama periode yang dapat dikonfigurasi, secara otomatis ditingkatkan ke eksekusi latar belakang. Ini mencegah perintah yang berjalan lama memblokir agen saat memproses secara diam-diam. Anda mendapatkan ID terminal untuk diperiksa nanti.

## Variabel Lingkungan VSCODE_AGENT

Saat Copilot Chat menjalankan perintah di terminal, variabel lingkungan `VSCODE_AGENT` sekarang diatur. Berguna jika Anda memiliki skrip atau alat yang berperilaku berbeda saat dipanggil dari sesi agen versus dipanggil secara interaktif.

## Tambahkan ke Chat dari Browser

Klik kanan di browser terintegrasi sekarang menampilkan opsi "Tambahkan ke Chat". Pilih konten dari halaman web dan tambahkan langsung ke konteks Copilot Chat tanpa copy-paste.

## Diperbaiki: Perintah Shell Multi-baris di Agent Host

Perbaikan bug yang sudah lama ditunggu: perintah shell multi-baris di alat terminal Agent Host sekarang berfungsi dengan benar. Sebelumnya ini bisa gagal atau menghasilkan perilaku yang salah.

## Autentikasi SSH Keyboard-Interaktif

Koneksi SSH Agent Host sekarang mendukung autentikasi keyboard-interaktif — metode autentikasi fallback yang digunakan oleh beberapa server SSH (termasuk beberapa konfigurasi perusahaan yang lebih lama). Agen yang bekerja pada host SSH jarak jauh lebih kecil kemungkinannya mengalami kegagalan autentikasi.

Posting asli: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
