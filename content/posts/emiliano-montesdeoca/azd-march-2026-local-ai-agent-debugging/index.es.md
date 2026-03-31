---
title: "azd ahora te permite ejecutar y depurar agentes IA localmente — Esto es lo que cambió en marzo 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "El Azure Developer CLI publicó siete versiones en marzo 2026. Lo destacado: un bucle local de ejecución y depuración para agentes IA, integración con GitHub Copilot en la configuración de proyectos, y soporte para Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}}).*

Siete versiones en un mes. Eso es lo que el equipo del Azure Developer CLI (`azd`) publicó en marzo 2026, y la función estrella es la que estaba esperando: **un bucle local de ejecución y depuración para agentes IA**.

PC Chan [publicó el resumen completo](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), y aunque hay mucho contenido, déjame filtrarlo a lo que realmente importa para desarrolladores .NET que construyen apps con IA.

## Ejecutar y depurar agentes IA sin desplegar

Esta es la grande. La nueva extensión `azure.ai.agents` añade un conjunto de comandos que te dan una experiencia de bucle interno adecuada para agentes IA:

- `azd ai agent run` — inicia tu agente localmente
- `azd ai agent invoke` — le envía mensajes (local o desplegado)
- `azd ai agent show` — muestra el estado del contenedor y su salud
- `azd ai agent monitor` — transmite logs del contenedor en tiempo real

Antes, probar un agente IA significaba desplegarlo en Microsoft Foundry cada vez que hacías un cambio. Ahora puedes iterar localmente, probar el comportamiento de tu agente, y solo desplegarlo cuando estés listo. Si has estado construyendo agentes con el Microsoft Agent Framework o Semantic Kernel, esto cambia tu flujo de trabajo diario.

El comando invoke funciona tanto contra agentes locales como desplegados, lo que significa que puedes usar el mismo flujo de pruebas sin importar dónde esté corriendo el agente. Ese es el tipo de detalle que te ahorra mantener dos conjuntos de scripts de prueba.

## GitHub Copilot configura tu proyecto azd

`azd init` ahora ofrece una opción "Set up with GitHub Copilot (Preview)". En lugar de responder prompts manualmente sobre la estructura de tu proyecto, un agente Copilot genera la configuración por ti. Verifica que el directorio de trabajo esté limpio antes de modificar archivos y pide consentimiento de herramientas MCP por adelantado.

Cuando un comando falla, `azd` ahora ofrece troubleshooting asistido por IA: elige una categoría (explicar, guiar, solucionar o saltar), deja que el agente sugiera una corrección, y reintenta — todo sin salir de la terminal. Para configuraciones de infraestructura complejas, eso ahorra tiempo real.

## Container App Jobs y mejoras de despliegue

Algunas funciones de despliegue que vale la pena mencionar:

- **Container App Jobs**: `azd` ahora despliega `Microsoft.App/jobs` a través de la configuración existente `host: containerapp`. Tu plantilla Bicep determina si el destino es un Container App o un Job — sin configuración extra.
- **Timeouts configurables**: Nueva flag `--timeout` en `azd deploy` y un campo `deployTimeout` en `azure.yaml`. Sin más adivinanzas sobre el límite predeterminado de 1200 segundos.
- **Fallback de build remoto**: Cuando falla el build remoto en ACR, `azd` hace fallback automático a Docker/Podman local.
- **Validación preflight local**: Los parámetros de Bicep se validan localmente antes de desplegar, detectando parámetros faltantes sin un viaje de ida y vuelta a Azure.

## Pulido en la experiencia de desarrollador

Algunas mejoras más pequeñas que se suman:

- **Detección automática de pnpm/yarn** para proyectos JS/TS
- **Soporte para pyproject.toml** para paquetes Python
- **Directorios de plantillas locales** — `azd init --template` ahora acepta rutas del sistema de archivos para iteración offline
- **Mejores mensajes de error** en modo `--no-prompt` — todos los valores faltantes reportados de una vez con comandos de resolución
- **Variables de entorno de build** inyectadas en todos los subprocesos de build (.NET, Node.js, Java, Python)

La última es sutil pero importante: tu build .NET ahora tiene acceso a las variables de entorno de `azd`, lo que significa que puedes hacer inyección de configuración en tiempo de compilación sin scripting adicional.

## Para cerrar

El bucle de depuración local de agentes IA es la estrella de esta versión, pero la acumulación de mejoras de despliegue y refinamiento de DX hace que `azd` se sienta más maduro que nunca. Si estás desplegando apps .NET en Azure — especialmente agentes IA — esta actualización vale la pena.

Revisa las [notas completas de la versión](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) para todos los detalles, o comienza con [la instalación de azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).
