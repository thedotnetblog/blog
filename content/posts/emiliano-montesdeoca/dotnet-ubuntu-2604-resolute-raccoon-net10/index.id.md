---
title: ".NET 10 Hadir Bersama Ubuntu 26.04 LTS — Ini yang Baru"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) hadir dengan .NET 10 sebagai toolchain kelas satu. Native AOT, Chiseled container, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

Ini hari Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) diluncurkan hari ini dengan [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

## Instal .NET 10 dengan Dua Perintah

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Container: Perbarui `-noble` ke `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: Startup 3ms, Binary 1,4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# binary native 1,4MB, startup 3ms
```

Untuk beban kerja cloud-native di mana waktu cold-start penting — Functions, container, serverless — ini pengubah permainan nyata.

## Butuh .NET 8 atau 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[Posting lengkap](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) memiliki lebih banyak detail.
