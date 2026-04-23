---
title: "Segera Patch: Pembaruan Keamanan OOB .NET 10.0.7 untuk ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 adalah rilis out-of-band yang memperbaiki kerentanan keamanan di Microsoft.AspNetCore.DataProtection — managed authenticated encryptor menghitung HMAC pada byte yang salah, yang dapat menyebabkan privilege escalation. Perbarui sekarang juga."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Pembaruan ini tidak opsional. Jika aplikasi Anda menggunakan `Microsoft.AspNetCore.DataProtection`, Anda perlu memperbarui ke 10.0.7.

## Apa yang Terjadi

Setelah rilis Patch Tuesday `.NET 10.0.6`, beberapa pengguna mulai melaporkan bahwa dekripsi gagal di aplikasi mereka. Saat menyelidiki regresi tersebut, tim juga menemukan kerentanan keamanan: **CVE-2026-40372**.

Pada versi `10.0.0` hingga `10.0.6` dari `Microsoft.AspNetCore.DataProtection`, managed authenticated encryptor menghitung tag validasi HMAC-nya pada **byte yang salah** dari payload lalu membuang hash yang dihitung. Hal ini dapat menyebabkan privilege escalation.

Secara sederhana: pemeriksaan integritas tidak melakukan apa yang seharusnya dilakukan. Data Protection menggunakan authenticated encryption untuk mencegah manipulasi — HMAC adalah pemeriksaan "apakah ini sudah diubah?". Jika HMAC dihitung pada data yang salah, jaminan itu hilang.

## Siapa yang Terpengaruh

Setiap aplikasi .NET 10 yang menggunakan `Microsoft.AspNetCore.DataProtection` — versi 10.0.0 hingga 10.0.6. Kabar baiknya, paket ini khusus untuk .NET 10. Jika Anda masih memakai .NET 8 atau 9, Anda tidak terdampak oleh CVE ini.

Kasus penggunaan umum Data Protection: enkripsi cookie, token antiforgery, temp data di MVC, dan penggunaan lain `IDataProtector` di aplikasi Anda.

## Cara Memperbaikinya

Perbarui paket NuGet `Microsoft.AspNetCore.DataProtection` ke **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Atau perbarui SDK/runtime Anda: [unduh .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Verifikasi bahwa Anda berada di versi yang benar:

```bash
dotnet --info
```

Lalu **bangun ulang dan terapkan ulang** aplikasi Anda. Perbaikan tidak berlaku sampai Anda menjalankan paket yang telah diperbarui.

## Gambaran Besar

Rilis keamanan out-of-band jarang terjadi — biasanya muncul saat kerentanannya cukup serius untuk tidak menunggu Patch Tuesday berikutnya. Kasus ini merupakan akibat langsung dari regresi di 10.0.6 yang menciptakan celah keamanan. Fakta bahwa masalah ini ditemukan melalui laporan bug adalah tanda yang baik: prosesnya berjalan. Perbaikannya cepat dan cakupannya sempit.

Jika Anda menjalankan .NET 10 di produksi dengan framework aplikasi web apa pun, ini adalah pembaruan hari itu juga.

Pengumuman asli oleh Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).