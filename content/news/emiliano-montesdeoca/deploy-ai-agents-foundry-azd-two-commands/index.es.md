---
title: "Del portátil a producción: desplegando agentes de IA en Microsoft Foundry con dos comandos"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "El Azure Developer CLI ahora tiene comandos 'azd ai agent' que llevan tu agente de IA desde el desarrollo local a un endpoint en Foundry en minutos. Aquí está el flujo de trabajo completo."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

¿Conoces esa brecha entre "funciona en mi máquina" y "está desplegado y sirviendo tráfico"? Para agentes de IA, esa brecha ha sido dolorosamente amplia. Necesitas provisionar recursos, desplegar modelos, configurar identidad, montar monitoreo — y eso es antes de que alguien pueda realmente llamar a tu agente.

El Azure Developer CLI acaba de convertir esto en [un asunto de dos comandos](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## El nuevo flujo de trabajo `azd ai agent`

Déjame mostrarte cómo se ve esto realmente. Tienes un proyecto de agente de IA — digamos un agente concierge de hotel. Funciona localmente. Quieres que corra en Microsoft Foundry.

```bash
azd ai agent init
azd up
```

Eso es todo. Dos comandos. `azd ai agent init` genera la infraestructura como código en tu repositorio, y `azd up` provisiona todo en Azure y publica tu agente. Obtienes un enlace directo a tu agente en el portal de Foundry.

## Qué pasa por debajo

El comando `init` genera plantillas Bicep reales e inspeccionables en tu repositorio:

- Un **Foundry Resource** (contenedor de nivel superior)
- Un **Foundry Project** (donde vive tu agente)
- Configuración de **despliegue de modelo** (GPT-4o, etc.)
- **Identidad administrada** con asignaciones de roles RBAC apropiadas
- `azure.yaml` para el mapa de servicios
- `agent.yaml` con metadatos del agente y variables de entorno

La parte clave: todo esto es tuyo. Es Bicep versionado en tu repositorio. Puedes inspeccionarlo, personalizarlo y hacer commit junto con el código de tu agente. Sin cajas negras mágicas.

## El ciclo interno de desarrollo

Lo que realmente me gusta es la historia de desarrollo local. Cuando estás iterando sobre la lógica del agente, no quieres redesplegar cada vez que cambias un prompt:

```bash
azd ai agent run
```

Esto inicia tu agente localmente. Combínalo con `azd ai agent invoke` para enviar prompts de prueba, y tienes un ciclo de retroalimentación rápido. Editar código, reiniciar, invocar, repetir.

El comando `invoke` es inteligente con el enrutamiento también — cuando un agente local está corriendo, lo apunta automáticamente. Cuando no, apunta al endpoint remoto.

## Monitoreo en tiempo real

Esta es la característica que me convenció. Una vez que tu agente está desplegado:

```bash
azd ai agent monitor --follow
```

Cada petición y respuesta que fluye a través de tu agente se transmite a tu terminal en tiempo real. Para depurar problemas en producción, esto es invaluable. Sin buscar en log analytics, sin esperar a que las métricas se agreguen — ves lo que está pasando ahora mismo.

## El set completo de comandos

Aquí la referencia rápida:

| Comando | Qué hace |
|---------|----------|
| `azd ai agent init` | Genera un proyecto de agente Foundry con IaC |
| `azd up` | Provisiona recursos Azure y despliega el agente |
| `azd ai agent invoke` | Envía prompts al agente remoto o local |
| `azd ai agent run` | Ejecuta el agente localmente para desarrollo |
| `azd ai agent monitor` | Transmite logs en tiempo real del agente publicado |
| `azd ai agent show` | Verifica la salud y estado del agente |
| `azd down` | Limpia todos los recursos Azure |

## Por qué esto importa para desarrolladores .NET

Aunque el ejemplo del anuncio está basado en Python, la historia de infraestructura es agnóstica al lenguaje. Tu agente .NET obtiene el mismo scaffolding Bicep, la misma configuración de identidad administrada, el mismo pipeline de monitoreo. Y si ya estás usando `azd` para tus apps .NET Aspire o despliegues Azure, esto encaja directamente en tu flujo de trabajo existente.

La brecha de despliegue para agentes de IA ha sido uno de los mayores puntos de fricción en el ecosistema. Pasar de un prototipo funcional a un endpoint de producción con identidad, networking y monitoreo adecuados no debería requerir una semana de trabajo DevOps. Ahora requiere dos comandos y unos minutos.

## Para cerrar

`azd ai agent` está disponible ahora. Si has estado posponiendo el despliegue de tus agentes de IA porque la configuración de infraestructura parecía demasiado trabajo, dale una oportunidad. Revisa el [tutorial completo](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) para el paso a paso completo incluyendo integración de app de chat frontend.
