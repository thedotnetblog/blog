---
title: "Foundry Local 1.1: Transkripsi Real-Time, Embeddings, dan Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 menambahkan transkripsi langsung dari mikrofon, embeddings teks, dan dukungan Responses API — semuanya berjalan secara lokal tanpa ketergantungan cloud, tanpa latensi jaringan, tanpa biaya per token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 telah membuktikan konsepnya: menjalankan model AI secara lokal di Windows, macOS (Apple Silicon), dan Linux x64 dengan SDK yang ramah pengembang. Versi 1.1 menambahkan tiga kemampuan yang mencakup banyak kasus penggunaan produksi nyata.

## Transkripsi Audio Langsung

Fitur baru paling signifikan: streaming konversi ucapan ke teks secara real-time langsung dari mikrofon. Keterangan, antarmuka suara, transkripsi rapat, alat aksesibilitas — semuanya berjalan secara lokal tanpa ketergantungan cloud sama sekali.

API berbasis sesi dan melakukan streaming hasil saat tiba, dengan penanda `is_final` untuk membedakan teks sementara dari teks final. Tersedia di semua binding bahasa: JavaScript, C#, Python, dan Rust.

Muat model ucapan streaming dari katalog, buat sesi dengan pengaturan audio (laju sampel, saluran, bahasa), mulai sesi, dorong potongan audio PCM mentah, dan konsumsi aliran hasil asinkron. Artikel ini memiliki contoh lengkap Python dan C#.

## Embeddings Teks

Pencarian semantik, pipeline RAG, pengelompokan, pencocokan kemiripan — semua ini memerlukan embeddings. Foundry Local 1.1 menambahkan dukungan model embedding sehingga Anda dapat menghasilkan vektor secara lokal dari SDK yang sama, tanpa mengirim data ke endpoint cloud.

Untuk aplikasi yang mengutamakan residensi data atau yang memproses konten sensitif, pembuatan embedding lokal adalah kemampuan yang bermakna.

## Responses API

Foundry Local kini mendukung [Responses API](https://platform.openai.com/docs/api-reference/responses) — antarmuka terstruktur yang dirancang untuk interaksi agentik. Ini menambahkan:

- **Pemanggilan alat** — izinkan model yang berjalan secara lokal untuk memanggil alat yang Anda definisikan
- **Input multimodal vision-bahasa** — teruskan gambar + teks ke model berkemampuan vision
- Kompatibel dengan bentuk API standar, sehingga agen yang ada yang menargetkan Responses API OpenAI bekerja terhadap model lokal

## Peningkatan Ukuran Paket

Dua perubahan mengurangi ukuran paket JavaScript:
- Lapisan FFI `koffi` telah diganti dengan addon C Node-API khusus
- Penyedia eksekusi WebGPU dikirimkan sebagai plugin terpisah, sehingga aplikasi yang tidak memerlukan akselerasi GPU tidak menanggung biaya ukuran

C# SDK kini menargetkan versi framework yang lebih rendah untuk kompatibilitas .NET yang lebih luas.

## Mengapa Ini Penting

Ketiga kemampuan tersebut — transkripsi, embeddings, pemanggilan alat — mencakup blok bangunan inti dari banyak aplikasi AI. Menjalankannya secara lokal berarti:
- Tidak memerlukan internet
- Tidak ada biaya per token
- Tidak ada data yang meninggalkan mesin
- Latensi konsisten terlepas dari kondisi jaringan

Foundry Local adalah pilihan tepat untuk skenario edge, beban kerja yang sensitif terhadap privasi, aplikasi offline, atau apa pun yang ingin Anda hindari ketergantungan cloud selama pengembangan.

Posting asli: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
