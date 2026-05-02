---
title: ".NET 10 Se Incluye con Ubuntu 26.04 LTS — Qué hay de Nuevo"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) llegó con .NET 10 como toolchain de primera clase. Native AOT, contenedores chiseled, Linux 7.0 — esto es lo que necesitas saber."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Es el día de Ubuntu LTS. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) llegó hoy, y como con cada Ubuntu LTS, incluye el último .NET LTS — en este caso, [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

LTS sobre LTS — cinco años de soporte para el OS, alineados con la ventana de soporte a largo plazo de .NET 10.

## Instala .NET 10 en dos comandos

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET es uno de los [toolchains oficialmente soportados en Ubuntu](https://ubuntu.com/toolchains) — no un add-on de terceros.

## Pruébalo de inmediato

```bash
docker run --rm -it ubuntu:resolute
apt update
apt install -y dotnet-sdk-10.0
dotnet run - << 'EOF'
using System.Runtime.InteropServices;
Console.WriteLine($"Hello {RuntimeInformation.OSDescription} from .NET {RuntimeInformation.FrameworkDescription}");
EOF
```

## Contenedores: actualiza `-noble` a `-resolute`

La migración es de una línea:

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

Todos los sabores de imagen existentes — incluyendo [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) — están disponibles.

## Native AOT: arranque en 3ms, binario de 1.4MB

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# artifacts/app/app — binario nativo de 1.4MB
# real 0m0.003s
```

Para cargas de trabajo cloud-native donde el tiempo de arranque en frío importa — Functions, contenedores, serverless — esto es un cambio real.

## ¿Necesitas .NET 8 o 9?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

El [post completo](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) tiene más detalles sobre cgroup v2, post-quantum cryptography y Linux 7.0.
