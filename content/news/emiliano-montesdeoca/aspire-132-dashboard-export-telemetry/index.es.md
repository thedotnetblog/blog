---
title: "El Dashboard de Aspire 13.2 ahora tiene una API de telemetría — y lo cambia todo"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 trae exportación inteligente de telemetría, una API programática para trazas y logs, y mejoras en la visualización de GenAI. Te cuento por qué importa para tu flujo de depuración."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "aspire-132-dashboard-export-telemetry.md" >}}).*

Si has estado construyendo aplicaciones distribuidas con .NET Aspire, ya sabes que el dashboard es lo mejor de toda la experiencia. Todas tus trazas, logs y métricas en un solo lugar — sin Jaeger externo, sin configuración de Seq, sin momentos de "déjame revisar la otra terminal".

Aspire 13.2 acaba de mejorar todo significativamente. James Newton-King [anunció la actualización](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), y honestamente, las funciones de exportación de telemetría y la API por sí solas justifican la actualización.

## Exportar telemetría como una persona normal

Este es el escenario que todos hemos vivido: estás depurando un problema distribuido, finalmente lo reproduces después de veinte minutos de configuración, y ahora necesitas compartir lo que pasó con tu equipo. ¿Antes? Capturas de pantalla. Copiar y pegar IDs de trazas. El desastre de siempre.

Aspire 13.2 añade un diálogo de **Gestión de logs y telemetría** donde puedes:

- Limpiar toda la telemetría (útil antes de reproducir un bug)
- Exportar telemetría seleccionada a un archivo ZIP en formato estándar OTLP/JSON
- Re-importar ese ZIP en cualquier dashboard de Aspire después

Esa última parte es la función estrella. Reproduces un bug, exportas la telemetría, la adjuntas a tu work item, y tu compañero puede importarla en su propio dashboard para ver exactamente lo que tú viste. No más "¿puedes reproducirlo en tu máquina?"

Las trazas, spans y logs individuales también tienen una opción "Export JSON" en sus menús contextuales. ¿Necesitas compartir una traza específica? Clic derecho, copiar JSON, pegar en la descripción de tu PR. Listo.

## La API de telemetría es el verdadero cambio de juego

Esto es lo que más me emociona. El dashboard ahora expone una API HTTP bajo `/api/telemetry` para consultar datos de telemetría programáticamente. Endpoints disponibles:

- `GET /api/telemetry/resources` — listar recursos con telemetría
- `GET /api/telemetry/spans` — consultar spans con filtros
- `GET /api/telemetry/logs` — consultar logs con filtros
- `GET /api/telemetry/traces` — listar trazas
- `GET /api/telemetry/traces/{traceId}` — obtener todos los spans de una traza

Todo vuelve en formato OTLP JSON. Esto potencia los nuevos comandos `aspire agent mcp` y `aspire otel` del CLI, pero la implicación real es mayor: ahora puedes construir herramientas, scripts e integraciones con agentes IA que consulten la telemetría de tu app directamente.

Imagina un agente de IA que pueda ver tus trazas distribuidas reales mientras depuras. Eso ya no es hipotético — es lo que esta API permite.

## La telemetría de GenAI se vuelve práctica

Si estás construyendo apps con IA usando Semantic Kernel o Microsoft.Extensions.AI, apreciarás el visualizador de telemetría GenAI mejorado. Aspire 13.2 añade:

- Descripciones de herramientas IA renderizadas como Markdown
- Un botón dedicado de GenAI en la página de trazas para acceso rápido
- Mejor manejo de errores para JSON de GenAI truncado o no estándar
- Navegación click-to-highlight entre definiciones de herramientas

El post menciona que VS Code Copilot chat, Copilot CLI y OpenCode soportan configurar un `OTEL_EXPORTER_OTLP_ENDPOINT`. Apúntalos al dashboard de Aspire y literalmente puedes ver a tus agentes IA pensar en tiempo real a través de la telemetría. Esa es una experiencia de depuración que no encontrarás en ningún otro lado.

## Para cerrar

Aspire 13.2 transforma el dashboard de "bonita UI de depuración" a "plataforma de observabilidad programable". El flujo de exportación/importación por sí solo ahorra tiempo real en depuración distribuida, y la API de telemetría abre la puerta al diagnóstico asistido por IA.

Si ya estás en Aspire, actualiza. Si no — esta es una buena razón para echarle un vistazo a [aspire.dev](https://aspire.dev).
