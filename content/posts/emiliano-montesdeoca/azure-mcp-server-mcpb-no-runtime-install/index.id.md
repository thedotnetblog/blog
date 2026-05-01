---
title: "Azure MCP Server Kini .mcpb — Instal Tanpa Runtime Apapun"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server kini tersedia sebagai MCP Bundle (.mcpb) — unduh, seret ke Claude Desktop, selesai. Tidak perlu Node.js, Python, atau .NET."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Tahu apa yang menjengkelkan dari pengaturan server MCP? Anda memerlukan runtime. Node.js untuk versi npm, Python untuk pip/uvx, .NET SDK untuk varian dotnet.

[Azure MCP Server baru saja mengubah itu](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Kini tersedia sebagai `.mcpb` — MCP Bundle — dan pengaturannya adalah seret-dan-lepas.

## Apa itu MCP Bundle?

Bayangkan seperti ekstensi VS Code (`.vsix`) atau ekstensi browser (`.crx`), tetapi untuk server MCP. File `.mcpb` adalah arsip ZIP mandiri yang menyertakan biner server dan semua dependensinya.

## Cara Menginstal

**1. Unduh bundle untuk platform Anda**

Buka [halaman GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) dan unduh file `.mcpb` untuk OS dan arsitektur Anda.

**2. Instal di Claude Desktop**

Cara termudah: seret dan lepas file `.mcpb` ke jendela Claude Desktop saat Anda berada di halaman pengaturan Extensions (`☰ → File → Settings → Extensions`). Tinjau detail server, klik Install, konfirmasi.

**3. Autentikasi ke Azure**

```bash
az login
```

Selesai. Azure MCP Server menggunakan kredensial Azure Anda yang ada.

## Untuk Memulai

- **Unduhan**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repo**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Baca [posting lengkap](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
