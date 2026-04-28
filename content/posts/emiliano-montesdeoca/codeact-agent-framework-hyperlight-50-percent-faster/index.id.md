---
title: "CodeAct di Agent Framework: Cara Memotong Latensi Agen Anda Setengahnya"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct menyatukan rantai alat multi-langkah menjadi satu blok kode yang disandbox — memangkas latensi 52% dan penggunaan token 64%."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Posting ini telah diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Ada momen dalam setiap proyek agen di mana Anda melihat trace dan berpikir: "kenapa ini lama sekali?" Model tidak masalah. Alat-alat bekerja. Tapi ada tujuh round trip untuk mendapatkan hasil yang bisa dihitung dalam satu langkah.

Itulah persis masalah yang dipecahkan CodeAct — dan [tim Agent Framework baru saja merilis dukungan alpha](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) melalui paket baru `agent-framework-hyperlight`.

## Apa itu CodeAct?

[Pola CodeAct](https://arxiv.org/abs/2402.01030) secara elegan sederhana: alih-alih memberi model daftar alat untuk dipanggil satu per satu, Anda memberinya satu alat `execute_code` dan membiarkannya mengekspresikan *seluruh rencana* sebagai program Python singkat.

| Pendekatan | Waktu | Token |
|--------|------|--------|
| Tradisional | 27,81d | 6.890 |
| CodeAct | 13,23d | 2.489 |
| **Peningkatan** | **52,4%** | **63,9%** |

## Keamanan: Micro-VM Hyperlight

Paket `agent-framework-hyperlight` menggunakan micro-VM [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Setiap pemanggilan `execute_code` mendapat micro-VM baru yang baru dibuat. Startup diukur dalam milidetik. Isolasi hampir gratis.

Alat Anda tetap berjalan di host. Kode lem yang dihasilkan model berjalan di sandbox. Itulah pembagian yang benar.

## Pengaturan Minimal

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## Kapan Menggunakan CodeAct (dan Kapan Tidak)

**Gunakan CodeAct ketika:**
- Tugas merantai banyak pemanggilan alat kecil (pencarian, penggabungan, perhitungan)
- Latensi dan biaya token penting
- Anda ingin isolasi kuat per pemanggilan untuk kode yang dihasilkan model

**Tetap gunakan tool-calling tradisional ketika:**
- Agen hanya melakukan satu atau dua pemanggilan alat per giliran
- Setiap pemanggilan memiliki efek samping yang perlu disetujui secara individual

## Coba Sekarang

```bash
pip install agent-framework-hyperlight --pre
```

Baca [posting lengkap di blog Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).
