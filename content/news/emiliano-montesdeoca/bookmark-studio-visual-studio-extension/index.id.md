---
title: "Bookmark Studio Menghadirkan Navigasi Berbasis Slot dan Berbagi ke Bookmark Visual Studio"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Ekstensi Bookmark Studio baru dari Mads Kristensen menambahkan navigasi slot berbasis keyboard, manajer bookmark, warna, label, dan kemampuan ekspor/berbagi ke bookmark Visual Studio."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "bookmark-studio-visual-studio-extension" >}}).*

Bookmark di Visual Studio selalu... cukup baik. Anda mengaturnya, menavigasi ke yang berikutnya, lupa mana yang mana.

Mads Kristensen baru saja [merilis Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), ekstensi eksperimental yang mengisi kesenjangan yang mungkin Anda temui jika menggunakan bookmark secara teratur.

## Navigasi berbasis slot

Tambahan utama: bookmark sekarang dapat ditetapkan ke slot 1–9 dan langsung melompat dengan `Alt+Shift+1` hingga `Alt+Shift+9`. Ini mengubah bookmark dari "saya punya beberapa bookmark di suatu tempat" menjadi "Slot 3 adalah controller API saya, Slot 5 adalah lapisan layanan."

## Manajer Bookmark

Jendela alat baru menampilkan semua bookmark Anda di satu tempat dengan pemfilteran berdasarkan nama, file, lokasi, warna, atau slot.

## Organisasi dengan label, warna, dan folder

Bookmark secara opsional dapat memiliki label dan warna serta dikelompokkan ke dalam folder. Semua metadata disimpan per solusi.

## Ekspor dan berbagi

Bookmark Studio memungkinkan Anda mengekspor bookmark sebagai teks biasa, Markdown, atau CSV:
- Sertakan jalur bookmark dalam deskripsi pull request
- Bagikan jejak investigasi dengan rekan tim

Ambil dari [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio).
