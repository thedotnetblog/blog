---
title: "Los Agent Harnesses Importan Porque los Prompts No Son Suficientes"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "El nuevo walkthrough de claw y harness de Microsoft Agent Framework es un recordatorio útil de que los agentes reales necesitan un shell de ejecución alrededor del modelo: herramientas, planificación, memoria, sesiones y un bucle de ejecución práctico."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Uno de los errores más fáciles en el desarrollo de agentes es pensar que el prompt es el producto.

No lo es.

El nuevo walkthrough sobre **agent harness y claw** del equipo de Microsoft Agent Framework es valioso porque mantiene el enfoque en la parte que realmente determina si un agente se siente usable: el shell de ejecución alrededor del modelo.

Eso incluye:

- herramientas
- planificación
- estado de sesión
- memoria
- modos de ejecución
- una consola o interfaz utilizable para la iteración

Ahí es donde los agentes dejan de ser demos ingeniosos y empiezan a sentirse como software.

## El patrón harness es práctico

Lo que me gusta aquí es lo abordable que es la idea.

Empiezas con un cliente de chat.

Luego lo envuelves en un harness con instrucciones y herramientas.

Luego lo ejecutas a través de un shell que soporta planificación, tareas pendientes, sesiones e interacción en streaming.

Ese es un patrón saludable porque separa responsabilidades claramente:

- el modelo maneja el razonamiento
- el harness maneja el comportamiento en tiempo de ejecución
- la app decide qué herramientas y experiencias importan

## Esto encaja muy bien con cómo los desarrolladores .NET construyen sistemas

La idea del harness también se mapea bien con la mentalidad .NET.

Generalmente nos va mejor cuando el comportamiento en tiempo de ejecución es explícito y componible. Middleware, pipelines, opciones, providers y adaptadores se sienten naturales en este mundo.

Por eso creo que Agent Framework tiene buenas posibilidades de conectar con los desarrolladores .NET. No está forzando a todos a entrar en una abstracción mágica. Te está dando piezas estructuradas de ejecución que puedes conectar.

## Mi opinión

La parte más útil de este post es el recordatorio de que los agentes necesitan más que un buen modelo y un string de instrucciones ingenioso.

Necesitan un shell de ejecución que les dé estructura, memoria, acceso a herramientas, planificación y un bucle de desarrollo funcional.

Eso es lo que el harness te proporciona.

Y honestamente, por eso vale la pena prestar atención a este patrón.

Post original: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)