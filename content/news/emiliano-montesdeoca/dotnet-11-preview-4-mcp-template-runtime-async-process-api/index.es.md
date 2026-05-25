---
title: ".NET 11 Preview 4: Plantilla de Servidor MCP, Bibliotecas Runtime-Async, API de Procesos"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 ya está disponible. Los puntos destacados: la plantilla de servidor MCP en el SDK, bibliotecas de tiempo de ejecución compiladas con runtime-async, dotnet watch para móvil y una importante expansión de la API de procesos."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 está disponible. Cada versión de una preview principal de .NET añade una larga lista de elementos en el runtime, SDK, bibliotecas, ASP.NET Core, MAUI, C# y Entity Framework. En lugar de repetir la lista completa, aquí están las cosas que me llamaron la atención.

## La Plantilla de Servidor MCP Llega al SDK de .NET

El elemento más interesante: ahora se incluye una plantilla de proyecto de servidor MCP en el SDK. Esto significa que `dotnet new mcp-server` (o como acabe llamándose el comando) funciona de serie. Para cualquiera que construya herramientas MCP en .NET, esto elimina considerablemente la fricción inicial. La integración de MCP en la cadena de herramientas de la plataforma señala la dirección en que se dirige el ecosistema.

## Bibliotecas de Runtime Compiladas con Runtime-Async

El propio runtime ahora compila sus bibliotecas estándar usando la característica runtime-async. Es un cambio interno que afecta al rendimiento: las máquinas de estado async en el runtime se vuelven más eficientes. Lo importante aquí no son los cambios visibles en la API; es que runtime-async está lo suficientemente maduro para usarse con la propia BCL, lo cual es una señal significativa sobre la preparación de la característica.

## Optimizaciones del JIT e Intrínsecos de Hardware

Preview 4 continúa el trabajo del JIT. Aquí se publican mejoras en los intrínsecos de hardware y en la generación de código — los detalles están en las notas de la versión del runtime. Este tipo de cambios suelen mejorar el rendimiento en bucles de cálculo intensivo sin necesidad de modificar tu código.

## Expansión de la API de Procesos

Preview 4 incluye una actualización importante a `System.Diagnostics.Process`:

- `Process.RunAndCaptureTextAsync` — inicia un proceso, captura stdout/stderr, espera la salida, todo en una sola llamada sin riesgo de deadlock
- `KillOnParentExit` — acoplamiento ligero del ciclo de vida entre procesos padre e hijo
- APIs basadas en `SafeProcessHandle` más amigables con el trimmer

Si alguna vez has escrito código repetitivo para capturar la salida de un proceso sin provocar deadlocks (lectura async de stdout *y* stderr simultáneamente), `RunAndCaptureTextAsync` es la API que te faltaba.

## dotnet watch para Android e iOS

`dotnet watch` ahora admite la selección de dispositivo para proyectos .NET MAUI en Android e iOS. Iteración más rápida en móvil sin gestionar manualmente las conexiones de dispositivos en el bucle de compilación.

## APIs de Compresión Basadas en Span

En las bibliotecas llegan nuevas APIs de codificación/decodificación Deflate, ZLib y GZip basadas en span. Menos asignaciones al tratar con datos comprimidos, relevante si realizas procesamiento de datos de alto rendimiento.

## Pruébalo

[Descargar .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — es una preview, no apta para producción, pero vale la pena ejecutarla contra tus proyectos para detectar problemas antes del ciclo de RC.

Post original: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
