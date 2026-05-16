---
title: "A2A v1 Telah Hadir: Komunikasi Antar-Agen Cross-Platform di Microsoft Agent Framework untuk .NET"
date: 2026-05-04
author: "Emiliano Montesdeoca"
description: "Protokol A2A v1.0 telah dirilis dan paket Microsoft Agent Framework untuk .NET telah diperbarui — standar interoperabilitas stabil untuk menghubungkan dan mengekspos agen AI lintas penyedia."
tags:
  - .NET
  - Agent Framework
  - A2A
  - Interoperability
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[A2A v1 Telah Hadir: Komunikasi Antar-Agen Cross-Platform di Microsoft Agent Framework untuk .NET](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) — Protokol A2A baru saja mencapai v1.0, dan paket A2A Agent (klien) dan A2A Hosting (server) untuk .NET telah diperbarui.

## Apa Sebenarnya A2A v1

A2A adalah protokol interoperabilitas terbuka untuk agen AI yang didukung oleh komite pengarah teknis dengan perwakilan dari AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, dan ServiceNow. Label v1 berarti ini sekarang merupakan standar yang stabil dan siap produksi. Paket SDK dan Agent Framework yang mengimplementasikannya masih dalam preview, tetapi protokolnya sendiri sudah terkunci.

v1 meningkatkan v0.3 dengan dukungan multi-tenancy, Agent Cards bertanda tangan untuk identitas kriptografis, alur keamanan yang ditingkatkan, dan arsitektur yang selaras dengan web.

## Menghubungkan ke Agen A2A Jarak Jauh

Agen A2A jarak jauh hanyalah `AIAgent` dalam kode Anda — `RunAsync` yang sama, streaming yang sama, penanganan sesi yang sama:

```csharp
// Penemuan via URI well-known
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));

// Konfigurasi langsung
A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

// Streaming bekerja dengan cara yang sama
await foreach (var update in agent.RunStreamingAsync("Write a short summary..."))
    Console.Write(update.Text);
```

## Mengekspos Agen Anda sebagai Endpoint A2A

Setiap `AIAgent` yang telah Anda buat — di Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, atau AWS Bedrock — dapat diekspos sebagai endpoint A2A dengan dua baris di ASP.NET Core:

```csharp
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) => ...);
builder.AddA2AServer("weather-agent");
```

Kartu agen disajikan secara otomatis di `/.well-known/agent-card.json`.

## Apa Artinya Ini dalam Praktik

Protokol v1 yang stabil berarti Anda dapat menghubungkan agen .NET Anda dengan agen yang dibangun dalam Python, Java, atau bahasa lain tanpa khawatir tentang perubahan yang merusak. Identitas kriptografis dalam Agent Cards yang ditandatangani juga memberikan dasar untuk verifikasi kepercayaan antar agen.

Lihat [posting lengkap](https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/) untuk catatan perubahan lengkap dan catatan migrasi dari v0.3.
