---
title: 'Kemenangan UX Agen Sejati Adalah Otonomi Aman, Bukan Otonomi Maksimal'
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: 'Akses file, persetujuan, dan desain memori adalah tiga serangkai praktis untuk perilaku agen yang dapat dipercaya dalam produksi.'
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Sumber asli: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

Ini adalah salah satu postingan rekayasa agen paling berguna tahun ini karena menolak jebakan umum otonomi demo-first. Sebaliknya, ia berfokus pada bagaimana agen harus beroperasi di sekitar data pengguna nyata dan konsekuensi nyata.

Tiga blok bangunan yang disorot di sini tepat sekali.

Akses file memberikan agen landasan yang berguna dalam data milik pengguna.

Pembatasan persetujuan mencegah eksekusi diam-diam dari tindakan yang memiliki konsekuensi.

Memori yang tahan lama menghindari interaksi berulang tanpa mengorbankan kontrol.

Sebagian besar tim terlalu berinvestasi dalam breadth tool dan kurang berinvestasi dalam semantik izin. Itu terbalik. Agen dengan sepuluh tools dan batas persetujuan yang lemah kurang berharga dibandingkan agen dengan tiga tools dan titik kontrol yang dapat diprediksi.

Pola praktis terbaik dalam artikel ini adalah strategi persetujuan berlapis:

Selalu minta persetujuan untuk tools berdampak tinggi seperti trading atau operasi destruktif.

Otomatis setujui pembacaan berisiko rendah untuk menjaga alur.

Gunakan persetujuan standing terbatas untuk tindakan tepercaya berulang dalam sesi.

Ini menciptakan gradien risiko yang sehat. Pengguna tidak terganggu untuk pembacaan yang tidak berbahaya, tetapi mereka tetap dalam loop ketika konsekuensi menjadi mahal atau tidak dapat diubah.

Saya juga suka pemisahan eksplisit antara file memory dan Foundry memory. Tim harus berhenti mencoba memaksakan satu model memori untuk menyelesaikan setiap masalah. Artifak file eksplisit yang kasar sangat baik untuk state yang terlihat pengguna seperti laporan dan watchlist. Ekstraksi memori tingkat fakta lebih baik untuk preferensi dan konteks percakapan. Mencampur keduanya memberikan hasil yang lebih baik daripada mencoba berpura-pura salah satunya sudah cukup.

Pendapat saya: masa depan kualitas agen akan diukur tidak hanya oleh prompts yang cerdas tetapi lebih oleh ergonomi keamanan. Jika prompt persetujuan Anda berisik, pengguna mengklik secara membabi buta. Jika batas memori Anda tidak jelas, pengguna berhenti mempercayai asisten. Jika default akses data Anda permisif, tim keamanan akan menutup proyek.

Untuk tim .NET dan Python yang mengadopsi pola ini, langkah kuncinya adalah memperlakukan policy callbacks dan aturan persetujuan sebagai logika bisnis inti, dengan versi dan pengujian seperti kode kritis lainnya. Jangan biarkan mereka sebagai lambda ad-hoc yang terkubur dalam sampel.

Sistem agen yang mendapatkan kepercayaan bukanlah yang melakukan paling banyak. Mereka adalah yang melakukan persis apa yang diinginkan pengguna, tidak lebih, tidak kurang, dengan titik interupsi yang jelas ketika risiko meningkat.

Itulah perbedaan antara demo yang mengesankan dan perangkat lunak yang bersedia didelegasikan orang untuk pekerjaan nyata.