---
title: "Membangun Aplikasi Konferensi Bertenaga AI dengan Composable Stack .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft membangun ConferencePulse — aplikasi Blazor konferensi langsung — dengan menggabungkan Microsoft.Extensions.AI, DataIngestion, VectorData, MCP, dan Agent Framework. Begini cara bagian-bagiannya terhubung."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Membangun Aplikasi Konferensi Bertenaga AI dengan Composable Stack .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft membangun ConferencePulse, sebuah aplikasi Blazor Server untuk sesi konferensi langsung, dengan menggabungkan lima pustaka ekstensi .NET. Digunakan di MVP Summit.

## Apa yang dilakukan ConferencePulse

ConferencePulse berjalan selama sesi langsung dan menyediakan: polling yang dihasilkan AI dari konten sesi, Q&A audiens dengan pipeline RAG yang mengambil dari basis pengetahuan langsung, wawasan yang dihasilkan otomatis, dan ringkasan sesi yang dihasilkan oleh beberapa agen AI secara bersamaan. Stacknya adalah .NET 10, Blazor Server, Aspire, dibagi menjadi lima proyek: Web, Core, Ingestion, Agents, Mcp, dan AppHost.

## Microsoft.Extensions.AI: satu abstraksi untuk segalanya

`IChatClient` adalah abstraksi terpadu — dikonfigurasi sekali dan antarmuka yang sama berfungsi untuk Azure OpenAI, OpenAI, Anthropic, atau penyedia lainnya. Enam baris untuk mendapatkan klien yang dikonfigurasi penuh dengan pemanggilan fungsi, pelacakan OpenTelemetry, dan middleware logging:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

`IChatClient` yang sama digunakan kembali nanti untuk langkah pengayaan ingesti data — tidak perlu klien terpisah untuk itu.

## Pipeline DataIngestion

Konten sesi mengalir melalui pipeline: `MarkdownReader` → `HeaderChunker` (500 token, 50 token tumpang tindih) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Pengaya menggunakan `IChatClient` yang sama untuk menghasilkan ringkasan dan mengekstrak kata kunci sebelum pengindeksan. Pertanyaan audiens, pasangan Q&A, dan hasil polling dimasukkan secara real-time saat sesi berlangsung — basis pengetahuan bertumbuh selama presentasi.

## VectorData: pencarian agnostik penyedia

`VectorStoreCollection.SearchAsync()` bekerja sama baik backing store-nya Qdrant maupun Azure AI Search. Pencarian hibrida (vektor + teks penuh) didukung. Pipeline RAG untuk Q&A audiens mengkueri koleksi ini dan mendapatkan kembali potongan yang relevan untuk diteruskan sebagai konteks ke klien chat.

## MCP: konten sesi sebagai alat

Konten sesi diekspos melalui MCP sehingga klien yang kompatibel dengan MCP dapat mengaksesnya. Baik server maupun klien diimplementasikan — server mengekspos pengetahuan sesi sebagai alat MCP, dan klien memungkinkan pemanggilan alat tersebut dari dalam pipeline agen.

## Agent Framework: ringkasan multi-agen paralel

Ringkasan sesi dihasilkan oleh tiga agen yang berjalan secara bersamaan — `PollSummaryAgent`, `QuestionSummaryAgent`, dan `InsightSummaryAgent` — kemudian digabungkan. Ini menggunakan pola group chat atau eksekusi paralel dari Microsoft Agent Framework. Setiap agen menangani satu aspek; orkestrator menggabungkan outputnya.

## Prinsip desain

Posting ini membuat poin yang layak diingat: gunakan alat paling sederhana yang sesuai. Panggilan `IChatClient` langsung untuk tugas generasi sederhana. Pemanggilan alat/fungsi untuk ekstraksi data terstruktur. Agen penuh hanya ketika Anda membutuhkan penalaran multi-langkah yang otonom. Pelapisan pustaka memaksakan ini — Anda dapat mengambil `Microsoft.Extensions.AI` tanpa menarik Agent Framework penuh.

Lihat [posting lengkap](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) untuk struktur proyek lengkap dan tautan sumber.
