---
title: "Pembaruan April Visual Studio 2026: Agen Cloud, Agen Kustom, dan Agen Debugger"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "Pembaruan April Visual Studio 2026 (18.5) menghadirkan integrasi agen cloud, agen kustom tingkat pengguna, alat C++ menjadi GA, dan Agen Debugger yang memvalidasi perbaikan terhadap perilaku runtime nyata."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Pembaruan April Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) menghadirkan integrasi agen cloud, agen kustom tingkat pengguna, alat C++ yang mencapai GA, dan Agen Debugger baru.

## Agen cloud: mendelegasikan pekerjaan ke sesi Copilot jarak jauh

Dari pemilih agen di jendela Chat, memilih **Cloud** memungkinkan Anda mendelegasikan tugas ke agen coding Copilot jarak jauh. Anda mendeskripsikan pekerjaan, agen membuat issue GitHub di repositori Anda, lalu membuka PR saat selesai. Anda mendapat notifikasi dengan "View PR" / "Open in browser" — semuanya berjalan sementara Anda terus coding, atau bahkan dengan IDE tertutup.

## Agen kustom kini mengikuti Anda

Agen kustom tingkat pengguna yang tersimpan di `%USERPROFILE%/.github/agents/` tidak lagi terbatas pada repositori — mereka mengikuti Anda lintas proyek. Jalur penyimpanan dapat dikonfigurasi di Tools > Options > GitHub > Copilot > Chat. Tombol `+` di pemilih agen memungkinkan pembuatan agen baru secara langsung. Mereka mendapat kemampuan yang sama seperti agen berbasis repositori: kesadaran ruang kerja, alat, pemilihan model, dan koneksi MCP.

Agen bawaan: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Alat Pengeditan Kode C++ menjadi GA

Dua alat — `get_symbol_call_hierarchy` dan `get_symbol_class_hierarchy` — kini aktif secara default. Mereka memberi Copilot navigasi berbasis bahasa dari basis kode C++, mencakup hierarki warisan dan rantai pemanggilan fungsi. Aktifkan melalui ikon Tools di Copilot Chat. Bekerja paling baik dengan model tool-calling.

## Agen Debugger: perbaikan divalidasi terhadap perilaku runtime nyata

Mulai dari issue GitHub atau Azure DevOps (atau deskripsi bahasa alami), beralih ke mode Debugger, dan agen:

1. Membuat reproducer minimal
2. Menghasilkan hipotesis kegagalan
3. Menginstrumentasi aplikasi dengan tracepoint dan breakpoint bersyarat
4. Menjalankan sesi debug nyata
5. Menganalisis telemetri langsung
6. Menyarankan perbaikan yang tepat

Anda tetap terlibat selama proses — ini interaktif, tidak sepenuhnya otonom.

## Perbaikan prioritas IntelliSense

VS kini menekan penyelesaian Copilot saat daftar IntelliSense aktif. Satu saran pada satu waktu. Ini adalah titik gesekan yang sering terjadi dan kini aktif secara default.

Catatan rilis lengkap dan unduhan di [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
