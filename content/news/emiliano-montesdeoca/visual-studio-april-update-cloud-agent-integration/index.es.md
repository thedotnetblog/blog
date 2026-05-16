---
title: "Actualización de abril de Visual Studio 2026: agente en la nube, agentes personalizados y agente depurador"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "La actualización de abril de Visual Studio 2026 (18.5) trae integración de agente en la nube, agentes personalizados a nivel de usuario, herramientas C++ en GA y un Agente Depurador que valida correcciones contra el comportamiento real en tiempo de ejecución."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[La actualización de abril de Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) incluye integración de agente en la nube, agentes personalizados a nivel de usuario, herramientas C++ que llegan a GA y un nuevo Agente Depurador.

## Agente en la nube: delegar trabajo a una sesión remota de Copilot

Desde el selector de agentes en la ventana Chat, seleccionar **Cloud** permite delegar una tarea a un agente de codificación remoto de Copilot. Describes el trabajo, el agente crea un issue en GitHub en tu repositorio y abre un PR cuando termina. Recibes una notificación con "View PR" / "Open in browser" — todo funciona mientras sigues codificando, o incluso con el IDE cerrado.

## Los agentes personalizados ahora te acompañan

Los agentes personalizados a nivel de usuario almacenados en `%USERPROFILE%/.github/agents/` ya no están limitados al repositorio — te siguen a través de los proyectos. La ruta de almacenamiento es configurable en Tools > Options > GitHub > Copilot > Chat. El botón `+` en el selector de agentes permite crear nuevos agentes directamente. Obtienen las mismas capacidades: conciencia del espacio de trabajo, herramientas, selección de modelo y conexiones MCP.

Agentes integrados: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Las herramientas de edición de código C++ llegan a GA

Dos herramientas — `get_symbol_call_hierarchy` y `get_symbol_class_hierarchy` — están ahora activadas por defecto. Proporcionan a Copilot navegación consciente del lenguaje en bases de código C++, cubriendo jerarquías de herencia y cadenas de llamadas de funciones. Activa mediante el icono Tools en Copilot Chat. Funciona mejor con modelos de llamada de herramientas.

## Agente Depurador: correcciones validadas contra el comportamiento real en tiempo de ejecución

Comienza desde un issue de GitHub o Azure DevOps (o una descripción en lenguaje natural), cambia al modo Debugger, y el agente:

1. Crea un reproductor mínimo
2. Genera hipótesis de fallo
3. Instrumenta la aplicación con tracepoints y breakpoints condicionales
4. Ejecuta una sesión de depuración real
5. Analiza telemetría en vivo
6. Sugiere una corrección precisa

Te mantienes en el bucle durante todo el proceso — es interactivo, no completamente autónomo.

## Corrección de prioridad de IntelliSense

VS ahora suprime las completaciones de Copilot mientras la lista de IntelliSense está activa. Un solo sugerencia a la vez. Era un punto de fricción frecuente y ahora está activado por defecto.

Notas de lanzamiento completas y descarga en [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
