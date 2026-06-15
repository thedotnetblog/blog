---
title: "Update Mei Visual Studio sebenarnya tentang kontrol yang lebih baik antara ide dan perubahan"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Update Mei Visual Studio menambahkan Plan agent, peningkatan manajemen skill, visibilitas context window, dan pengalaman diff ringkasan multi-file yang lebih kuat. Tema yang sama adalah kontrol yang lebih baik atas inner loop berbantuan AI."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *Artikel ini diterjemahkan secara otomatis. Baca versi aslinya [di sini]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}).* 

Hal paling menarik dari update Mei Visual Studio bukanlah satu fitur tunggal.

Melainkan arah yang dibawa bersama-sama.

Rilis ini terus memperbaiki ruang di antara:

- sebuah ide
- sebuah rencana
- perubahan yang dihasilkan
- review
- hasil yang disempurnakan

Itulah bagian dari development berbantuan AI yang menentukan apakah workflow terasa tepercaya atau kacau.

## Daftar fiturnya beragam, tetapi niatnya konsisten

Di atas kertas, rilis ini berisi campuran hal-hal berikut:

- Plan agent baru
- peningkatan manajemen skill
- visibilitas context window
- multi-file summary diff
- pembersihan workflow terkait Copilot
- update MSVC di sisi C++

Itu bisa terlihat seperti kumpulan acak.

Menurut saya tidak.

Benang merahnya cukup jelas: **Visual Studio mencoba memberi developer lebih banyak kontrol atas pekerjaan berbantuan AI tanpa memperlambat mereka.**

Itu tradeoff yang tepat untuk dikejar.

## Plan agent adalah pusat filosofis dari rilis ini

Meskipun fitur lain penting, saya masih menganggap Plan agent adalah bagian paling revealing dari update ini.

Itu membuat sesuatu yang sering kita rasakan saat memakai coding agent menjadi eksplisit:

memulai dengan cepat tidak selalu sama dengan bergerak secara efektif.

Rilis ini menegaskan itu dengan menjadikan planning, review, dan controlled implementation sebagai urutan yang lebih natural.

Itu sehat.

## Pekerjaan multi-file diff diam-diam adalah peningkatan besar

Saya juga pikir multi-file summary diff pantas mendapat lebih banyak kredit daripada yang mungkin akan diterimanya.

Saat agent mengubah beberapa file sekaligus, pengalaman review menjadi produknya.

Jika review perubahan terasa berantakan, developer jadi kurang percaya pada workflow.

Jika review perubahan terasa koheren, developer lebih mungkin terus memakai tool tersebut.

Itulah mengapa unified summary view sangat penting. Itu menurunkan biaya kognitif untuk mengatakan ya atau tidak pada pekerjaan yang dihasilkan.

## context window indicator adalah tambahan yang lebih pintar dari yang terdengar

Saya juga suka indikator penggunaan context.

Ini mungkin terdengar kecil, tetapi ia menyelesaikan masalah workflow AI yang sangat nyata: tidak tahu kapan tool mulai melupakan bagian awal percakapan.

Membuatnya terlihat adalah keputusan desain yang bagus.

Ia tidak secara ajaib memperluas context model. Tetapi ia membuat batasnya terlihat, dan itu sering kali opsi terbaik berikutnya.

## Pendapat saya

Update ini sebenarnya tentang memberi developer lebih banyak visibilitas dan kontrol atas loop berbantuan AI.

Bukan lebih banyak hal baru.
Bukan lebih banyak kekacauan.
Lebih banyak kontrol.

Itulah tempat yang tepat untuk berinvestasi jika tujuannya adalah membuat tooling AI terasa lebih tepercaya di dalam workflow IDE yang serius.

Artikel asli: [Update Mei Visual Studio — Plan, Review, Refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)