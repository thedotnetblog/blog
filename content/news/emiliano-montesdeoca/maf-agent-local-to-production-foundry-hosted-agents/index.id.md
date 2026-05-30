---
title: "Agen MAF Lokal Anda Baru Saja Mendapatkan Rumah di Produksi"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents memberikan agen Microsoft Agent Framework Anda identitas, penskalaan, persistensi sesi, dan observabilitas tanpa konfigurasi tambahan. Berikut tampilan praktisnya."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Membuat agen bekerja secara lokal adalah bagian yang menyenangkan. Bagian yang rumit adalah semua yang datang setelahnya: men-deploy-nya tanpa kehilangan akal, mengelola sesi, menyiapkan identitas, menyambungkan observabilitas. Biasanya itu berarti banyak infrastruktur kustom.

Foundry Hosted Agents baru saja menghapus sebagian besar infrastruktur tersebut untuk pengguna Microsoft Agent Framework (MAF).

## Apa yang Sebenarnya Dilakukan Foundry Hosted Agents

Saat Anda men-deploy agen MAF ke Foundry Hosted Agents, platform menangani daftar yang mengejutkan panjangnya dari hal-hal yang seharusnya Anda bangun sendiri:

- **Scale to zero** — agen Anda tidak memerlukan biaya saat idle dan menyala kembali secara otomatis
- **Sandbox terisolasi VM per sesi** — setiap sesi pengguna mendapat sandbox-nya sendiri dengan persistensi filesystem yang bertahan dari peristiwa scale-down
- **Entra ID bawaan** — setiap agen mendapat identitas sendiri untuk memanggil model Foundry, Toolbox, dan layanan Azure tanpa rahasia yang tertanam dalam image
- **Deployment berversi** — setiap deployment adalah snapshot yang tidak dapat diubah, dengan dukungan blue/green dan canary rollout
- **Observabilitas tanpa konfigurasi** — `APPLICATIONINSIGHTS_CONNECTION_STRING` diinjeksi saat runtime sehingga trace OpenTelemetry MAF mengalir otomatis ke App Insights

Yang terakhir ini benar-benar menyenangkan. Tidak ada sambungan tambahan, tidak ada konfigurasi tambahan. Trace langsung muncul.

## Perbedaan Kode Sangat Kecil

Inilah yang paling saya hargai dari integrasi ini. Anda tidak perlu menulis ulang agen Anda. Cukup bungkus saja:

**Dalam .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Dalam Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Itu saja. Logika yang sama yang Anda uji secara lokal adalah yang berjalan di produksi. Platform membungkusnya dengan infrastruktur manajemen sesi, identitas, dan penskalaan.

## Dua Protokol, Satu Agen

Hosted Agents mendukung dua gaya endpoint:

- **Responses** (`/responses`) — kompatibel OpenAI, mengelola riwayat percakapan dan streaming. Default yang baik untuk agen berbentuk chat.
- **Invocations** (`/invocations`) — Anda mendefinisikan skema permintaan/respons. Baik untuk alur kerja non-percakapan.

Jika Anda membangun sesuatu yang terlihat seperti percakapan, mulai dengan Responses. Jika Anda membangun agen berbentuk API yang mengambil input terstruktur dan mengembalikan output terstruktur, Invocations memberi Anda fleksibilitas.

## Alur Deployment dengan `azd`

Saat Anda menjalankan `azd up` dengan agen MAF:

1. Opsional membuat proyek Foundry dan men-deploy model
2. Mengemas kode Anda dan mendorong image ke Azure Container Registry
3. Menyediakan komputasi dari image ACR
4. Menetapkan Entra ID khusus ke agen
5. Mengekspos endpoint stabil (`https://{project_endpoint}/agents/{agent_name}`)
6. Menangani segalanya dari titik itu

Sesi bertahan hingga 30 hari. Komputasi yang idle di-deprovision setelah 15 menit dan dipulihkan secara transparan pada permintaan berikutnya. Dari perspektif agen, tidak ada yang berubah.

## Penutup

Jarak antara "berjalan secara lokal" dan "berjalan di produksi" secara historis telah lama dan menyakitkan untuk agen AI. Foundry Hosted Agents + MAF menutup celah tersebut secara signifikan. Jika Anda sudah memiliki agen lokal yang dibangun dengan Agent Framework, ini layak dicoba hari ini.

Tim mengatakan GA akan segera hadir — ini saat ini dalam preview. Periksa [dokumen integrasi MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) dan [contoh .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) untuk memulai.

Artikel asli: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
