---
title: "Microsoft Foundry Marzo 2026 — GPT-5.4, Agent Service GA y la Renovación del SDK Que lo Cambia Todo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La actualización de marzo 2026 de Microsoft Foundry es enorme: Agent Service llega a GA, GPT-5.4 trae razonamiento confiable, el SDK azure-ai-projects se estabiliza en todos los lenguajes, y Fireworks AI trae modelos abiertos a Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}}).*

Los posts mensuales de "Novedades en Microsoft Foundry" suelen ser una mezcla de mejoras incrementales y alguna que otra característica destacada. ¿La [edición de marzo 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Básicamente son todas características destacadas. Foundry Agent Service llega a GA, GPT-5.4 se lanza para producción, el SDK recibe una versión estable importante, y Fireworks AI trae inferencia de modelos abiertos a Azure. Vamos a desglosar lo que importa para los desarrolladores .NET.

## Foundry Agent Service está listo para producción

Esta es la grande. El runtime de agentes de nueva generación está disponible de forma general — construido sobre la API de Responses de OpenAI, compatible a nivel de protocolo con los agentes de OpenAI, y abierto a modelos de múltiples proveedores. Si estás construyendo con la API de Responses hoy, migrar a Foundry añade seguridad empresarial, redes privadas, RBAC de Entra, trazabilidad completa y evaluación sobre tu lógica de agentes existente.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Adiciones clave: redes privadas de extremo a extremo, expansión de autenticación MCP (incluyendo passthrough de OAuth), vista previa de Voice Live para agentes de voz a voz, y agentes alojados en 6 nuevas regiones.

## GPT-5.4 — confiabilidad sobre inteligencia pura

GPT-5.4 no se trata de ser más inteligente. Se trata de ser más confiable. Razonamiento más sólido en interacciones largas, mejor adherencia a instrucciones, menos fallos en medio de flujos de trabajo, y capacidades integradas de uso de computadora. Para agentes en producción, esa confiabilidad importa mucho más que las puntuaciones en benchmarks.

| Modelo | Precio (por M tokens) | Ideal Para |
|--------|----------------------|------------|
| GPT-5.4 (≤272K) | $2.50 / $15 salida | Agentes en producción, código, flujos de documentos |
| GPT-5.4 Pro | $30 / $180 salida | Análisis profundo, razonamiento científico |
| GPT-5.4 Mini | Económico | Clasificación, extracción, llamadas ligeras a herramientas |

La jugada inteligente es una estrategia de enrutamiento: GPT-5.4 Mini maneja el trabajo de alto volumen y baja latencia mientras GPT-5.4 se encarga de las solicitudes con razonamiento pesado.

## El SDK finalmente es estable

El SDK `azure-ai-projects` lanzó versiones estables en todos los lenguajes — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0 y .NET 2.0.0 (1 de abril). La dependencia de `azure-ai-agents` desapareció — todo vive bajo `AIProjectClient`. Instala con `pip install azure-ai-projects` y el paquete incluye `openai` y `azure-identity` como dependencias directas.

Para los desarrolladores .NET, esto significa un único paquete NuGet para toda la superficie de Foundry. No más malabarismo con SDKs de agentes separados.

## Fireworks AI trae modelos abiertos a Azure

Quizás la adición más interesante arquitectónicamente: Fireworks AI procesando más de 13 billones de tokens diarios a ~180K solicitudes/segundo, ahora disponible a través de Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5 y MiniMax M2.5 en el lanzamiento.

La verdadera historia es **trae-tus-propios-pesos** — sube pesos cuantizados o ajustados desde cualquier lugar sin cambiar la pila de servicio. Despliega mediante pago por token sin servidor o throughput provisionado.

## Otros destacados

- **Phi-4 Reasoning Vision 15B** — razonamiento multimodal para gráficos, diagramas y diseños de documentos
- **Evaluaciones GA** — evaluadores listos para usar con monitoreo continuo de producción canalizado a Azure Monitor
- **Procesamiento Prioritario** (Preview) — carril de cómputo dedicado para cargas de trabajo sensibles a la latencia
- **Voice Live** — runtime de voz a voz que se conecta directamente a los agentes de Foundry
- **Tracing GA** — inspección de trazas de agentes de extremo a extremo con ordenamiento y filtrado
- **Deprecación de PromptFlow** — migración a Microsoft Framework Workflows para enero de 2027

## Conclusión

Marzo 2026 es un punto de inflexión para Foundry. Agent Service GA, SDKs estables en todos los lenguajes, GPT-5.4 para agentes de producción confiables, e inferencia de modelos abiertos vía Fireworks AI — la plataforma está lista para cargas de trabajo serias.

Lee el [resumen completo](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) y [construye tu primer agente](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) para empezar.
