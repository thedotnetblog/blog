---
title: "Azure DevOps Akhirnya Memperbaiki UX Editor Markdown yang Dikeluhkan Semua Orang"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Editor Markdown Azure DevOps untuk item kerja mendapatkan perbedaan yang lebih jelas antara mode pratinjau dan mode edit. Ini perubahan kecil yang memperbaiki masalah alur kerja yang benar-benar mengganggu."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-devops-markdown-editor-work-items" >}}).*

Jika Anda menggunakan Azure Boards, Anda mungkin pernah mengalami ini: Anda sedang membaca deskripsi item kerja, mungkin meninjau kriteria penerimaan, dan secara tidak sengaja mengklik dua kali. Boom — Anda dalam mode edit. Anda tidak ingin mengedit apa pun. Anda hanya membaca.

Dan Hellem [mengumumkan perbaikannya](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), dan ini adalah salah satu perubahan yang terdengar kecil tetapi sebenarnya menghilangkan gesekan nyata dari alur kerja harian Anda.

## Apa yang berubah

Editor Markdown untuk bidang teks item kerja sekarang dibuka dalam **mode pratinjau secara default**. Anda dapat membaca dan berinteraksi dengan konten — mengikuti tautan, meninjau pemformatan — tanpa khawatir secara tidak sengaja masuk ke mode edit.

Saat Anda benar-benar ingin mengedit, Anda mengklik ikon edit di bagian atas bidang. Setelah selesai, Anda keluar kembali ke mode pratinjau secara eksplisit.

## Mengapa ini lebih penting dari kedengarannya

[Thread umpan balik komunitas](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) tentang ini panjang. Perilaku klik-dua-kali-untuk-edit diperkenalkan dengan editor Markdown pada Juli 2025, dan keluhan dimulai hampir seketika.

## Status peluncuran

Ini sudah diluncurkan ke sebagian pelanggan dan akan diperluas ke semua orang dalam dua hingga tiga minggu ke depan.
