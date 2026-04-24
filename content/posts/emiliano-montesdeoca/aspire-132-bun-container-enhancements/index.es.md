---
title: "Aspire 13.2: Soporte para Bun, Mejores Contenedores y Menos Fricción en el Debug"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 añade soporte de primera clase para Bun en apps Vite, corrige la fiabilidad de Yarn y trae mejoras en contenedores que hacen el comportamiento local más predecible."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Si llevas tiempo construyendo backends .NET con frontends JavaScript en Aspire, la versión 13.2 es el tipo de actualización que mejora tu día sin anunciar grandes cambios. Sin nuevos paradigmas llamativos. Solo mejoras sólidas a cosas que eran levemente molestas.

## Bun es Ahora Ciudadano de Primera Clase

La característica principal: soporte para Bun en apps Vite. Una llamada fluida, listo.

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Si tu equipo ya usa Bun — con sus tiempos de instalación dramáticamente más rápidos — Aspire ya no te hace pelear contra la corriente.

## Yarn es Más Confiable

Los usuarios de Yarn reciben algo igualmente importante: menos fallos misteriosos. Aspire 13.2 mejora la fiabilidad de `withYarn()` con `addViteApp()`.

## Mejoras en Contenedores

### Pull Policy Explícita

```typescript
const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);
```

Perfecto para flujos donde construyes imágenes localmente y quieres que Compose use exactamente esa sin ir al registry.

### PostgreSQL 18+ Funciona Correctamente

PostgreSQL 18 cambió su estructura interna de directorios, lo que rompía silenciosamente el mapeo de volúmenes. Aspire 13.2 lo corrige.

## Mejoras de Depuración

- `DebuggerDisplayAttribute` en tipos core — valores útiles en el debugger en lugar de árboles de objetos
- Mensajes de error más claros para `WaitFor`
- `BeforeResourceStartedEvent` se dispara en el momento correcto

## Resumiendo

Aspire 13.2 es una versión de calidad enfocada. Vale la pena actualizar, especialmente si usas PostgreSQL 18 con volúmenes de datos.

Post original de David Pine: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
