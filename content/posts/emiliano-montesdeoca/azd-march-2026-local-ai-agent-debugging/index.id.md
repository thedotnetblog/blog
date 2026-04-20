---
title: "azd Kini Memungkinkan Anda Menjalankan dan Men-debug Agen AI Secara Lokal — Apa yang Berubah di Maret 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI merilis tujuh rilis di Maret 2026. Highlight: loop jalankan-dan-debug lokal untuk agen AI, integrasi GitHub Copilot dalam pengaturan proyek, dan dukungan Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azd-march-2026-local-ai-agent-debugging" >}}).*

Tujuh rilis dalam satu bulan. Itulah yang didorong oleh tim Azure Developer CLI (`azd`) di Maret 2026, dan fitur unggulan adalah yang sudah saya tunggu: **loop jalankan-dan-debug lokal untuk agen AI**.

## Jalankan dan debug agen AI tanpa deploy

Ini yang besar. Ekstensi `azure.ai.agents` baru menambahkan serangkaian perintah:

- `azd ai agent run` — memulai agen Anda secara lokal
- `azd ai agent invoke` — mengirim pesan ke agen (lokal atau ter-deploy)
- `azd ai agent show` — menampilkan status dan kesehatan container
- `azd ai agent monitor` — streaming log container secara real time

Sebelumnya, menguji agen AI berarti deploy ke Microsoft Foundry setiap kali ada perubahan. Sekarang Anda bisa beriterasi secara lokal.

## GitHub Copilot men-scaffold proyek azd Anda

`azd init` kini menawarkan opsi "Set up with GitHub Copilot (Preview)". Agen Copilot men-scaffold konfigurasi untuk struktur proyek Anda.

## Container App Jobs dan peningkatan deployment

- **Container App Jobs**: `azd` kini men-deploy `Microsoft.App/jobs` melalui konfigurasi `host: containerapp` yang ada
- **Timeout deployment yang dapat dikonfigurasi**: Flag `--timeout` baru pada `azd deploy`
- **Fallback build lokal**: Ketika remote ACR build gagal, `azd` otomatis beralih ke Docker/Podman lokal
- **Validasi preflight lokal**: Parameter Bicep divalidasi secara lokal sebelum deploy

## Kesimpulan

Loop debugging agen AI lokal adalah bintang rilis ini. Cek [catatan rilis lengkap](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/).
