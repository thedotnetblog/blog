---
title: "Azure Functions MCP extension makin praktis di setiap pembaruan"
date: 2026-06-26
author: "Emiliano Montesdeoca"
description: "Pembaruan terbaru Azure Functions MCP extension menambahkan resources, prompts, MCP Apps, opsi autentikasi yang lebih kuat, dan pengalaman builder .NET yang lebih baik. Cerita besarnya adalah bahwa MCP tanpa server di Azure benar-benar makin siap untuk produksi."
tags:
  - Azure Functions
  - MCP
  - .NET
  - Azure
  - Serverless
---

*Artikel ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Azure Functions MCP extension sudah lama melampaui fase «lihat, kamu bisa mengekspos sebuah tool».

Itulah yang ditegaskan oleh pembaruan terbaru ini.

Pada titik ini, ceritanya jauh lebih luas:

- tools
- resources
- prompts
- MCP Apps
- autentikasi bawaan
- API konfigurasi .NET yang lebih baik

Dan itu mengubah cara saya memandang platform ini.

## Extension ini matang dari novelty preview menjadi bahan bangunan yang nyata

Pengumuman MCP awal terutama soal mengaktifkan protokolnya. Berguna, tetapi masih cukup mentah.

Sekarang extension ini berkembang menjadi sesuatu yang lebih lengkap untuk tim yang berpikir production:

- dukungan primitive yang lebih kaya
- dukungan autentikasi yang lebih baik
- konten dan schema yang terstruktur
- konfigurasi .NET yang lebih natural dengan builder
- jalur yang lebih jelas menuju integrasi Foundry

Itulah yang ingin Anda lihat.

## Mengapa Azure Functions sangat cocok untuk MCP

Saya masih berpikir Azure Functions adalah salah satu opsi hosting paling praktis untuk remote MCP servers.

Anda mendapatkan:

- hosting tanpa server
- eksekusi yang dapat diskalakan
- pola trigger dan binding yang familier
- integrasi identitas bawaan
- keselarasan yang baik dengan permukaan tool bergaya API

Dan dengan extension MCP, jarak antara «saya punya fungsi yang berguna» dan «saya punya permukaan tool yang bisa ditemukan oleh agent» terus mengecil.

## Cerita fluent builder di .NET sangat menarik

Tambahan .NET menarik perhatian saya karena mereka melanjutkan tren menuju konfigurasi yang lebih ekspresif di dalam kode.

Mendeklarasikan metadata, schema, UI bindings, dan perilaku MCP yang lebih kaya secara fluent membuat extension ini terasa lebih seperti tool developer kelas satu, bukan sekadar pembungkus protokol yang tipis.

Itulah arah yang saya inginkan.

## Pandangan saya

Ceritanya bukan satu fitur tunggal. Cerita sebenarnya adalah bahwa Azure Functions MCP extension sedang menjadi pilihan platform yang realistis bagi tim yang ingin meng-host kemampuan MCP di Azure tanpa membangun semuanya dari nol.

Dan khususnya untuk developer .NET, pengalamannya terus membaik.

Tulisan asli: [Azure Functions MCP Extension: What’s New at Build 2026](https://devblogs.microsoft.com/azure-sdk/functions-mcp-updates-build-2026/)