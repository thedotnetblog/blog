---
title: "NL2SQL adalah SQL Injection di Era Agen"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Sebelum membiarkan agen mengkueri database Anda dengan bahasa alami, baca ini. NL2SQL terlihat sederhana sampai Anda memikirkan kelengkapan skema, non-determinisme, dan apa yang sebenarnya diselesaikan SQL MCP Server."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Ada versi pitch NL2SQL yang terdengar sempurna: pengguna mengajukan pertanyaan dalam bahasa alami, agen menghasilkan SQL, data dikembalikan. Lebih sedikit layar, lebih sedikit kueri, lebih sedikit kode. Sederhana.

Kemudian Anda memikirkannya selama lima menit lagi.

## Masalah yang Tidak Dibicarakan Siapapun di Demo

**Skema tidak dirancang untuk menjelaskan sesuatu.** Nama tabel yang kriptik, nama kolom yang tidak konsisten, hubungan yang valid secara teknis namun tidak valid secara semantik tanpa predikat tambahan — ini umum dalam database enterprise. Ini bukan bug, hanya sejarah perubahan bisnis yang terakumulasi. Tetapi ketika Anda meminta model untuk menyimpulkan niat dari skema yang tidak dirancang untuk menyampaikan niat, model akan mencoba bagaimanapun juga. Ia tidak menyerah. Ia menghasilkan kueri terbaiknya dan mengembalikan hasil dengan percaya diri.

**Model tidak deterministik.** Ajukan pertanyaan yang sama pada database yang sama dua kali dan Anda mungkin mendapatkan SQL yang berbeda. Model menghitung probabilitas, dan variasi kecil dalam konteks menghasilkan output yang berbeda. Anda tidak dapat mencapai jaminan melalui pengujian bahwa agen selalu menghasilkan kueri yang benar.

**Ulasan pengguna tidak skalabel.** "Cukup tinjau setiap kueri sebelum dieksekusi" terdengar aman. Tetapi itu mengasumsikan pengguna adalah ahli dalam model data dan SQL — persis orang-orang yang tidak membutuhkan antarmuka bahasa alami. Ini juga memperkenalkan kelebihan kognitif dan kelas baru bias konfirmasi, di mana pengguna yang kewalahan oleh kompleksitas kueri menyetujui kueri yang tidak valid alih-alih menyelidikinya.

**Dan kemudian ada injeksi.** Dalam pengembangan SQL tradisional, parameterisasi memecahkan injeksi karena input pengguna mengisi parameter, bukan struktur SQL. Dengan NL2SQL, model menghasilkan SQL itu sendiri. Prompt, konteks skema, riwayat percakapan, dan data yang diambil semuanya memengaruhi apa yang dieksekusi. Jika seseorang membuat prompt yang mengubah apa yang dihasilkan model, itu adalah injeksi — bukan pada tingkat parameter, tetapi pada tingkat pembuatan kueri. Dan tidak seperti DROP TABLE (jelas, dapat dipulihkan), injeksi NL2SQL menghasilkan kueri yang mengembalikan hasil yang salah tanpa error yang terlihat. Keputusan bisnis dibuat berdasarkan data yang salah.

## Apa yang Sebenarnya Diselesaikan SQL MCP Server

Di sinilah artikel membuat poin praktis paling bergunanya. Alih-alih memberikan agen akses skema sewenang-wenang dan berharap yang terbaik, SQL MCP Server mengekspos **permukaan API yang dikurasi** yang dibangun di atas [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

Perbedaannya penting: agen tidak menghasilkan SQL. Ia memanggil endpoint bernama yang mengembalikan bentuk hasil yang telah ditentukan sebelumnya. SQL ditulis sekali, oleh developer, dan deterministik. Non-determinisme agen dibatasi untuk memilih *endpoint mana* yang akan dipanggil, bukan membuat kueri sewenang-wenang.

Ini analog dengan apa yang dilakukan parameterisasi untuk injeksi SQL dalam model aplikasi tradisional — menghilangkan kemampuan untuk membuat kueri sewenang-wenang dari input yang tidak dipercaya.

## Pertanyaan yang Benar

Artikel ini tidak mengatakan "jangan pernah gunakan NL2SQL." Ia mengatakan: berhati-hatilah tentang *di mana* Anda menerapkannya dan *apa* yang Anda ekspos. Untuk analisis eksplorasi di lingkungan yang terkontrol, dengan skema terbatas dan akses hanya baca, NL2SQL mungkin baik-baik saja. Untuk sistem produksi di mana keputusan bisnis bergantung pada hasilnya, lapisan API yang dikurasi jauh lebih aman.

Dengan jujur: beberapa masalah benar-benar lebih baik diselesaikan dengan kueri terstruktur di balik endpoint bernama daripada bahasa alami ke SQL. SQL MCP Server memberi Anda opsi tersebut tanpa meninggalkan antarmuka agentik sepenuhnya.

Pos asli: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
