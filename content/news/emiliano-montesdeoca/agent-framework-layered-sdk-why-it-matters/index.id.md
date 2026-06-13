---
title: "Mengapa desain berlapis Microsoft Agent Framework benar-benar penting"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Penjelasan baru tentang SDK berlapis Microsoft Agent Framework lebih dari sekadar obrolan arsitektur. Ini menunjukkan bagaimana Microsoft ingin para developer berpindah dari loop sederhana ke orkestrasi siap produksi tanpa membuang semuanya."
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).

Pengumuman framework biasanya dibuka dengan fitur.

Yang satu ini dibuka dengan **filosofi desain**, dan menurut saya itulah tepatnya alasan kenapa ini penting.

Penjelasan baru tentang bagaimana Microsoft Agent Framework disusun di sekitar **agent loops**, **workflows**, dan **harnesses** memberi kita sinyal yang jauh lebih baik daripada daftar fitur biasa. Ini memberi tahu kita bagaimana tim berharap aplikasi nyata akan tumbuh.

Dan bagi siapa pun yang membangun agent di .NET, itulah bagian yang bernilai.

## Kebanyakan aplikasi agent tumbuh melampaui arsitektur pertamanya dengan sangat cepat

Anda mulai dengan panggilan model.

Lalu menambahkan tools.

Lalu memory.

Lalu planner.

Lalu retries, telemetry, approvals, agent khusus, dan sedikit logika workflow, karena satu loop saja tidak lagi cukup.

Di sinilah banyak aplikasi AI menjadi berantakan. Versi pertama berjalan, tetapi setiap kemampuan baru ditempelkan dari level abstraksi yang berbeda.

Yang saya suka dari tulisan Agent Framework adalah ia membuat lapisannya jadi eksplisit:

- **loops** untuk siklus eksekusi inti
- **workflows** untuk orkestrasi terstruktur
- **harnesses** untuk kemampuan runtime yang bisa dipakai ulang di sekitar agent

Awalnya mungkin terdengar akademis, tetapi ini menyelesaikan masalah yang sangat praktis: **Anda bisa mengembangkan aplikasi tanpa harus menulis ulang model mental setiap kali aplikasi menjadi lebih kompleks**.

## Konsep harness sangat penting

Jika saya harus memilih satu bagian yang menurut saya akan semakin penting, itu adalah ide **harness**.

Harness adalah tempat pengembangan agent berubah menjadi engineering, bukan sekadar prompting.

Di lapisan itu, Anda mulai memedulikan:

- tools dan middleware
- perilaku perencanaan
- integrasi memory
- observability
- kontrol dan governance
- perilaku runtime yang dapat diulang

Itu juga alasan desain ini cocok dengan seluruh stack Microsoft. Foundry, tooling governance, hosted agents, evaluasi, dan ekosistem tools semua jadi lebih masuk akal ketika shell runtime di sekitar model diperlakukan sebagai sesuatu yang kelas pertama.

## Ini pertanda baik bagi developer .NET

Satu hal yang selalu saya cari dalam ekosistem seperti ini adalah apakah framework tetap terasa berguna setelah demo pertama.

Pendekatan berlapis ini menunjukkan Microsoft memikirkan seluruh jalur:

1. membangun agent loop sederhana
2. menambah kemampuan terstruktur tanpa kekacauan
3. berpindah ke workflow yang lebih formal saat aplikasi membutuhkannya
4. menjaga runtime tetap cukup composable untuk terintegrasi dengan sistem enterprise

Itu jalur pertumbuhan yang jauh lebih sehat daripada: ini abstraksi monolitik, semoga berhasil.

Dan itu sangat selaras dengan cara developer .NET biasanya suka bekerja: sistem berlapis, komposisi yang eksplisit, batas yang bisa diuji, dan kontrol runtime yang kuat.

## Pandangan saya

Post ini mudah diremehkan karena tidak menampilkan screenshot yang mencolok atau dump API yang besar.

Namun catatan arsitektur seperti ini sering kali menjadi prediktor yang lebih baik untuk melihat apakah sebuah framework akan bertahan enam bulan lagi.

Microsoft Agent Framework jelas berusaha menjadi lebih dari sekadar pembungkus main-main di atas panggilan model. Cerita SDK berlapis ini menunjukkan bahwa tim sedang membangun untuk bagian tengah yang rumit: tempat agent membutuhkan orkestrasi, tools, layanan runtime, dan disiplin produksi.

Itulah tepatnya area yang saya pedulikan.

Postingan asli: [ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
