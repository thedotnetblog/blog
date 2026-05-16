---
title: "Menghilangkan Pekerjaan Berulang Migrasi dengan Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape memandu migrasi deployment AWS Terraform nyata ke Azure Bicep — mengekstrak intent deployment dan meremetakan arsitektur daripada melakukan konversi sintaks 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — panduan langkah demi langkah Git-Ape (alat git agentic platform engineering) yang memigrasikan repo Terraform AWS nyata ke Azure, berfokus pada ekstraksi intent daripada konversi baris per baris.

## Input: contoso-migration

Sumbernya adalah proyek Terraform nyata (`contoso-migration`) yang mendeploy aplikasi Next.js di AWS — EC2 untuk komputasi, ALB untuk load balancing, S3 untuk artefak, dan kunci IAM untuk identitas. Biaya: ~$34/bulan. Tujuannya bukan mereproduksi infrastruktur yang sama di Azure; melainkan memahami apa yang sebenarnya ingin dilakukan oleh deployment dan membangun ulang menggunakan layanan Azure-native.

## Langkah 1: Validasi dan autentikasi

Git-Ape memulai dengan memvalidasi semua alat CLI yang diperlukan — `az`, `aws`, `gh`, `jq`, `git` — dan mengkonfirmasi sesi autentikasi yang aktif sebelum menyentuh apapun. Tidak ada eksekusi parsial.

## Langkah 2: Ekstraksi intent

Agen membaca seluruh repo sumber melalui GitHub API dan mengekstrak intent deployment: runtime (Node.js), tipe komputasi, pola ingress, penanganan artefak, model identitas, jaringan, dan monitoring. Ini adalah langkah kunci — membangun model semantik tentang apa yang dilakukan deployment, bukan kata kunci Terraform apa yang digunakan.

## Langkah 3: Pemetaan layanan

Layanan AWS dipetakan ke padanan Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Load balancing bawaan App Service
- Peran/kunci IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Langkah 4: Agen kritik

Sebelum menghasilkan output, agen kritik berjalan dan menangkap dua masalah yang memblokir:

1. **Anti-pola build-on-startup** — Terraform asli menjalankan `npm install && npm run build` di EC2 saat startup. Perbaikan: build di CI, deploy artefak yang sudah siap.
2. **Blob Storage yang tidak perlu** — S3 digunakan untuk staging artefak yang bisa dihilangkan dengan CI/CD yang tepat. Agen kritik menghapusnya sepenuhnya.

## Langkah 5: Output yang dihasilkan

Hasilnya adalah ~80 baris Bicep alih-alih 200+ baris Terraform asli. Agen membuat repo GitHub baru dengan `infra/main.bicep` dan `.github/workflows/deploy.yml` dan menghapus semua file khusus AWS.

## Perbandingan postur keamanan

Migrasi juga menghasilkan peningkatan keamanan yang berarti:

| AWS asli | Output Azure |
|---|---|
| HTTP saja | HTTPS saja, TLS 1.2 |
| SSH terbuka ke 0.0.0.0/0 | Tidak ada eksposur SSH |
| Kunci akses IAM | OIDC + Managed Identity |
| Tanpa monitoring | Application Insights |

Biaya: ~$13/bulan vs $34/bulan asli.

## Apa yang membedakan ini dari konverter sintaks

Langkah agen kritik inilah yang memisahkan ini dari terjemahan mekanis. Ia menangkap pola yang akan bekerja di AWS tetapi salah di Azure — dan memperbaikinya daripada mereplikasinya. Outputnya bukan "AWS dalam sintaks Azure"; melainkan deployment Azure-native yang mencapai tujuan yang sama dengan lebih bersih.

Lihat [panduan lengkap](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) untuk jejak agen lengkap dan file yang dihasilkan.
