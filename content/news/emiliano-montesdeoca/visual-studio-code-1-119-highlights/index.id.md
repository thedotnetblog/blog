---
title: "VS Code 1.119: OpenTelemetry untuk Sesi Agen, Integrasi Browser, dan Keamanan"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (Mei 2026) menambahkan pelacakan OpenTelemetry untuk sesi agen, berbagi tab browser, peningkatan kepercayaan dan keamanan, serta patch keamanan 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) dirilis 6 Mei 2026 (dengan patch keamanan 1.119.1 segera setelahnya). Rilis ini berfokus pada observabilitas agen, interaksi browser, dan pengurangan gangguan.

## Pelacakan OpenTelemetry untuk sesi agen

Ini adalah fitur unggulan bagi siapa pun yang menjalankan agen dalam produksi atau men-debug alur kerja agentik. Aktifkan dengan dua pengaturan:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Jejak mengikuti konvensi semantik GenAI. Setiap permintaan agen menghasilkan span root `invoke_agent` dengan span anak bersarang: `chat`, `execute_tool`, dan `execute_hook`. Penggunaan token dilaporkan per permintaan — termasuk hitungan pembacaan cache dan pembuatan cache.

Bekerja dengan agen lokal, agen latar belakang Copilot CLI, dan agen Claude. Backend yang kompatibel OTLP menerima jejak — [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) bekerja baik untuk pengembangan lokal.

## Agen kini dapat mengakses tab browser

Agen dapat meminta akses ke tab browser terintegrasi Anda — tetapi tidak otomatis. Anda harus secara eksplisit berbagi tab melalui pemilih konteks, seret dan lepas, atau konteks yang disarankan. Ada tombol berbagi di browser untuk mencabut akses. Ketika agen mencoba membuka tab baru pada domain yang sama dengan tab yang sudah terbuka (tidak dibagikan), VS Code meminta Anda untuk menggunakan kembali tab yang ada.

## Penggunaan token yang dioptimalkan

Model ringan eksperimental kini menangani manajemen daftar tugas agen, menjaga pekerjaan administrasi ini dari model utama yang lebih mahal. Mengurangi penggunaan token pada tugas yang tidak memerlukan kapasitas penalaran penuh.

## Kepercayaan dan keamanan

Lebih sedikit gangguan: VS Code 1.119 mengurangi perintah untuk permintaan akses jaringan dan penulisan folder temp oleh agen. Patch 1.119.1 mengatasi masalah keamanan tertentu — layak diperbarui jika belum dilakukan.

## Pergantian cepat ke pratinjau Markdown

Kecil tapi berguna: Anda kini dapat dengan cepat beralih editor saat ini ke pratinjau Markdown tanpa navigasi.

## VS Code Agents (pratinjau Insiders)

UI sesi agen yang didesain ulang — pemilih repositori baru (lokal/repo/jarak jauh), peningkatan sub-sesi, polesan web dan mobile, animasi kemajuan — tersedia di Insiders di [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Changelog lengkap: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
