---
title: ".NET 10 wordt Geleverd met Ubuntu 26.04 LTS — Dit Is Nieuw"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) is uitgebracht met .NET 10 als eersteklas toolchain. Native AOT, Chiseled containers, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

Het is Ubuntu LTS-dag. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) is vandaag uitgebracht met [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

## .NET 10 in twee commando's installeren

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET is een van de [officieel ondersteunde toolchains op Ubuntu](https://ubuntu.com/toolchains).

## Containers: `-noble` bijwerken naar `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: 3ms opstart, 1,4MB binair bestand

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# native binair bestand van 1,4MB, opstart in 3ms
```

Voor cloud-native workloads waarbij koude starttijd belangrijk is — Functions, containers, serverless — een echte gamechanger.

## .NET 8 of 9 nodig?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

Het [volledige bericht](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) bevat meer details.
