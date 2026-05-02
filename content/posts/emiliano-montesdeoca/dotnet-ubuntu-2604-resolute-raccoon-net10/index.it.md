---
title: ".NET 10 Arriva con Ubuntu 26.04 LTS — Le Novità"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) è uscito con .NET 10 come toolchain di prima classe. Native AOT, contenitori chiseled, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

È il giorno dell'Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) è uscito oggi con [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS su LTS — cinque anni di supporto per l'OS, in linea con la finestra di supporto a lungo termine di .NET 10.

## Installa .NET 10 in due comandi

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET è una delle [toolchain ufficialmente supportate su Ubuntu](https://ubuntu.com/toolchains) — non un add-on di terze parti.

## Container: aggiorna `-noble` a `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: avvio in 3ms, binario da 1,4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# binario nativo da 1,4MB, avvio in 3ms
```

Per carichi di lavoro cloud-native dove il tempo di cold-start conta — Functions, container, serverless — un vero cambio di gioco.

## Hai bisogno di .NET 8 o 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

Il [post completo](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) ha più dettagli.
