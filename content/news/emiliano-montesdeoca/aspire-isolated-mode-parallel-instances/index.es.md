---
title: "El Modo Aislado de Aspire Resuelve la Pesadilla de Conflictos de Puertos en Desarrollo Paralelo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduce el modo --isolated: puertos aleatorios, secretos separados y cero colisiones al ejecutar múltiples instancias del mismo AppHost. Perfecto para agentes de IA, worktrees y flujos de trabajo paralelos."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Si alguna vez intentaste ejecutar dos instancias del mismo proyecto al mismo tiempo, conoces el dolor. El puerto 8080 ya está en uso. El puerto 17370 está ocupado. Mata algo, reinicia, malabarea variables de entorno — es un asesino de productividad.

Este problema está empeorando, no mejorando. Los agentes de IA crean git worktrees para trabajar de forma independiente. Los agentes en segundo plano levantan entornos separados. Los desarrolladores hacen checkout del mismo repo dos veces para ramas de funcionalidades. Cada uno de estos escenarios choca con la misma pared: dos instancias de la misma app peleando por los mismos puertos.

Aspire 13.2 resuelve esto con un solo flag. James Newton-King del equipo de Aspire [escribió todos los detalles](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), y es una de esas funcionalidades de "¿por qué no teníamos esto antes?"

## La solución: `--isolated`

```bash
aspire run --isolated
```

Eso es todo. Cada ejecución obtiene:

- **Puertos aleatorios** — no más colisiones entre instancias
- **Secretos de usuario aislados** — cadenas de conexión y claves API permanecen separados por instancia

Sin reasignación manual de puertos. Sin malabarismo de variables de entorno. Cada ejecución obtiene un entorno limpio y libre de colisiones automáticamente.

## Escenarios reales donde esto brilla

**Múltiples checkouts.** Tienes una rama de funcionalidad en un directorio y un bugfix en otro:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Ambos se ejecutan sin conflictos. El dashboard muestra qué está corriendo y dónde.

**Agentes en segundo plano en VS Code.** Cuando el agente en background de Copilot Chat crea un git worktree para trabajar en tu código de forma independiente, puede necesitar ejecutar tu AppHost de Aspire. Sin `--isolated`, eso es una colisión de puertos con tu worktree principal. Con él, ambas instancias simplemente funcionan.

El skill de Aspire que viene con `aspire agent init` instruye automáticamente a los agentes a usar `--isolated` cuando trabajan en worktrees. Así que el agente en background de Copilot debería manejar esto de forma nativa.

**Tests de integración junto al desarrollo.** ¿Necesitas ejecutar tests contra un AppHost en vivo mientras sigues construyendo funcionalidades? El modo aislado le da a cada contexto sus propios puertos y configuración.

## Cómo funciona internamente

Cuando pasas `--isolated`, el CLI genera un ID de instancia único para la ejecución. Esto impulsa dos comportamientos:

1. **Aleatorización de puertos** — en vez de vincularse a puertos predecibles definidos en la configuración de tu AppHost, el modo aislado elige puertos aleatorios disponibles para todo — el dashboard, los endpoints de servicio, todo. El service discovery se ajusta automáticamente, así que los servicios se encuentran entre sí sin importar qué puertos les tocaron.

2. **Aislamiento de secretos** — cada ejecución aislada obtiene su propio almacén de secretos de usuario, identificado por el ID de instancia. Las cadenas de conexión y claves API de una ejecución no se filtran a otra.

Tu código no necesita cambios. El service discovery de Aspire resuelve los endpoints en tiempo de ejecución, así que todo se conecta correctamente sin importar la asignación de puertos.

## Cuándo usarlo

Usa `--isolated` cuando ejecutes múltiples instancias del mismo AppHost simultáneamente — ya sea desarrollo paralelo, tests automatizados, agentes de IA o git worktrees. Para desarrollo de instancia única donde prefieras puertos predecibles, el `aspire run` regular sigue funcionando bien.

## Para cerrar

El modo aislado es una funcionalidad pequeña que resuelve un problema real y cada vez más común. A medida que el desarrollo asistido por IA nos empuja hacia más flujos paralelos — múltiples agentes, múltiples worktrees, múltiples contextos — la capacidad de simplemente levantar otra instancia sin pelear por puertos es esencial.

Lee el [post completo](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) para todos los detalles técnicos y pruébalo con `aspire update --self` para obtener la 13.2.
