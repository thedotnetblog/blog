---
title: "Respons Latar Belakang di Microsoft Agent Framework: Tidak Ada Lagi Kecemasan Timeout"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework kini memungkinkan Anda membongkar tugas AI yang berjalan lama dengan token kelanjutan. Begini cara respons latar belakang bekerja dan mengapa itu penting untuk agen .NET Anda."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

Jika Anda pernah membangun sesuatu dengan model penalaran seperti o3 atau GPT-5.2, Anda tahu rasa sakitnya. Agen Anda mulai memproses tugas yang kompleks, klien menunggu, dan di suatu titik koneksi habis waktu.

Microsoft Agent Framework baru saja merilis [respons latar belakang](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — dan sejujurnya, ini adalah salah satu fitur yang seharusnya ada sejak hari pertama.

## Cara token kelanjutan bekerja

Alih-alih memblokir, Anda memulai tugas agen dan mendapatkan kembali **token kelanjutan**. Anggap seperti klaim tiket di bengkel reparasi:

1. Kirim permintaan Anda dengan `AllowBackgroundResponses = true`
2. Jika agen mendukung pemrosesan latar belakang, Anda mendapat token kelanjutan
3. Poll sesuai jadwal Anda hingga token kembali `null`

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

## Kapan sebenarnya menggunakan ini

- **Tugas penalaran kompleks** — analisis multi-langkah, penelitian mendalam
- **Pembuatan konten panjang** — laporan terperinci, dokumen multi-bagian
- **Jaringan tidak dapat diandalkan** — klien mobile, deployment edge
- **Pola UX asinkron** — kirim tugas, lakukan hal lain, kembali untuk hasil

Lihat [dokumentasi lengkap](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/).
