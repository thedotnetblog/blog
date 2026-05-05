---
title: "Dari Laptop ke Produksi: Deploy Agen AI ke Microsoft Foundry dengan Dua Perintah"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI kini memiliki perintah 'azd ai agent' yang membawa agen AI Anda dari pengembangan lokal ke endpoint Foundry langsung dalam hitungan menit."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

Anda tahu kesenjangan antara "berfungsi di mesin saya" dan "sudah di-deploy dan melayani traffic"? Untuk agen AI, kesenjangan itu sangat lebar.

Azure Developer CLI baru saja menjadikan ini [urusan dua perintah](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## Alur kerja `azd ai agent` baru

```bash
azd ai agent init
azd up
```

Itu saja. `azd ai agent init` membuat scaffolding infrastruktur-sebagai-kode di repo Anda, dan `azd up` menyediakan semua hal di Azure dan menerbitkan agen Anda.

## Yang terjadi di balik layar

Perintah `init` menghasilkan template Bicep yang nyata dan dapat diperiksa di repo Anda — Foundry Resource, Foundry Project, konfigurasi deployment model, managed identity dengan RBAC.

## Dev inner loop

```bash
azd ai agent run    # jalankan agen secara lokal
azd ai agent invoke # kirim prompt uji
azd ai agent monitor --follow  # stream log real-time
```

## Set perintah lengkap

| Perintah | Yang dilakukan |
|---------|-------------|
| `azd ai agent init` | Scaffold proyek agen Foundry dengan IaC |
| `azd up` | Provisioning sumber daya dan deploy agen |
| `azd ai agent invoke` | Kirim prompt ke agen remote atau lokal |
| `azd ai agent run` | Jalankan agen secara lokal |
| `azd ai agent monitor` | Stream log real-time |
| `azd down` | Bersihkan semua sumber daya Azure |

Lihat [panduan lengkap](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).
