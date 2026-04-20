---
title: "Di Mana Anda Harus Meng-host Agen AI di Azure? Panduan Keputusan Praktis"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure menawarkan enam cara untuk meng-host agen AI — dari kontainer mentah hingga Foundry Hosted Agents yang sepenuhnya dikelola. Inilah cara memilih yang tepat untuk workload .NET Anda."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "azure-ai-agent-hosting-options-guide" >}}).*

Jika Anda sedang membangun agen AI dengan .NET sekarang, Anda mungkin sudah memperhatikan: ada *banyak* cara untuk meng-host-nya di Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents.

Microsoft baru saja menerbitkan [panduan komprehensif untuk hosting agen Azure AI](https://devblogs.microsoft.com/all-things-azure/hostedagent/).

## Enam opsi sekilas

| Opsi | Terbaik untuk | Anda kelola |
|------|-------------|------------|
| **Container Apps** | Kontrol container penuh tanpa kerumitan K8s | Observabilitas, state, siklus hidup |
| **AKS** | Kepatuhan enterprise, multi-cluster | Semuanya |
| **Azure Functions** | Tugas singkat berbasis event | Hampir tidak ada |
| **App Service** | Agen HTTP sederhana | Deployment, scaling |
| **Foundry Agents** | Agen opsional kode | Hampir tidak ada |
| **Foundry Hosted Agents** | Agen framework kustom | Hanya kode agen Anda |

## Foundry Hosted Agents — titik manis untuk developer agen .NET

Deployment benar-benar sederhana:

```bash
azd ext install azure.ai.agents
azd ai agent init
azd up
```

Satu perintah `azd up` membangun container, mendorongnya ke ACR, menyediakan proyek Foundry, dan memulai agen.

## Kerangka keputusan saya

1. **Butuh infrastruktur nol?** → Foundry Agents
2. **Punya kode agen kustom tapi ingin hosting terkelola?** → Foundry Hosted Agents
3. **Tugas singkat berbasis event?** → Azure Functions
4. **Kontrol container maksimum?** → Container Apps
5. **Kepatuhan ketat dan multi-cluster?** → AKS

## Kesimpulan

Untuk sebagian besar developer .NET yang membangun dengan Semantic Kernel atau Microsoft Agent Framework, Hosted Agents kemungkinan adalah titik awal yang tepat. Cek [panduan lengkap dari Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/).
