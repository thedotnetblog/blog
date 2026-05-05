---
title: ".NET Abril 2026 Servicing — Parches de seguridad que deberías aplicar hoy"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "La actualización de servicing de abril 2026 corrige 6 CVEs en .NET 10, .NET 9, .NET 8 y .NET Framework — incluyendo dos vulnerabilidades de ejecución remota de código."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}}).*

Las [actualizaciones de servicing de abril 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) para .NET y .NET Framework ya están disponibles, y esta incluye correcciones de seguridad que vas a querer aplicar pronto. Seis CVEs parcheados, incluyendo dos vulnerabilidades de ejecución remota de código (RCE).

## Qué se ha parcheado

Aquí va el resumen rápido:

| CVE | Tipo | Afecta a |
|-----|------|----------|
| CVE-2026-26171 | Omisión de característica de seguridad | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Ejecución remota de código** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Ejecución remota de código** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denegación de servicio | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denegación de servicio | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denegación de servicio | .NET Framework 2.0–4.8.1 |

Los dos CVEs de RCE (CVE-2026-32178 y CVE-2026-33116) afectan al mayor rango de versiones de .NET y deberían ser la prioridad.

## Versiones actualizadas

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Todas están disponibles a través de los canales habituales — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), imágenes de contenedores en MCR y gestores de paquetes de Linux.

## Qué hacer

Actualiza tus proyectos y pipelines de CI/CD a las últimas versiones parcheadas. Si estás corriendo contenedores, descarga las últimas imágenes. Si estás en .NET Framework, revisa las [notas de versión de .NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) para los parches correspondientes.

Para quienes están corriendo .NET 10 en producción (es la versión actual), 10.0.6 es una actualización obligatoria. Lo mismo para .NET 9.0.15 y .NET 8.0.26 si estás en esas versiones LTS. Dos vulnerabilidades de RCE no son algo que se pospone.
