---
title: "Mission Control para Agentes de Codificación: Una Experiencia Unificada en VS Code"
description: "VS Code reúne agentes de codificación locales, en la nube, CLI y de terceros en Sesiones de Agentes para que los desarrolladores puedan rastrear, interrumpir y coordinar el trabajo autónomo."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

# Mission Control para Agentes de Codificación: Una Experiencia Unificada en VS Code

Un único asistente de codificación es fácil de entender. Varios agentes trabajando en lugares diferentes no lo son.

Un agente se ejecuta localmente en VS Code. Otro trabaja en un problema de GitHub en la nube. Un agente CLI vive en la terminal. Un agente de codificación de terceros puede tener un modelo de sesión diferente y límites distintos. Sin una vista compartida, los desarrolladores pasan más tiempo rastreando el trabajo que supervisándolo.

La experiencia de agente unificada de VS Code aborda ese problema de coordinación con Sesiones de Agentes: un lugar para lanzar agentes, ver su estado, abrir sus conversaciones e intervenir cuando el plan cambia.

Esto se trata menos de agregar otro agente y más de hacer que múltiples agentes sean manejables.

## Una Vista para Diferentes Tipos de Trabajo

El artículo de origen describe cuatro participantes distintos: GitHub Copilot local, Agente de Codificación de Copilot en la nube, Copilot CLI de GitHub y OpenAI Codex para suscriptores elegibles de Copilot.

Tienen diferentes fortalezas:

- Un agente local puede inspeccionar el espacio de trabajo actual y realizar cambios rápidos.
- Un agente de codificación en la nube puede trabajar de manera asincrónica en un problema y abrir una solicitud de extracción.
- Un agente CLI se ajusta a flujos de trabajo pesados en terminal y comandos operacionales.
- Otro proveedor puede ofrecer un modelo diferente o un estilo de razonamiento diferente.

Sesiones de Agentes brinda a esas tareas un hogar común. Puedes ver qué se está ejecutando, qué está haciendo y dónde continuar la conversación.

Esa visibilidad es importante porque el trabajo autónomo no elimina la coordinación. Hace que la coordinación sea una tarea de ingeniería de primera clase.

## Las Interrupciones Son Parte del Flujo de Trabajo

El artículo de origen hace una observación simple: "Es común enviar un mensaje y darse cuenta de que olvidaste algo importante". Anteriormente, la opción era a menudo esperar o cancelar. Con editores de chat, puedes abrir una sesión activa y agregar información mientras el agente está trabajando.

Eso está más cerca de una colaboración real. Los requisitos cambian. Una prueba revela una suposición. Un revisor nota que una API debe permanecer compatible hacia atrás. El agente útil no es el que nunca necesita corrección; es el que puede absorber la corrección sin perder toda la tarea.

Para el trabajo en .NET, una interrupción podría ser tan simple como:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

La instrucción es breve porque el repositorio ya lleva el contexto más amplio. La sesión es el lugar para corregir la dirección, no para reafirmar todo el sistema.

## Los Agentes Personalizados Convierten los Hábitos del Equipo en Roles

VS Code también introduce agentes especializados como Plan. En lugar de implementar inmediatamente, un agente de planificación hace preguntas sobre alcance, componentes, bibliotecas y restricciones antes de producir una especificación de implementación.

Ese patrón es útil más allá de un agente integrado. Un equipo puede definir roles enfocados:

- **Research** recopila evidencia y escribe un registro de decisión breve.
- **Review** verifica un cambio contra las convenciones del repositorio.
- **Testing** identifica casos faltantes y propone un plan de prueba.
- **Architecture** compara opciones sin modificar archivos.

Una definición de agente personalizado pequeña podría verse así:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

La parte útil no es el YAML. Es la separación explícita de responsabilidades. Un agente de planificación no debe editar silenciosamente código de producción. Un agente de revisión no debe reescribir el diseño que se supone debe evaluar.

## Los Subagentes Reducen Colisiones de Contexto

Las conversaciones largas acumulan contexto no relacionado. Los subagentes proporcionan un espacio de trabajo aislado para una tarea de investigación limitada, luego devuelven el resultado a la sesión principal.

Eso se ajusta bien a preguntas como:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

El agente principal se mantiene enfocado en la implementación mientras el agente de investigación maneja una pregunta más estrecha. El mismo principio se aplica a los equipos: la delegación clara produce mejores resultados que lanzar varios agentes con autoridad superpuesta.

## La Advertencia: Más Agentes Significan Más Coordinación

Sesiones de Agentes puede mostrar actividad, pero no puede resolver la propiedad conflictiva. Dos agentes que editan la misma área aún pueden crear un problema de fusión. Un agente en la nube y un agente local pueden hacer suposiciones incompatibles. Un agente personalizado puede producir una recomendación que otro agente ignora.

Establece límites:

1. Un agente es propietario de la implementación para una rama determinada.
2. Los agentes de investigación devuelven artefactos, no ediciones no rastreadas.
3. Las solicitudes de extracción permanecen como límite de revisión.
4. Los nombres y mensajes de los agentes indican qué pueden cambiar.
5. La salida de la sesión se retiene cuando explica una decisión importante.

## Mi Opinión

El futuro multi-agente no es una cola de ventanas de chat. Es un pequeño equipo con roles, trasferencias y responsabilidad.

Sesiones de Agentes es valioso porque reconoce esa realidad. Brinda a los desarrolladores una superficie de control para el trabajo que ya está sucediendo en el editor, terminal y nube. La próxima ganancia de productividad vendrá menos de tener más agentes y más de hacer que sus límites sean legibles.

Para un equipo de .NET, comenzaría con un agente de planificación y un agente de implementación. Usa la salida de planificación como la especificación de problema o solicitud de extracción, luego deja que el agente de implementación trabaje dentro de ese límite. Mide el trabajo rehecho antes de agregar más roles.

El mejor mission control sigue siendo el que hace que la propiedad sea obvia.
