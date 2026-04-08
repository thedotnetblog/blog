---
title: "Construyendo UIs Multi-Agente en Tiempo Real Que No Se Sientan Como una Caja Negra"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI y Microsoft Agent Framework se unen para darle a los flujos multi-agente un frontend de verdad — con streaming en tiempo real, aprobaciones humanas y visibilidad total de lo que hacen tus agentes."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

La verdad sobre los sistemas multi-agente: se ven increíbles en las demos. Tres agentes pasándose trabajo, resolviendo problemas, tomando decisiones. Luego intentas ponerlo frente a usuarios reales y... silencio. Un indicador girando. Sin idea de qué agente está haciendo qué ni por qué el sistema se pausó. Eso no es un producto — es un problema de confianza.

El equipo de Microsoft Agent Framework acaba de publicar un [fantástico tutorial](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) sobre cómo combinar flujos MAF con [AG-UI](https://github.com/ag-ui-protocol/ag-ui), un protocolo abierto para transmitir eventos de ejecución de agentes a un frontend mediante Server-Sent Events. Y sinceramente, este es el puente que nos hacía falta.

## Por qué esto importa para desarrolladores .NET

Si estás construyendo apps potenciadas por IA, probablemente ya te topaste con esta pared. Tu orquestación backend funciona perfecto — los agentes se pasan tareas, las herramientas se ejecutan, las decisiones se toman. Pero el frontend no tiene ni idea de lo que pasa detrás de escena. AG-UI resuelve esto definiendo un protocolo estándar para transmitir eventos de agentes (piensa en `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) directamente a tu capa de UI por SSE.

La demo que construyeron es un flujo de soporte al cliente con tres agentes: un agente de triaje que enruta solicitudes, un agente de reembolsos que maneja temas de dinero, y un agente de pedidos que gestiona reemplazos. Cada agente tiene sus propias herramientas, y la topología de handoff está definida explícitamente — nada de "descúbrelo desde el prompt".

## La topología de handoff es la verdadera estrella

Lo que me llamó la atención es cómo `HandoffBuilder` te permite declarar un grafo dirigido de enrutamiento entre agentes:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Cada `add_handoff` crea una arista dirigida con una descripción en lenguaje natural. El framework genera herramientas de handoff para cada agente basándose en esta topología. Así que las decisiones de enrutamiento están fundamentadas en tu estructura de orquestación, no solo en lo que al LLM se le ocurra hacer. Eso es un cambio enorme para la confiabilidad en producción.

## Human-in-the-loop que realmente funciona

La demo muestra dos patrones de interrupción que cualquier app de agentes del mundo real necesita:

**Interrupciones de aprobación de herramientas** — cuando un agente llama a una herramienta marcada con `approval_mode="always_require"`, el flujo se pausa y emite un evento. El frontend renderiza un modal de aprobación con el nombre de la herramienta y sus argumentos. Sin bucles de reintento que quemen tokens — solo un flujo limpio de pausa-aprobación-reanudación.

**Interrupciones de solicitud de información** — cuando un agente necesita más contexto del usuario (como un ID de pedido), se pausa y pregunta. El frontend muestra la pregunta, el usuario responde, y la ejecución se reanuda exactamente donde se detuvo.

Ambos patrones se transmiten como eventos estándar de AG-UI, así que tu frontend no necesita lógica personalizada por agente — simplemente renderiza cualquier evento que llegue por la conexión SSE.

## Conectarlo todo es sorprendentemente simple

La integración entre MAF y AG-UI se reduce a una sola llamada de función:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

El `workflow_factory` crea un flujo nuevo por hilo, así cada conversación obtiene estado aislado. El endpoint maneja toda la plomería SSE automáticamente. Si ya estás usando FastAPI (o puedes añadirlo como una capa ligera), esto tiene prácticamente cero fricción.

## Mi opinión

Para nosotros los desarrolladores .NET, la pregunta inmediata es: "¿Puedo hacer esto en C#?" El Agent Framework está disponible tanto para .NET como para Python, y el protocolo AG-UI es agnóstico de lenguaje (solo es SSE). Así que aunque esta demo específica usa Python y FastAPI, el patrón se traduce directamente. Podrías montar una API mínima de ASP.NET Core con endpoints SSE siguiendo el mismo esquema de eventos de AG-UI.

La conclusión más importante es que las UIs multi-agente se están convirtiendo en una preocupación de primera clase, no algo que se deja para después. Si estás construyendo cualquier cosa donde los agentes interactúan con humanos — soporte al cliente, flujos de aprobación, procesamiento de documentos — esta combinación de orquestación MAF y transparencia AG-UI es el patrón a seguir.

## Para cerrar

AG-UI + Microsoft Agent Framework te da lo mejor de ambos mundos: orquestación multi-agente robusta en el backend y visibilidad en tiempo real en el frontend. No más interacciones de agentes como cajas negras.

Revisa el [tutorial completo](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) y el [repositorio del protocolo AG-UI](https://github.com/ag-ui-protocol/ag-ui) para profundizar más.
