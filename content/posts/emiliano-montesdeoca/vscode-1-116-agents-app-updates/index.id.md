---
title: "VS Code 1.116 — Aplikasi Agen Mendapatkan Navigasi Keyboard dan Penyelesaian Konteks File"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 berfokus pada polesan aplikasi Agen — keybinding khusus, peningkatan aksesibilitas, penyelesaian konteks file, dan resolusi tautan CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "vscode-1-116-agents-app-updates" >}}).*

VS Code 1.116 adalah rilis April 2026, dan meskipun lebih ringan dari beberapa pembaruan terbaru, perubahannya fokus dan bermakna — terutama jika kamu menggunakan aplikasi Agen setiap hari.

Inilah yang mendarat, berdasarkan [catatan rilis resmi](https://code.visualstudio.com/updates/v1_116).

## Peningkatan aplikasi Agen

Aplikasi Agen terus matang dengan polesan kegunaan yang membuat perbedaan nyata dalam alur kerja sehari-hari:

**Keybinding khusus** — kamu sekarang bisa memfokuskan tampilan Changes, pohon file dalam Changes, dan tampilan Chat Customizations dengan perintah dan pintasan keyboard khusus.

**Dialog bantuan aksesibilitas** — menekan `Alt+F1` di kotak input chat sekarang membuka dialog bantuan aksesibilitas yang menampilkan perintah dan keybinding yang tersedia.

**Penyelesaian konteks file** — ketik `#` di chat aplikasi Agen untuk memicu penyelesaian konteks file yang dicakup ke workspace saat ini.

## Resolusi tautan CSS `@import`

Sesuatu yang bagus untuk developer frontend: VS Code sekarang menyelesaikan referensi CSS `@import` yang menggunakan jalur node_modules. Kamu bisa `Ctrl+klik` melalui import seperti `@import "some-module/style.css"` saat menggunakan bundler.

## Kesimpulan

VS Code 1.116 tentang penyempurnaan — membuat aplikasi Agen lebih mudah dinavigasi, lebih mudah diakses, dan lebih ramah keyboard. Lihat [catatan rilis lengkapnya](https://code.visualstudio.com/updates/v1_116) untuk daftar lengkap.
