---
title: "¿Dónde deberías alojar tus agentes de IA en Azure? Una guía práctica de decisión"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure ofrece seis formas de alojar agentes de IA — desde contenedores crudos hasta Foundry Hosted Agents completamente gestionados. Así es como elegir el adecuado para tu carga de trabajo .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Si estás construyendo agentes de IA con .NET ahora mismo, probablemente hayas notado algo: hay *muchas* formas de alojarlos en Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — y todos suenan razonables hasta que realmente necesitas elegir uno. Microsoft acaba de publicar una [guía completa sobre alojamiento de agentes IA en Azure](https://devblogs.microsoft.com/all-things-azure/hostedagent/) que aclara esto, y quiero desglosarlo desde la perspectiva práctica de un desarrollador .NET.

## Las seis opciones de un vistazo

Así es como yo resumiría el panorama:

| Opción | Ideal para | Tú gestionas |
|--------|-----------|--------------|
| **Container Apps** | Control total de contenedores sin complejidad K8s | Observabilidad, estado, ciclo de vida |
| **AKS** | Cumplimiento empresarial, multi-clúster, redes personalizadas | Todo (ese es el punto) |
| **Azure Functions** | Tareas de agentes cortas y dirigidas por eventos | Casi nada — serverless puro |
| **App Service** | Agentes HTTP simples, tráfico predecible | Despliegue, configuración de escalado |
| **Foundry Agents** | Agentes sin código vía portal/SDK | Casi nada |
| **Foundry Hosted Agents** | Agentes con framework personalizado e infra gestionada | Solo tu código de agente |

Las primeras cuatro son computación de propósito general — *puedes* ejecutar agentes en ellas, pero no fueron diseñadas para eso. Las dos últimas son nativas de agentes: entienden conversaciones, llamadas a herramientas y ciclos de vida de agentes como conceptos de primera clase.

## Foundry Hosted Agents — el punto ideal para desarrolladores .NET de agentes

Esto es lo que me llamó la atención. Foundry Hosted Agents se sitúan justo en el medio: obtienes la flexibilidad de ejecutar tu propio código (Semantic Kernel, Agent Framework, LangGraph — lo que sea) pero la plataforma gestiona infraestructura, observabilidad y gestión de conversaciones.

La pieza clave es el **Hosting Adapter** — una capa de abstracción fina que conecta tu framework de agentes con la plataforma Foundry. Para Microsoft Agent Framework, se ve así:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Esa es toda tu historia de hosting. El adapter gestiona traducción de protocolos, streaming vía server-sent events, historial de conversación y trazado OpenTelemetry — todo automáticamente. Sin middleware personalizado, sin plomería manual.

## Desplegar es genuinamente simple

He desplegado agentes en Container Apps antes y funciona, pero terminas escribiendo mucho código de pegamento para gestión de estado y observabilidad. Con Hosted Agents y `azd`, el despliegue es:

```bash
# Instalar la extensión de agente IA
azd ext install azure.ai.agents

# Inicializar desde una plantilla
azd ai agent init

# Construir, subir, desplegar — listo
azd up
```

Ese único `azd up` construye tu contenedor, lo sube a ACR, provisiona el proyecto Foundry, despliega endpoints de modelo e inicia tu agente. Cinco pasos colapsados en un solo comando.

## Gestión de conversaciones integrada

Esta es la parte que ahorra más tiempo en producción. En lugar de construir tu propio almacén de estado de conversación, Hosted Agents lo gestionan nativamente:

```python
# Crear una conversación persistente
conversation = openai_client.conversations.create()

# Primer turno
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Segundo turno — el contexto se preserva
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Sin Redis. Sin almacén de sesiones Cosmos DB. Sin middleware personalizado para serialización de mensajes. La plataforma simplemente lo gestiona.

## Mi framework de decisión

Después de revisar las seis opciones, aquí está mi modelo mental rápido:

1. **¿Necesitas cero infraestructura?** → Foundry Agents (portal/SDK, sin contenedores)
2. **¿Tienes código de agente personalizado pero quieres hosting gestionado?** → Foundry Hosted Agents
3. **¿Necesitas tareas de agente cortas dirigidas por eventos?** → Azure Functions
4. **¿Necesitas máximo control de contenedores sin K8s?** → Container Apps
5. **¿Necesitas cumplimiento estricto y multi-clúster?** → AKS
6. **¿Tienes un agente HTTP simple con tráfico predecible?** → App Service

Para la mayoría de desarrolladores .NET que construyen con Semantic Kernel o Microsoft Agent Framework, Hosted Agents es probablemente el punto de partida correcto. Obtienes scale-to-zero, OpenTelemetry integrado, gestión de conversaciones y flexibilidad de framework — sin gestionar Kubernetes ni montar tu propia pila de observabilidad.

## Para terminar

El panorama de alojamiento de agentes en Azure está madurando rápido. Si estás empezando un nuevo proyecto de agente IA hoy, consideraría seriamente Foundry Hosted Agents antes de recurrir a Container Apps o AKS por costumbre. La infraestructura gestionada ahorra tiempo real, y el patrón de hosting adapter te permite mantener tu elección de framework.

Echa un vistazo a la [guía completa de Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) y al [repositorio de ejemplos de Foundry](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) para ejemplos funcionales.
