---
title: "azd + GitHub Copilot: Penyiapan Proyek Berbantuan AI dan Pemecahan Masalah Error Cerdas"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI kini terintegrasi dengan GitHub Copilot untuk membuat infrastruktur proyek dan menyelesaikan error deployment — tanpa keluar dari terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Artikel ini diterjemahkan secara otomatis. Untuk versi asli dalam bahasa Inggris, [klik di sini]({{< ref "index.md" >}}).*

Kamu pasti pernah mengalami momen ketika ingin men-deploy aplikasi yang sudah ada ke Azure, lalu menatap file `azure.yaml` yang kosong sambil mencoba mengingat apakah Express API-mu harus menggunakan Container Apps atau App Service? Momen itu kini jauh lebih singkat.

Azure Developer CLI (`azd`) kini terintegrasi dengan GitHub Copilot dalam dua cara yang nyata: scaffolding proyek berbantuan AI selama `azd init`, dan pemecahan masalah error cerdas ketika deployment gagal. Kedua fitur ini sepenuhnya berjalan di dalam terminal.

## Setup dengan Copilot selama azd init

Saat menjalankan `azd init`, kini ada opsi "Set up with GitHub Copilot (Preview)". Pilih itu dan Copilot akan menganalisis codebase-mu untuk menghasilkan `azure.yaml`, template infrastruktur, dan modul Bicep — berdasarkan kode aslimu.

```
azd init
# Pilih: "Set up with GitHub Copilot (Preview)"
```

Prasyarat:

- **azd 1.23.11 atau lebih baru** — cek dengan `azd version` atau perbarui dengan `azd update`
- **Langganan GitHub Copilot aktif** (Individual, Business, atau Enterprise)
- **GitHub CLI (`gh`)** — `azd` akan meminta login jika diperlukan

Yang menurutku benar-benar berguna: ini bekerja dua arah. Membangun dari nol? Copilot membantu mengonfigurasi layanan Azure yang tepat sejak awal. Punya aplikasi yang ingin di-deploy? Arahkan Copilot ke sana dan konfigurasi akan dibuat tanpa perlu restrukturisasi kode apapun.

### Yang sebenarnya dilakukan

Katakanlah kamu punya Node.js Express API dengan dependensi PostgreSQL. Daripada memutuskan manual antara Container Apps dan App Service, lalu menulis Bicep dari nol, Copilot mendeteksi stack-mu dan menghasilkan:

- `azure.yaml` dengan pengaturan `language`, `host`, dan `build` yang tepat
- Modul Bicep untuk Azure Container Apps
- Modul Bicep untuk Azure Database for PostgreSQL

Dan menjalankan pemeriksaan awal sebelum mengubah apapun — memverifikasi direktori git bersih, meminta persetujuan alat server MCP di awal. Tidak ada yang terjadi tanpa kamu tahu persis apa yang akan berubah.

## Pemecahan Masalah Error dengan Copilot

Error deployment adalah hal yang tak terhindarkan. Parameter yang hilang, masalah izin, ketersediaan SKU — dan pesan error jarang memberitahumu satu hal yang benar-benar perlu kamu ketahui: *cara memperbaikinya*.

Tanpa Copilot, siklusnya terlihat seperti: salin error → cari di docs → baca tiga jawaban Stack Overflow yang tidak relevan → jalankan beberapa perintah `az` CLI → coba lagi dan berharap. Dengan Copilot terintegrasi di `azd`, siklus ini runtuh. Saat perintah `azd` apapun gagal, langsung ditawarkan empat pilihan:

- **Explain** — penjelasan dalam bahasa sederhana tentang apa yang salah
- **Guidance** — instruksi langkah demi langkah untuk memperbaiki masalah
- **Diagnose and Guide** — analisis lengkap + Copilot menerapkan perbaikan (dengan persetujuanmu) + retry opsional
- **Skip** — tangani sendiri

Poin kuncinya: Copilot sudah memiliki konteks tentang proyekmu, perintah yang gagal, dan detail error. Sarannya spesifik untuk *situasimu*.

### Mengatur Perilaku Default

Jika selalu memilih opsi yang sama, lewati prompt interaktif:

```
azd config set copilot.errorHandling.category troubleshoot
```

Nilai: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Kamu juga bisa mengaktifkan auto-fix dan retry:

```
azd config set copilot.errorHandling.fix allow
```

Kembali ke mode interaktif kapan saja:

```
azd config unset copilot.errorHandling.category
```

## Kesimpulan

Jalankan `azd update` untuk mendapatkan versi terbaru dan coba `azd init` di proyek berikutnya.

Baca [pengumuman aslinya di sini](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
