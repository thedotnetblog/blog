---
title: ".NET 10 Inclòs amb Ubuntu 26.04 LTS — Les Novetats"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) arriba amb .NET 10 com a toolchain de primera classe. Native AOT, contenidors chiseled, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

És el dia d'Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) ha arribat avui amb [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

## Instal·la .NET 10 en dos comandes

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Contenidors: actualitza `-noble` a `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: arrencada en 3ms, binari de 1.4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# binari natiu de 1.4MB, arrencada en 3ms
```

## Necessites .NET 8 o 9?

```bash
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

Consulta el [post complet](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) per a més detalls.
