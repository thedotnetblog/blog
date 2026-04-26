---
title: "68 Menit Sehari Mengulang Penjelasan Kode ke Copilot? Ada Solusinya"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot itu nyata — agent AI Anda mulai melenceng setelah 30 turn, dan Anda membayar compaction tax setiap jam. auto-memory memberi GitHub Copilot CLI recall yang presisi tanpa membakar ribuan token."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Anda tahu momen ketika sesi Copilot Anda kena `/compact` dan agent benar-benar lupa apa yang sedang Anda kerjakan? Lima menit berikutnya Anda menjelaskan ulang struktur folder, test yang gagal, dan tiga pendekatan yang sudah dicoba. Lalu itu terjadi lagi. Dan lagi.

Desi Villanueva mencatatnya: **68 menit per hari** — hanya untuk re-orientasi. Bukan menulis kode. Bukan review PR. Hanya mengingatkan AI tentang hal-hal yang sebenarnya sudah ia ketahui.

Ternyata ada alasan konkret mengapa ini terjadi, dan ada solusi konkret juga.

## Kebohongan Jendela Konteks

Agent Anda datang dengan angka besar di kotak. 200K token. Kedengarannya masif. Dalam praktiknya, itu adalah batas atas, bukan jaminan.

Ini matematika yang sebenarnya:

- 200K context total
- Dikurangi sekitar 65K untuk tool MCP yang dimuat saat startup (~33%)
- Dikurangi sekitar 10K untuk file instruksi seperti `AGENTS.md` atau `copilot-instructions.md`

Itu menyisakan kira-kira **125K sebelum Anda mengetik satu kata pun**. Dan makin buruk — LLM tidak menurun secara mulus saat context penuh. Mereka membentur tembok di sekitar 60% kapasitas. Model mulai kehilangan hal-hal yang disebut 30 turn sebelumnya, membantah jawaban sebelumnya, dan menghalusinasi nama file yang tadi ia sebut dengan sangat percaya diri 10 menit lalu. Industri menyebut ini masalah "lost in the middle".

Batas efektif: **45K token** sebelum kualitas turun. Itu mungkin hanya 20-30 turn percakapan aktif sebelum agent mulai melenceng. Itulah kenapa Anda kena `/compact` setiap 45 menit — bukan karena Anda sudah mengisi 200K token, tapi karena model sudah mulai rusak di 120K.

## Pajak Kompaksi

Setiap `/compact` mengambil state alur kerja Anda. Anda sedang berada di sesi debugging yang dalam. Context bersama sudah terbentuk selama 30 menit. Agent tahu struktur file, test yang gagal, dan hipotesisnya. Lalu peringatannya muncul.

- Abaikan → agent makin bodoh perlahan, mulai menghalusinasi state lama
- Jalankan `/compact` → agent hanya mendapat ringkasan dua paragraf dari investigasi 30 menit

Apa pun pilihannya, Anda kalah. Apa pun pilihannya, Anda menjelaskan proyek Anda seperti orang baru pada hari pertama.

Bagian kejamnya? **Memori itu sebenarnya sudah ada**. Copilot CLI menulis setiap sesi ke database SQLite lokal di `~/.copilot/session-store.db` — setiap file yang disentuh, setiap turn, setiap checkpoint. Semuanya ada di disk. Agent cuma tidak bisa membacanya.

## auto-memory: lapisan recall, bukan sistem memori

Itulah ide utama di balik [auto-memory](https://github.com/dezgit2025/auto-memory): jangan bangun sistem memori baru — bangun lapisan query read-only di atas yang sudah ada.

```bash
pip install auto-memory
```

Sekitar 1.900 baris Python. Tanpa dependensi. Terpasang dalam 30 detik.

Alih-alih membanjiri context dengan hasil grep, Anda memberi agent akses bedah ke hal yang benar-benar penting:

| Operasi | Token | Apa yang Anda dapat |
|---------|-------|---------------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 hasil, sebagian besar tidak relevan |
| `find . -name "*.py"` | ~2,000 | Semua file Python, tanpa konteks |
| Re-orientasi agent | ~2,000 | Anda menjelaskan apa yang seharusnya sudah ia tahu |
| **`auto-memory files --json --limit 10`** | **~50** | **10 file yang Anda sentuh kemarin** |

Itu peningkatan 200x. Agent melewati penggalian arkeologi dan langsung menuju hal yang penting.

Alur yang direkomendasikan: saat Anda mendekati penggunaan 50-70% context, jalankan `/clear` lalu prompt dengan: "review last sessions we discussed topic X". Alih-alih membakar 12K token untuk pencarian buta, auto-memory mengambil konteks yang relevan hanya dalam 50 token.

## Kenapa Ini Penting untuk Developer .NET

Jika Anda memakai GitHub Copilot CLI untuk pekerjaan .NET — scaffolding service, debugging query EF Core, iterasi pada komponen Blazor — masalah context rot menghantam sama kerasnya. Solusi kompleks dengan banyak proyek, library bersama, dan call chain yang dalam adalah jenis codebase yang paling cepat membuat agent kehilangan arah.

Panduan instalasi menjelaskan cara mengarahkan Copilot CLI ke sana. Itu setup satu kali.

Sejujurnya? Mengembalikan 68 menit per hari bukan sekadar tweak kecil untuk kualitas hidup. Itu hampir 6 jam per minggu.

## Penutup

Context rot adalah batasan arsitektural yang nyata, bukan bug yang akan dipatch. auto-memory mengatasinya dengan memberi agent mekanisme recall yang murah dan presisi, bukan re-exploration yang mahal dan berisik. Kalau Anda melakukan pengembangan serius berbantuan AI dengan GitHub Copilot CLI, instalasi 30 detiknya layak dilakukan.

Lihat: [auto-memory di GitHub](https://github.com/dezgit2025/auto-memory). Post asli oleh Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).