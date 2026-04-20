---
title: "Dashboard Aspire 13.2 Kini Memiliki Telemetry API — dan Ini Mengubah Segalanya"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 hadir dengan ekspor telemetri yang lebih cerdas, API yang dapat diprogram untuk trace dan log, dan peningkatan visualisasi GenAI. Inilah mengapa ini penting untuk alur kerja debugging Anda."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

Jika Anda membangun aplikasi terdistribusi dengan .NET Aspire, Anda sudah tahu bahwa dashboard adalah bagian terbaik dari seluruh pengalaman. Aspire 13.2 membuatnya jauh lebih baik.

## Mengekspor telemetri dengan cara yang masuk akal

Aspire 13.2 menambahkan dialog **Kelola log dan telemetri** yang tepat di mana Anda dapat:
- Menghapus semua telemetri
- Mengekspor telemetri yang dipilih ke file ZIP dalam format OTLP/JSON standar
- Mengimpor ulang ZIP tersebut ke dashboard Aspire mana pun nanti

Bagian terakhir adalah fitur unggulan. Reproduksi bug, ekspor telemetri, lampirkan ke item kerja, dan rekan tim Anda dapat mengimpornya ke dashboard mereka sendiri.

## Telemetry API adalah pengubah permainan sesungguhnya

Dashboard kini mengekspos HTTP API di bawah `/api/telemetry`:
- `GET /api/telemetry/resources` — daftar sumber daya dengan telemetri
- `GET /api/telemetry/spans` — kueri span dengan filter
- `GET /api/telemetry/logs` — kueri log dengan filter
- `GET /api/telemetry/traces` — daftar trace

Ini mendukung perintah CLI `aspire agent mcp` dan `aspire otel` yang baru.

## Telemetri GenAI menjadi praktis

VS Code Copilot chat dan Copilot CLI mendukung konfigurasi `OTEL_EXPORTER_OTLP_ENDPOINT` — arahkan ke dashboard Aspire dan Anda bisa melihat agen AI Anda berpikir secara real-time melalui telemetri.

## Kesimpulan

Aspire 13.2 mengubah dashboard dari "UI debugging yang bagus" menjadi "platform observabilitas yang dapat diprogram". Kunjungi [aspire.dev](https://aspire.dev).
