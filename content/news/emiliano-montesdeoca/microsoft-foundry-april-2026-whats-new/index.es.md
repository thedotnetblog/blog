---
title: "Microsoft Foundry Abril 2026: Foundry Local GA, GPT-5.5, CodeAct con Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "El resumen de Foundry de abril es importante: Foundry Local alcanza GA, llega GPT-5.5, Agent Framework obtiene trazado OpenTelemetry, CodeAct ejecuta Python en micro-VMs Hyperlight, y llega el Panel de Monitoreo de Agentes."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Un mes ocupado para Microsoft Foundry. Estos son los anuncios más importantes.

## Foundry Local Está Disponible de Forma General

Foundry Local — el runtime de IA local multiplataforma de Microsoft — pasa de vista previa a GA en Windows, macOS (Apple Silicon) y Linux x64. Inferencia de modelos locales lista para producción con un SDK amigable para desarrolladores. La versión 1.1 agrega soporte para transcripción, embeddings y la API Responses.

## GPT-5.5

El último modelo de la familia GPT-5 ya está disponible en Foundry. Cuota predeterminada para suscripciones Tier 5 y Tier 6. Si has estado trabajando con variantes anteriores de GPT-5, vale la pena evaluarlo para tus casos de uso.

## Trazado de Agent Framework en Foundry

Dos características de trazado se incluyen en vista previa este mes:

**Trazado de Microsoft Agent Framework** — Los agentes MAF ahora pueden emitir trazas OpenTelemetry en Foundry. Depura el comportamiento de los agentes, rastrea la ejecución de múltiples pasos, detecta latencia y errores en llamadas a herramientas. Esto llena un vacío real: saber *qué hizo realmente tu agente* en producción, no solo qué devolvió.

**Trazado de agentes hospedados** — Las sesiones, llamadas a herramientas y pasos de ejecución de los agentes hospedados también aparecen en las trazas de Foundry. La misma historia de observabilidad extendida al nivel hospedado.

## CodeAct con Hyperlight (Alpha)

Esta es la adición técnicamente más interesante: Agent Framework ahora puede ejecutar código Python dentro de micro-máquinas virtuales [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct es el patrón donde un agente genera y ejecuta código Python como herramienta. La preocupación obvia es la seguridad: estás ejecutando código generado por el modelo. Las micro-VMs de Hyperlight proporcionan aislamiento a nivel de proceso con tiempo de inicio cercano al nativo, haciendo que la ejecución de código en sandbox sea práctica sin la sobrecarga de contenedores o VMs completos.

Para flujos de trabajo agenticos donde la ejecución de código es necesaria, esto es una mejora de seguridad significativa sobre ejecutar código en el proceso host.

## Panel de Monitoreo de Agentes (Vista Previa)

Un panel de operaciones unificado que combina uso de tokens, latencia, tasa de éxito de ejecución y puntuaciones de evaluadores en una sola vista. La distinción de los paneles de observabilidad regulares: incluye resultados de evaluación junto con métricas operativas, por lo que puedes correlacionar "el agente es más lento" con "las puntuaciones del evaluador cayeron" — o confirmar que no están relacionados.

## Evaluadores Personalizados de Evaluación Continua (Vista Previa)

Ahora puedes traer tus propios evaluadores basados en código o en prompts a los pipelines de evaluación continua. Anteriormente, la evaluación continua estaba limitada a evaluadores integrados. Los evaluadores personalizados te permiten hacer cumplir criterios de calidad específicos del equipo en tu bucle de monitoreo de producción.

## Inventario de Agentes en el Plano de Control

La vista Operate del Plano de Control de Foundry ahora muestra todos los agentes compatibles en una suscripción: agentes de Foundry, Azure SRE Agent, bucles de agentes de Logic Apps y agentes personalizados registrados. Una vista para entender qué está desplegado y dónde.

Publicación original: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
