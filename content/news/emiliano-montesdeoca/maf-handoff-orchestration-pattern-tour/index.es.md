---
title: "El Patrón Handoff: Cuando Un Agente No Es Suficiente"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "El patrón de orquestación Handoff de Microsoft Agent Framework permite a los agentes decidir quién maneja el siguiente turno — sin perder el contexto de la conversación ni romper las reglas de topología."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

En algún momento, todo sistema multi-agente supera un enrutador simple. La primera señal suele aparecer cuando un agente especialista necesita hacer una pregunta de seguimiento, o se da cuenta a mitad del turno de que otro agente debería continuar. Un pipeline fijo falla ahí. Un enrutador de un solo paso falla ahí.

Exactamente para eso está diseñado el patrón de orquestación Handoff en Microsoft Agent Framework.

## Cómo Funciona Handoff

El desarrollador declara un grafo: aquí están los agentes, aquí están las aristas entre ellos. El framework hace el resto — sintetiza una herramienta de handoff por cada arista de salida y la inyecta en cada agente. Cuando un agente decide pasar el control, llama a la herramienta. El framework aplica la topología.

Tres cosas hacen esto diferente a simplemente hacer que los agentes se llamen entre sí:

1. **Un transcripto compartido** — el agente receptor ve el historial completo de la conversación. Sin empezar desde cero.
2. **Aplicación de topología** — un agente solo puede hacer handoff a destinos declarados. Los errores de enrutamiento se detectan en tiempo de autoría, no en producción.
3. **Terminación natural** — cuando el agente activo termina su turno sin llamar a una herramienta de handoff, el flujo de trabajo cede al usuario. Sin sondeo, sin condiciones de salida explícitas.

## Un Ejemplo Mínimo

En .NET, construir un flujo de trabajo handoff se ve así:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage puede enviar a cualquier especialista. Ambos especialistas pueden enviar de vuelta a triage. El grafo es compatible con acíclico pero admite aristas hacia atrás cuando las necesitas ("necesito más información" → de vuelta a investigación).

## Cuándo Usar Handoff (y Cuándo No)

Handoff es una buena opción cuando:

- **La propiedad puede cambiar a mitad de conversación** — un agente puede darse cuenta de que es el especialista equivocado
- **Las aristas hacia atrás importan** — puede que necesites revisar un paso anterior sin reiniciar
- **Las decisiones de enrutamiento son difusas** — la decisión de hacer handoff es contextual y mejor tomada por el modelo que por predicados tipificados

*No* es la elección correcta cuando:

- Tu pipeline es fijo y secuencial — usa el flujo de trabajo `Sequential` para eso
- Cada paso es independiente — los agentes compartiendo un transcripto donde solo uno de ellos lo necesitaba es solo ruido
- Necesitas garantías estrictas de procesamiento — la no determinismo del enrutamiento impulsado por modelos no es lo que deseas

## Aristas hacia Atrás y Humano en el Bucle

Una de las formas más interesantes que Handoff permite son las aristas hacia atrás genuinas. Un agente puede decidir "no tengo suficiente información" y enrutar de vuelta a un paso de investigación, no con un bucle codificado, sino porque el modelo decide que es la decisión correcta.

Las interacciones de humano en el bucle también se componen naturalmente. Cuando un especialista necesita entrada del usuario, el flujo de trabajo cede de vuelta al usuario a través del bucle de turno predeterminado, recopila la respuesta y se reanuda con contexto completo. El agente nunca perdió la conversación.

## Conclusión

Handoff es uno de esos patrones que suena simple pero permite mucho una vez que lo internalizas: enrutamiento descentralizado, contexto compartido, topología aplicada, terminación natural. Es el siguiente paso correcto cuando tus agentes comienzan a decir "en realidad, alguien más debería manejar esto."

Lee el recorrido completo en el post original: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
