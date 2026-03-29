---
title: "El MCP Server de Azure DevOps llega a Microsoft Foundry: Qué significa para tus agentes de IA"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "El MCP Server de Azure DevOps ya está disponible en Microsoft Foundry. Conecta tus agentes de IA directamente a flujos de trabajo de DevOps — work items, repos, pipelines — con unos pocos clics."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) está teniendo su momento. Si has estado siguiendo el ecosistema de agentes de IA, probablemente hayas notado que los servidores MCP están apareciendo por todas partes — dándoles a los agentes la capacidad de interactuar con herramientas y servicios externos a través de un protocolo estandarizado.

Ahora el [MCP Server de Azure DevOps está disponible en Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), y esta es una de esas integraciones que te hace pensar en las posibilidades prácticas.

## Qué está pasando realmente aquí

Microsoft ya lanzó el MCP Server de Azure DevOps como [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — ese es el servidor MCP en sí. Lo nuevo es la integración con Foundry. Ahora puedes agregar el MCP Server de Azure DevOps a tus agentes de Foundry directamente desde el catálogo de herramientas.

Para los que no están familiarizados con Foundry todavía: es la plataforma unificada de Microsoft para construir y gestionar aplicaciones y agentes impulsados por IA a escala. Acceso a modelos, orquestación, evaluación, despliegue — todo en un solo lugar.

## Configurándolo

La configuración es sorprendentemente sencilla:

1. En tu agente de Foundry, ve a **Add Tools** > **Catalog**
2. Busca "Azure DevOps"
3. Selecciona el Azure DevOps MCP Server (preview) y haz clic en **Create**
4. Ingresa el nombre de tu organización y conecta

Eso es todo. Tu agente ahora tiene acceso a las herramientas de Azure DevOps.

## Controlando a qué puede acceder tu agente

Esta es la parte que aprecio: no estás atrapado con un enfoque de todo o nada. Puedes especificar qué herramientas están disponibles para tu agente. Así que si solo quieres que lea work items pero no toque pipelines, puedes configurar eso. Principio de mínimo privilegio, aplicado a tus agentes de IA.

Esto importa para escenarios empresariales donde no quieres que un agente accidentalmente dispare un pipeline de despliegue porque alguien le pidió que "ayude con el release."

## Por qué esto es interesante para equipos .NET

Piensa en lo que esto habilita en la práctica:

- **Asistentes de planificación de sprint** — agentes que pueden obtener work items, analizar datos de velocidad y sugerir capacidad de sprint
- **Bots de code review** — agentes que entienden el contexto de tu PR porque realmente pueden leer tus repos y work items vinculados
- **Respuesta a incidentes** — agentes que pueden crear work items, consultar despliegues recientes y correlacionar bugs con cambios recientes
- **Onboarding de desarrolladores** — "¿En qué debería trabajar?" obtiene una respuesta real respaldada por datos reales del proyecto

Para equipos .NET que ya usan Azure DevOps para sus pipelines de CI/CD y gestión de proyectos, tener un agente de IA que pueda interactuar directamente con esos sistemas es un paso significativo hacia la automatización útil (no solo chatbot-como-servicio).

## El panorama más amplio de MCP

Esto es parte de una tendencia más amplia: los servidores MCP se están convirtiendo en la forma estándar en que los agentes de IA interactúan con el mundo exterior. Los estamos viendo para GitHub, Azure DevOps, bases de datos, APIs SaaS — y Foundry se está convirtiendo en el hub donde todas estas conexiones se unen.

Si estás construyendo agentes en el ecosistema .NET, vale la pena prestar atención a MCP. El protocolo está estandarizado, las herramientas están madurando, y la integración con Foundry lo hace accesible sin tener que conectar manualmente las conexiones del servidor.

## Para cerrar

El MCP Server de Azure DevOps en Foundry está en preview, así que espera que evolucione. Pero el flujo de trabajo principal es sólido: conectar, configurar acceso a herramientas, y dejar que tus agentes trabajen con tus datos de DevOps. Si ya estás en el ecosistema de Foundry, esto está a unos pocos clics. Dale una oportunidad y ve qué flujos de trabajo puedes construir.

Revisa el [anuncio completo](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) para la configuración paso a paso y más detalles.
