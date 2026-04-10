---
title: "VS Code 1.116 — La App de Agentes Obtiene Navegación por Teclado y Autocompletado de Contexto de Archivos"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 se enfoca en pulir la app de Agentes — atajos de teclado dedicados, mejoras de accesibilidad, autocompletado de contexto de archivos y resolución de enlaces CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "vscode-1-116-agents-app-updates.md" >}}).*

VS Code 1.116 es la versión de abril de 2026, y aunque es más ligera que algunas actualizaciones recientes, los cambios son enfocados y significativos — especialmente si estás usando la app de Agentes a diario.

Esto es lo que llegó, basado en las [notas de la versión oficial](https://code.visualstudio.com/updates/v1_116).

## Mejoras en la app de Agentes

La app de Agentes sigue madurando con pulido de usabilidad que marca una diferencia real en los flujos de trabajo diarios:

**Atajos de teclado dedicados** — ahora puedes enfocar la vista de Cambios, el árbol de archivos dentro de Cambios, y la vista de Personalizaciones del Chat con comandos dedicados y atajos de teclado. Si has estado haciendo clic por toda la app de Agentes para navegar, esto trae flujos de trabajo completamente controlados por teclado.

**Diálogo de ayuda de accesibilidad** — presionar `Alt+F1` en el cuadro de entrada del chat ahora abre un diálogo de ayuda de accesibilidad que muestra los comandos y atajos disponibles. Los usuarios de lectores de pantalla también pueden controlar la verbosidad de los anuncios. La buena accesibilidad beneficia a todos.

**Autocompletado de contexto de archivos** — escribe `#` en el chat de la app de Agentes para activar el autocompletado de contexto de archivos dentro de tu espacio de trabajo actual. Esta es una de esas pequeñas mejoras de calidad de vida que aceleran cada interacción — no más escribir rutas completas de archivos al referenciar código.

## Resolución de enlaces CSS `@import`

Una buena para los desarrolladores frontend: VS Code ahora resuelve las referencias CSS `@import` que usan rutas de node_modules. Puedes hacer `Ctrl+clic` a través de imports como `@import "some-module/style.css"` cuando usas bundlers. Pequeño pero elimina un punto de fricción en los flujos de trabajo CSS.

## Conclusión

VS Code 1.116 trata sobre refinamiento — hacer la app de Agentes más navegable, más accesible y más amigable con el teclado. Si pasas tiempo significativo en la app de Agentes (y sospecho que muchos de nosotros lo hacemos), estos cambios se acumulan.

Revisa las [notas de la versión completas](https://code.visualstudio.com/updates/v1_116) para la lista completa.
