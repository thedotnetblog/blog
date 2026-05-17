---
title: "Microsoft Agent Framework Bagian 3: Dari Alat ke Alur Kerja — Blok Bangunan Klik ke Tempatnya"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Bagian 3 dari seri Building Blocks for AI di .NET mencakup Microsoft Agent Framework — dari agen tunggal dengan alat hingga alur kerja multi-agen dengan memori. Inilah yang benar-benar penting."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Postingan ini telah diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Jika kamu mengikuti seri Building Blocks for AI di .NET, kamu tahu: Bagian 1 memberi kita `IChatClient` (antarmuka model universal) dan Bagian 2 memberi kita `Microsoft.Extensions.VectorData` (pencarian semantik dan RAG). Keduanya fundamental dan berguna sendiri-sendiri. Tapi di sinilah semuanya mulai terhubung.

Bagian 3 tentang [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — dan sejujurnya, ini adalah bagian yang saya tunggu-tunggu di .NET. Versi 1.0 rilis April lalu. API-nya stabil. Saatnya benar-benar membangun agen.

## Apa itu Agen (vs. Chatbot)

Sebelum terjun ke kode, mari kita perjelas perbedaan ini. Chatbot menerima input, memanggil model, mengembalikan output. Loop sederhana.

Agen memiliki *otonomi*. Ia dapat bernalar tentang tugas, memutuskan alat mana yang digunakan, memanggilnya, mengevaluasi hasil, dan memutuskan apa yang harus dilakukan selanjutnya — semua tanpa kamu menulis logika langkah demi langkah untuk setiap skenario. Kamu memberinya alat dan instruksi, dan ia mengurus orkestrasi sendiri.

Pikirkan begini: `IChatClient` seperti mengobrol. Agen seperti mendelegasikan daftar tugas kepada seseorang.

## Agen Pertamamu dalam 10 Baris

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

Metode ekstensi `.AsAIAgent()` adalah jembatannya. Pola yang sama seperti `.AsIChatClient()` dari MEAI — membungkus SDK penyedia dalam abstraksi yang stabil. Bekerja dengan Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry, atau model lokal.

Streaming juga berfungsi:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Memberi Alat kepada Agen

Di sinilah agen berhenti menjadi chatbot canggih. Alat adalah fungsi yang dapat diputuskan oleh model untuk dipanggil berdasarkan permintaan pengguna. Tidak perlu logika routing dari sisimu — model yang mencari tahu sendiri.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Dua hal yang perlu diperhatikan. Pertama, `AIFunctionFactory` berasal dari MEAI — tool factory yang sama yang kamu gunakan dengan `IChatClient` biasa. Jika kamu sudah mendefinisikan alat untuk skenario chat, mereka juga berfungsi di sini.

Kedua, atribut `Description` sangat penting. Inilah cara model memahami apa yang dilakukan alat dan kapan menggunakannya. Perlakukan mereka sebagai dokumentasi untuk AI kamu, bukan untuk manusia.

## Sesi: Percakapan yang Benar-benar Ingat

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Tanpa sesi, setiap panggilan `RunAsync` tidak berstateful. Dengan sesi, agen tahu lelucon mana yang kamu maksud. `AgentSession` menyimpan riwayat percakapan di antara giliran.

Untuk layanan tanpa state di produksi, sesi dapat diserialisasikan dengan bersih:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... simpan di suatu tempat ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Ini krusial jika agenmu berjalan di lingkungan serverless atau horizontally-scaled.

## AIContextProvider: Memori Persisten Lintas Sesi

Sesi menyimpan riwayat percakapan *dalam* satu sesi. Tapi bagaimana dengan mengetahui hal-hal tentang pengguna lintas sesi? `AIContextProvider` menangani itu.

Ia memiliki dua hook:
- **`ProvideAIContextAsync`** — berjalan *sebelum* setiap interaksi, menyuntikkan konteks ke agen
- **`StoreAIContextAsync`** — berjalan *setelah* setiap interaksi, memungkinkan pembelajaran dan persistensi

Polanya elegan: kamu dapat menumpuk beberapa provider — satu untuk preferensi pengguna, satu untuk interaksi terbaru, satu yang mengkueri store VectorData kamu untuk dokumen yang relevan. Yang terakhir adalah persis pola RAG dari Bagian 2, kini berjalan otomatis sebagai bagian dari setiap panggilan agen.

## Alur Kerja Multi-Agen

Di sinilah framework mendapatkan namanya. Framework ini menyertakan sistem alur kerja berbasis grafik di mana eksekutor (agen, fungsi, apa saja) terhubung melalui edge.

Beberapa pola yang didukung secara native:

- **Sekuensial**: Output Agen A mengalir ke Agen B
- **Konkuren (fan-out/fan-in)**: Dispatch ke beberapa agen secara paralel, kumpulkan hasilnya
- **Routing kondisional**: Arahkan pekerjaan ke agen berbeda berdasarkan output
- **Loop penulis-kritikus**: Satu agen menulis, yang lain mengevaluasi, loop sampai disetujui
- **Sub-alur kerja**: Menyusun alur kerja secara hierarkis

Contoh penulis-kritikus:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Bersih, mudah dibaca, dan routing berbasis kondisi berarti kamu tidak perlu menulis logika loop sendiri.

## Human-in-the-Loop

Tidak semua hal harus berjalan sepenuhnya otonom. Untuk operasi sensitif — penulisan database, transaksi keuangan, pengiriman komunikasi — kamu ingin manusia menyetujui sebelum agen mengeksekusi.

Framework memiliki dukungan bawaan untuk ini melalui `FunctionApprovalRequestContent` dan `FunctionApprovalResponseContent`. Agen mengusulkan pemanggilan alat, kode aplikasimu mempresentasikannya ke pengguna, dan responnya menentukan apakah eksekusi dilanjutkan.

Inilah cara yang benar untuk berpikir tentang agen dalam pengaturan enterprise: tidak sepenuhnya otonom, tapi *otonomi dengan pembatas*.

## Gambaran Lengkap

Jika kamu mundur sebentar:

- **MEAI** memberimu antarmuka universal ke model manapun
- **VectorData** memberi agenmu akses ke pengetahuan organisasimu melalui pencarian semantik
- **Agent Framework** mengorkestrasikan semuanya — menggunakan `IChatClient` di balik layar, berkomposisi dengan context provider, dan berkoordinasi melalui alur kerja

Setiap bagian dirancang untuk berkomposisi dengan bagian lainnya. Lihat [postingan asli Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) dan [repositori GitHub Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) untuk sampel lengkapnya.

## Kesimpulan

Postingan Bagian 3 Microsoft Agent Framework menutup loop dari seri building blocks. Untuk developer .NET yang ingin membangun agen AI — bukan hanya chatbot, tapi agen nyata yang menggunakan alat, mengingat hal-hal, dan berkoordinasi — inilah jalannya.

Rilis stabil 1.0 berarti kamu bisa membangun ini di produksi. Jika kamu menunggu untuk terjun ke pengembangan agen di .NET, waktunya adalah sekarang.
