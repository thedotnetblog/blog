---
title: "Cosmos DB Shell Kini dalam Pratinjau Publik — Dan Dilengkapi Server MCP Bawaan"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell adalah CLI open source baru yang mengekspos perintah database sebagai alat MCP. Agen AI Anda dapat menavigasi container, menjalankan kueri, dan mengelola data menggunakan antarmuka yang sama yang Anda gunakan."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Jika Anda pernah harus berpindah-pindah antara tab portal, contoh SDK, dan skrip setengah jadi hanya untuk menjawab satu pertanyaan tentang Cosmos DB, Anda sudah mengenal gesekan yang dirancang untuk dihilangkan oleh proyek ini.

Azure Cosmos DB Shell baru saja memasuki pratinjau publik. Ini adalah CLI open source dengan sintaks mirip bash dan — bagian yang membuatnya menarik — server MCP terintegrasi.

## Yang Membuatnya Berbeda dari CLI Database Lainnya

CLI-nya sendiri sudah berguna: perintah yang familiar, dukungan skripting, integrasi CI/CD. Bagian itu adalah standar minimum untuk alat database yang berorientasi pada developer.

Bagian menariknya adalah integrasi server MCP. Setiap perintah yang diekspos CLI menjadi tersedia sebagai alat MCP yang dapat dipanggil oleh agen AI Anda. Tidak ada lapisan API kustom, tidak ada kode integrasi yang perlu ditulis. Agen Anda dapat:

- Menavigasi hierarki database dengan `cd`, `ls`, `pwd`
- Menjalankan kueri SQL dengan `query` dan mendapatkan hasil terstruktur
- Membuat dan memodifikasi item dengan `create item`, `update`, `rm`
- Mengelola database dan container dengan `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Memeriksa konteks saat ini dengan `endpoint`, `pwd`

Perubahan utama: agen Anda tidak berbicara dengan API Cosmos DB — melainkan berbicara dengan antarmuka shell yang sama yang Anda gunakan. Perintah-perintahnya deterministik, dapat diaudit, dan open source sehingga Anda dapat memeriksa tepatnya apa yang sedang terjadi.

## Fondasi Open Source Itu Penting

Ini bukan layanan terkelola kotak hitam. Shell-nya open source, yang berarti:

- Tim keamanan dapat mengaudit implementasinya
- Tim platform dapat mem-fork dan memperluas untuk standar spesifik mereka
- Developer dapat berkontribusi peningkatan yang menguntungkan semua orang

Bagi tim enterprise yang mengadopsi alat AI, "dapatkah kita melihat cara kerjanya secara tepat" semakin tidak lagi menjadi persyaratan opsional. Open source di sini adalah pembeda yang signifikan.

## Tiga Skenario yang Menjadi Lebih Mudah

**Analisis data cerdas** — hubungkan agen ke shell, ajukan pertanyaan dalam bahasa alami, dapatkan hasil kueri terstruktur. Agen menangani pembangunan kueri; shell menangani eksekusi.

**Manajemen data otonom** — alur kerja yang perlu membuat, memperbarui, atau menghapus data di Cosmos DB dapat melakukannya melalui alat MCP tanpa memerlukan integrasi kustom.

**Pemantauan dan peringatan real-time** — agen dapat meminta kueri container secara berkala, membandingkan hasil, dan melaporkan anomali melalui saluran notifikasi yang sesuai.

Antarmuka MCP membuat skenario-skenario ini dapat digabungkan dengan platform AI apa pun yang mendukung MCP — tidak hanya alat Microsoft.

## Memulai

Shell ini dalam pratinjau publik. Instal, konfigurasikan koneksi Cosmos DB Anda, dan aktifkan server MCP. Dari sana, host agen yang kompatibel MCP mana pun dapat menemukan dan menggunakan alat-alatnya.

Postingan asli: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
