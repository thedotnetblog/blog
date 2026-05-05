---
title: ".NET 10 随 Ubuntu 26.04 LTS 发布 — 新特性概览"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) 携 .NET 10 作为一等工具链发布。Native AOT、Chiseled 容器、Linux 7.0。"
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*本文已自动翻译。如需查看原文，请[点击此处]({{< ref "index.md" >}})。*

Ubuntu LTS 发布日。[Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) 今天发布，与每个 Ubuntu LTS 一样，携带最新的 .NET LTS — 这次是 [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/)。

## 两条命令安装 .NET 10

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET 是 [Ubuntu 官方支持的工具链](https://ubuntu.com/toolchains)之一，不是第三方附加组件。

## 容器：将 `-noble` 更新为 `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

包括 [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) 在内的所有现有镜像变体均可用。

## Native AOT：3ms 启动，1.4MB 二进制文件

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# 1.4MB 原生二进制文件，启动时间 3ms
```

对于冷启动时间至关重要的云原生工作负载——Functions、容器、Serverless——这是真正的游戏规则改变者。

## 需要 .NET 8 或 9？

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[完整文章](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/)包含有关 cgroup v2、后量子密码学和 Linux 7.0 的更多详情。
