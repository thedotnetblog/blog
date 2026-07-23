---
title: "Agent Governance Toolkit MCP Extensions Membuat Jalur Aman Jauh Lebih Mudah di .NET"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Agent Governance Toolkit MCP extensions untuk .NET menempatkan penegakan kebijakan, pemindaian startup, dan sanitasi respons langsung ke dalam alur builder MCP server. Itulah cerita secure-by-default yang ingin saya lihat."
tags:
  - .NET
  - MCP
  - AI
  - Security
  - Agent Governance Toolkit
---

Salah satu masalah terbesar dalam alat agen saat ini adalah bahwa happy path biasanya adalah jalur yang tidak aman.

Anda dapat membuat MCP server dengan cepat. Anda dapat mengekspos tools dengan cepat. Anda dapat membuat demo berfungsi.

Kemudian pertanyaan tidak nyaman tiba segera setelah itu:

- siapa yang diizinkan memanggil apa?
- apa yang terjadi jika metadata tool bersifat berbahaya atau menyesatkan?
- bagaimana jika output tidak aman mengalir kembali ke model?
- seberapa banyak ini kebijakan, dan seberapa banyak hanya konvensi?

Itulah mengapa **Agent Governance Toolkit MCP extensions untuk .NET** itu penting.

Extensions ini tidak menyelesaikan setiap masalah keamanan di ekosistem agen, tetapi melakukan sesuatu yang sangat penting: mereka membuat alur builder .NET default jauh lebih mudah untuk diperkuat.

## Kalimat paling penting dalam pengumuman tersebut

Postingan sumber mengatakan paket ini menambahkan "**one-call governance**" ke `IMcpServerBuilder`.

Itulah frasa yang akan saya fokuskan.

Karena sebagian besar tim tidak gagal membangun tata kelola agen karena kurangnya kesadaran. Mereka gagal karena jalur aman membutuhkan lebih banyak pekerjaan, lebih banyak wiring, lebih banyak kode kustom, dan lebih banyak kesempatan untuk menunda pembersihan sampai nanti.

Dan "nanti" adalah tempat risiko suka tinggal.

## Mengapa ini adalah cerita .NET yang baik

Yang saya suka di sini adalah betapa alaminya paket ini cocok dengan model builder yang ada.

Alih-alih memaksa tim ke:

- sidecar
- proxy terpisah
- arsitektur wrapper kustom
- atau SDK alternatif yang aneh

paket ini memperluas alur builder MCP C# resmi secara langsung.

Itu sangat penting.

Jika keamanan membutuhkan akrobat arsitektural, adopsi turun seketika. Jika keamanan terlihat seperti bagian normal dari konfigurasi server, adopsi menjadi jauh lebih realistis.

## Model ancaman tidak lagi teoretis

Satu hal yang saya rasa tim tidak boleh remehkan adalah seberapa cepat risiko terkait MCP menjadi nyata dalam sistem produksi.

Artikel sumber menyoroti pertanyaan seperti:

- "**Haruskah setiap tool yang terdaftar bisa dipanggil oleh setiap agen?**"
- "**Apa yang terjadi jika deskripsi tool menyertakan instruksi bergaya prompt injection?**"

Itu adalah pertanyaan yang tepat.

Karena begitu tools menjadi permukaan eksekusi untuk agen, sistem tidak lagi hanya menghasilkan teks. Sistem membuat keputusan yang dapat memiliki konsekuensi keamanan, keandalan, dan tata kelola.

Itu mengubah standar.

## Apa yang dilakukan paket ini dengan benar

Keputusan desain terkuat dari ekstensi ini adalah menggabungkan beberapa lapisan keamanan ke dalam satu alur yang koheren:

- pemindaian startup untuk definisi tool yang tidak aman
- penegakan kebijakan saat eksekusi
- tata kelola yang sadar identitas
- sanitasi respons sebelum konten mengalir kembali ke klien atau model
- hook audit dan metrik

Itu adalah bentuk yang tepat.

Bukan satu mode "keamanan" raksasa. Satu set kontrol spesifik yang mencakup titik kegagalan yang berbeda dalam siklus hidup.

### Pemindaian startup lebih penting dari yang disadari banyak tim

Saya terutama suka bahwa metadata tool yang tidak aman dapat menggagalkan startup secara default.

Itu adalah opini yang kuat, dan saya pikir itu adalah opini yang benar.

Semakin awal Anda dapat memblokir definisi tool yang berbahaya atau mencurigakan, semakin baik. Menunggu sampai runtime sudah terlambat untuk seluruh kelas masalah.

### Sanitasi respons juga merupakan lapisan yang sangat praktis

Poin lain yang kurang dihargai dalam pengumuman ini adalah fokus pada sanitasi output.

Banyak tim memikirkan input berbahaya.

Lebih sedikit yang berpikir cukup hati-hati tentang output berbahaya yang kembali dari tool dan langsung diberikan ke loop agen.

Itu adalah tempat yang mudah untuk terbakar.

## Apa yang masih akan saya awasi dengan hati-hati

Meskipun saya sangat menyukai paket ini, saya masih akan berhati-hati tentang satu hal: alat tata kelola hanya berfungsi jika tim benar-benar mendefinisikan dan memelihara kebijakan yang berarti.

Ekstensi memudahkan untuk menghubungkan mekanisme. Itu bagus.

Tetapi tim masih perlu melakukan pekerjaan organisasi yang lebih sulit untuk memutuskan:

- tools mana yang diizinkan
- agen atau identitas mana yang dapat memanggilnya
- apa arti "deny by default" sebenarnya di lingkungan mereka
- bagaimana false positive dan pengecualian ditangani

Jadi saya akan memperlakukan paket ini sebagai lapisan penegakan yang kuat, bukan pengganti penilaian arsitektural.

## Pendapat saya

Ini adalah salah satu pengumuman agen **secure-by-default** .NET paling jelas yang pernah saya lihat.

Bukan karena menjanjikan sihir, tetapi karena mengambil kategori pekerjaan keamanan yang cenderung diimplementasikan tim secara tidak konsisten dan memberinya rumah yang lebih bersih dan alami di builder pipeline.

Itulah jenis paket yang saya inginkan di ekosistem ini.

Ini tidak mengakhiri percakapan tata kelola yang lebih luas. Ini melakukan sesuatu yang lebih praktis: membuatnya jauh lebih sulit untuk berpura-pura bahwa tata kelola adalah tugas pembersihan orang lain nanti.

Dan itu adalah kemajuan nyata.

Postingan asli: [Announcing Agent Governance Toolkit MCP Extensions for .NET](https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/)