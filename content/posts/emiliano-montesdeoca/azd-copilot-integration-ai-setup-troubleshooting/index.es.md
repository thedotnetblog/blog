---
title: "azd + GitHub Copilot: Configuración de proyectos con IA y resolución inteligente de errores"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "El Azure Developer CLI ahora se integra con GitHub Copilot para generar la infraestructura de tu proyecto y resolver errores de despliegue — sin salir del terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Este artículo fue traducido automáticamente. Para ver la versión original en inglés, [haz clic aquí]({{< ref "index.md" >}}).*

¿Conoces ese momento en que quieres desplegar una app existente en Azure y te quedas mirando un `azure.yaml` en blanco, intentando recordar si tu API Express debería usar Container Apps o App Service? Ese momento acaba de volverse mucho más corto.

El Azure Developer CLI (`azd`) ahora se integra con GitHub Copilot de dos formas muy concretas: scaffolding asistido por IA durante `azd init`, y resolución inteligente de errores cuando los despliegues fallan. Ambas funciones se quedan completamente en tu terminal, que es exactamente donde quiero que estén.

## Configuración con Copilot durante azd init

Cuando ejecutas `azd init`, ahora aparece la opción "Set up with GitHub Copilot (Preview)". Selecciónala y Copilot analiza tu codebase para generar el `azure.yaml`, las plantillas de infraestructura y los módulos Bicep — basándose en tu código real, no en suposiciones.

```
azd init
# Selecciona: "Set up with GitHub Copilot (Preview)"
```

Para que funcione necesitas:

- **azd 1.23.11 o superior** — comprueba con `azd version` o actualiza con `azd update`
- **Una suscripción activa de GitHub Copilot** (Individual, Business o Enterprise)
- **GitHub CLI (`gh`)** — `azd` pedirá login si es necesario

Lo que me parece genuinamente útil es que funciona en los dos sentidos. ¿Construyendo desde cero? Copilot te ayuda a configurar los servicios Azure correctos desde el principio. ¿Tienes una app existente que llevas tiempo sin desplegar? Apunta Copilot hacia ella y genera la configuración sin que tengas que reestructurar nada.

### Lo que hace realmente

Imagina que tienes una API Express en Node.js con dependencia de PostgreSQL. En lugar de decidir manualmente entre Container Apps o App Service, y luego escribir Bicep desde cero, Copilot detecta tu stack y genera:

- Un `azure.yaml` con los ajustes correctos de `language`, `host` y `build`
- Un módulo Bicep para Azure Container Apps
- Un módulo Bicep para Azure Database for PostgreSQL

Y hace comprobaciones previas antes de tocar nada — verifica que tu directorio git esté limpio, pide consentimiento para las herramientas del servidor MCP. Nada ocurre sin que sepas exactamente qué va a cambiar.

## Resolución de errores potenciada por Copilot

Los errores de despliegue son inevitables. Parámetros faltantes, problemas de permisos, disponibilidad de SKUs — y el mensaje de error raramente te dice lo único que realmente necesitas saber: *cómo solucionarlo*.

Sin Copilot, el ciclo es: copiar el error → buscar en docs → leer tres respuestas irrelevantes de Stack Overflow → ejecutar algunos comandos `az` CLI → volver a intentarlo y rezar. Con Copilot integrado en `azd`, ese ciclo se colapsa. Cuando cualquier comando `azd` falla, ofrece inmediatamente cuatro opciones:

- **Explain** — descripción en lenguaje natural de qué salió mal
- **Guidance** — instrucciones paso a paso para solucionarlo
- **Diagnose and Guide** — análisis completo + Copilot aplica la solución (con tu aprobación) + reintento opcional
- **Skip** — gestionarlo tú mismo

Lo clave: Copilot ya tiene contexto sobre tu proyecto, el comando que falló y la salida del error. Sus sugerencias son específicas para *tu situación*, no documentación genérica.

### Ejemplos reales donde brilla

**Proveedor de recursos no registrado:**
```
ERROR: deployment failed: MissingSubscriptionRegistration:
The subscription is not registered to use namespace 'Microsoft.App'.
```
Esto falla a cualquiera que despliega en una suscripción nueva. Copilot puede registrar el proveedor y relanzar el despliegue automáticamente.

**SKU no disponible:**
```
ERROR: deployment failed: SkuNotAvailable:
The requested VM size 'Standard_D2s_v3' is not available in location 'westus'.
```
Copilot explica qué tamaño de VM o región está bloqueado y sugiere alternativas disponibles en tu suscripción.

**Colisión de nombre de cuenta de almacenamiento:**
```
ERROR: deployment failed: StorageAccountAlreadyTaken:
The storage account named 'myappstorage' is already taken.
```
La unicidad global le pasa a todo el mundo al menos una vez. Copilot sugiere añadir el nombre del entorno o un sufijo aleatorio a tus parámetros Bicep.

### Configurar un comportamiento predeterminado

Si siempre quieres la misma opción, salta el prompt interactivo:

```
azd config set copilot.errorHandling.category troubleshoot
```

Opciones: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. También puedes habilitar auto-fix y reintento:

```
azd config set copilot.errorHandling.fix allow
```

Vuelve al modo interactivo en cualquier momento:

```
azd config unset copilot.errorHandling.category
```

## Por qué importa esto para los desarrolladores .NET

Si estás construyendo en Azure — ya sea una app .NET Aspire, una API en contenedor, o cualquier otra cosa — `azd` es la herramienta que debes conocer. Esta integración con Copilot elimina la última barrera de fricción que antes hacía que necesitaras una chuleta para empezar.

La pieza de scaffolding es genial para proyectos brownfield. Tienes una app ASP.NET Core funcionando localmente perfectamente, pero llevarla a Azure siempre ha requerido algo de conocimiento de infraestructura. Ahora Copilot tiende ese puente. Y la función de resolución de errores es algo que desearía haber tenido la última vez que pasé 45 minutos depurando un error `SkuNotAvailable` en tres regiones diferentes.

## Conclusión

Esta es exactamente el tipo de integración de Copilot que aporta valor real — no IA por el gusto de la IA, sino IA que entiende tu contexto y te ahorra tiempo real. Pruébalo ejecutando `azd update` para obtener la última versión, y usa `azd init` en tu próximo proyecto. El equipo está trabajando en funciones más profundas incluyendo personalización de infraestructura asistida por Copilot, así que ahora es un buen momento para [apuntarte a la investigación de usuarios](https://aka.ms/azd-user-research-signup).

Lee el [anuncio original aquí](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
