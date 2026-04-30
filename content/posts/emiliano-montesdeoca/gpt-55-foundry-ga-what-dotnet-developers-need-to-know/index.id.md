---
title: "GPT-5.5 Hadir di Azure Foundry — Yang Perlu Diketahui Developer .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 tersedia umum di Microsoft Foundry. Evolusi dari GPT-5 ke 5.5, apa yang benar-benar meningkat dan cara mulai menggunakannya di agent Anda hari ini."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Microsoft baru saja mengumumkan bahwa [GPT-5.5 tersedia umum di Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Jika Anda membangun agent di Azure, inilah pembaruan yang Anda tunggu.

## Evolusi GPT-5

- **GPT-5**: menyatukan penalaran dan kecepatan dalam satu sistem
- **GPT-5.4**: penalaran multi-langkah yang lebih kuat, kemampuan agentik awal untuk enterprise
- **GPT-5.5**: penalaran konteks panjang yang lebih dalam, eksekusi agentik yang lebih andal, efisiensi token yang lebih baik

## Yang Benar-benar Berubah

**Pengkodean agentik yang ditingkatkan**: GPT-5.5 mempertahankan konteks di seluruh basis kode besar, mendiagnosis kegagalan tingkat arsitektur, dan mengantisipasi persyaratan pengujian. Model bernalar tentang *apa lagi* yang dipengaruhi perbaikan sebelum bertindak.

**Efisiensi token**: Output berkualitas lebih tinggi dengan lebih sedikit token dan lebih sedikit percobaan ulang. Biaya dan latensi langsung lebih rendah untuk deployment produksi.

## Harga

| Model | Input ($/M token) | Input Cache | Output ($/M token) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Mengapa Foundry Penting

Foundry Agent Service memungkinkan Anda mendefinisikan agent dalam YAML atau menghubungkannya dengan Microsoft Agent Framework, GitHub Copilot SDK, LangGraph, atau OpenAI Agents SDK — dan menjalankannya sebagai agent yang di-host secara terisolasi dengan sistem file persisten, identitas Microsoft Entra tersendiri, dan harga scale-to-zero.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Anda adalah asisten yang membantu.", name: "AgentSaya");
```

Lihat [pengumuman lengkap](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) untuk semua detail.
