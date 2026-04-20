---
title: "VS Code 1.117: Agen Mendapatkan Cabang Git Sendiri dan Saya Sangat Setuju"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 menghadirkan isolasi worktree untuk sesi agen, mode Autopilot yang persisten, dan dukungan subagen. Alur kerja coding agentik semakin nyata."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

Garis antara "asisten AI" dan "rekan tim AI" terus menipis. VS Code 1.117 baru saja mendarat dan [catatan rilis lengkap](https://code.visualstudio.com/updates/v1_117) penuh, tapi ceritanya jelas: agen menjadi warga kelas satu dalam alur kerjamu.

Inilah yang sebenarnya penting.

## Mode Autopilot akhirnya mengingat preferensimu

Sebelumnya, kamu harus mengaktifkan kembali Autopilot setiap kali memulai sesi baru. Menjengkelkan. Sekarang mode izinmu persisten antar sesi, dan kamu bisa mengonfigurasi defaultnya.

Agent Host mendukung tiga konfigurasi sesi:

- **Default** — alat meminta konfirmasi sebelum berjalan
- **Bypass** — menyetujui segalanya secara otomatis
- **Autopilot** — sepenuhnya otonom, menjawab pertanyaannya sendiri dan terus berjalan

Jika kamu membuat scaffold proyek .NET baru dengan migrasi, Docker, dan CI — atur ke Autopilot sekali dan lupakan. Preferensi itu bertahan.

## Isolasi Worktree dan git untuk sesi agen

Ini yang besar. Sesi agen sekarang mendukung isolasi worktree dan git penuh. Artinya ketika agen mengerjakan tugas, ia mendapatkan cabang dan direktori kerja sendiri. Cabang utamamu tetap tidak tersentuh.

Bahkan lebih baik — Copilot CLI menghasilkan nama cabang yang bermakna untuk sesi worktree ini. Tidak ada lagi `agent-session-abc123`. Kamu mendapatkan sesuatu yang benar-benar mendeskripsikan apa yang dilakukan agen.

Untuk developer .NET yang menjalankan beberapa cabang fitur atau memperbaiki bug sementara tugas scaffolding panjang berjalan, ini adalah perubahan besar.

## Subagen dan tim agen

Agent Host Protocol sekarang mendukung subagen. Agen bisa menjalankan agen lain untuk menangani bagian dari sebuah tugas. Agen utama berkoordinasi, dan agen khusus menangani bagian-bagiannya.

## Output terminal otomatis disertakan saat agen mengirim input

Kecil tapi bermakna. Ketika agen mengirim input ke terminal, output terminal sekarang secara otomatis disertakan dalam konteks. Jika kamu pernah melihat agen menjalankan `dotnet build`, gagal, dan kemudian membutuhkan giliran ekstra hanya untuk melihat kesalahan — gesekan itu hilang.

## Aplikasi Agen yang memperbarui dirinya sendiri di macOS

Aplikasi Agen mandiri di macOS sekarang memperbarui dirinya sendiri. Tidak perlu lagi mengunduh versi baru secara manual.

## Kesimpulan

VS Code 1.117 adalah infrastruktur. Isolasi worktree, izin persisten, protokol subagen — ini adalah blok bangunan untuk alur kerja di mana agen menangani tugas nyata dan paralel tanpa mengganggu kodemu. Jika kamu membangun dengan .NET dan belum menyelami alur kerja agentik, sejujurnya, sekarang adalah waktu yang tepat untuk mulai.
