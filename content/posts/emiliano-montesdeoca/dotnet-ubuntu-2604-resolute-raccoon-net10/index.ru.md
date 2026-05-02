---
title: ".NET 10 поставляется с Ubuntu 26.04 LTS — Что Нового"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) вышел с .NET 10 в качестве первоклассного тулчейна. Native AOT, Chiseled-контейнеры, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Этот пост переведён автоматически. Чтобы просмотреть оригинал, [нажмите здесь]({{< ref "index.md" >}}).*

День Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) вышел сегодня вместе с [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS на LTS — пять лет поддержки ОС, совпадающих с окном долгосрочной поддержки .NET 10.

## Установить .NET 10 двумя командами

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET является одним из [официально поддерживаемых тулчейнов на Ubuntu](https://ubuntu.com/toolchains).

## Контейнеры: обновить `-noble` на `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

Все существующие варианты образов — включая [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) — доступны.

## Native AOT: запуск за 3мс, бинарник 1,4МБ

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# нативный бинарник 1,4МБ, запуск за 3мс
```

Для cloud-native рабочих нагрузок, где время холодного запуска важно — Functions, контейнеры, serverless — реальная игра меняется.

## Нужен .NET 8 или 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[Полный пост](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) содержит больше деталей о cgroup v2, пост-квантовой криптографии и Linux 7.0.
