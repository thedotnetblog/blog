---
title: "VS Code 1.119: OpenTelemetry para sesiones de agentes, integración del navegador y seguridad"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (mayo 2026) añade trazado OpenTelemetry para sesiones de agentes, compartición de pestañas del navegador, mejoras de confianza y seguridad, y un parche de seguridad 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) salió el 6 de mayo de 2026 (con un parche de seguridad 1.119.1 poco después). La versión se centra en la observabilidad de los agentes, la interacción con el navegador y la reducción de interrupciones.

## Trazado OpenTelemetry para sesiones de agentes

Esta es la característica destacada para cualquiera que ejecute agentes en producción o depure flujos de trabajo agénticos. Actívala con dos configuraciones:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Las trazas siguen las convenciones semánticas de GenAI. Cada solicitud de agente produce un span raíz `invoke_agent` con spans hijo anidados: `chat`, `execute_tool` y `execute_hook`. El uso de tokens se reporta por solicitud — incluyendo recuentos de lectura y creación de caché.

Funciona con el agente local, el agente de fondo de Copilot CLI y el agente de Claude. Cualquier backend compatible con OTLP acepta las trazas — el [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) funciona bien para el desarrollo local.

## Los agentes ahora pueden acceder a las pestañas del navegador

Los agentes pueden solicitar acceso a las pestañas de tu navegador integrado — pero no es automático. Debes compartir explícitamente una pestaña mediante el selector de contexto, arrastrar y soltar, o contexto sugerido. Hay un botón de compartición en el navegador para revocar el acceso. Cuando un agente intenta abrir una nueva pestaña en el mismo dominio que una pestaña abierta (no compartida), VS Code te pide que reutilices la pestaña existente.

## Uso optimizado de tokens

Un modelo ligero experimental ahora gestiona las listas de tareas de los agentes, manteniendo ese trabajo administrativo fuera del modelo principal más caro. Reduce el consumo de tokens para tareas que no necesitan capacidad de razonamiento completa.

## Confianza y seguridad

Menos interrupciones: VS Code 1.119 reduce las solicitudes de acceso a la red y escrituras en carpetas temporales por parte de los agentes. El parche 1.119.1 aborda problemas de seguridad específicos — vale la pena actualizar si aún no lo has hecho.

## Cambio rápido a vista previa de Markdown

Pequeño pero útil: ahora puedes cambiar rápidamente el editor actual a la vista previa de Markdown sin navegar.

## VS Code Agents (vista previa Insiders)

La interfaz de sesión de agentes rediseñada — nuevo selector de repositorios (local/repos/remoto), mejoras de subsesiones, pulido web y móvil, animaciones de progreso — está disponible en Insiders en [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Registro de cambios completo: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
