---
title: "Revisar pull requests dentro de Visual Studio es exactamente el tipo de reducción de fricción que me gusta"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio ahora puede revisar pull requests de principio a fin sin salir del IDE. Puede sonar incremental, pero para los equipos que viven todo el día dentro de Visual Studio, elimina mucho cambio de contexto innecesario."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *Esta publicación se ha traducido automáticamente. Lee el original [aquí]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}}).* 

El navegador ha estado robando demasiada parte del flujo de trabajo de code review durante demasiado tiempo.

Por eso me alegra mucho ver a Visual Studio avanzar más hacia la **revisión de pull requests de principio a fin dentro del IDE**.

Esta es una de esas funciones que quizá no genere grandes titulares, pero que puede mejorar muchísimo el desarrollo diario.

## El valor principal es simple: menos cambio de contexto

Cuando tu bucle de revisión vive en parte dentro del IDE y en parte en el navegador, la fricción se acumula:

- abrir el PR en otro lugar
- inspeccionar los cambios en una herramienta
- volver a la solución para investigar más a fondo
- cambiar otra vez para comentar o aprobar

No es catastrófico. Solo es ineficiente.

Si Visual Studio te permite abrir, inspeccionar, comentar, aprobar y hacer merge desde el mismo entorno de trabajo, eso sí es una ganancia real de productividad.

## La opción de "review sin checkout" es especialmente buena

Una parte que me gusta especialmente es poder revisar sin hacer checkout de la rama del PR.

Puede sonar pequeño, pero es perfecto para:

- pasadas rápidas de review
- solicitudes de feedback interrumpidas
- mantener intactos tu rama actual y tu estado local

Eso es exactamente el tipo de flexibilidad que necesitan las buenas herramientas de code review.

## Mi opinión

Esto no es una función revolucionaria.

Es algo mejor: algo práctico.

Para los equipos que pasan la mayor parte del día en Visual Studio, un soporte más estrecho para revisar PR significa menos interrupciones del flujo de trabajo y un camino más fluido desde la inspección hasta la acción.

En mi opinión, es una mejora que vale la pena.

Publicación original: [Revisa pull requests sin salir de Visual Studio](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)