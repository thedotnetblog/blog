---
title: "Cosmos DB Shell Está en Vista Previa Pública — Y Tiene un Servidor MCP Integrado"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell es una nueva CLI de código abierto que expone los comandos de la base de datos como herramientas MCP. Tus agentes de IA pueden navegar por contenedores, ejecutar consultas y gestionar datos usando la misma interfaz que usas tú."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Si alguna vez has tenido que ir y venir entre una pestaña del portal, una muestra de SDK y un script a medio terminar solo para responder una pregunta de Cosmos DB, ya conoces la fricción que este proyecto está diseñado para eliminar.

Azure Cosmos DB Shell acaba de entrar en vista previa pública. Es una CLI de código abierto con sintaxis tipo bash y — la parte que lo hace interesante — un servidor MCP integrado.

## Qué lo Hace Diferente de Otras CLIs de Base de Datos

La CLI en sí es útil: comandos familiares, soporte para scripts, integración CI/CD. Esa parte es lo mínimo esperado para una herramienta de base de datos orientada a desarrolladores.

La parte interesante es la integración del servidor MCP. Cada comando que expone la CLI se convierte en una herramienta MCP que tus agentes de IA pueden llamar. No hay ninguna capa de API personalizada, ni código de integración que escribir. Tu agente puede:

- Navegar por las jerarquías de bases de datos con `cd`, `ls`, `pwd`
- Ejecutar consultas SQL con `query` y obtener resultados estructurados
- Crear y modificar elementos con `create item`, `update`, `rm`
- Gestionar bases de datos y contenedores con `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Inspeccionar el contexto actual con `endpoint`, `pwd`

El cambio clave: tu agente no está hablando con una API de Cosmos DB — está hablando con la misma interfaz de shell que usas tú. Los comandos son deterministas, auditables y de código abierto para que puedas inspeccionar exactamente qué está pasando.

## La Base de Código Abierto Importa

Esto no es un servicio gestionado de caja negra. El shell es de código abierto, lo que significa:

- Los equipos de seguridad pueden auditar la implementación
- Los equipos de plataforma pueden hacer fork y ampliarlo para sus estándares específicos
- Los desarrolladores pueden contribuir con mejoras que beneficien a todos

Para los equipos empresariales que adoptan herramientas de IA, "¿podemos ver exactamente cómo funciona?" es cada vez menos un requisito opcional. El código abierto aquí es un diferenciador significativo.

## Tres Escenarios que Se Vuelven Más Fáciles

**Análisis inteligente de datos** — conecta un agente al shell, haz preguntas en lenguaje natural, obtén resultados de consultas estructurados. El agente se encarga de la construcción de la consulta; el shell se encarga de la ejecución.

**Gestión autónoma de datos** — los flujos de trabajo que necesitan crear, actualizar o eliminar datos en Cosmos DB pueden hacerlo a través de las herramientas MCP sin necesitar una integración personalizada.

**Supervisión y alertas en tiempo real** — un agente puede consultar contenedores periódicamente, comparar resultados y mostrar anomalías a través del canal de notificación que tenga sentido.

La interfaz MCP hace que estos escenarios sean composables con cualquier plataforma de IA que hable MCP — no solo las herramientas de Microsoft.

## Para Empezar

El shell está en vista previa pública. Instálalo, configura tu conexión de Cosmos DB y habilita el servidor MCP. Desde allí, cualquier host de agente compatible con MCP puede descubrir y usar las herramientas.

Post original: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
