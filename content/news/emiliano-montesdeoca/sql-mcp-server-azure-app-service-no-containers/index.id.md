---
title: "SQL MCP Server di Azure App Service — Tanpa Container"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server kini dapat berjalan di Azure App Service tanpa Docker atau Kubernetes. Apa artinya bagi developer .NET yang membangun agen AI yang berkomunikasi dengan database SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Postingan ini telah diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Jujur saja: setiap kali melihat "membutuhkan container" dalam sebuah tutorial, ada rasa lelah yang muncul. Container memang hebat — sampai tim kamu tidak punya strategi container, dan fitur yang tampak sederhana tiba-tiba tersangkut pada kompleksitas orkestrasi yang tidak direncanakan siapapun.

Itulah mengapa ini menarik perhatian saya. SQL MCP Server kini dapat berjalan di Azure App Service — tanpa Docker, tanpa Kubernetes, hanya dengan file konfigurasi Data API Builder (DAB) yang sama yang mengekspos database SQL kamu melalui MCP, REST, dan GraphQL.

## Apa itu SQL MCP Server?

Pengenalan singkat jika kamu belum familiar. SQL MCP Server berada di antara agen AI kamu dan database SQL. Alih-alih memberikan akses langsung ke database pada agen (ide yang buruk), ia mengekspos tabel dan view kamu sebagai lapisan abstraksi — entitas dengan izin yang terdefinisi.

Dibangun di atas [Data API Builder](https://learn.microsoft.com/id-id/azure/data-api-builder/), yang berarti satu file konfigurasi mengelola MCP *dan* REST *dan* GraphQL sekaligus. Agen kamu berkomunikasi dengan endpoint MCP. Aplikasi tradisional berkomunikasi dengan REST atau GraphQL. Konfigurasi yang sama, runtime yang sama, permukaan yang berbeda.

Ini benar-benar berguna — kamu tidak perlu memelihara dua lapisan API yang terpisah.

## Masalah Container (dan Solusinya)

Model deployment awal SQL MCP Server menggunakan container. Ini berfungsi dengan baik di banyak tim — tapi tidak semua. Banyak tim .NET menggunakan Azure App Service atau VM sebagai standar. Mengharuskan runtime container hanya untuk mengekspos endpoint SQL menambah hambatan yang tidak diminta siapapun.

Panduan baru menunjukkan cara melewatkan container sepenuhnya. Semuanya berjalan dengan perintah `dab start`, di-host di App Service sebagai proses web .NET 8 standar.

```bash
# Instal Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Inisialisasi konfigurasi
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Tambahkan entitas
dab add products --source dbo.products --permissions "authenticated:*"

# Konfigurasi penyedia autentikasi App Service
dab configure --runtime.host.authentication.provider AppService

# Jalankan server
dab start
```

Pada titik ini kamu memiliki MCP di `/mcp`, REST dan GraphQL dari proses yang sama — dan tidak ada yang berjalan di container.

## Autentikasi Tanpa API Key Bersama

Inilah bagian yang paling saya hargai. Saat deploy ke App Service, kamu mengonfigurasi Microsoft Entra ID sebagai penyedia autentikasi. Tidak ada rahasia bersama dalam file konfigurasi, tidak ada API key untuk dirotasi.

Connection string tetap berada di variabel lingkungan App Service (bukan di `dab-config.json`), dan endpoint MCP dilindungi oleh autentikasi platform. Jika workload Azure kamu sudah selaras dengan Entra ID, ini akan terintegrasi secara alami.

Untuk development lokal, beralih ke mode `Simulator` dan transport STDIO. Kembali ke mode `AppService` sebelum deployment. Bersih dan eksplisit.

## Deploy ke App Service

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Kemudian deploy proyek DAB kamu menggunakan metode deployment kode yang sudah digunakan tim kamu. Detail kuncinya: ini adalah deployment **kode**, bukan deployment container.

## Mengapa Penting bagi Developer .NET

Jika kamu membangun agen AI di .NET, cepat atau lambat agen kamu perlu berkomunikasi dengan database. SQL MCP Server memberimu cara terstruktur untuk melakukannya — tanpa mengekspos connection string mentah.

Lihat panduan lengkapnya di [postingan blog asli](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) dan [repositori sampel GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Kesimpulan

SQL MCP Server di App Service adalah pilihan pragmatis untuk tim .NET yang ingin memberikan akses data SQL terstruktur kepada agen mereka tanpa strategi container. Coba — agen kamu akan mengapresiasi permukaan API yang bersih.
