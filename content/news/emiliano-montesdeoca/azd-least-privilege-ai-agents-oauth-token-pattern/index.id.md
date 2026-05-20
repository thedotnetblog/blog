---
title: "Agen AI Anda Punya Masalah Identitas (Dan Ini Template yang Mengatasinya)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Template azd baru dari Curity dan Microsoft menunjukkan cara membangun agen AI yang menggunakan token OAuth berumur pendek dengan scope yang granular — sehingga agen tidak pernah bisa melihat data yang tidak seharusnya mereka lihat."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Ada momen dalam setiap proyek agen AI yang berjalan kurang lebih seperti ini: demo berjalan sempurna, agen menginterpretasikan bahasa alami, memanggil API yang tepat, mengembalikan data yang tepat. Kemudian Anda mulai memikirkan pengguna nyata.

Apa yang mencegah sesi agen satu pengguna dari melihat data pengguna lain? Bagaimana jika agen ditipu melalui injeksi prompt? Bagaimana jika agen memanggil sebuah tool dengan cara yang tidak terduga?

Ini bukan edge case. Ini adalah keputusan desain yang perlu Anda buat sebelum rilis.

Template `azd` baru dari Curity dan Microsoft memberi Anda referensi yang bekerja persis untuk masalah ini.

## Masalah Inti: Autentikasi ≠ Otorisasi

Sebagian besar sampel agen menangani autentikasi pengguna dengan baik. Mereka menangani otorisasi dengan buruk. Mengetahui *siapa* pengguna tidak memberi tahu Anda *data apa* yang seharusnya mereka lihat.

Aplikasi klien tradisional melakukan panggilan API yang dapat diprediksi. Agen AI bersifat non-deterministik — ia menginterpretasikan bahasa alami dan memutuskan apa yang akan dipanggil. Ia bisa kreatif. Ia juga bisa salah. Dan jika dimanipulasi melalui injeksi prompt, Anda memerlukan aturan yang tidak bergantung pada AI yang berperilaku baik.

Solusi yang didemonstrasikan template ini: **token berumur pendek yang membawa informasi yang tepat untuk setiap hop**.

## Cara Kerja Rantai Token

Template menggunakan token akses OAuth 2.0 dengan pertukaran token untuk mempersempit izin di setiap langkah. Token pengguna dipertukarkan dua kali sebelum mencapai server MCP:

1. **Pertukaran pertama** — mempersempit scope dan mengonversi token buram menjadi JWT
2. **Pertukaran kedua** — menambahkan identitas agen dan audiens baru untuk hop server MCP

Tampilan token server MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

`customer_id` disematkan dalam token oleh server otorisasi, bukan diteruskan sebagai parameter yang dikendalikan agen. API memeriksa token, bukan instruksi agen.

Artinya: bahkan jika seseorang menipu agen untuk mencoba mengambil data pelanggan lain, token tidak akan mengotorisasinya.

## Apa yang Dideploy Template

Dengan beberapa perintah `azd` Anda mendapatkan:

- Agen backend di Microsoft Foundry (C#, Microsoft A2A dan MCP SDK)
- Server MCP yang mengekspos API portofolio sampel
- Curity Identity Server sebagai server otorisasi, bersama Entra ID untuk autentikasi
- Gateway API eksternal dan internal yang menangani pertukaran token dan logging audit
- Bicep untuk semua infrastruktur Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, storage

Seluruh pola dapat diinspeksi dan dikustomisasi.

## Prinsip Desain yang Layak Dipinjam

Bahkan jika Anda tidak menggunakan Curity, polanya dapat ditransfer: **agen seharusnya tidak pernah memiliki akses API permanen**. Setiap tindakan harus menggunakan token berumur pendek dengan scope minimum yang diperlukan untuk panggilan spesifik tersebut, diterbitkan untuk identitas agen spesifik, membawa klaim yang dibutuhkan API untuk membuat keputusan otorisasi.

Ini tahan terhadap agen yang kreatif, kesalahan, dan injeksi prompt dengan cara yang "pastikan saja agen tidak melakukan hal buruk" tidak akan pernah bisa.

## Kesimpulan

Pola keamanan untuk agen AI masih sedang dirumuskan di seluruh industri. Template ini adalah salah satu implementasi referensi paling lengkap yang pernah saya lihat — ini mencakup alur otorisasi yang sebenarnya, bukan hanya autentikasi.

Postingan asli: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
