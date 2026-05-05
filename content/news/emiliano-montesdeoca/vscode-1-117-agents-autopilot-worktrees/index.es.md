---
title: "VS Code 1.117: Los Agentes Están Obteniendo Sus Propias Ramas de Git y Estoy Totalmente a Favor"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 trae aislamiento con worktrees para sesiones de agentes, modo Autopilot persistente y soporte para subagentes. El flujo de trabajo con agentes de código se puso mucho más serio."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

La línea entre "asistente de IA" y "compañero de equipo de IA" sigue haciéndose más delgada. VS Code 1.117 acaba de salir y las [notas de la versión completas](https://code.visualstudio.com/updates/v1_117) están cargadas, pero la historia está clara: los agentes se están convirtiendo en ciudadanos de primera clase en tu flujo de trabajo de desarrollo.

Esto es lo que realmente importa.

## El modo Autopilot finalmente recuerda tu preferencia

Antes, tenías que volver a activar Autopilot cada vez que iniciabas una nueva sesión. Molesto. Ahora tu modo de permisos persiste entre sesiones y puedes configurar el valor por defecto.

El Agent Host soporta tres configuraciones de sesión:

- **Default** — las herramientas piden confirmación antes de ejecutarse
- **Bypass** — aprueba todo automáticamente
- **Autopilot** — totalmente autónomo, responde sus propias preguntas y sigue adelante

Si estás creando un nuevo proyecto .NET con migraciones, Docker y CI — configúralo en Autopilot una vez y olvídate. Esa preferencia se mantiene.

## Worktree y aislamiento de git para sesiones de agentes

Esta es la grande. Las sesiones de agentes ahora soportan aislamiento completo con worktrees y git. Eso significa que cuando un agente trabaja en una tarea, obtiene su propia rama y directorio de trabajo. Tu rama principal queda intacta.

Mejor aún — Copilot CLI genera nombres de rama significativos para estas sesiones de worktree. Se acabó el `agent-session-abc123`. Obtienes algo que realmente describe lo que el agente está haciendo.

Para desarrolladores .NET que manejan múltiples ramas de features o corrigen bugs mientras una tarea larga de scaffolding corre, esto es un cambio total. Puedes tener un agente construyendo tus controladores de API en un worktree mientras tú depuras un problema en la capa de servicios en otro. Sin conflictos. Sin stashing. Sin desorden.

## Subagentes y equipos de agentes

El Agent Host Protocol ahora soporta subagentes. Un agente puede lanzar otros agentes para manejar partes de una tarea. Piénsalo como delegar — tu agente principal coordina, y agentes especializados se encargan de las piezas.

Esto es temprano, pero el potencial para flujos de trabajo .NET es obvio. Imagina un agente manejando tus migraciones de EF Core mientras otro configura tus pruebas de integración. No estamos totalmente ahí todavía, pero que el soporte del protocolo aterrice ahora significa que las herramientas vendrán rápido.

## La salida del terminal se incluye automáticamente cuando los agentes envían input

Pequeño pero significativo. Cuando un agente envía input al terminal, la salida del terminal ahora se incluye automáticamente en el contexto. Antes, el agente tenía que hacer un turno extra solo para leer lo que pasó.

Si alguna vez viste a un agente ejecutar `dotnet build`, fallar, y luego tomar otro viaje de ida y vuelta solo para ver el error — esa fricción desapareció. Ve la salida inmediatamente y reacciona.

## La app de Agents en macOS se auto-actualiza

La app independiente de Agents en macOS ahora se auto-actualiza. No más descargas manuales de nuevas versiones. Simplemente se mantiene al día.

## Las cosas más pequeñas que vale la pena saber

- Los **hovers de package.json** ahora muestran tanto la versión instalada como la última disponible. Útil si manejas herramientas npm junto con tus proyectos .NET.
- Las **imágenes en comentarios JSDoc** se renderizan correctamente en hovers y completados.
- Las **sesiones de Copilot CLI** ahora indican si fueron creadas por VS Code o externamente — práctico cuando saltas entre terminales.
- **Copilot CLI, Claude Code y Gemini CLI** son reconocidos como tipos de shell. El editor sabe lo que estás ejecutando.

## La conclusión

VS Code 1.117 no es un volcado de features llamativas. Es infraestructura. Aislamiento con worktrees, permisos persistentes, protocolos de subagentes — estos son los bloques de construcción para un flujo de trabajo donde los agentes manejan tareas reales y paralelas sin pisar tu código.

Si estás construyendo con .NET y todavía no te has metido en el flujo de trabajo con agentes, honestamente, ahora es el momento de empezar.
