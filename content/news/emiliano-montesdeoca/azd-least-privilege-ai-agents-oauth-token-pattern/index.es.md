---
title: "Tu Agente de IA Tiene un Problema de Identidad (Y Aquí Está la Plantilla que lo Resuelve)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Una nueva plantilla azd de Curity y Microsoft muestra cómo construir agentes de IA que usan tokens OAuth de corta duración con ámbitos de grano fino — para que los agentes nunca puedan ver datos que no deberían ver."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Hay un momento en cada proyecto de agente de IA que va más o menos así: la demo funciona perfectamente, el agente interpreta el lenguaje natural, llama a las API correctas, devuelve los datos correctos. Entonces empiezas a pensar en los usuarios reales.

¿Qué impide que la sesión del agente de un usuario vea los datos de otro usuario? ¿Qué pasa si el agente es engañado a través de inyección de prompts? ¿Qué pasa si llama a una herramienta de una manera inesperada?

Estos no son casos extremos. Son decisiones de diseño que debes tomar antes de lanzar.

Una nueva plantilla `azd` de Curity y Microsoft te da una referencia funcional para exactamente este problema.

## El Problema Central: Autenticación ≠ Autorización

La mayoría de las muestras de agentes gestionan bien la autenticación de usuarios. Gestionan mal la autorización. Saber *quién* es el usuario no te dice *qué datos* debería ver.

Una aplicación cliente tradicional hace llamadas de API predecibles. Un agente de IA es no determinista — interpreta el lenguaje natural y decide a quién llamar. Puede ser creativo. También puede estar equivocado. Y si es manipulado a través de inyección de prompts, necesitas reglas que no dependan de que la IA se comporte bien.

La solución que demuestra esta plantilla: **tokens de corta duración que transportan exactamente la información correcta para cada salto**.

## Cómo Funciona la Cadena de Tokens

La plantilla usa tokens de acceso OAuth 2.0 con intercambio de tokens para reducir los permisos en cada paso. Un token de usuario se intercambia dos veces antes de llegar al servidor MCP:

1. **Primer intercambio** — reduce el ámbito y convierte el token opaco en un JWT
2. **Segundo intercambio** — añade la identidad del agente y una nueva audiencia para el salto del servidor MCP

Cómo luce el token del servidor MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

El `customer_id` está integrado en el token por el servidor de autorización, no se pasa como un parámetro que controla el agente. La API comprueba el token, no las instrucciones del agente.

Esto significa: incluso si alguien engaña al agente para que intente obtener los datos de otro cliente, el token no lo autorizará.

## Qué Despliega la Plantilla

Con unos pocos comandos `azd` obtienes:

- Un agente backend en Microsoft Foundry (C#, SDK de Microsoft A2A y MCP)
- Un servidor MCP que expone una API de cartera de muestra
- Curity Identity Server como servidor de autorización, junto con Entra ID para la autenticación
- Pasarelas de API externas e internas que gestionan el intercambio de tokens y el registro de auditoría
- Bicep para toda la infraestructura Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, almacenamiento

Todo el patrón es inspeccionable y personalizable.

## El Principio de Diseño que Vale la Pena Adoptar

Incluso si no usas Curity, el patrón es transferible: **los agentes nunca deberían tener acceso permanente a la API**. Cada acción debería usar un token de corta duración con el mínimo ámbito necesario para esa llamada específica, emitido para la identidad específica del agente, llevando las afirmaciones que la API necesita para tomar decisiones de autorización.

Esto resiste agentes creativos, errores e inyección de prompts de maneras que "asegúrate de que el agente no haga cosas malas" nunca lo hará.

## Conclusión

Los patrones de seguridad para agentes de IA todavía se están definiendo en toda la industria. Esta plantilla es una de las implementaciones de referencia más completas que he visto — cubre el flujo de autorización real, no solo la autenticación.

Post original: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
