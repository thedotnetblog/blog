---
title: "Docker Sandbox Memungkinkan Agen Copilot Melakukan Refaktor Kode Tanpa Membahayakan Mesin Anda"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox memberi agen GitHub Copilot microVM yang aman untuk melakukan refaktor sesuka hati — tanpa prompt izin, tanpa risiko ke host. Inilah mengapa itu mengubah segalanya untuk modernisasi .NET skala besar."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Jika Anda menggunakan mode agen Copilot untuk sesuatu selain pengeditan kecil, Anda tahu rasa sakitnya. Setiap penulisan file, setiap perintah terminal — prompt izin lainnya.

Tim Azure baru saja menerbitkan postingan tentang [Docker Sandbox untuk agen GitHub Copilot](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/).

## Yang sebenarnya diberikan Docker Sandbox

Ide dasarnya sederhana: jalankan microVM ringan dengan lingkungan Linux penuh, sinkronkan workspace Anda ke dalamnya, dan biarkan agen Copilot beroperasi bebas di dalam.

Ini lebih dari sekadar "jalankan sesuatu dalam container":
- **Sinkronisasi workspace dua arah** yang mempertahankan jalur absolut
- **Docker daemon privat** yang berjalan di dalam microVM
- **Proxy penyaringan HTTP/HTTPS** yang mengontrol akses jaringan
- **Mode YOLO** — agen berjalan tanpa prompt izin

## Mengapa developer .NET harus peduli

Dengan Docker Sandbox, Anda dapat mengarahkan agen Copilot ke proyek, membiarkannya melakukan refaktor dengan bebas di dalam microVM, menjalankan `dotnet build` dan `dotnet test` untuk validasi, dan hanya menerima perubahan yang benar-benar berfungsi.

## Kesimpulan

Docker Sandbox memecahkan ketegangan fundamental dalam agentic coding: agen membutuhkan kebebasan untuk berguna, tetapi kebebasan di mesin host Anda berbahaya. MicroVM memberi Anda keduanya.
