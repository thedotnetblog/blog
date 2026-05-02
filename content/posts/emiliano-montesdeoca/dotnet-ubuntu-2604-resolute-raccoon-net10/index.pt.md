---
title: ".NET 10 Vem com Ubuntu 26.04 LTS — O que há de Novo"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) chegou com .NET 10 como toolchain de primeira classe. Native AOT, contêineres chiseled, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

É o dia do Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) chegou hoje com [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS sobre LTS — cinco anos de suporte para o OS, alinhados com a janela de suporte de longo prazo do .NET 10.

## Instale .NET 10 em dois comandos

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

## Contêineres: atualize `-noble` para `-resolute`

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: inicialização em 3ms, binário de 1,4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# binário nativo de 1,4MB, inicialização em 3ms
```

Para cargas de trabalho cloud-native onde o tempo de cold-start importa — Functions, contêineres, serverless — uma mudança real.

## Precisa de .NET 8 ou 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

O [post completo](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) tem mais detalhes sobre cgroup v2, criptografia pós-quântica e Linux 7.0.
