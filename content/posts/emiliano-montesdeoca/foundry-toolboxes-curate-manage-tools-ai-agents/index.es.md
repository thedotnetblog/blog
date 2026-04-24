---
title: "Foundry Toolboxes: Un único endpoint para todas las herramientas de tus agentes"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry acaba de lanzar Toolboxes en preview pública — una forma de curar, gestionar y exponer herramientas de agentes IA a través de un único endpoint compatible con MCP, sin tener que reconfigurar todo en cada agente."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Aquí hay un problema que parece aburrido hasta que lo sufres en carne propia: tu organización está construyendo múltiples agentes de IA, cada uno necesita herramientas, y cada equipo las conecta desde cero. La misma integración de búsqueda web, la misma config de Azure AI Search, la misma conexión al servidor MCP de GitHub — pero en otro repositorio, por otro equipo, con otras credenciales y sin ninguna gobernanza compartida.

Microsoft Foundry acaba de lanzar [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) en preview pública, y es una respuesta directa a ese problema.

## ¿Qué es un Toolbox?

Un Toolbox es un bundle de herramientas con nombre, reutilizable, que defines una vez en Foundry y expones a través de un único endpoint compatible con MCP. Cualquier runtime de agente que hable MCP puede consumirlo — no estás bloqueado en Foundry Agents.

La propuesta es simple: **build once, consume anywhere**. Define las herramientas, configura la autenticación de forma centralizada (OAuth passthrough, identidad administrada de Entra), publica el endpoint. Cada agente que necesite esas herramientas se conecta al endpoint y las obtiene todas.

Sin configuración por herramienta. Sin gestión de credenciales por agente.

## Los cuatro pilares (dos disponibles hoy)

| Pilar | Estado | Qué hace |
|-------|--------|----------|
| **Discover** | Próximamente | Encuentra herramientas aprobadas sin buscar manualmente |
| **Build** | Disponible hoy | Agrupa herramientas en un bundle reutilizable |
| **Consume** | Disponible hoy | Un único endpoint MCP expone todas las herramientas |
| **Govern** | Próximamente | Auth centralizada + observabilidad en todas las llamadas |

Hoy el foco está en Build y Consume. Suficiente para eliminar la fricción más inmediata.

## Empezando en la práctica

El SDK es Python primero por ahora. Comienzas creando un `AIProjectClient` y luego construyes un toolbox:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

Luego creas una versión del toolbox con las herramientas que quieres agrupar:

```python
toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Buscar en documentación y responder a issues de GitHub.",
    tools=[
        {"type": "web_search", "description": "Buscar documentación pública"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Una vez publicado, Foundry te da un endpoint unificado que cualquier runtime MCP puede consumir. Un punto de conexión, todas las herramientas.

## No estás bloqueado en Foundry Agents

Los Toolboxes se **crean y gestionan** en Foundry, pero la superficie de consumo es el protocolo MCP abierto. Puedes usarlos desde agentes personalizados con Microsoft Agent Framework o LangGraph, GitHub Copilot y otros IDEs compatibles con MCP, o cualquier runtime que hable MCP.

## Por qué importa ahora

La ola de multi-agentes está llegando a producción. Los equipos están construyendo 5, 10, 20 agentes — y el problema de la configuración de herramientas escala rápido. Cada nuevo agente es una nueva superficie para configuración duplicada, credenciales desactualizadas y comportamiento inconsistente.

Los Toolboxes no resuelven la gobernanza y el discovery todavía (esos pilares están por venir), pero la base de Build + Consume es suficiente para empezar a centralizar. Cuando llegue el pilar Govern, tendrás una capa de herramientas observable y controlada centralmente para toda tu flota de agentes.

## Conclusión

Esto es pronto — preview pública, SDK Python primero, con Discover y Govern todavía por llegar. Pero el modelo es sólido, y el diseño nativo de MCP significa que funciona con las herramientas que ya estás construyendo. Echa un vistazo al [anuncio oficial](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) para empezar.
