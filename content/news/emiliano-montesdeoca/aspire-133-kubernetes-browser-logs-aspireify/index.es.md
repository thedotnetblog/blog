---
title: "Aspire 13.3: Soporte de Kubernetes, Registros del Navegador y la Habilidad Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Cinco semanas después del 13.2, Aspire 13.3 llega con 45 nuevas características incluyendo despliegue AKS de primera clase, una habilidad de incorporación asistida por IA, captura de registros del navegador y resultados de comandos estructurados."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Cinco semanas no es mucho tiempo para una versión, pero Aspire 13.3 no lo parece. Los elementos principales son significativos: despliegue de Kubernetes y AKS de primera clase con Helm, una habilidad de incorporación asistida por agente llamada Aspireify, captura de registros del navegador directamente en el dashboard y resultados de comandos estructurados. Además, 45 nuevas características, 134 mejoras y 93 correcciones de errores.

Vamos a los puntos destacados.

## Aspireify: Incorporación Asistida por Agente

Agregar Aspire a un proyecto existente suena simple — coloca un AppHost, listo. En la práctica implica mucha arqueología: qué puertos importan, qué variables de entorno son dependencias reales, qué servicios de Docker Compose deben mapearse a integraciones de Aspire.

La nueva **habilidad Aspireify** le da a tu agente de código un flujo de trabajo guiado exactamente para esto. Cuando `aspire init` crea un AppHost esqueleto, la habilidad Aspireify ayuda al agente a inspeccionar el repositorio, entender cómo ya funciona y conectar el AppHost para adaptarse a la aplicación — no al revés.

La postura predeterminada es "minimizar los cambios en tu código." Si tu aplicación ya lee `DATABASE_URL`, el agente lo mapea con `WithEnvironment()` en lugar de pedirte que reescribas tu configuración. Si un puerto está codificado de forma fija, la habilidad le indica al agente cuándo preservarlo.

Este es el tipo de herramientas de IA que realmente ahorran tiempo en lugar de generar más trabajo por revisar.

## Despliegue de Kubernetes y AKS de Primera Clase

Esta es una que ha estado en la lista de deseos durante un tiempo. Aspire 13.3 incluye **soporte de despliegue de Kubernetes y AKS de primera clase con Helm**. Ahora puedes apuntar a AKS como destino de despliegue directamente desde las herramientas de Aspire.

Para los equipos que ya ejecutan cargas de trabajo de producción en AKS, esto cierra una brecha significativa. Tu modelo de aplicación de Aspire ahora tiene un camino limpio desde el desarrollo local hasta Kubernetes sin necesidad de escribir manualmente gráficos Helm.

## Registros del Navegador en el Dashboard

Esta es una de esas características que parecen pequeñas hasta que estás depurando un problema de frontend.

La nueva API `WithBrowserLogs()` adjunta un recurso de navegador rastreado a cualquier recurso capaz de endpoints. Aspire lanza Chromium usando un pipe CDP privado y transmite registros de consola, solicitudes de red y errores directamente al flujo de registros del recurso:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

El AppHost de TypeScript admite lo mismo:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Errores de consola, solicitudes de red fallidas, excepciones del lado del cliente — todo visible en el mismo dashboard donde ya estás observando trazas y métricas. Sin necesidad de cambiar de pestaña a las DevTools del navegador para las cosas básicas.

## Resultados de Comandos Estructurados

Los comandos de recursos recibieron una mejora significativa. Hasta ahora, los comandos devolvían éxito/fracaso. Ahora devuelven resultados estructurados: texto, JSON o markdown que fluye a través del modelo, la interfaz del dashboard, la CLI y las herramientas MCP.

El dashboard une todo esto con un nuevo centro de notificaciones en el encabezado. Los resultados de los comandos aparecen como notificaciones con marca de tiempo con renderización de markdown y una acción "Ver respuesta".

Esto hace que los comandos de recursos sean verdaderamente componibles. Una integración ahora puede exponer un comando que devuelve una salida significativa — como una URL de túnel — en lugar de simplemente cambiar el estado en algún lugar.

## Conclusión

Aspire 13.3 vale la actualización aunque sea solo por el soporte de Kubernetes. Los registros del navegador y los resultados de comandos estructurados parecen el tipo de mejoras de calidad de vida que se acumulan rápidamente en el flujo de trabajo de desarrollo cotidiano.

Notas de versión completas: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
