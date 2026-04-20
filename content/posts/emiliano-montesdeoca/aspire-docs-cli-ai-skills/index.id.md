---
title: "Aspire 13.2 Memiliki CLI Dokumentasi — dan Agen AI Anda Bisa Menggunakannya Juga"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 menambahkan aspire docs — CLI untuk mencari, menelusuri, dan membaca dokumentasi resmi tanpa meninggalkan terminal. Juga berfungsi sebagai alat untuk agen AI."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-docs-cli-ai-skills" >}}).*

Anda tahu momen ketika Anda sedang dalam Aspire AppHost, menghubungkan integrasi, dan perlu memeriksa parameter apa yang diharapkan integrasi Redis? Anda alt-tab ke browser, berburu di aspire.dev. Konteks hilang.

Aspire 13.2 baru saja [mengirimkan perbaikan untuk itu](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). CLI `aspire docs` memungkinkan Anda mencari, menelusuri, dan membaca dokumentasi Aspire resmi langsung dari terminal.

## Tiga perintah, nol tab browser

```bash
# Daftar semua dokumen
aspire docs list

# Cari topik
aspire docs search "redis"

# Baca halaman penuh
aspire docs get redis-integration

# Hanya satu bagian
aspire docs get redis-integration --section "Add Redis resource"
```

## Sudut agen AI

Perintah `aspire docs` yang sama berfungsi sebagai alat untuk agen AI. Alih-alih mengarang API Aspire berdasarkan data pelatihan lama, agen bisa memanggil `aspire docs search "postgres"`, menemukan dokumen integrasi resmi, dan membaca halaman yang tepat.

## Kesimpulan

`aspire docs` adalah fitur kecil yang memecahkan masalah nyata dengan bersih. Lihat [deep dive David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/).
