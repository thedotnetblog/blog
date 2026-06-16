---
title: "Agent Harness, Hosted Agents, dan CodeAct: inilah pembaruan Agent Framework yang paling saya perhatikan"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Pengumuman Agent Framework di Build 2026 memang padat, tetapi tiga benang merah terpentingnya adalah model harness, hosted agents di Foundry, dan CodeAct untuk mengurangi overhead orkestrasi."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Pengumuman besar Agent Framework di Build mencakup banyak hal, tetapi tiga tema langsung menonjol bagi saya:

- **harness yang menjadi bagian runtime yang lebih utama**
- **hosted agents di Foundry yang memberi jalur ke production**
- **CodeAct yang mengurangi overhead orkestrasi multi-langkah**

Itulah bagian-bagian yang akan terus saya perhatikan.

## Harness sedang menjadi pusat gravitasi yang sebenarnya

Posting sumber menggambarkan harness sebagai lapisan tempat penalaran model bertemu eksekusi nyata.

Itu deskripsi yang tepat, dan itulah alasan saya menganggap bagian ini lebih penting daripada banyak poin fitur lainnya.

Begitu sebuah agen membutuhkan:

- akses file
- eksekusi shell
- mode perencanaan
- to-do
- memori sesi
- alur persetujuan

Anda tidak lagi berbicara tentang prompt plus model.

Anda sedang berbicara tentang perilaku runtime.

Di situlah framework menjadi berguna atau justru menjadi mainan.

Dan Microsoft Agent Framework jelas sedang berusaha menjadi lebih berguna tepat di lapisan itu.

## Hosted agents adalah tempat cerita dari lokal ke production menjadi nyata

Saya juga pikir bagian hosted agents adalah salah satu bagian paling strategis dari pengumuman ini.

Posting sumber secara eksplisit menyebutnya sebagai cara paling mudah untuk memberi agent itu rumah di production.

Frasa itu penting karena sebagian besar framework agent masih jauh lebih kuat untuk eksperimen lokal daripada untuk deployment operasional.

Jika hosted agents di Foundry benar-benar membuat perpindahan dari pengembangan lokal ke:

- scaling
- observability
- managed identity
- session handling
- versioning

jauh lebih mudah, maka itu menutup salah satu celah terbesar dalam ekosistem agent saat ini.

Itu peningkatan yang berarti.

## CodeAct adalah ide teknis paling menarik dalam pembaruan ini

Jika saya harus memilih konsep teknis paling menarik di posting ini, saya mungkin akan memilih CodeAct.

Masalah yang ingin dipecahkannya sangat nyata: terlalu banyak workflow agen multi-langkah yang mahal karena loop orkestrasi itu sendiri menghabiskan terlalu banyak putaran model.

Jadi ketika posting sumber menunjukkan hasil seperti ini:

- 52.4% lebih cepat
- 63.9% lebih sedikit token

itu langsung menarik perhatian saya.

Tentu saja, itu angka benchmark untuk beban kerja representatif, bukan hukum universal. Tetapi ide besarnya tetap sangat meyakinkan.

Jika model bisa memadatkan rantai tool-calling menjadi bentuk eksekusi yang lebih efisien, ekonomi sistem agen bisa berubah cukup besar.

## Yang menurut saya seharusnya benar-benar diambil developer dari pembaruan ini

Pelajaran pentingnya bukan jumlah fitur yang dirilis.

Pelajarannya adalah bahwa framework ini makin kuat di tempat yang paling dibutuhkan aplikasi nyata:

- runtime shell
- jalur deployment
- efisiensi eksekusi
- pola operasional bawaan

Itulah jenis sinyal kematangan yang jauh lebih saya pedulikan daripada daftar fitur AI yang dangkal lagi.

## Pendapat saya

Pembaruan ini penting karena bukan cuma menambah permukaan fitur.

Pembaruan ini memperkuat cerita runtime dan deployment di sekitar agen dengan cara yang seharusnya penting untuk aplikasi nyata, terutama bagi tim yang ingin bergerak dari eksperimen lokal ke sistem yang benar-benar bisa dijalankan dan dipelihara.

Di situlah framework ini menjadi lebih menarik.

Dan kalau saya mengikuti rilis ini dengan dekat, harness, hosted agents, dan CodeAct jelas akan menjadi tiga hal yang paling saya perhatikan.

Tulisan asli: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
