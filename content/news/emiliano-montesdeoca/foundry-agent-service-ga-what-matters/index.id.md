---
title: "Foundry Agent Service Sudah GA: Yang Benar-benar Penting untuk Pengembang Agen .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Foundry Agent Service Microsoft baru saja mencapai GA dengan jaringan privat, Voice Live, evaluasi produksi, dan runtime multi-model terbuka."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

Mari jujur — membangun prototipe agen AI adalah bagian yang mudah. Bagian sulitnya adalah semua yang datang setelah itu.

[Foundry Agent Service baru saja GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), dan rilis ini sangat fokus pada kesenjangan "semua yang datang setelah itu".

## Dibangun di atas Responses API

Foundry Agent Service generasi berikutnya dibangun di atas OpenAI Responses API. Arsitekturnya sengaja terbuka — Anda tidak terkunci pada satu penyedia model.

## Jaringan privat: hambatan enterprise dihilangkan

- **Tanpa egress publik** — traffic agen tidak pernah menyentuh internet publik
- **Injeksi container/subnet** ke jaringan Anda
- **Konektivitas alat disertakan** — server MCP, Azure AI Search melalui jalur privat

## Autentikasi MCP

| Metode auth | Kapan digunakan |
|-------------|-------------|
| Berbasis kunci | Akses bersama sederhana |
| Identitas Agen Entra | Service-to-service |
| Identitas Terkelola Entra | Isolasi per-proyek |
| Passthrough identitas OAuth | Akses yang didelegasikan pengguna |

## Voice Live

Voice Live menggabungkan STT, LLM, dan TTS menjadi satu API terkelola.

## Evaluasi

1. **Evaluator siap pakai** — koherensi, relevansi, keterpancaran
2. **Evaluator kustom** — logika bisnis Anda sendiri
3. **Evaluasi berkelanjutan** — pengambilan sampel traffic produksi langsung

Lihat [panduan quickstart](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) dan [pengumuman GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
