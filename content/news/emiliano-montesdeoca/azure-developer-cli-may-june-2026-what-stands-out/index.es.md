---
title: "Azure Developer CLI se sigue convirtiendo en una mejor herramienta del inner loop"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Las versiones de mayo y junio de 2026 de Azure Developer CLI añaden mucho, pero el mayor valor está en cómo mejoran el ciclo diario: mejor gestión de herramientas, aprovisionamiento más seguro, mayor soporte para extensiones y flujos de ejecución más prácticos."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Este artículo se tradujo automáticamente. Para ver la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Los grandes resúmenes de CLI pueden ser agotadores de leer porque mezclan mejoras de flujo de trabajo importantes con pequeños arreglos en una sola pared de texto.

Así que aquí va mi versión corta: las últimas actualizaciones de **Azure Developer CLI** importan porque `azd` sigue convirtiéndose en una **mejor herramienta del inner loop**, no solo en un envoltorio de despliegue.

Ese es el cambio importante.

## La gestión de herramientas está pasando a formar parte del producto, no de una tarea secundaria

Una de mis novedades favoritas son los nuevos comandos `azd tool`.

Cualquier cosa que reduzca la fricción de configuración merece atención, especialmente en proyectos donde un entorno funcional depende de una mezcla de SDKs, CLIs, Docker, Bicep y extensiones.

Si ahora la herramienta puede ayudar a descubrir, instalar, comprobar y actualizar esas dependencias directamente, elimina muchos de los modos de fallo molestos que suelen golpear primero a los recién llegados.

Eso sí que es valor real.

## `azd exec` también parece más importante de lo que suena

A primera vista, `azd exec` puede parecer una pequeña comodidad.

Yo no lo veo así.

Ejecutar comandos con todo el contexto del entorno `azd`, incluida la resolución de secretos, es justo el tipo de capacidad que hace que la automatización local y el scripting sean mucho más limpios.

Eso reduce la necesidad de scripts pegamento adicionales y ayuda a mantener la ejecución consistente entre entornos.

Eso es una ganancia práctica.

## El aprovisionamiento más seguro y el mejor comportamiento de cancelación son mejoras infravaloradas

La versión también incluye cambios en dependencias de aprovisionamiento, manejo de cancelación y comportamiento de despliegue, cosas que quizá no se vean glamurosas pero son muy bienvenidas.

Los avisos interactivos de cancelación, un mejor modelado de dependencias y un estado de despliegue más claro son exactamente el tipo de mejoras que hacen que un CLI se sienta fiable cuando trabajas con recursos reales de Azure.

Y la confianza es un tema muy grande para herramientas como esta.

## Mi lectura

Cuanto más mejora `azd` en configuración, scripting, seguridad de despliegue y soporte para extensiones, más se siente como algo que puedes mantener en tu ciclo diario en lugar de tocarlo solo justo antes del despliegue.

Esa es la dirección correcta.

Para los equipos que construyen aplicaciones cloud-native o impulsadas por IA en Azure, esto hace que el CLI sea más útil justo donde más importa: durante el desarrollo real.

Publicación original: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)