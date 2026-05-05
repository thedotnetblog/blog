---
title: "CodeAct en Agent Framework: Cómo Reducir la Latencia de tu Agente a la Mitad"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct colapsa cadenas de herramientas de múltiples pasos en un único bloque de código sandboxed — reduciendo la latencia un 52% y el uso de tokens un 64%. Aquí está lo que significa para tus agentes y cuándo usarlo."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Hay un momento en todo proyecto de agentes en que miras el trace y piensas: "¿por qué tarda tanto esto?" El modelo está bien. Las herramientas funcionan. Pero hay siete round trips para obtener un resultado que podría calcularse de una sola vez.

Ese es exactamente el problema que resuelve CodeAct — y el [equipo de Agent Framework acaba de publicar soporte alpha para ello](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) a través de un nuevo paquete `agent-framework-hyperlight`.

## ¿Qué es CodeAct?

El [patrón CodeAct](https://arxiv.org/abs/2402.01030) es elegantemente simple: en lugar de darle al modelo una lista de herramientas y dejar que las llame una por una, le das una única herramienta `execute_code` y le permites expresar el *plan completo* como un programa Python corto. El agente escribe el código una vez, el sandbox lo ejecuta, y obtienes de vuelta un único resultado consolidado.

Un plan de cinco pasos que antes requería cinco turnos del modelo ahora se convierte en un turno `execute_code` que contiene un script Python que llama a tus herramientas vía `call_tool(...)`.

El benchmark del repositorio lo hace concreto. Ocho usuarios, docenas de pedidos, cinco herramientas (listar usuarios, obtener pedidos, tasa de descuento, tasa de impuesto, calcular total de línea). Mismo modelo, mismas herramientas, mismo prompt — solo cableado diferente:

| Cableado | Tiempo | Tokens |
|--------|------|--------|
| Tradicional | 27.81s | 6.890 |
| CodeAct | 13.23s | 2.489 |
| **Mejora** | **52,4%** | **63,9%** |

Eso no es un micro-benchmark. Es una carga de trabajo realista con overhead de orquestación real.

## La pieza de seguridad: micro-VMs de Hyperlight

Aquí está lo que me entusiasmó realmente: la seguridad ha sido históricamente el talón de Aquiles de CodeAct. Si estás ejecutando código generado por el modelo, ¿exactamente dónde se ejecuta? ¿Contra tu proceso? ¿En un contenedor compartido?

El paquete `agent-framework-hyperlight` resuelve esto con micro-VMs de [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Cada llamada `execute_code` obtiene su propia micro-VM recién creada — con su propia memoria, sin acceso al sistema de archivos del host más allá de lo que montes explícitamente, y sin acceso a la red más allá de los dominios que permitas. El arranque se mide en milisegundos. El aislamiento es prácticamente gratuito.

Tus herramientas siguen ejecutándose en el host (son tu código, con tu acceso). El *pegamento* generado por el modelo — el Python que decide qué herramientas llamar y en qué orden — se ejecuta en el sandbox. Esa es la división correcta.

## Cómo conectarlo

La configuración mínima es sencilla:

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)

result = await agent.run(
    "Get the weather for Seattle and Amsterdam and compare them."
)
```

El proveedor registra `execute_code` en cada ejecución e inyecta las instrucciones de CodeAct en el prompt del sistema automáticamente.

## Mezclando CodeAct con herramientas que requieren aprobación

Aquí se pone interesante. No todas las herramientas deberían ejecutarse dentro del sandbox sin aprobación. Puede que quieras aprobar `send_email` o `charge_credit_card` individualmente. El framework maneja esto de forma limpia:

```python
@tool(approval_mode="always_require")
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email. Requires approval on every call."""
    ...

agent = Agent(
    client=client,
    name="MixedToolsAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
    tools=[send_email],  # invocado directamente, con aprobación
)
```

Herramientas en el proveedor → el modelo las alcanza vía `call_tool(...)` dentro del sandbox, baratas y encadenables.  
Herramientas directamente en el agente → el modelo las llama como herramientas de primera clase, la aprobación aplica individualmente.

## Cuándo usar CodeAct (y cuándo no)

**Usa CodeAct cuando:**
- La tarea encadena muchas llamadas pequeñas a herramientas (búsquedas, joins, cálculos, formateo)
- Te importa la latencia y el costo de tokens
- Quieres aislamiento fuerte por llamada en código generado por el modelo por defecto
- Las herramientas son baratas y seguras para invocar en secuencia

**Quédate con el tool-calling tradicional cuando:**
- El agente solo hace una o dos llamadas a herramientas por turno
- Cada llamada a herramienta tiene efectos secundarios que quieres aprobar individualmente
- Las descripciones de herramientas son escasas o ambiguas — CodeAct depende de buenos docstrings

## Pruébalo ahora

```bash
pip install agent-framework-hyperlight --pre
# o
uv add --prerelease=allow agent-framework-hyperlight
```

Los ejemplos están en [`python/packages/hyperlight/samples/`](https://github.com/microsoft/agent-framework/tree/main/python/packages/hyperlight/samples). El [ejemplo de benchmark](https://github.com/microsoft/agent-framework/blob/main/python/packages/hyperlight/samples/codeact_benchmark.py) es el mejor punto de partida.

Vale la pena mencionar: Linux y Windows son compatibles hoy. El soporte para macOS está en camino. Un equivalente para .NET también está llegando.

## Resumiendo

CodeAct no es magia — es un patrón sensato que era demasiado arriesgado de usar sin sandboxing adecuado. Hyperlight cambia esa ecuación. Aislamiento en micro-VM por llamada, arranque en milisegundos, mejora de latencia del 50%+ en las cargas de trabajo adecuadas. Vale la pena experimentar.

Consulta el [post completo en el blog de Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) para cobertura más profunda sobre montajes de sistema de archivos, política de red y el cableado independiente de `HyperlightExecuteCodeTool`.
