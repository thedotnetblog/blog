---
title: "Microsoft Foundry April 2026: Foundry Local GA, GPT-5.5, CodeAct dengan Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Rekap Foundry bulan April kaya konten: Foundry Local mencapai GA, GPT-5.5 hadir, Agent Framework mendapat pelacakan OpenTelemetry, CodeAct menjalankan Python di mikro-VM Hyperlight, dan Agent Monitoring Dashboard hadir."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Bulan yang sibuk untuk Microsoft Foundry. Berikut pengumuman-pengumuman terpenting.

## Foundry Local Tersedia Secara Umum

Foundry Local — runtime AI lokal lintas platform Microsoft — telah beralih dari pratinjau ke GA di Windows, macOS (Apple Silicon), dan Linux x64. Inferensi model lokal yang siap produksi dengan SDK ramah pengembang. Versi 1.1 menambahkan dukungan transkripsi, embeddings, dan Responses API.

## GPT-5.5

Model terbaru dalam keluarga GPT-5 kini tersedia di Foundry. Kuota default untuk langganan Tier 5 dan Tier 6. Jika Anda telah bekerja dengan varian GPT-5 sebelumnya, ini layak dievaluasi terhadap kasus penggunaan Anda.

## Pelacakan Agent Framework di Foundry

Dua fitur pelacakan hadir dalam pratinjau bulan ini:

**Pelacakan Microsoft Agent Framework** — Agen MAF kini dapat mengekspor jejak OpenTelemetry ke Foundry. Debug perilaku agen, lacak eksekusi multi-langkah, tampilkan latensi dan kesalahan di seluruh pemanggilan alat. Ini mengisi kesenjangan nyata: mengetahui *apa yang sebenarnya dilakukan agen di produksi*, bukan hanya apa yang dikembalikannya.

**Pelacakan Agen yang Di-host** — Sesi, pemanggilan alat, dan langkah jalankan agen yang di-host juga muncul di jejak Foundry. Cerita observabilitas yang sama diperluas ke tingkat yang di-host.

## CodeAct dengan Hyperlight (Alpha)

Ini adalah tambahan yang paling menarik secara teknis: Agent Framework kini dapat mengeksekusi kode Python di dalam mesin virtual mikro [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct adalah pola di mana agen menghasilkan dan mengeksekusi kode Python sebagai alat. Kekhawatiran yang jelas adalah keamanan — Anda menjalankan kode yang dihasilkan model. Mikro-VM Hyperlight menyediakan isolasi tingkat proses dengan waktu startup mendekati native, membuat eksekusi kode sandbox praktis tanpa overhead penuh dari kontainer atau VM.

Untuk alur kerja agen yang memerlukan eksekusi kode, ini adalah peningkatan keamanan yang signifikan dibandingkan menjalankan kode di proses host.

## Dashboard Pemantauan Agen (Pratinjau)

Dashboard operasional terpadu yang menggabungkan penggunaan token, latensi, tingkat keberhasilan jalankan, dan skor evaluator dalam satu tampilan. Perbedaan dari dashboard observabilitas biasa: ini menyertakan hasil evaluasi di samping metrik operasional, sehingga Anda dapat mengkorelasikan "agen menjadi lebih lambat" dengan "skor evaluator turun" — atau mengonfirmasi bahwa keduanya tidak terkait.

## Evaluator Kustom Evaluasi Berkelanjutan (Pratinjau)

Anda kini dapat membawa evaluator berbasis kode atau berbasis prompt Anda sendiri ke dalam pipeline evaluasi berkelanjutan. Sebelumnya, evaluasi berkelanjutan terbatas pada evaluator bawaan. Evaluator kustom memungkinkan Anda menerapkan standar kualitas spesifik tim dalam loop pemantauan produksi.

## Inventori Agen di Control Plane

Tampilan Operate pada control plane Foundry kini menampilkan semua agen yang didukung di seluruh langganan Anda: agen Foundry, Azure SRE Agent, loop agen Logic Apps, dan agen kustom yang terdaftar. Satu tampilan untuk memahami apa yang di-deploy di mana.

Posting asli: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
