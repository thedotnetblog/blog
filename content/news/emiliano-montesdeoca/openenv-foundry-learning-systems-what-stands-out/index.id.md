---
title: "OpenEnv dan Foundry mendorong percakapan melampaui agen statis"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "Kisah baru OpenEnv dan Foundry jauh lebih dari sekadar jargon reinforcement learning. Ini sebenarnya dorongan ke arah sistem agen yang bisa dievaluasi, dioptimalkan, dan ditingkatkan dari waktu ke waktu berdasarkan hasil bisnis nyata."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *Artikel ini diterjemahkan secara otomatis. Baca versi aslinya [di sini]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

Kebanyakan percakapan tentang agen masih berhenti di inferensi.

Apakah model bisa menjawab prompt? Apakah bisa memanggil tool? Apakah bisa menyelesaikan tugas sekali saja?

Percakapan baru **OpenEnv + Foundry** menarik karena mencoba menggeser pembicaraan ke arah yang lebih ambisius: **bagaimana membangun sistem agen yang benar-benar membaik dari waktu ke waktu?**

Itu pertanyaan yang jauh lebih baik.

## Pergeseran kuncinya adalah dari respons ke loop pembelajaran

Posting Foundry membingkai masalah di sekitar environment, evals, rubrics, optimization, dan post-training.

Semua itu bisa diringkas dalam satu kalimat:

**tujuannya bukan lagi sekadar menjalankan agen, tetapi memiliki loop yang mengukur dan memperbaiki agen terhadap hasil nyata Anda.**

Itulah bagian yang menurut saya perlu diperhatikan developer.

Karena begitu dilihat seperti itu, aset yang tahan lama bukan cuma model atau prompt. Itu adalah sistem di sekitarnya:

- environment tempat ia bertindak
- rubric yang menilainya
- traces yang menjelaskan apa yang terjadi
- optimizer yang memperbaiki konfigurasi

Itu cara berpikir yang jauh lebih siap untuk enterprise.

## Mengapa ini penting meskipun Anda tidak melakukan riset RL

Jujur saja: istilah seperti OpenEnv, post-training, dan world-modeling bisa membuat banyak developer langsung tidak tertarik.

Namun, takeaway praktisnya lebih sederhana daripada terminologinya.

Bahkan jika Anda tidak pernah menyentuh training loop secara langsung, pekerjaan ini membentuk cerita platform untuk pengembangan agen di masa depan:

- evaluasi menjadi first-class
- optimasi menjadi terus-menerus, bukan sesekali
- environment menjadi aset yang bisa dipakai ulang
- perilaku agen yang lebih baik menjadi sesuatu yang terukur, bukan sekadar "terasa lebih bagus di demo"

Itu langkah besar ke depan.

## Pendapat saya

Hal paling cerdas dari pengumuman ini bukan satu detail riset tertentu.

Melainkan framing-nya.

Microsoft jelas mencoba menggeser ekosistem dari prompt engineering statis menuju **sistem agen yang berorientasi hasil**. Sistem yang bisa dievaluasi, disetel, diatur, dan ditingkatkan secara bertahap.

Di situlah nilai platform yang serius berada.

Dan kalau Anda sedang membangun agen hari ini, bahkan di level aplikasi, ada baiknya mengikuti ke mana arah ini bergerak.

Artikel asli: [Sistem pembelajaran berorientasi hasil: RL enterprise dengan OpenEnv dan Foundry](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)