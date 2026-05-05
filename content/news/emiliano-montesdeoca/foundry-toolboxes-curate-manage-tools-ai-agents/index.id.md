---
title: "Foundry Toolboxes: Satu Endpoint untuk Semua Alat Agen AI"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry meluncurkan Toolboxes dalam preview publik — cara untuk mengelola dan mengekspos alat agen AI melalui satu endpoint yang kompatibel dengan MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Ada masalah yang terlihat sepele sampai benar-benar dihadapi: organisasi membangun beberapa agen AI, masing-masing butuh alat, dan setiap tim mengonfigurasinya dari awal. Integrasi pencarian web yang sama, konfigurasi Azure AI Search yang sama, koneksi server GitHub MCP yang sama — tapi di repositori berbeda, oleh tim berbeda, dengan kredensial berbeda, tanpa tata kelola bersama.

Microsoft Foundry baru saja meluncurkan [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) dalam preview publik, dan ini adalah jawaban langsung atas masalah tersebut.

## Apa itu Toolbox?

Toolbox adalah bundel alat bernama yang dapat digunakan kembali, didefinisikan sekali di Foundry dan diekspos melalui satu endpoint yang kompatibel dengan MCP. Runtime agen apa pun yang berbicara MCP dapat mengonsumsinya — tidak ada lock-in ke Foundry Agents.

Janjinya sederhana: **build once, consume anywhere**. Definisikan alat, konfigurasikan autentikasi secara terpusat (OAuth passthrough, identitas terkelola Entra), terbitkan endpoint. Setiap agen yang membutuhkan alat tersebut terhubung ke endpoint dan mendapatkan semuanya.

## Empat pilar (dua tersedia hari ini)

| Pilar | Status | Apa yang dilakukan |
|-------|--------|-------------------|
| **Discover** | Segera hadir | Temukan alat yang disetujui tanpa pencarian manual |
| **Build** | Tersedia | Kelompokkan alat ke dalam bundel yang dapat digunakan kembali |
| **Consume** | Tersedia | Satu endpoint MCP mengekspos semua alat |
| **Govern** | Segera hadir | Autentikasi terpusat + observabilitas untuk semua panggilan alat |

## Contoh praktis

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Cari dokumentasi dan respons issues GitHub.",
    tools=[
        {"type": "web_search", "description": "Cari dokumentasi publik"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Setelah diterbitkan, Foundry menyediakan endpoint terpadu. Satu koneksi, semua alat.

## Tidak terkunci di Foundry Agents

Toolboxes **dibuat dan dikelola** di Foundry, tapi permukaan konsumsinya adalah protokol MCP yang terbuka. Bisa digunakan dari agen kustom (Microsoft Agent Framework, LangGraph), GitHub Copilot dan IDE lain yang mendukung MCP.

## Mengapa penting sekarang

Gelombang multi-agen sedang tiba di produksi. Setiap agen baru adalah permukaan baru untuk konfigurasi duplikat, kredensial usang, dan perilaku tidak konsisten. Fondasi Build + Consume cukup untuk mulai sentralisasi. Ketika pilar Govern tiba, akan ada lapisan alat yang sepenuhnya dapat diamati dan dikontrol secara terpusat untuk seluruh armada agen.

## Penutup

Ini masih awal — preview publik, Python SDK dulu, Discover dan Govern masih akan datang. Tapi modelnya kokoh dan desain MCP-native berarti bekerja dengan alat yang sudah dibangun. Cek [pengumuman resmi](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) untuk memulai.
