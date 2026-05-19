---
title: "Private Endpoints, VNet, NSG — Aspire Kini Mengelola Jaringan"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Dukungan jaringan enterprise Azure baru di Aspire memungkinkan Anda memodelkan VNet, private endpoint, NAT gateway, NSG, dan Network Security Perimeter langsung di AppHost — tanpa infrastructure drift."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Saya sudah terlalu sering melihat skenario ini. Aplikasi sudah selesai. Demo terlihat hebat. Kemudian checklist keamanan muncul: pindahkan storage dari internet publik, jalankan dalam VNet, sediakan IP keluar untuk allowlist mitra, buktikan bahwa hanya subnet yang benar yang berkomunikasi dengan layanan yang benar.

Pada titik ini model aplikasi dan model infrastruktur mulai menyimpang dengan cara yang menyakitkan untuk dipertahankan.

Dukungan jaringan enterprise Azure baru di Aspire mengatasi hal ini secara langsung. Anda menggambarkan bentuk jaringan di AppHost di sebelah resource yang menggunakannya.

## Blok Bangunan

Inilah kegunaan setiap konsep jaringan Azure, dirangkum:

| Fitur | Gunakan ketika | Mengapa penting |
|---------|------------|----------------|
| Virtual Network | Anda membutuhkan ruang alamat privat | Batas jaringan untuk subnet, private endpoint, dan routing |
| Subnet | Anda perlu memisahkan beban kerja dalam VNet | Setiap bagian sistem mendapatkan rentang alamat dan permukaan kebijakannya sendiri |
| Delegated Subnet | Layanan platform (mis. ACA) perlu mengelola subnet | Memungkinkan layanan menempatkan infrastruktur terkelola dengan aman di VNet Anda |
| NAT Gateway | Anda membutuhkan IP publik keluar yang dapat diprediksi | Alamat stabil untuk allowlist dan audit |
| Private Endpoint | Anda ingin resource PaaS dapat diakses secara privat | Menempatkan IP privat untuk layanan tersebut di dalam VNet Anda, menghapus eksposur publik |
| NSG | Anda membutuhkan aturan lalu lintas tingkat subnet | Izinkan/tolak eksplisit untuk lalu lintas masuk dan keluar per subnet |

## Menggambarkan di AppHost

Perubahan kunci di sini adalah Anda memodelkan jaringan *bersama* resource yang menggunakannya, bukan dalam file Bicep terpisah yang menyimpang dari model aplikasi seiring waktu.

Dari AppHost Anda dapat:

- Membuat VNet dan subnet dengan `AddVirtualNetwork()` dan `AddSubnet()`
- Melampirkan NAT gateway ke subnet untuk IP keluar yang stabil
- Membuat private endpoint untuk storage, Key Vault, SQL, dan layanan PaaS lainnya
- Mendefinisikan NSG dengan aturan keamanan masuk dan keluar
- Mengonfigurasi Network Security Perimeter untuk kebijakan lintas resource

Hasilnya adalah saat Anda menjalankan `azd up`, infrastruktur cocok dengan apa yang dikatakan model aplikasi bahwa ia butuhkan. Bukan apa yang dikatakan template yang dikelola secara manual.

## Mengapa Ini Penting untuk Aplikasi Nyata

Beberapa hal yang menjadi jauh lebih mudah setelah jaringan dimodelkan di Aspire:

**Private endpoint untuk Key Vault dan storage** — Anda menggambarkan `WithPrivateEndpoint()` pada resource tersebut, dan Aspire menangani konfigurasi zona DNS dan pemasangan endpoint. Aplikasi tidak pernah berubah.

**IP keluar yang konsisten** — Tambahkan NAT gateway ke subnet yang relevan, dan setiap permintaan keluar dari aplikasi Anda melewati IP yang dikenal dan stabil. Mitra dapat menambahkannya ke allowlist. Auditor dapat melacaknya.

**Aturan NSG dari kode** — Alih-alih mengklik di portal atau mempertahankan cuplikan Bicep, aturan keamanan Anda ada di AppHost di sebelah resource yang mereka lindungi.

Inilah jenis integrasi yang tidak membuat demo menjadi menarik tetapi membuat sistem produksi dapat dipelihara.

## Penutup

Keamanan jaringan yang muncul terlambat dalam siklus hidup proyek adalah masalah yang terpecahkan jika Anda memodelkannya bersama aplikasi sejak awal. Dukungan jaringan enterprise Aspire memungkinkan hal itu tanpa membutuhkan jalur infrastruktur terpisah.

Detail lengkap di postingan asli: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
