---
title: "Azure MCP Server 2.0 Baru Dirilis — Otomasi Cloud Agentic Self-Hosted Sudah Ada"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 mencapai stabilitas dengan deployment remote self-hosted, 276 alat di 57 layanan Azure, dan keamanan tingkat enterprise."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

Jika Anda baru-baru ini membangun sesuatu dengan MCP dan Azure, Anda mungkin sudah tahu bahwa pengalaman lokal bekerja dengan baik. Tapi ketika Anda perlu berbagi pengaturan itu ke seluruh tim? Di situlah hal-hal menjadi rumit.

Tidak lagi. Azure MCP Server [baru saja mencapai 2.0 stabil](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), dan fitur utamanya adalah persis yang telah diminta tim enterprise: **dukungan server MCP remote self-hosted**.

## Apa itu Azure MCP Server?

Azure MCP Server mengimplementasikan spesifikasi [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) dan mengekspos kemampuan Azure sebagai alat terstruktur dan dapat ditemukan. Angkanya berbicara sendiri: **276 alat MCP di 57 layanan Azure**.

## Hal besar: deployment remote self-hosted

Dalam skenario tim nyata, Anda membutuhkan:
- Akses bersama untuk developer dan sistem agen internal
- Konfigurasi terpusat
- Batas jaringan dan kebijakan enterprise
- Integrasi ke pipeline CI/CD

Azure MCP Server 2.0 mengatasi semua ini. Untuk autentikasi, ada dua opsi:
1. **Managed Identity** — saat berjalan bersama [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **Alur On-Behalf-Of (OBO)** — delegasi OpenID Connect dengan izin pengguna yang sebenarnya

## Pengerasan keamanan

Rilis 2.0 menambahkan validasi endpoint yang lebih kuat, perlindungan terhadap pola injection, dan kontrol isolasi yang lebih ketat.

## Memulai

- **[GitHub Repo](https://aka.ms/azmcp)** — kode sumber, dokumentasi
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — deployment dalam container
- **[Ekstensi VS Code](https://aka.ms/azmcp/download/vscode)** — integrasi IDE
- **[Panduan self-hosting](https://aka.ms/azmcp/self-host)** — fitur unggulan 2.0
