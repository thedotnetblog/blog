---
title: ".NET 10 wird mit Ubuntu 26.04 LTS ausgeliefert — Was Neu Ist"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) ist mit .NET 10 als erstklassiger Toolchain erschienen. Native AOT, Chiseled Container, Linux 7.0 — hier ist, was du wissen musst."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Es ist Ubuntu-LTS-Tag. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) ist heute erschienen und liefert wie jede Ubuntu-LTS die neueste .NET-LTS aus — in diesem Fall [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS auf LTS — fünf Jahre Support für das OS, passend zum eigenen Langzeit-Support-Fenster von .NET 10.

## .NET 10 in zwei Befehlen installieren

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET ist einer der [offiziell unterstützten Toolchains auf Ubuntu](https://ubuntu.com/toolchains) — kein Drittanbieter-Add-on.

## Container: `-noble` zu `-resolute` aktualisieren

Die Migration ist einzeilig:

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

Alle bestehenden Image-Varianten — einschließlich [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) — sind verfügbar.

## Native AOT: 3ms Start, 1,4MB Binary

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# artifacts/app/app — 1,4MB natives Binary
# real 0m0.003s
```

Für cloud-native Workloads, bei denen Kaltstart-Zeit wichtig ist — Functions, Container, Serverless — ein echter Gamechanger.

## Benötigst du .NET 8 oder 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

Der [vollständige Beitrag](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) enthält weitere Details zu cgroup v2, Post-Quanten-Kryptografie und Linux 7.0.
