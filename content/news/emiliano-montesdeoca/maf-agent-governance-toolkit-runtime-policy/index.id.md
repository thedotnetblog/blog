---
title: "Membangun Agen Adalah Bagian Mudah — Menjalankannya dengan Aman Adalah Bagian Sulit"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework dan Agent Governance Toolkit bekerja sama untuk menerapkan kebijakan runtime, mengatur panggilan alat, dan menyediakan log audit rantai Merkle — tanpa menyentuh prompt agen."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Ada pola dalam pengembangan agen AI yang mulai saya sebut "penyesalan demo". Agen bekerja dengan baik dalam demo. Kemudian seseorang bertanya: apa yang terjadi jika ia memanggil alat yang salah? Bagaimana jika ia mengakses data yang seharusnya tidak? Siapa yang mengaudit itu?

Microsoft Agent Framework mendukung Anda dalam membangun dan mengorkestrasikan. Agent Governance Toolkit (AGT) mencakup bagian setelah itu — tata kelola, penegakan kebijakan, dan kemampuan audit pada runtime.

## Apa yang Sebenarnya Dilakukan Setiap Proyek

**Microsoft Agent Framework (MAF)** memberi Anda model pemrograman: alur kerja multi-agen, interoperabilitas protokol A2A, hook middleware, memori, dan hosting terkelola melalui Foundry Agent Service. Menangani keamanan konten di level input/output model.

**Agent Governance Toolkit (AGT)** terhubung ke pipeline middleware yang sama untuk mengatur *tindakan*. Setiap panggilan alat, akses sumber daya, dan pesan antar-agen dievaluasi terhadap kebijakan sebelum eksekusi. Overhead sub-milidetik. Tanpa sidecar, tanpa proxy, tanpa prompt yang dimodifikasi.

```
Tindakan Agen --> Pemeriksaan Kebijakan --> Izinkan / Tolak --> Log Audit    (< 0.1 ms)
```

Layer berbeda, cakupan lengkap, satu pipeline.

## Terhubung Hanya Menambahkan Middleware

Di Python, AGT menambahkan ke parameter `middleware` yang sama yang Anda gunakan untuk logging atau filter konten:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

Di .NET, pola yang sama melalui `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Agen yang sama, orkestrasi yang sama, alat yang sama. AGT menambahkan kemampuan tata kelola tanpa menyentuh logika agen.

## Apa yang Anda Dapatkan

- **GovernancePolicyMiddleware** — mengevaluasi setiap tindakan terhadap aturan kebijakan deklaratif
- **CapabilityGuardMiddleware** — daftar putih alat yang diizinkan dipanggil oleh agen (alat `approve_small_loan` sengaja tidak ada dalam daftar yang diizinkan di atas)
- **RogueDetectionMiddleware** — mendeteksi pola perilaku anomali pada runtime
- **AuditTrailMiddleware** — log audit rantai Merkle agar setiap tindakan tahan terhadap pemalsuan secara kriptografis

Yang terakhir penting untuk kepatuhan. Rantai Merkle berarti jika seseorang memodifikasi log, rantainya terputus. Audit adalah buktinya.

## Lima Skenario Industri

Repositori AGT dilengkapi lima skenario lengkap end-to-end: layanan keuangan (petugas pinjaman), layanan kesehatan (data pasien), hukum (tinjauan kontrak), pemerintahan (layanan warga), dan manufaktur (kontrol kualitas). Masing-masing memadukan agen MAF nyata dengan middleware tata kelola AGT nyata.

Ini bukan demo mainan. Inilah jenis skenario di mana Anda benar-benar membutuhkan tata kelola dalam produksi.

## Kesimpulan

Jika Anda membangun agen yang menyentuh data nyata, membuat keputusan yang berdampak, atau berjalan tanpa pengawasan di produksi — tata kelola bukanlah opsional. Kombinasi MAF + AGT memberi Anda tumpukan lengkap: bangun dengan Agent Framework, kelola dengan AGT.

Kedua proyek bersumber terbuka. Artikel aslinya memiliki tautan ke sampel kode lengkap.

Posting asli: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
