---
title: "Azure DevOps Server Patch April 2026 — Perbaikan Penyelesaian PR dan Pembaruan Keamanan"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server mendapatkan Patch 3 dengan perbaikan kegagalan penyelesaian PR, validasi keluar yang ditingkatkan, dan koneksi PAT GitHub Enterprise Server yang dipulihkan."
tags:
  - azure-devops
  - devops
  - patches
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-devops-server-april-2026-patch" >}}).*

Info cepat untuk tim yang menjalankan Azure DevOps Server sendiri: Microsoft merilis [Patch 3 untuk April 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) dengan tiga perbaikan terarah.

## Yang diperbaiki

- **Kegagalan penyelesaian pull request** — pengecualian null reference selama penyelesaian otomatis item kerja dapat menyebabkan penggabungan PR gagal
- **Validasi pengalihan saat keluar** — validasi yang ditingkatkan untuk mencegah pengalihan berbahaya
- **Koneksi PAT GitHub Enterprise Server** — membuat koneksi Personal Access Token dipulihkan

## Cara memperbarui

Unduh [Patch 3](https://aka.ms/devopsserverpatch3) dan jalankan installer. Untuk memverifikasi patch diterapkan:

```bash
<patch-installer>.exe CheckInstall
```

Microsoft sangat merekomendasikan untuk selalu menggunakan patch terbaru demi keamanan dan keandalan.
