---
title: "Conecta tus servidores MCP en Azure Functions a Foundry Agents — Así es como"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Construye tu servidor MCP una vez, despliégalo en Azure Functions y conéctalo a agentes de Microsoft Foundry con autenticación adecuada. Tus herramientas funcionan en todas partes — VS Code, Cursor y ahora agentes de IA empresariales."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}}).*

Esto es algo que me encanta del ecosistema MCP: construyes tu servidor una vez y funciona en todas partes. VS Code, Visual Studio, Cursor, ChatGPT — cada cliente MCP puede descubrir y usar tus herramientas. Ahora, Microsoft está añadiendo otro consumidor a esa lista: los agentes de Foundry.

Lily Ma del equipo de Azure SDK [publicó una guía práctica](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) sobre cómo conectar servidores MCP desplegados en Azure Functions con agentes de Microsoft Foundry. Si ya tienes un servidor MCP, esto es puro valor agregado — no necesitas reconstruir nada.

## Por qué esta combinación tiene sentido

Azure Functions te da infraestructura escalable, autenticación integrada y facturación serverless para alojar servidores MCP. Microsoft Foundry te da agentes de IA que pueden razonar, planificar y tomar acciones. Conectar ambos significa que tus herramientas personalizadas — consultar una base de datos, llamar a una API de negocio, ejecutar lógica de validación — se convierten en capacidades que los agentes de IA empresariales pueden descubrir y usar de forma autónoma.

El punto clave: tu servidor MCP se mantiene igual. Solo estás añadiendo Foundry como otro consumidor. Las mismas herramientas que funcionan en tu configuración de VS Code ahora potencian un agente de IA con el que tu equipo o clientes interactúan.

## Opciones de autenticación

Aquí es donde el post realmente aporta valor. Cuatro métodos de autenticación según tu escenario:

| Método | Caso de uso |
|--------|-------------|
| **Basado en clave** (predeterminado) | Desarrollo o servidores sin autenticación Entra |
| **Microsoft Entra** | Producción con identidades administradas |
| **Passthrough de identidad OAuth** | Producción donde cada usuario se autentica individualmente |
| **Sin autenticación** | Desarrollo/pruebas o solo datos públicos |

Para producción, Microsoft Entra con identidad del agente es el camino recomendado. El passthrough de identidad OAuth es para cuando el contexto del usuario importa — el agente pide a los usuarios que inicien sesión, y cada solicitud lleva el token propio del usuario.

## Configurándolo

El flujo general:

1. **Despliega tu servidor MCP en Azure Functions** — hay ejemplos disponibles para [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript y Java
2. **Habilita la autenticación MCP integrada** en tu function app
3. **Obtén tu URL de endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Añade el servidor MCP como herramienta en Foundry** — navega a tu agente en el portal, añade una nueva herramienta MCP, proporciona endpoint y credenciales

Luego pruébalo en el playground de Agent Builder enviando un prompt que active una de tus herramientas.

## Mi opinión

La historia de composabilidad aquí se está volviendo realmente fuerte. Construye tu servidor MCP una vez en .NET (o Python, TypeScript, Java), despliégalo en Azure Functions, y cada cliente compatible con MCP puede usarlo — herramientas de programación, apps de chat, y ahora agentes de IA empresariales. Es un patrón de "escribe una vez, usa en todas partes" que realmente funciona.

Para desarrolladores .NET específicamente, la [extensión MCP de Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) hace esto sencillo. Defines tus herramientas como Azure Functions, despliegas, y tienes un servidor MCP de nivel producción con toda la seguridad y escalabilidad que Azure Functions proporciona.

## Para cerrar

Si tienes herramientas MCP ejecutándose en Azure Functions, conectarlas a agentes de Foundry es una victoria rápida — tus herramientas personalizadas se convierten en capacidades de IA empresarial con autenticación adecuada y sin cambios de código en el servidor.

Lee la [guía completa](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) para instrucciones paso a paso sobre cada método de autenticación, y consulta la [documentación detallada](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) para configuraciones de producción.
