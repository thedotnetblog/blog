---
title: "GPT-5.5 Ya Está Aquí en Azure Foundry — Lo que los Desarrolladores .NET Necesitan Saber"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 ya está disponible en Microsoft Foundry. La progresión desde GPT-5 hasta 5.5, qué mejoró realmente y cómo empezar a usarlo en tus agentes hoy."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Microsoft acaba de anunciar que [GPT-5.5 ya está disponible en Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Si has estado construyendo agentes en Azure, esta es la actualización que esperabas.

## La progresión de GPT-5

No es solo un incremento de versión:

- **GPT-5**: unificó razonamiento y velocidad en un solo sistema
- **GPT-5.4**: razonamiento multi-paso más robusto, capacidades agénticas tempranas para empresas
- **GPT-5.5**: razonamiento de largo contexto más profundo, ejecución agéntica más fiable, mayor eficiencia de tokens

## Qué cambió realmente

**Mejor codificación agéntica**: GPT-5.5 mantiene el contexto a través de grandes bases de código, diagnostica fallos arquitectónicos y anticipa requisitos de pruebas. El modelo razona sobre *qué más* afecta una corrección antes de actuar.

**Eficiencia de tokens**: Salidas de mayor calidad con menos tokens y menos reintentos. Esto se traduce directamente en menor costo y latencia en producción.

**Análisis de largo contexto**: Maneja documentos extensos, bases de código y historiales multi-sesión sin perder el hilo.

## Precios

| Modelo | Entrada ($/M tokens) | Entrada en caché | Salida ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## Por qué importa Foundry

Foundry Agent Service permite definir agentes en YAML o conectarlos con Microsoft Agent Framework, GitHub Copilot SDK, LangGraph o el SDK de OpenAI Agents — y ejecutarlos como agentes hospedados aislados con sistema de archivos persistente, identidad de Microsoft Entra y precios de escala a cero.

## Cómo empezar

```csharp
// C# — solo actualiza el nombre del modelo
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Eres un asistente útil.", name: "MiAgente");
```

Consulta el [anuncio completo](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) para los detalles completos.
