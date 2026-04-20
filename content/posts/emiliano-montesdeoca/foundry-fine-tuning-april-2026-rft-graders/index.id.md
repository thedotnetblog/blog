---
title: "RFT Foundry Menjadi Lebih Murah dan Lebih Pintar — Inilah yang Berubah"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry mengirimkan tiga pembaruan RFT bulan ini: pelatihan global untuk o4-mini, penilai model GPT-4.1 baru, dan panduan praktik terbaik."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Jika Anda membangun aplikasi .NET yang mengandalkan model yang disetel halus, pembaruan Foundry bulan ini layak diperhatikan.

Detail lengkap ada di [pengumuman resmi](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/).

## Pelatihan Global untuk o4-mini

o4-mini adalah model yang digunakan untuk beban kerja penalaran berat dan agentik. Anda kini dapat meluncurkan pekerjaan penyetelan halus dari 13+ region Azure dengan tarif pelatihan per-token yang lebih rendah.

```bash
"trainingType": "globalstandard"
```

## Penilai Model Baru: Keluarga GPT-4.1

Tiga opsi baru: GPT-4.1, GPT-4.1-mini, dan GPT-4.1-nano.

Strategi pengelompokan:
- **GPT-4.1-nano** untuk iterasi awal. Biaya rendah, loop umpan balik cepat.
- **GPT-4.1-mini** setelah rubrik penilaian stabil.
- **GPT-4.1** untuk penilaian produksi.

## Jebakan Format Data RFT

Format data RFT berbeda dari SFT. Pesan terakhir di setiap baris harus berperan User atau Developer — bukan Assistant.

## Mengapa ini penting bagi pengembang .NET

Pelatihan yang lebih murah berarti Anda dapat melakukan iterasi lebih agresif. [Panduan praktik terbaik di GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) akan menghemat waktu debugging.
