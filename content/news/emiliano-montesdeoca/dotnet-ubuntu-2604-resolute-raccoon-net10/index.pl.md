---
title: ".NET 10 Jest Dostarczany z Ubuntu 26.04 LTS — Co Nowego"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) wyszedł z .NET 10 jako toolchain pierwszej klasy. Native AOT, kontenery chiseled, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

To dzień Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) wyszedł dziś z [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

## Zainstaluj .NET 10 dwoma poleceniami

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Kontenery: zaktualizuj `-noble` do `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: uruchomienie w 3ms, binarny plik 1,4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# natywny plik binarny 1,4MB, uruchomienie w 3ms
```

Dla cloud-native workloadów, gdzie czas zimnego startu ma znaczenie — Functions, kontenery, serverless — prawdziwa zmiana gry.

## Potrzebujesz .NET 8 lub 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[Pełny post](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) zawiera więcej szczegółów.
