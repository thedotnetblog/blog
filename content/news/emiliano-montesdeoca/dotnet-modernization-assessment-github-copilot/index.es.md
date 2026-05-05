---
title: "La evaluación de modernización de GitHub Copilot es la mejor herramienta de migración que aún no estás usando"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La extensión de modernización de GitHub Copilot no solo sugiere cambios de código — produce una evaluación completa de migración con issues accionables, comparaciones de destinos Azure y un flujo de trabajo colaborativo. Aquí te explico por qué el documento de evaluación es la clave de todo."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}}).*

Migrar una aplicación legacy de .NET Framework a .NET moderno es una de esas tareas que todos saben que deberían hacer pero nadie quiere empezar. Nunca es solo "cambiar el target framework." Son APIs que desaparecieron, paquetes que ya no existen, modelos de hosting que funcionan completamente diferente, y un millón de pequeñas decisiones sobre qué containerizar, qué reescribir y qué dejar como está.

Jeffrey Fritz acaba de publicar una [inmersión profunda en la evaluación de modernización de GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), y honestamente, es el mejor tooling de migración que he visto para .NET. No por la generación de código — eso ya es estándar. Por el documento de evaluación que produce.

## No es solo un motor de sugerencias de código

La extensión de VS Code sigue un modelo de **Evaluar → Planificar → Ejecutar**. La fase de evaluación analiza todo tu código base y produce un documento estructurado que captura todo: qué necesita cambiar, qué recursos de Azure aprovisionar, qué modelo de despliegue usar. Todo lo posterior — infraestructura como código, containerización, manifiestos de despliegue — fluye de lo que la evaluación encuentra.

La evaluación se almacena en `.github/modernize/assessment/` en tu proyecto. Cada ejecución produce un reporte independiente, así que acumulas un historial y puedes rastrear cómo evoluciona tu postura de migración a medida que corriges issues.

## Dos formas de empezar

**Evaluación Recomendada** — el camino rápido. Elige entre dominios curados (Actualización Java/.NET, Cloud Readiness, Seguridad) y obtén resultados significativos sin tocar configuración. Genial para una primera mirada a dónde está tu aplicación.

**Evaluación Personalizada** — el camino dirigido. Configura exactamente qué analizar: cómputo objetivo (App Service, AKS, Container Apps), SO objetivo, análisis de containerización. Elige múltiples destinos Azure para comparar enfoques de migración lado a lado.

Esa vista de comparación es genuinamente útil. Una app con 3 issues obligatorios para App Service podría tener 7 para AKS. Ver ambos ayuda a decidir el hosting antes de comprometerse con un camino de migración.

## El desglose de issues es accionable

Cada issue viene con un nivel de criticidad:

- **Obligatorio** — debe corregirse o la migración falla
- **Potencial** — podría impactar la migración, necesita juicio humano
- **Opcional** — mejoras recomendadas, no bloquean la migración

Y cada issue enlaza a archivos afectados y números de línea, proporciona una descripción detallada de qué está mal y por qué importa para tu plataforma objetivo, da pasos concretos de remediación (no solo "arregla esto"), e incluye enlaces a documentación oficial.

Puedes asignar issues individuales a desarrolladores y tienen todo lo que necesitan para actuar. Esa es la diferencia entre una herramienta que te dice "hay un problema" y una que te dice cómo resolverlo.

## Las rutas de actualización cubiertas

Para .NET específicamente:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Cada ruta de actualización tiene reglas de detección que saben qué APIs fueron eliminadas, qué patrones no tienen equivalente directo, y qué issues de seguridad necesitan atención.

Para equipos que gestionan múltiples aplicaciones, también hay un CLI que soporta evaluaciones batch multi-repo — clona todos los repos, evalúalos todos, obtén reportes por app más una vista de portafolio agregada.

## Mi opinión

Si estás sentado sobre aplicaciones legacy de .NET Framework (y seamos honestos, la mayoría de los equipos empresariales lo están), esta es *la* herramienta con la que empezar. Solo el documento de evaluación vale el tiempo — convierte un vago "deberíamos modernizar" en una lista concreta y priorizada de elementos de trabajo con caminos claros hacia adelante.

El flujo de trabajo colaborativo también es inteligente: exporta evaluaciones, compártelas con tu equipo, impórtalas sin re-ejecutar. ¿Revisiones de arquitectura donde los que toman decisiones no son los que ejecutan las herramientas? Cubierto.

## Para cerrar

La evaluación de modernización de GitHub Copilot transforma la migración de .NET de un proyecto aterrador e indefinido en un proceso estructurado y rastreable. Empieza con una evaluación recomendada para ver dónde estás, luego usa evaluaciones personalizadas para comparar destinos Azure y construir tu plan de migración.

Lee el [walkthrough completo](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) y descarga la [extensión de VS Code](https://aka.ms/ghcp-appmod/vscode-ext) para probarlo en tu propio código.
