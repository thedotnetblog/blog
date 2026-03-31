---
title: "La actualización de marzo de Visual Studio te permite crear agentes Copilot personalizados — y find_symbol es clave"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "La actualización de marzo 2026 de Visual Studio trae agentes Copilot personalizados, skills reutilizables, la herramienta find_symbol con reconocimiento de lenguaje, y profiling con Copilot desde Test Explorer."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}}).*

Visual Studio acaba de recibir su actualización de Copilot más significativa hasta ahora. Mark Downie [anunció la versión de marzo](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), y el titular son los agentes personalizados — pero honestamente, la herramienta `find_symbol` podría ser la función que más cambie tu flujo de trabajo.

## Agentes Copilot personalizados en tu repo

¿Quieres que Copilot siga los estándares de código de tu equipo, ejecute tu pipeline de build, o consulte tus docs internos? Ahora puedes construir exactamente eso.

Los agentes personalizados se definen como archivos `.agent.md` que colocas en `.github/agents/` en tu repositorio. Cada agente tiene acceso completo al workspace, comprensión del código, herramientas, tu modelo preferido, y conexiones MCP a servicios externos.

## Agent skills: paquetes de instrucciones reutilizables

Los skills se cargan automáticamente desde `.github/skills/` en tu repo o `~/.copilot/skills/` en tu perfil. Piensa en los skills como experiencia modular que puedes mezclar y combinar.

## find_symbol: navegación con reconocimiento de lenguaje

La nueva herramienta `find_symbol` le da al modo agente de Copilot navegación de símbolos basada en servicios de lenguaje. En lugar de buscar texto, el agente puede encontrar todas las referencias a un símbolo, acceder a información de tipos, declaraciones y alcance.

Para desarrolladores .NET, esto es una mejora enorme — las bases de código C# con jerarquías de tipos profundas e interfaces se benefician enormemente.

## Perfilar tests con Copilot

Hay un nuevo comando **Profile with Copilot** en el menú contextual del Test Explorer. Selecciona un test, haz clic en perfilar, y el Profiling Agent lo ejecuta y analiza automáticamente.

## Perf tips durante debugging en vivo

La optimización de rendimiento ahora ocurre mientras depuras. Visual Studio muestra tiempo de ejecución y señales de rendimiento inline. ¿Ves una línea lenta? Haz clic en el Perf Tip y pídele a Copilot sugerencias de optimización.

## Corregir vulnerabilidades de NuGet desde Solution Explorer

Cuando se detecta una vulnerabilidad en un paquete NuGet, verás un enlace **Fix with GitHub Copilot** directamente en Solution Explorer.

## Para cerrar

Agentes personalizados y skills son el titular, pero `find_symbol` es la joya oculta — cambia fundamentalmente la precisión de Copilot al refactorizar código .NET. Combinado con profiling en vivo y corrección de vulnerabilidades, esta actualización hace que las funciones de IA de Visual Studio se sientan genuinamente prácticas.

Descarga [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) para probarlo todo.
