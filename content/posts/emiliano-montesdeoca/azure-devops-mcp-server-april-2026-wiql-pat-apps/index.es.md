---
title: "Actualización de Abril del Azure DevOps MCP Server: Consultas WIQL, Auth PAT y MCP Apps Experimental"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "El Azure DevOps MCP Server recibe consultas de work items con WIQL, autenticación con Personal Access Token, anotaciones MCP, y una característica experimental de MCP Apps que empaqueta flujos de trabajo comunes."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-devops-mcp-server-april-2026-wiql-pat-apps/).*

El Azure DevOps MCP Server sigue mejorando. La actualización de abril de Dan Hellem cubre tanto los servidores local como remoto, y hay algunas adiciones genuinamente útiles.

## Soporte de Consultas WIQL

La nueva herramienta `wit_query_by_wiql` permite ejecutar consultas Work Item Query Language directamente desde tu cliente MCP. Tus sesiones de Copilot pueden ahora obtener conjuntos precisos de work items sin filtrar manualmente.

## Personal Access Tokens en el Servidor Local

El servidor MCP local ahora soporta autenticación PAT — importante para escenarios de integración donde la autenticación interactiva no está disponible.

## Anotaciones MCP en el Servidor Remoto

Etiquetas de metadatos para herramientas de solo lectura, destructivas y de mundo abierto — fundamentales para la fiabilidad de los agentes.

## Consolidación de Herramientas Wiki

5 herramientas separadas de wiki → 2 herramientas más capaces. Menos herramientas = mejor rendimiento del LLM.

## Experimental: MCP Apps

Flujos de trabajo empaquetados que se ejecutan dentro del entorno del servidor MCP. La idea es correcta — más composición de flujos de trabajo en la capa MCP, menos encadenamiento ad-hoc de herramientas.

Post original de Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).
