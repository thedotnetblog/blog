---
title: "Di Mana Agen Anda Mengingat Hal-hal? Panduan Praktis Penyimpanan Riwayat Obrolan"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Dikelola layanan atau klien? Linear atau percabangan? Keputusan arsitektur yang menentukan apa yang benar-benar bisa dilakukan agen AI Anda — dengan contoh kode C# dan Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Saat membangun agen AI, Anda menghabiskan sebagian besar energi pada model, alat, dan prompt. Pertanyaan *di mana riwayat percakapan disimpan* tampak seperti detail implementasi — tetapi itu adalah salah satu keputusan arsitektur terpenting yang akan Anda buat.

Hal ini menentukan apakah pengguna dapat memisahkan percakapan, membatalkan jawaban, melanjutkan sesi setelah restart, dan apakah data Anda pernah meninggalkan infrastruktur Anda. [Tim Agent Framework menerbitkan analisis mendalam](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Dua pola mendasar

**Dikelola layanan**: Layanan AI menyimpan status percakapan. Aplikasi Anda menyimpan referensi dan layanan secara otomatis menyertakan riwayat yang relevan dalam setiap permintaan.

**Dikelola klien**: Aplikasi Anda mempertahankan riwayat lengkap dan mengirim pesan yang relevan dengan setiap permintaan. Layanan tidak memiliki status. Anda mengontrol segalanya.

## Cara Agent Framework mengabstraksi ini

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Nama saya Alice.", session);
var second = await agent.RunAsync("Siapa nama saya?", session);
```

```python
session = agent.create_session()
first = await agent.run("Nama saya Alice.", session=session)
second = await agent.run("Siapa nama saya?", session=session)
```

## Referensi cepat penyedia

| Penyedia | Penyimpanan | Model | Kompaksi |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Klien | N/A | Anda |
| Foundry Agent Service | Layanan | Linear | Layanan |
| Responses API (default) | Layanan | Percabangan | Layanan |
| Anthropic Claude, Ollama | Klien | N/A | Anda |

## Cara memilih

1. **Butuh percabangan atau "batalkan"?** → Responses API dikelola layanan
2. **Butuh kedaulatan data?** → Dikelola klien dengan backend database
3. **Chatbot sederhana?** → Linear dikelola layanan sudah cukup

Baca [posting lengkap](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) untuk pohon keputusan lengkap.
