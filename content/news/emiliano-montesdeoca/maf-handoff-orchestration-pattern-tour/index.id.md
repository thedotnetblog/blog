---
title: "Pola Handoff: Ketika Satu Agen Tidak Cukup"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Pola orkestrasi Handoff dalam Microsoft Agent Framework memungkinkan agen menentukan siapa yang menangani giliran berikutnya — tanpa kehilangan konteks percakapan atau melanggar aturan topologi."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

Pada titik tertentu, setiap sistem multi-agen melampaui router sederhana. Tanda pertama biasanya ketika agen spesialis perlu mengajukan pertanyaan lanjutan, atau menyadari di tengah giliran bahwa agen lain harus melanjutkan. Pipeline tetap gagal di sana. Router satu-kali gagal di sana.

Itulah tepatnya masalah yang dirancang untuk diselesaikan oleh pola orkestrasi Handoff di Microsoft Agent Framework.

## Cara Kerja Handoff

Pengembang mendeklarasikan sebuah graf: ini agen-agennya, ini edge-edge di antara mereka. Framework melakukan sisanya — mensintesis tool handoff per edge keluar dan menyuntikkannya ke setiap agen. Ketika agen memutuskan untuk menyerahkan kendali, ia memanggil tool tersebut. Framework menerapkan topologi.

Tiga hal yang membuat ini berbeda dari sekadar membuat agen saling memanggil:

1. **Satu transkrip bersama** — agen penerima melihat riwayat percakapan lengkap. Tanpa memulai dari nol.
2. **Penegakan topologi** — agen hanya dapat handoff ke tujuan yang dideklarasikan. Bug routing terdeteksi saat authoring, bukan di produksi.
3. **Penghentian alami** — ketika agen aktif mengakhiri gilirannya tanpa memanggil tool handoff, workflow menyerahkan kepada pengguna. Tanpa polling, tanpa kondisi keluar eksplisit.

## Contoh Minimal

Di .NET, membangun workflow handoff terlihat seperti ini:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage dapat mengirim ke salah satu spesialis. Kedua spesialis dapat mengirim kembali ke triage. Graf mendukung asiklik tetapi mendukung back-edge saat dibutuhkan ("saya butuh lebih banyak informasi" → kembali ke penelitian).

## Kapan Menggunakan Handoff (dan Kapan Tidak)

Handoff adalah pilihan yang baik ketika:

- **Kepemilikan dapat berubah di tengah percakapan** — agen mungkin menyadari bahwa dirinya adalah spesialis yang salah
- **Back-edge penting** — Anda mungkin perlu mengunjungi kembali langkah sebelumnya tanpa restart
- **Keputusan routing halus** — keputusan untuk handoff bersifat kontekstual dan lebih baik diambil oleh model daripada predikat bertipe

*Bukan* pilihan yang tepat ketika:

- Pipeline Anda tetap dan berurutan — gunakan workflow `Sequential` untuk itu
- Setiap langkah independen — agen berbagi transkrip di mana hanya satu yang membutuhkannya hanyalah kebisingan
- Anda memerlukan jaminan pemrosesan yang ketat — non-determinisme routing berbasis model bukan yang Anda inginkan

## Back-Edge dan Human-in-the-Loop

Salah satu bentuk paling menarik yang diaktifkan Handoff adalah back-edge sejati. Agen dapat memutuskan "saya tidak punya cukup informasi" dan routing kembali ke langkah penelitian — bukan dengan loop hardcoded, tetapi karena model memutuskan itu adalah keputusan yang tepat.

Interaksi human-in-the-loop juga tersusun secara alami. Ketika spesialis memerlukan input pengguna, workflow menyerahkan kembali kepada pengguna melalui loop giliran default, mengumpulkan respons, dan melanjutkan dengan konteks lengkap. Agen tidak pernah kehilangan percakapan.

## Kesimpulan

Handoff adalah salah satu pola yang terlihat sederhana tetapi memungkinkan banyak hal setelah diinternalisasi: routing terdesentralisasi, konteks bersama, topologi yang diterapkan, penghentian alami. Ini adalah langkah selanjutnya yang tepat ketika agen Anda mulai berkata "sebenarnya, orang lain yang harus menangani ini."

Baca panduan lengkap di posting aslinya: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
