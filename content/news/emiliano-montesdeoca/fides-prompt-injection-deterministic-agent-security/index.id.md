---
title: "FIDES adalah jenis kisah keamanan agen deterministik yang ingin saya lihat lebih sering"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Kemampuan baru FIDES di Agent Framework penting karena memindahkan pertahanan terhadap prompt injection dari heuristik ke kebijakan yang dapat ditegakkan berdasarkan konten berlabel dan pemeriksaan middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Tulisan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Pertahanan terhadap prompt injection sering terasa seperti berdiri di atas tanah yang rapuh.

Anda menambahkan system prompt yang lebih kuat. Anda menambahkan filter. Anda menaruh beberapa allowlist. Dan Anda berharap input aneh berikutnya tidak merusak asumsi.

Itulah sebabnya **FIDES** menarik.

Bagian terkuat dari kisah ini adalah bahwa ia menggeser keamanan ke sesuatu yang lebih deterministik:

- label pada konten
- propagasi label melalui workflow
- enforcement lewat middleware sebelum alat berprivilege dijalankan
- batas kebijakan yang jelas tentang apa yang boleh dipengaruhi oleh konteks yang tidak tepercaya

## Artikel sumbernya lugas dengan cara yang tepat

Ia dibuka dengan menyebut prompt injection sebagai "**risiko nomor 1 di OWASP LLM Top 10**".

Bagus.

Saya suka gaya blak-blakan seperti ini, karena terlalu banyak tim masih memperlakukan keamanan agen seolah-olah itu masalah masa depan, bukan masalah desain runtime yang ada sekarang.

Dan artikel itu lalu memberi kontras praktis yang kuat: sebagian besar pertahanan saat ini bersifat heuristik, sementara FIDES mencoba mengarahkan sistem ke kebijakan dan enforcement.

Itulah perubahan yang tepat.

## Apa yang membuatnya lebih meyakinkan daripada whitepaper keamanan lain

Banyak tulisan tentang keamanan AI tetap abstrak.

Artikel ini melakukan sesuatu yang lebih baik. Ia berjalan melalui contoh yang sangat konkret: agen triase issue GitHub, isi issue yang berbahaya, pembacaan file berprivilege, dan upaya kebocoran komentar publik.

Itu berguna karena mengikat seluruh diskusi ke workflow nyata.

Dan begitu Anda melihat skenario itu, nilai kontrol deterministik menjadi jauh lebih mudah dipahami.

## Ide utamanya bukan "buat modelnya lebih pintar"

Hal terpenting di sini adalah bahwa FIDES tidak meminta model untuk secara ajaib menjadi lebih baik dalam mendeteksi serangan.

Ia mengubah kontrak runtime.

Artinya:

- konten diberi label
- label menyebar
- alat menyatakan apa yang mereka terima
- middleware memblokir jalur yang tidak aman sebelum eksekusi

Itu pendekatan yang jauh lebih sehat.

Karena begitu agen bisa memanggil alat dengan konsekuensi nyata, keamanan tidak bisa bergantung hanya pada apakah model sedang punya hari yang baik atau tidak.

## Pendapat saya

Inilah jenis arah keamanan agen yang ingin saya lihat lebih sering.

Bukan "percayai model untuk mengabaikan instruksi buruk", melainkan "bangun pagar kebijakan di dalam runtime".

Itu model yang jauh lebih sehat.

Dan jika framework agen ingin dianggap serius dalam produksi, mereka akan membutuhkan lebih banyak kisah seperti ini.

Postingan asli: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)