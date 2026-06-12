---
title: "El nuevo Plan agent de Visual Studio resuelve un problema muy real del flujo de trabajo de IA"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "El nuevo Plan agent de Visual Studio importa porque crea una fase de planificación estructurada antes de la implementación, justo lo que suelen necesitar las funciones grandes y las refactorizaciones."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Esta publicación se ha traducido automáticamente. Lee el original [aquí]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

Uno de los flujos de trabajo de programación con IA más frustrantes es cuando la implementación empieza demasiado rápido.

El código puede incluso ser técnicamente correcto, pero está resolviendo la versión equivocada del problema que tenías en mente.

Querías una refactorización. Empezó una reescritura.
Querías una mejora acotada. Tocó medio proyecto.
Querías hablar de opciones. Saltó directamente a cambios de archivos.

Por eso el nuevo **Plan agent** de Visual Studio es una adición tan útil.

## Esto resuelve un problema real de workflow, no solo un problema estético

La publicación original describe una situación muy familiar: "**El código no está mal... simplemente no es lo que querías.**"

Esa frase es perfecta.

Porque el punto débil de mucho desarrollo asistido por IA no es si el modelo puede producir código. Es si el workflow crea suficiente espacio para acordar la forma deseada del trabajo antes de empezar la implementación.

Eso importa especialmente para:

- funciones grandes
- bases de código desconocidas
- refactorizaciones no triviales
- cambios sensibles a la arquitectura
- trabajo que necesita revisión del equipo antes de empezar a editar

En esas situaciones, saltar directamente a implementar suele ser el movimiento equivocado.

## Planificar no es sobrecarga cuando la tarea es real

Creo que los equipos a veces subestiman cuánto tiempo pierden al empezar a implementar demasiado pronto.

Si el agente:

- toca los archivos equivocados
- elige el enfoque equivocado
- pasa por alto una restricción clave
- ignora un caso límite necesario

entonces el inicio "rápido" acaba convirtiéndose en un workflow más lento en conjunto.

Por eso me gusta esta función.

Da espacio para:

- preguntas de aclaración
- redacción del plan
- edición directa del plan
- compartir el plan antes de que empiecen los cambios de código

Eso no es burocracia. Muchas veces es simplemente buena ingeniería.

## El archivo de plan en markdown es una elección inteligente

Un detalle que me gusta especialmente es que cada plan se guarda en `.copilot/plans/plan-{title}.md`.

Eso hace que el paso de planificación sea tangible.

Significa que el plan no queda atrapado dentro de un transcript de chat. Se convierte en algo que puedes:

- revisar
- editar
- versionar mentalmente
- discutir con el equipo
- pasar a la implementación de forma más deliberada

Eso hace que la función se sienta mucho más seria que un simple preámbulo temporal antes de generar código.

## Aquí es donde los workflows de IA empiezan a respetar el proceso del equipo

Creo que esta es una de las señales más claras de que estas herramientas están madurando.

Los mejores workflows de IA para desarrolladores no son los que eliminan todos los pasos intermedios. Son los que mejoran los pasos intermedios correctos.

Y la planificación es uno de esos pasos.

Si el plan es sólido, implementar es más fácil.
Si el plan es débil, la implementación se vuelve ruidosa.

Esta función lo reconoce directamente.

## Mi opinión

Esto no es solo una comodidad de IA.

Es una mejora del workflow.

Y para funciones reales y refactorizaciones reales, es exactamente el tipo de mejora que puede ahorrar mucho churn innecesario, ruido de review y rework del tipo "eso no es lo que quise decir".

Creo que cada vez más experiencias de agentes acabarán necesitando algo así.

Visual Studio llegó antes, y de una forma que se siente útil.

Publicación original: [Planifica antes de construir: introduciendo el Plan agent en Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)