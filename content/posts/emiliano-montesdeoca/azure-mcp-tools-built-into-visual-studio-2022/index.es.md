---
title: "Las herramientas Azure MCP ahora vienen integradas en Visual Studio 2022 — Sin extensión necesaria"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Las herramientas Azure MCP se incluyen como parte de la carga de trabajo de desarrollo Azure en Visual Studio 2022. Más de 230 herramientas, 45 servicios de Azure, cero extensiones que instalar."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Este artículo fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}}).*

Si has estado usando las herramientas Azure MCP en Visual Studio a través de la extensión separada, ya conoces el proceso — instalar el VSIX, reiniciar, cruzar los dedos para que no se rompa, gestionar incompatibilidades de versiones. Esa fricción se acabó.

Yun Jung Choi [anunció](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) que las herramientas Azure MCP ahora se incluyen directamente como parte de la carga de trabajo de desarrollo Azure en Visual Studio 2022. Sin extensión. Sin VSIX. Sin el baile de reiniciar.

## Qué significa esto realmente

A partir de Visual Studio 2022 versión 17.14.30, el Azure MCP Server viene incluido con la carga de trabajo de desarrollo Azure. Si ya tienes esa carga de trabajo instalada, solo necesitas activarlo en GitHub Copilot Chat y listo.

Más de 230 herramientas en 45 servicios de Azure — accesibles directamente desde la ventana de chat. Lista tus cuentas de almacenamiento, despliega una app ASP.NET Core, diagnostica problemas en App Service, consulta Log Analytics — todo sin abrir una pestaña del navegador.

## Por qué esto importa más de lo que parece

La cosa con las herramientas de desarrollo es esta: cada paso extra es fricción, y la fricción mata la adopción. Tener MCP como extensión separada significaba incompatibilidades de versiones, fallos en la instalación, y una cosa más que mantener actualizada. Integrarlo en la carga de trabajo significa:

- **Una sola vía de actualización** a través del Visual Studio Installer
- **Sin desviaciones de versión** entre la extensión y el IDE
- **Siempre actualizado** — el MCP Server se actualiza con las versiones regulares de VS

Para equipos que estandarizan en Azure, esto es muy importante. Instalas la carga de trabajo una vez, activas las herramientas, y están ahí para cada sesión.

## Qué puedes hacer con esto

Las herramientas cubren todo el ciclo de vida del desarrollo a través de Copilot Chat:

- **Aprender** — pregunta sobre servicios de Azure, buenas prácticas, patrones de arquitectura
- **Diseñar y desarrollar** — obtén recomendaciones de servicios, configura el código de tu aplicación
- **Desplegar** — aprovisiona recursos y despliega directamente desde el IDE
- **Solucionar problemas** — consulta logs, verifica el estado de los recursos, diagnostica problemas en producción

Un ejemplo rápido — escribe esto en Copilot Chat:

```
List my storage accounts in my current subscription.
```

Copilot llama a las herramientas Azure MCP detrás de escena, consulta tus suscripciones, y devuelve una lista formateada con nombres, ubicaciones y SKUs. Sin necesidad del portal.

## Cómo activarlo

1. Actualiza a Visual Studio 2022 **17.14.30** o superior
2. Asegúrate de tener instalada la carga de trabajo **Azure development**
3. Abre GitHub Copilot Chat
4. Haz clic en el botón **Select tools** (el icono de las dos llaves)
5. Activa **Azure MCP Server**

Eso es todo. Se mantiene activado entre sesiones.

## Una advertencia

Las herramientas están desactivadas por defecto — necesitas activarlas manualmente. Y las herramientas específicas de VS 2026 no están disponibles en VS 2022. La disponibilidad de herramientas también depende de los permisos de tu suscripción de Azure, igual que en el portal.

## El panorama general

Esto es parte de una tendencia clara: MCP se está convirtiendo en el estándar para exponer herramientas de la nube en los IDEs de desarrollo. Ya hemos visto el [lanzamiento estable de Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) e integraciones de MCP en VS Code y otros editores. Tenerlo integrado en el sistema de cargas de trabajo de Visual Studio es la progresión natural.

Para los que somos desarrolladores .NET y vivimos en Visual Studio, esto elimina una razón más para cambiar de contexto al portal de Azure. Y sinceramente, mientras menos cambio de pestañas, mejor.
