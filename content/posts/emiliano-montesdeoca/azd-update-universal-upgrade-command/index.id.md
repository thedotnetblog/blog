---
title: "azd update — Satu Perintah untuk Semua Package Manager Anda"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI kini memiliki perintah pembaruan universal yang bekerja terlepas dari cara Anda menginstalnya — winget, Homebrew, Chocolatey, atau skrip instalasi."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azd-update-universal-upgrade-command" >}}).*

Anda tahu pesan "Versi baru azd tersedia" yang muncul setiap beberapa minggu? Yang Anda abaikan karena tidak ingat apakah Anda menginstal `azd` melalui winget, Homebrew, atau skrip curl enam bulan lalu? Ini akhirnya diperbaiki.

Microsoft baru saja merilis [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — perintah tunggal yang memperbarui Azure Developer CLI ke versi terbaru terlepas dari cara asli Anda menginstalnya.

## Cara kerjanya

```bash
azd update
```

Itu saja. Untuk akses awal ke fitur baru:

```bash
azd update --channel daily
azd update --channel stable
```

Perintah mendeteksi metode instalasi Anda saat ini dan menggunakan mekanisme pembaruan yang sesuai di balik layar.

## Catatan kecil

`azd update` hadir mulai versi 1.23.x. Jika Anda menggunakan versi lebih lama, Anda perlu melakukan satu pembaruan manual terakhir. Setelah itu, `azd update` menangani semuanya.

## Mengapa ini penting

Ini adalah peningkatan kualitas hidup yang kecil, tetapi bagi yang menggunakan `azd` setiap hari untuk men-deploy agen AI dan aplikasi Aspire ke Azure, tetap terkini itu penting.

Baca [pengumuman lengkap](https://devblogs.microsoft.com/azure-sdk/azd-update/).
