---
title: "Mission Control untuk Agen Coding: Pengalaman Terpadu di VS Code"
description: "VS Code menyatukan agen coding lokal, cloud, CLI, dan pihak ketiga ke dalam Agent Sessions sehingga pengembang dapat melacak, menyela, dan mengoordinasikan pekerjaan otonom."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> **Pemberitahuan:** Artikel ini adalah terjemahan otomatis dari [versi Inggris]({{< ref "index.md" >}}). Untuk konten asli, lihat tautan di atas.

# Mission Control untuk Agen Coding: Pengalaman Terpadu di VS Code

Satu asisten coding mudah dipahami. Beberapa agen yang bekerja di tempat berbeda tidak.

Satu agen berjalan secara lokal di VS Code. Agen lain bekerja pada isu GitHub di cloud. Agen CLI tinggal di terminal. Agen coding pihak ketiga mungkin memiliki model sesi dan batasan berbeda. Tanpa tampilan bersama, pengembang menghabiskan lebih banyak waktu untuk melacak pekerjaan daripada mengawasnya.

Pengalaman agen terpadu VS Code mengatasi masalah koordinasi dengan Agent Sessions: satu tempat untuk meluncurkan agen, melihat status mereka, membuka percakapan mereka, dan campur tangan ketika rencana berubah.

Ini kurang tentang menambahkan agen lain dan lebih tentang membuat beberapa agen dapat dikelola.

## Satu Tampilan untuk Jenis Pekerjaan Berbeda

Artikel sumber menjelaskan empat peserta yang berbeda: GitHub Copilot lokal, Copilot Coding Agent di cloud, GitHub Copilot CLI, dan OpenAI Codex untuk pelanggan Copilot yang memenuhi syarat.

Mereka memiliki kekuatan berbeda:

- Agen lokal dapat memeriksa ruang kerja saat ini dan membuat perubahan cepat.
- Agen coding cloud dapat bekerja secara asinkron pada isu dan membuka permintaan tarik.
- Agen CLI cocok untuk alur kerja berat terminal dan perintah operasional.
- Penyedia lain dapat menawarkan model atau gaya penalaran yang berbeda.

Agent Sessions memberikan tugas-tugas tersebut rumah bersama. Anda dapat melihat apa yang berjalan, apa yang dilakukannya, dan di mana melanjutkan percakapan.

Visibilitas itu penting karena pekerjaan otonom tidak menghilangkan koordinasi. Ini membuat koordinasi menjadi tugas teknik kelas satu.

## Interupsi Adalah Bagian dari Alur Kerja

Sumber membuat observasi sederhana: "Adalah umum untuk mengirim prompt dan menyadari Anda lupa sesuatu yang penting." Sebelumnya, pilihan sering adalah menunggu atau membatalkan. Dengan editor chat, Anda dapat membuka sesi aktif dan menambahkan informasi saat agen bekerja.

Itu lebih dekat dengan kolaborasi nyata. Persyaratan berubah. Tes mengungkap asumsi. Pengulas memperhatikan bahwa API harus tetap kompatibel mundur. Agen yang berguna bukan yang tidak pernah memerlukan koreksi; itu yang dapat menyerap koreksi tanpa kehilangan seluruh tugas.

Untuk pekerjaan .NET, interupsi mungkin sesederhana:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

Instruksi singkat karena repositori sudah membawa konteks yang lebih besar. Sesi adalah tempat untuk memperbaiki arah, bukan untuk menyatakan kembali seluruh sistem.

## Agen Khusus Mengubah Kebiasaan Tim Menjadi Peran

VS Code juga memperkenalkan agen khusus seperti Plan. Alih-alih mengimplementasikan segera, agen perencanaan mengajukan pertanyaan tentang ruang lingkup, komponen, perpustakaan, dan kendala sebelum menghasilkan spesifikasi implementasi.

Pola itu berguna di luar agen bawaan. Tim dapat mendefinisikan peran yang fokus:

- **Penelitian** mengumpulkan bukti dan menulis catatan keputusan singkat.
- **Ulasan** memeriksa perubahan terhadap konvensi repositori.
- **Pengujian** mengidentifikasi kasus yang hilang dan mengusulkan rencana pengujian.
- **Arsitektur** membandingkan opsi tanpa memodifikasi file.

Definisi agen khusus kecil mungkin terlihat seperti ini:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

Bagian yang berguna bukan YAML. Ini adalah pemisahan tanggung jawab eksplisit. Agen perencanaan tidak boleh secara diam-diam mengedit kode produksi. Agen ulasan tidak boleh menulis ulang desain yang seharusnya dievaluasi.

## Subagen Mengurangi Tabrakan Konteks

Percakapan panjang menumpuk konteks yang tidak terkait. Subagen menyediakan ruang kerja terisolasi untuk tugas penelitian yang terbatas, kemudian mengembalikan hasilnya ke sesi utama.

Itu cocok untuk pertanyaan seperti:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

Agen utama tetap fokus pada implementasi sementara agen penelitian menangani pertanyaan yang lebih sempit. Prinsip yang sama berlaku untuk tim: delegasi yang jelas menghasilkan hasil yang lebih baik daripada meluncurkan beberapa agen dengan wewenang yang tumpang tindih.

## Peringatan: Lebih Banyak Agen Berarti Lebih Banyak Koordinasi

Agent Sessions dapat menunjukkan aktivitas, tetapi tidak dapat menyelesaikan kepemilikan yang bertentangan. Dua agen yang mengedit area yang sama masih dapat membuat masalah penggabungan. Agen cloud dan agen lokal dapat membuat asumsi yang tidak kompatibel. Agen khusus dapat menghasilkan rekomendasi yang agen lain abaikan.

Tetapkan batas:

1. Satu agen memiliki implementasi untuk cabang tertentu.
2. Agen penelitian mengembalikan artefak, bukan pengedit yang tidak terlacak.
3. Permintaan tarik tetap menjadi batas ulasan.
4. Nama dan prompt agen menyatakan apa yang dapat mereka ubah.
5. Output sesi disimpan ketika menjelaskan keputusan penting.

## Pendapat Saya

Masa depan multi-agen bukan antrian jendela chat. Ini adalah tim kecil dengan peran, penyerahan, dan akuntabilitas.

Agent Sessions berharga karena mengakui kenyataan itu. Ini memberikan pengembang permukaan kontrol untuk pekerjaan yang sudah terjadi di seluruh editor, terminal, dan cloud. Keuntungan produktivitas berikutnya akan datang lebih sedikit dari memiliki lebih banyak agen dan lebih dari membuat batas mereka jelas.

Untuk tim .NET, saya akan memulai dengan satu agen perencanaan dan satu agen implementasi. Gunakan output perencanaan sebagai spesifikasi isu atau permintaan tarik, kemudian biarkan agen implementasi bekerja dalam batas itu. Ukur pekerjaan ulang sebelum menambahkan peran lebih banyak.

Kontrol misi terbaik masih yang membuat kepemilikan jelas.
