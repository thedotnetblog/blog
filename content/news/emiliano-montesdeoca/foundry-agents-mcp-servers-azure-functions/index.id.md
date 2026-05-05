---
title: "Hubungkan Server MCP Anda di Azure Functions ke Agen Foundry — Begini Caranya"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Bangun server MCP Anda sekali, deploy ke Azure Functions, dan hubungkan ke agen Microsoft Foundry dengan autentikasi yang tepat."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

Ada satu hal yang saya sukai tentang ekosistem MCP: Anda membangun server sekali dan bekerja di mana saja.

Lily Ma dari tim Azure SDK [menerbitkan panduan praktis](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) tentang menghubungkan server MCP yang di-deploy ke Azure Functions dengan agen Microsoft Foundry.

## Mengapa kombinasi ini masuk akal

Azure Functions memberi Anda infrastruktur yang dapat diskalakan, autentikasi bawaan, dan penagihan tanpa server. Microsoft Foundry memberi Anda agen AI yang dapat bernalar dan bertindak. Menghubungkan keduanya berarti alat kustom Anda menjadi kemampuan agen AI perusahaan.

## Opsi autentikasi

| Metode | Kasus Penggunaan |
|--------|----------|
| **Berbasis kunci** | Pengembangan atau server tanpa Entra auth |
| **Microsoft Entra** | Produksi dengan managed identity |
| **OAuth identity passthrough** | Produksi dengan konteks pengguna |
| **Tanpa autentikasi** | Dev/pengujian atau data publik saja |

## Pengaturan

1. **Deploy server MCP ke Azure Functions** — sampel tersedia untuk [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
2. **Aktifkan autentikasi MCP bawaan**
3. **Dapatkan URL endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Tambahkan server MCP sebagai alat di Foundry**

Baca [panduan lengkap](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/).
