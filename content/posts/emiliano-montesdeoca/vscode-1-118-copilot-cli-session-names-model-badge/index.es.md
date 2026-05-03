---
title: "VS Code 1.118: Copilot CLI Obtiene Nombres de Sesión, Insignias de Modelo y TypeScript 7.0 Nightly"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Visual Studio Code 1.118 es un lanzamiento enfocado en mejoras de Copilot CLI — nombrado de sesiones, insignias de modelo, selección automática de modelo y opt-in a TypeScript 7.0 nightly."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
  - TypeScript
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Visual Studio Code 1.118](https://code.visualstudio.com/updates/v1_118) es un lanzamiento pequeño y enfocado — principalmente refinamientos de Copilot CLI — pero hay algunas cosas a destacar.

## Copilot CLI: las sesiones tienen nombres reales

Las APIs de título de sesión del SDK de Copilot CLI ahora se usan como fuente de verdad para los nombres de sesión. Antes obtenías etiquetas auto-generadas; ahora las sesiones muestran el nombre real del SDK. Mejora de calidad de vida que hace mucho menos confusa la navegación entre múltiples sesiones de agente.

## Cambia de sesión más rápido con atajos de teclado

La app de Agents ahora tiene `Ctrl+1`, `Ctrl+2`, etc. asignados para cambiar rápidamente entre sesiones. Si estás ejecutando múltiples sesiones de Copilot CLI en paralelo, esto elimina mucho clic con el ratón.

## Insignias de modelo en el chat

Las respuestas de Copilot CLI en el panel de chat ahora muestran una insignia de modelo — puedes ver de un vistazo qué modelo manejó cada solicitud.

## Selección automática de modelo en Copilot CLI

La selección automática de modelo — previamente disponible en otras partes de Copilot — ahora funciona también en el agente Copilot CLI.

## Opt-in a TypeScript 7.0 nightly

Ahora puedes optar por probar los nightly de TypeScript 7.0 directamente desde la configuración de VS Code. TypeScript 7.0 es un lanzamiento importante (la [beta llegó hace unos días](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)), y el path de opt-in facilita la prueba sin cambiar tu instalación global de TypeScript.

## Bajo el capó: limpieza de `node-pty`

El SDK de Copilot CLI ahora resuelve `node-pty` desde VS Code via `hostRequire` en lugar de copiar binarios a la carpeta prebuilds del SDK. Cambio interno que simplifica la distribución.

Consulta las [notas de versión completas](https://code.visualstudio.com/updates/v1_118).
