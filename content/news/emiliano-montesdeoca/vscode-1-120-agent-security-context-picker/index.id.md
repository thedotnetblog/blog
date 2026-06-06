---
title: "VS Code 1.120: Prompt Kata Sandi Aman, Pemilih Ukuran Konteks, Metadata GitHub di Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 adalah rilis terfokus untuk pengguna Copilot: penanganan prompt kata sandi yang aman, pemilih ukuran konteks model, metadata PR GitHub di sesi agen, dan manajemen arsip sesi."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 hadir dengan serangkaian peningkatan agen Copilot yang kecil secara individual tetapi terasa lebih baik dalam penggunaan sehari-hari.

## Deteksi Prompt Kata Sandi Aman di Terminal Agen

Saat agen Copilot menjalankan perintah terminal yang memicu prompt kata sandi atau passphrase, VS Code kini mendeteksinya dan menampilkan dialog konfirmasi. Dialog memfokuskan terminal sehingga Anda dapat mengetik rahasia secara langsung — dan yang penting, rahasia tidak pernah diarahkan melalui model.

Ini adalah peningkatan keamanan yang signifikan. Sebelumnya, agen yang menjalankan perintah yang memicu prompt autentikasi dapat menciptakan situasi di mana pengguna mungkin secara tidak sengaja mengekspos kredensial. Pengumuman pembaca layar berarti pengguna aksesibilitas juga mendapatkan notifikasi.

## Pemilih Ukuran Konteks di Pemilih Model

Pemilih ukuran konteks baru memungkinkan Anda memilih berapa banyak konteks yang digunakan model untuk sebuah sesi. Model yang berbeda memiliki ukuran jendela konteks yang berbeda, dan beberapa alur kerja mendapat manfaat dari membatasinya (latensi lebih rendah, biaya lebih rendah) atau memaksimalkannya (basis kode yang kompleks, sesi yang berjalan lama).

## Metadata PR GitHub di Sesi Agent Host

Untuk sesi yang didukung oleh repositori GitHub, VS Code kini menampilkan metadata GitHub — termasuk tombol pull request — di UI agent host. Lebih sedikit perpindahan konteks ke browser atau ekstensi GitHub saat Anda mengerjakan PR.

## Manajemen Arsip Sesi Chat

Dua peningkatan untuk Quick Pick sesi:
- Sesi yang diarsipkan disembunyikan secara default (lebih sedikit kekacauan visual)
- Pencarian masih cocok dengan sesi yang diarsipkan, sehingga Anda dapat memulihkan satu berdasarkan judul

Sesi juga dikelompokkan berdasarkan kebaruan secara default, memudahkan pencarian pekerjaan terbaru.

## Penemuan Plugin CLI Copilot

VS Code kini secara otomatis menemukan plugin Copilot CLI yang diinstal pengguna dari `~/.copilot/installed-plugins/`. Jika Anda telah menyiapkan WinUI atau keterampilan agen khusus domain lainnya, mereka diambil tanpa konfigurasi manual.

## API Editor Diff Kustom (Pratinjau)

Untuk penulis ekstensi: API yang diusulkan baru `customDiffEditorProvider` memungkinkan ekstensi merender diff terpadu dalam satu webview dengan akses ke dokumen asli dan yang dimodifikasi, alih-alih dua tampilan editor kustom berdampingan.

Posting asli: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
