---
title: "Microsoft Agent Framework Llega a 1.0 — Esto Es Lo Que Realmente Importa para Desarrolladores .NET"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0 está listo para producción con APIs estables, orquestación multi-agente y conectores para todos los principales proveedores de IA. Esto es lo que necesitas saber como desarrollador .NET."
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "agent-framework-1-0-production-ready.md" >}}).*

Si has estado siguiendo el camino de Agent Framework desde los primeros días de Semantic Kernel y AutoGen, esto es importante. Microsoft Agent Framework acaba de [llegar a la versión 1.0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) — listo para producción, APIs estables, compromiso de soporte a largo plazo. Está disponible tanto para .NET como para Python, y está genuinamente preparado para cargas de trabajo reales.

Voy a cortar el ruido del anuncio y centrarme en lo que importa si estás construyendo apps con IA usando .NET.

## La versión corta

Agent Framework 1.0 unifica lo que solían ser Semantic Kernel y AutoGen en un único SDK de código abierto. Una abstracción de agente. Un motor de orquestación. Múltiples proveedores de IA. Si has estado saltando entre Semantic Kernel para patrones empresariales y AutoGen para flujos de trabajo multi-agente de nivel investigación, puedes parar. Este es el único SDK ahora.

## Empezar es casi injustamente simple

Aquí tienes un agente funcional en .NET:

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

Eso es todo. Un puñado de líneas y tienes un agente de IA ejecutándose contra Azure Foundry. El equivalente en Python es igual de conciso. Añade herramientas de funciones, conversaciones multi-turno y streaming a medida que avanzas — la superficie de la API escala sin volverse rara.

## Orquestación multi-agente — esto va en serio

Los agentes individuales están bien para demos, pero los escenarios de producción generalmente necesitan coordinación. Agent Framework 1.0 viene con patrones de orquestación probados en batalla directamente de Microsoft Research y AutoGen:

- **Secuencial** — los agentes procesan en orden (escritor → revisor → editor)
- **Concurrente** — distribuye a múltiples agentes en paralelo, converge resultados
- **Handoff** — un agente delega a otro basándose en la intención
- **Chat grupal** — múltiples agentes discuten y convergen en una solución
- **Magentic-One** — el patrón multi-agente de nivel investigación de MSR

Todos soportan streaming, checkpointing, aprobaciones con humano en el bucle, y pausa/reanudación. La parte de checkpointing es crucial — los flujos de trabajo de larga duración sobreviven a reinicios de proceso. Para nosotros los desarrolladores .NET que hemos construido flujos de trabajo durables con Azure Functions, esto se siente familiar.

## Las funcionalidades que más importan

Aquí va mi lista de lo que vale la pena saber:

**Hooks de middleware.** ¿Sabes cómo ASP.NET Core tiene pipelines de middleware? Mismo concepto, pero para la ejecución de agentes. Intercepta cada etapa — añade seguridad de contenido, logging, políticas de cumplimiento — sin tocar los prompts del agente. Así es como haces que los agentes estén listos para empresa.

**Memoria conectable.** Historial conversacional, estado persistente clave-valor, recuperación basada en vectores. Elige tu backend: Foundry Agent Service, Mem0, Redis, Neo4j, o crea el tuyo propio. La memoria es lo que convierte una llamada LLM sin estado en un agente que realmente recuerda el contexto.

**Agentes declarativos en YAML.** Define las instrucciones de tu agente, herramientas, memoria y topología de orquestación en archivos YAML versionados. Carga y ejecuta con una sola llamada a la API. Esto es un cambio radical para equipos que quieren iterar en el comportamiento del agente sin redesplegar código.

**Soporte A2A y MCP.** MCP (Model Context Protocol) permite a los agentes descubrir e invocar herramientas externas dinámicamente. A2A (protocolo Agent-to-Agent) habilita la colaboración entre runtimes — tus agentes .NET pueden coordinarse con agentes ejecutándose en otros frameworks. El soporte para A2A 1.0 llegará pronto.

## Las funcionalidades en preview que vale la pena seguir

Algunas funcionalidades se lanzaron como preview en 1.0 — funcionales pero las APIs pueden evolucionar:

- **DevUI** — un depurador local basado en navegador para visualizar la ejecución del agente, flujos de mensajes y llamadas a herramientas en tiempo real. Piensa en Application Insights, pero para el razonamiento del agente.
- **GitHub Copilot SDK y Claude Code SDK** — usa Copilot o Claude como un harness de agente directamente desde tu código de orquestación. Compón un agente capaz de programar junto a tus otros agentes en el mismo flujo de trabajo.
- **Agent Harness** — un runtime local personalizable que da a los agentes acceso a shell, sistema de archivos y bucles de mensajería. Piensa en agentes de programación y patrones de automatización.
- **Skills** — paquetes reutilizables de capacidades de dominio que dan a los agentes capacidades estructuradas listas para usar.

## Migrando desde Semantic Kernel o AutoGen

Si tienes código existente de Semantic Kernel o AutoGen, hay asistentes de migración dedicados que analizan tu código y generan planes de migración paso a paso. La [guía de migración de Semantic Kernel](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel) y la [guía de migración de AutoGen](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen) te guían a través de todo.

Si has estado en los paquetes RC, actualizar a 1.0 es solo un cambio de versión.

## Para cerrar

Agent Framework 1.0 es el hito de producción que los equipos empresariales han estado esperando. APIs estables, soporte multi-proveedor, patrones de orquestación que realmente funcionan a escala, y rutas de migración desde tanto Semantic Kernel como AutoGen.

El framework es [completamente open source en GitHub](https://github.com/microsoft/agent-framework), y puedes empezar hoy con `dotnet add package Microsoft.Agents.AI`. Echa un vistazo a la [guía de inicio rápido](https://learn.microsoft.com/en-us/agent-framework/get-started/) y los [ejemplos](https://github.com/microsoft/agent-framework) para ponerte manos a la obra.

Si has estado esperando la señal de "seguro para usar en producción" — esta es.
