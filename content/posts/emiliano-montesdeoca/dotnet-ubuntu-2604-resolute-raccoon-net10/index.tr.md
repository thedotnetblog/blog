---
title: ".NET 10 Ubuntu 26.04 LTS ile Geliyor — Neler Yeni"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) .NET 10'u birinci sınıf araç zinciri olarak getiriyor. Native AOT, Chiseled konteyner, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Ubuntu LTS günü. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) bugün [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) ile yayımlandı.

## .NET 10'u İki Komutla Yükle

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Konteynerler: `-noble` yerine `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: 3ms Başlatma, 1,4MB İkili

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# 1,4MB yerel ikili, 3ms başlatma süresi
```

Soğuk başlangıç süresinin önemli olduğu cloud-native iş yükleri için — Functions, konteynerler, serverless — gerçek bir oyun değiştirici.

## .NET 8 veya 9'a İhtiyacın Var mı?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[Tam makale](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) cgroup v2, kuantum sonrası kriptografi ve Linux 7.0 hakkında daha fazla ayrıntı içeriyor.
