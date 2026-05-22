---
title: "Ekstensi MSSQL untuk VS Code diam-diam menjadi platform yang jauh lebih besar"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Pembaruan terbaru ekstensi MSSQL menambahkan provisioning Azure SQL, desain schema berbantuan Copilot, Data API builder, dan notebook. Bagian yang menarik adalah seberapa banyak pekerjaan database yang sekarang bisa tetap di dalam VS Code.
"
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Artikel ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Ekstensi MSSQL untuk VS Code sudah lama berkembang, tetapi pembaruan terbaru ini membuat arahnya jauh lebih jelas.

Ini bukan lagi sekadar «connect lalu jalankan beberapa query».

Dengan **provisioning Azure SQL**, **Schema Designer dengan Copilot**, **SQL Notebooks**, dan **Data API builder** yang semuanya didorong maju dalam satu rilis, ekstensi ini menjadi workspace yang jauh lebih lengkap untuk pengembangan yang berpusat pada database.

## Daya tarik praktisnya adalah provisioning langsung dari editor

Tulisan sumber mengatakan bahwa Anda sekarang bisa membuat cloud database yang dikelola penuh «langsung dari editor Anda tanpa biaya» menggunakan free tier.

Itu jenis fitur yang terdengar kecil sampai Anda menyadari betapa banyak friction setup yang dihilangkannya.

Bagi banyak developer, bagian yang merepotkan dari eksperimen berat data bukan SQL itu sendiri. Melainkan gap environment antara:

- ide
- database
- schema
- API
- backend yang bisa diuji

Jika gap itu dipersingkat di dalam satu tool, seluruh workflow menjadi lebih menarik.

## Inilah seperti apa inner loop yang lebih kuat untuk pekerjaan data

Yang saya suka dari rilis ini adalah ia menjaga lebih banyak workflow database di satu tempat:

- memprovision database
- mendesain schema
- meninjau perubahan
- menghasilkan script ORM
- mengekspos API
- menguji endpoint
- mendokumentasikan dan melakukan query lewat notebook

Itu adalah cerita yang jauh lebih meyakinkan daripada memperlakukan SQL sebagai tool sampingan yang terpisah di stack.

## Workflow schema berbantuan Copilot adalah tempat nilai AI terasa nyata

Tambahan pada schema designer sangat menarik karena tampaknya berhasil mencapai keseimbangan yang baik.

Nilainya bukan «AI mendesain model data Anda dan Anda mempercayainya begitu saja».

Nilainya adalah:

- titik awal yang lebih cepat
- review visual
- pelacakan perubahan
- output yang berorientasi migrasi
- kontrol accept/undo yang eksplisit

Itu adalah workflow AI yang jauh lebih sehat dibanding auto-generation penuh tanpa jalur inspeksi.

Dan untuk pekerjaan database, kemampuan review sangat penting.

## Data API builder adalah pengganda yang tenang

Fitur lain yang tidak akan saya abaikan adalah integrasi Data API builder.

Jika Anda bisa berpindah dari schema ke:

- REST
- GraphQL
- endpoint MCP

dalam environment yang sama, itu menciptakan jalur yang sangat efisien untuk prototype backend dan tool internal.

Itu tidak menggantikan rekayasa backend yang lebih dalam. Tetapi itu sangat mempersingkat jalan dari ide database ke antarmuka yang bekerja.

## Pandangan saya

Rilis ini membuat ekstensi MSSQL terasa lebih seperti platform kecil di dalam VS Code daripada sekadar add-on sederhana.

Bagi developer yang membangun API, tool data, tool admin, atau prototype berbasis SQL, itu adalah perubahan yang berarti.

Dan jika Microsoft terus mempertajam loop ini, ekstensi ini akan menjadi jauh lebih strategis daripada yang masih diasumsikan banyak orang.

Tulisan asli: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)