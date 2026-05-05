---
title: ".NET 10 Est Livré avec Ubuntu 26.04 LTS — Ce qui Est Nouveau"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) est sorti avec .NET 10 comme toolchain de première classe. Native AOT, conteneurs chiseled, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

C'est le jour de l'Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) est sorti aujourd'hui avec [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS sur LTS — cinq ans de support pour l'OS, correspondant à la fenêtre de support long terme de .NET 10.

## Installer .NET 10 en deux commandes

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET est l'une des [toolchains officiellement supportées sur Ubuntu](https://ubuntu.com/toolchains) — pas un add-on tiers.

## Conteneurs : mettre à jour `-noble` vers `-resolute`

La migration est une seule ligne :

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

Toutes les variantes d'images existantes — y compris [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) — sont disponibles.

## Native AOT : démarrage en 3ms, binaire de 1,4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# artifacts/app/app — binaire natif de 1,4MB
# real 0m0.003s
```

Pour les charges de travail cloud-native où le temps de démarrage à froid compte — Functions, conteneurs, serverless — c'est un vrai changement de jeu.

## Besoin de .NET 8 ou 9 ?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

Le [post complet](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) contient plus de détails.
