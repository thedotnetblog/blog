---
title: "Agent Skills di Visual Studio: Ajarkan Copilot Cara Kerja Tim Anda yang Sebenarnya"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio kini mendukung Agent Skills — set instruksi yang dapat digunakan ulang yang mengajarkan Copilot alur kerja, standar pengkodean, dan konvensi spesifik tim Anda. Definisikan sekali, terapkan secara otomatis."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Salah satu frustrasi yang terus-menerus dengan asisten pengkodean AI: mereka mengenal pemrograman umum dengan baik tetapi tidak mengenal konvensi spesifik *tim* Anda, API internal Anda, atau pola yang Anda sukai. Setiap sesi, Anda menjelaskan konteks kembali. Agent Skills di Visual Studio dirancang untuk mengatasi hal ini.

## Apa itu Agent Skills

Set instruksi yang dapat digunakan ulang — didefinisikan dalam file `SKILL.md` — yang mengajarkan agen Copilot cara menangani tugas-tugas tertentu. Definisikan skill untuk "cara menjalankan pipeline build kami", "cara menghasilkan boilerplate untuk lapisan layanan kami", atau "daftar periksa ulasan kode kami". Agen menerapkan skill secara otomatis saat relevan.

Ini bukan konsep baru (`.github/copilot-instructions.md` sudah ada sejak lama), tetapi integrasi Visual Studio menjadikannya objek kelas satu dengan UI penemuan.

## Membuat Skills di Visual Studio

Alur UI terintegrasi: klik ikon alat di Copilot Chat, buka panel skills, klik `+`. Anda memilih cakupan global (pribadi) atau tingkat solusi, pilih nama, dan Visual Studio menghasilkan template. Mode Agen Copilot kemudian dapat membantu Anda mengisi template — gunakan agen untuk menulis skill untuk agen.

Saat ini di saluran Insiders, segera hadir di Release.

Anda juga dapat membuat skills secara manual:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Lokasi Penemuan

Skills ditemukan secara otomatis dari jalur standar:

**Tingkat solusi (dibagikan melalui repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/pribadi (profil pengguna Anda, tersedia di mana saja):** `~/.copilot/skills/`, `~/.agents/skills/`

Dukungan multi-lokasi berarti konvensi yang sama berfungsi dengan GitHub Copilot, Claude Code, dan framework agen lainnya — definisikan skills Anda sekali, gunakan di mana saja.

## Format

Skills mengikuti format [agentskills.io/specification](https://agentskills.io/specification) — spesifikasi berbasis Markdown yang dapat dibaca oleh manusia dan dapat diurai oleh mesin. Anda dapat menyertakan skrip, template, dan contoh di samping `SKILL.md`.

## Nilai Praktis

Kekuatan nyata bukan pada fitur individual — melainkan pada kombinasi skills yang dibagikan tim (melalui `.github/skills/`) dan skills pribadi (melalui `~/.agents/skills/`). Skills tim mengkodekan cara organisasi Anda melakukan sesuatu. Skills pribadi mengkodekan cara Anda secara khusus bekerja. Agen mendapatkan kedua konteks secara otomatis.

Bagi organisasi yang sudah menggunakan Copilot secara intensif, ini adalah langkah penting menuju membuat alat benar-benar mengetahui konvensi spesifik codebase Anda daripada memberikan saran umum.

Pos asli: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
