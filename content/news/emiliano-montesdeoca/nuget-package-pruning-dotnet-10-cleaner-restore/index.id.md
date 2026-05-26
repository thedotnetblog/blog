---
title: "NuGet package pruning di .NET 10 adalah jenis peningkatan yang terasa di mana-mana"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "NuGet package pruning baru di .NET 10 mengurangi false-positive vulnerability reports, menyederhanakan restore graph, dan meningkatkan performa restore. Ini adalah salah satu perubahan platform yang diam-diam membuat pekerjaan harian menjadi lebih baik."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

*Artikel ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Beberapa peningkatan platform menarik karena membuka skenario baru.

Yang lain menarik karena membuat workflow yang sudah ada menjadi lebih sedikit noise, lebih tidak rapuh, dan lebih tidak mengganggu.

**NuGet package pruning di .NET 10** jelas masuk ke kategori kedua, dan saya maksud itu sebagai pujian.

## Mengapa ini penting

Jika Anda pernah berurusan dengan transitive vulnerability noise, restore graph yang terlalu besar, atau package yang secara teknis ada tetapi sebenarnya tidak relevan untuk runtime yang digunakan aplikasi Anda, perubahan ini menyentuh pain point yang nyata.

Pruning membantu dengan menghapus package yang disediakan platform dari effective dependency graph ketika runtime sudah menyediakannya.

Artinya:

- lebih sedikit false-positive vulnerability reports
- transitive dependency graph yang lebih bersih
- overhead restore yang lebih rendah
- hasil audit yang lebih actionable

## Pendapat saya

Inilah jenis peningkatan .NET yang saya sukai.

Ini membuat defaults lebih baik, mengurangi mental overhead, dan meningkatkan kualitas security signal sekaligus perilaku tooling sehari-hari.

Itu kemenangan, bahkan jika tidak pernah muncul di slide keynote.

Posting asli: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
