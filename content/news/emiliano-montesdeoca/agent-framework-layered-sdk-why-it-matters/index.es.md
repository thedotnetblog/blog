---
title: "Por qué el diseño en capas de Microsoft Agent Framework realmente importa"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "La nueva explicación del SDK en capas de Microsoft Agent Framework es más que charla de arquitectura. Muestra cómo Microsoft quiere que los desarrolladores pasen de bucles sencillos a una orquestación lista para producción sin tirar todo por la borda."
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).

Los anuncios de frameworks suelen abrir con funciones.

Este empezó con **filosofía de diseño**, y creo que precisamente por eso importa.

La nueva explicación de cómo Microsoft Agent Framework se estructura en torno a **agent loops**, **workflows** y **harnesses** nos da una señal mucho mejor que otra lista de funciones. Nos dice cómo espera el equipo que crezcan las aplicaciones reales.

Y para cualquiera que construya agentes en .NET, esa es la parte valiosa.

## La mayoría de las aplicaciones de agentes superan muy rápido su primera arquitectura

Empiezas con una llamada al modelo.

Luego añades herramientas.

Luego memoria.

Luego un planificador.

Luego reintentos, telemetría, aprobaciones, agentes especializados y algo de lógica de workflow, porque un solo loop ya no basta.

Aquí es donde muchas aplicaciones de IA se vuelven un lío. La primera versión funcionaba, pero cada nueva capacidad se añadió a golpe desde un nivel de abstracción distinto.

Lo que me gusta del artículo de Agent Framework es que hace explícitas las capas:

- **loops** para el ciclo de ejecución principal
- **workflows** para la orquestación estructurada
- **harnesses** para capacidades de runtime reutilizables alrededor del agente

Al principio puede sonar académico, pero resuelve un problema muy práctico: **puedes hacer evolucionar la aplicación sin reescribir el modelo mental cada vez que se vuelve más compleja**.

## El concepto de harness es especialmente importante

Si tuviera que elegir una parte que creo que será cada vez más importante, sería la idea de **harness**.

El harness es donde el desarrollo de agentes deja de ser solo prompts y pasa a ser ingeniería.

Ahí es donde empiezas a preocuparte por:

- herramientas y middleware
- comportamiento de planificación
- integración de memoria
- observabilidad
- controles y gobernanza
- comportamiento de runtime repetible

También por eso el diseño encaja tan bien con el resto de la pila de Microsoft. Foundry, las herramientas de gobernanza, los hosted agents, las evaluaciones y los ecosistemas de herramientas tienen mucho más sentido cuando la envoltura de ejecución alrededor del modelo se trata como algo de primera clase.

## Es una buena señal para los desarrolladores de .NET

Una cosa que siempre busco en estos ecosistemas es si el framework sigue siendo útil después de la primera demo.

El enfoque en capas sugiere que Microsoft está pensando en el recorrido completo:

1. construir un loop de agente sencillo
2. añadir capacidades estructuradas sin caos
3. pasar a workflows más formales cuando la app los necesita
4. mantener el runtime lo bastante componible como para integrarse con sistemas empresariales

Eso es una vía de crecimiento mucho más sana que: aquí tienes una abstracción monolítica, suerte.

Y encaja muy bien con la forma en que los desarrolladores de .NET suelen trabajar: sistemas por capas, composición explícita, límites comprobables y control fuerte del runtime.

## Mi opinión

A este post es fácil restarle importancia porque no trae una captura llamativa ni un volcado masivo de APIs.

Pero notas de arquitectura como esta suelen predecir mejor si un framework aguantará dentro de seis meses.

Microsoft Agent Framework claramente intenta ser más que un simple envoltorio de llamadas al modelo. La historia del SDK en capas dice que el equipo está construyendo para la parte difícil del camino: el punto en el que los agentes necesitan orquestación, herramientas, servicios de runtime y disciplina de producción.

Ese es exactamente el terreno que me interesa.

Publicación original: [ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
