---
title: "Foundry Agent Service está en GA: Lo que realmente importa para constructores de agentes .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "El Foundry Agent Service de Microsoft acaba de llegar a GA con redes privadas, Voice Live, evaluaciones de producción y un runtime multi-modelo abierto. Esto es lo que necesitas saber."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Seamos honestos — construir un prototipo de agente IA es la parte fácil. La parte difícil es todo lo que viene después: ponerlo en producción con aislamiento de red adecuado, ejecutar evaluaciones que realmente signifiquen algo, manejar requisitos de cumplimiento, y no romper cosas a las 2 AM.

El [Foundry Agent Service acaba de llegar a GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), y esta versión está enfocada como un láser en esa brecha del "todo lo que viene después".

## Construido sobre la Responses API

El titular: el Foundry Agent Service de nueva generación está construido sobre la OpenAI Responses API. Si ya estás construyendo con ese protocolo, migrar a Foundry requiere cambios mínimos de código. Lo que ganas: seguridad empresarial, redes privadas, RBAC con Entra, trazabilidad completa y evaluación — sobre tu lógica de agente existente.

La arquitectura es intencionalmente abierta. No estás atado a un proveedor de modelos ni a un framework de orquestación. Usa DeepSeek para planificación, OpenAI para generación, LangGraph para orquestación — el runtime maneja la capa de consistencia.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Si vienes del paquete `azure-ai-agents`, los agentes ahora son operaciones de primera clase en `AIProjectClient` en `azure-ai-projects`. Elimina la dependencia independiente y usa `get_openai_client()` para manejar las respuestas.

## Redes privadas: el bloqueador empresarial eliminado

Esta es la característica que desbloquea la adopción empresarial. Foundry ahora soporta redes privadas completas de extremo a extremo con BYO VNet:

- **Sin egress público** — el tráfico del agente nunca toca internet público
- **Inyección de contenedores/subredes** en tu red para comunicación local
- **Conectividad de herramientas incluida** — servidores MCP, Azure AI Search, agentes de datos Fabric, todos operan sobre rutas privadas

Ese último punto es crítico. No son solo las llamadas de inferencia las que se mantienen privadas — cada invocación de herramienta y llamada de recuperación también permanece dentro del límite de tu red. Para equipos que operan bajo políticas de clasificación de datos que prohíben el enrutamiento externo, esto era lo que faltaba.

## Autenticación MCP hecha correctamente

Las conexiones a servidores MCP ahora soportan el espectro completo de patrones de autenticación:

| Método de auth | Cuándo usarlo |
|----------------|---------------|
| Basado en clave | Acceso compartido simple para herramientas internas de toda la organización |
| Entra Agent Identity | Servicio a servicio; el agente se autentica como él mismo |
| Entra Managed Identity | Aislamiento por proyecto; sin gestión de credenciales |
| OAuth Identity Passthrough | Acceso delegado por usuario; el agente actúa en nombre de los usuarios |

OAuth Identity Passthrough es el interesante. Cuando los usuarios necesitan dar a un agente acceso a sus datos personales — su OneDrive, su organización de Salesforce, una API SaaS con alcance por usuario — el agente actúa en su nombre con flujos OAuth estándar. Sin identidad de sistema compartida pretendiendo ser todos.

## Voice Live: voz a voz sin la fontanería

Agregar voz a un agente solía significar unir STT, LLM y TTS — tres servicios, tres saltos de latencia, tres superficies de facturación, todo sincronizado a mano. **Voice Live** colapsa eso en una única API administrada con:

- Detección semántica de actividad de voz y fin de turno (entiende significado, no solo silencio)
- Supresión de ruido y cancelación de eco del lado del servidor
- Soporte de interrupción (los usuarios pueden interrumpir a mitad de respuesta)

Las interacciones de voz pasan por el mismo runtime de agente que el texto. Mismos evaluadores, mismas trazas, misma visibilidad de costos. Para soporte al cliente, servicio en campo o escenarios de accesibilidad, esto reemplaza lo que antes requería un pipeline de audio personalizado.

## Evaluaciones: de checkbox a monitoreo continuo

Aquí es donde Foundry se pone serio sobre la calidad en producción. El sistema de evaluación ahora tiene tres capas:

1. **Evaluadores incorporados** — coherencia, relevancia, fundamentación, calidad de recuperación, seguridad. Conecta a un dataset o tráfico en vivo y obtén puntuaciones.

2. **Evaluadores personalizados** — codifica tu propia lógica de negocio, estándares de tono y reglas de cumplimiento específicas del dominio.

3. **Evaluación continua** — Foundry muestrea tráfico de producción en vivo, ejecuta tu suite de evaluadores y muestra resultados en dashboards. Configura alertas de Azure Monitor para cuando la fundamentación baje o los umbrales de seguridad se superen.

Todo se publica en Azure Monitor Application Insights. Calidad del agente, salud de la infraestructura, costo y telemetría de la aplicación — todo en un solo lugar.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Seis nuevas regiones para agentes hospedados

Los agentes hospedados ahora están disponibles en East US, North Central US, Sweden Central, Southeast Asia, Japan East y más. Esto importa para requisitos de residencia de datos y para comprimir la latencia cuando tu agente corre cerca de sus fuentes de datos.

## Por qué esto importa para desarrolladores .NET

Aunque los ejemplos de código en el anuncio de GA son Python-first, la infraestructura subyacente es agnóstica al lenguaje — y el SDK de .NET para `azure-ai-projects` sigue los mismos patrones. La Responses API, el framework de evaluación, las redes privadas, la autenticación MCP — todo esto está disponible desde .NET.

Si has estado esperando a que los agentes IA pasen de "demo genial" a "realmente puedo enviar esto al trabajo", esta versión GA es la señal. Redes privadas, autenticación adecuada, evaluación continua y monitoreo de producción son las piezas que faltaban.

## Para cerrar

Foundry Agent Service está disponible ahora. Instala el SDK, abre [el portal](https://ai.azure.com), y empieza a construir. La [guía de inicio rápido](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) te lleva de cero a un agente en ejecución en minutos.

Para el análisis técnico completo con todos los ejemplos de código, revisa el [anuncio de GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
