---
title: "Azure DevOps MCP Server Hadir di Microsoft Foundry: Apa Artinya untuk Agen AI Anda"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server kini tersedia di Microsoft Foundry. Hubungkan agen AI Anda langsung ke alur kerja DevOps — item kerja, repo, pipeline — dengan beberapa klik."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) sedang naik daun. Jika Anda mengikuti ekosistem agen AI, Anda mungkin sudah melihat server MCP bermunculan di mana-mana.

Kini [Azure DevOps MCP Server tersedia di Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), dan ini adalah salah satu integrasi yang membuat Anda berpikir tentang kemungkinan praktisnya.

## Yang sebenarnya terjadi

Microsoft sudah merilis Azure DevOps MCP Server sebagai [pratinjau publik](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview). Yang baru adalah integrasi Foundry. Anda sekarang dapat menambahkan Azure DevOps MCP Server ke agen Foundry Anda langsung dari katalog alat.

## Cara menyiapkannya

Penyiapannya cukup mudah:

1. Di agen Foundry Anda, buka **Tambah Alat** > **Katalog**
2. Cari "Azure DevOps"
3. Pilih Azure DevOps MCP Server (pratinjau) dan klik **Buat**
4. Masukkan nama organisasi Anda dan hubungkan

## Mengontrol apa yang dapat diakses agen Anda

Anda dapat menentukan alat mana yang tersedia untuk agen Anda. Prinsip hak akses minimum, diterapkan ke agen AI Anda.

## Mengapa ini menarik untuk tim .NET

- **Asisten perencanaan sprint** — agen yang dapat menarik item kerja dan menyarankan kapasitas sprint
- **Bot code review** — agen yang memahami konteks PR
- **Respons insiden** — agen yang membuat item kerja dan mengkorelasikan bug
- **Orientasi developer** — jawaban nyata berdasarkan data proyek aktual

## Kesimpulan

Lihat [pengumuman lengkap](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) untuk detail lebih lanjut.
