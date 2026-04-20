---
title: "Mode Terisolasi Aspire Memperbaiki Mimpi Buruk Konflik Port dalam Pengembangan Paralel"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 memperkenalkan mode --isolated: port acak, rahasia terpisah, dan nol tabrakan saat menjalankan beberapa instans AppHost yang sama. Sempurna untuk agen AI, worktree, dan alur kerja paralel."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Jika Anda pernah mencoba menjalankan dua instans proyek yang sama secara bersamaan, Anda tahu rasa sakitnya. Port 8080 sudah digunakan.

Aspire 13.2 memperbaiki ini dengan satu flag. James Newton-King [menulis semua detailnya](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/).

## Perbaikan: `--isolated`

```bash
aspire run --isolated
```

Setiap run mendapat:
- **Port acak** — tidak ada tabrakan antar instans
- **User secrets terisolasi** — connection string dan API key tetap terpisah per instans

## Skenario nyata

**Beberapa checkout:**

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Keduanya berjalan tanpa konflik.

**Agen latar belakang di VS Code.** Ketika agen latar belakang Copilot Chat membuat git worktree untuk bekerja secara independen, mode terisolasi memastikan kedua instans berfungsi.

## Kesimpulan

Mode terisolasi adalah fitur kecil yang memecahkan masalah nyata yang semakin umum. Dapatkan 13.2 dengan `aspire update --self`.
