---
title: "Alat Azure MCP Kini Tertanam di Visual Studio 2022 — Tanpa Ekstensi"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Alat Azure MCP dikirim sebagai bagian dari workload pengembangan Azure di Visual Studio 2022. Lebih dari 230 alat, 45 layanan Azure, nol ekstensi untuk dipasang."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

Jika Anda menggunakan alat Azure MCP di Visual Studio melalui ekstensi terpisah, Anda tahu prosesnya — instal VSIX, restart, berharap tidak rusak, kelola ketidakcocokan versi. Gesekan itu hilang.

Yun Jung Choi [mengumumkan](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) bahwa alat Azure MCP kini dikirim langsung sebagai bagian dari workload pengembangan Azure di Visual Studio 2022. Tanpa ekstensi. Tanpa VSIX.

## Cara mengaktifkannya

1. Perbarui ke Visual Studio 2022 **17.14.30** atau lebih tinggi
2. Pastikan workload **Azure development** terinstal
3. Buka GitHub Copilot Chat
4. Klik tombol **Pilih alat** (ikon dua kunci pas)
5. Aktifkan **Azure MCP Server**

Tetap aktif di antara sesi.

## Catatan

Alat dinonaktifkan secara default — Anda perlu mengaktifkannya. Bagi developer .NET yang tinggal di Visual Studio, ini mengurangi alasan untuk beralih konteks ke portal Azure.
