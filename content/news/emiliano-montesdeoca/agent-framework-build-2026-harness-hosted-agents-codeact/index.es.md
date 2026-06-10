---
title: "Agent Harness, Hosted Agents y CodeAct: esta es la actualización de Agent Framework en la que me fijaría"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "El anuncio de Agent Framework en Build 2026 viene cargado, pero los hilos más importantes son el modelo harness, los agentes hospedados en Foundry y CodeAct para reducir la sobrecarga de orquestación."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

El gran anuncio de Agent Framework en Build cubre mucho, pero hay tres temas que me llaman la atención de inmediato:

- **que el harness pase a ser una pieza de runtime más de primera categoría**
- **que los agentes hospedados en Foundry den una vía clara hacia producción**
- **que CodeAct reduzca la sobrecarga de orquestación de varios pasos**

Esas son las partes a las que yo les seguiría la pista.

## El harness se está convirtiendo en el verdadero centro de gravedad

La publicación original describe el harness como la capa donde el razonamiento del modelo se encuentra con la ejecución real.

Esa es la descripción correcta, y también la razón por la que creo que esta parte pesa más que muchos puntos de función aislados.

En cuanto un agente necesita:

- acceso a archivos
- ejecución de shell
- modos de planificación
- tareas pendientes
- memoria de sesión
- flujos de aprobación

ya no estás hablando solo de un prompt con un modelo.

Estás hablando de comportamiento en tiempo de ejecución.

Ahí es donde los frameworks se vuelven realmente útiles o se quedan en juguetes.

Y Microsoft Agent Framework claramente está intentando ser más útil justo en esa capa.

## Los agentes hospedados son donde la historia de lo local a producción se vuelve real

También creo que la parte de los agentes hospedados es una de las más importantes estratégicamente del anuncio.

La publicación original dice explícitamente que es la forma más fácil de darle a ese agente un hogar en producción.

Esa frase importa porque la mayoría de los frameworks de agentes siguen siendo mucho más fuertes en la experimentación local que en el despliegue operativo.

Si los agentes hospedados en Foundry hacen mucho más fácil pasar del desarrollo local a:

- escalado
- observabilidad
- identidad administrada
- gestión de sesiones
- versionado

entonces se cierra una de las mayores brechas del ecosistema de agentes actual.

Eso sería una mejora significativa.

## CodeAct es la idea técnica más emocionante de la actualización

Si tuviera que elegir el concepto técnico más interesante de la publicación, probablemente elegiría CodeAct.

El problema que intenta resolver es muy real: demasiados flujos de agentes de varios pasos son caros porque el propio bucle de orquestación consume demasiadas vueltas del modelo.

Así que, cuando la publicación muestra un resultado como este:

- 52.4% más rápido
- 63.9% menos tokens

me llama la atención de inmediato.

Claro, son cifras de benchmark ligadas a una carga de trabajo representativa, no una ley universal. Pero la idea de fondo sigue siendo muy convincente.

Si el modelo puede comprimir una cadena de llamadas a herramientas en una forma de ejecución más eficiente, la economía de los sistemas de agentes puede cambiar bastante.

## Lo que creo que los desarrolladores deberían sacar de verdad de esta actualización

La lección importante no es cuántas funciones se han lanzado.

La lección es que el framework se está fortaleciendo en los lugares que las aplicaciones reales necesitan más:

- runtime
- ruta de despliegue
- eficiencia de ejecución
- patrones operativos incorporados

Ese es el tipo de señal de madurez que me importa mucho más que otra lista superficial de funciones de IA.

## Mi opinión

Esta actualización importa porque no solo añade más superficie.

Está reforzando la historia de runtime y despliegue alrededor de los agentes de una forma que debería importar para aplicaciones reales, especialmente para equipos que quieren pasar de experimentos locales a sistemas que de verdad puedan ejecutar y mantener.

Ahí es donde el framework se vuelve más convincente.

Y si siguiera este lanzamiento de cerca, el harness, los agentes hospedados y CodeAct serían sin duda donde pondría la mayor parte de mi atención.

Entrada original: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
