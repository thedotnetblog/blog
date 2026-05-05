---
title: "La Ingeniería de Plataformas Agéntica Se Está Haciendo Real — Git-APE Muestra Cómo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "El proyecto Git-APE de Microsoft pone en práctica la ingeniería de plataformas agéntica — usando agentes de GitHub Copilot y Azure MCP para convertir solicitudes en lenguaje natural en infraestructura cloud validada."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "agentic-platform-engineering-git-ape" >}}).*

La ingeniería de plataformas ha sido uno de esos términos que suena genial en conferencias pero que normalmente significa "construimos un portal interno y un wrapper de Terraform." La verdadera promesa — infraestructura self-service que realmente sea segura, gobernada y rápida — siempre ha estado a unos pasos de distancia.

El equipo de Azure acaba de publicar la [Parte 2 de su serie sobre ingeniería de plataformas agéntica](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), y esta es sobre la implementación práctica. Lo llaman **Git-APE** (sí, el acrónimo es intencional), y es un proyecto open source que usa agentes de GitHub Copilot más servidores Azure MCP para convertir solicitudes en lenguaje natural en infraestructura validada y desplegada.

## Qué hace Git-APE realmente

La idea central: en vez de que los desarrolladores aprendan módulos de Terraform, naveguen por UIs de portales o abran tickets al equipo de plataforma, hablan con un agente de Copilot. El agente interpreta la intención, genera Infrastructure-as-Code, la valida contra políticas y despliega — todo dentro de VS Code.

Aquí está la configuración:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Abre el workspace en VS Code, y los archivos de configuración del agente son descubiertos automáticamente por GitHub Copilot. Interactúas con el agente directamente:

```
@git-ape deploy a function app with storage in West Europe
```

El agente usa Azure MCP Server internamente para interactuar con los servicios de Azure. La configuración de MCP en las opciones de VS Code habilita capacidades específicas:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Por qué esto importa

Para los que construimos en Azure, esto cambia la conversación de ingeniería de plataformas de "cómo construimos un portal" a "cómo describimos nuestras barreras de seguridad como APIs." Cuando la interfaz de tu plataforma es un agente de IA, la calidad de tus restricciones y políticas se convierte en el producto.

El blog de la Parte 1 planteó la teoría: APIs bien descritas, esquemas de control y barreras explícitas hacen las plataformas agent-ready. La Parte 2 lo demuestra funcionando con herramientas reales. El agente no genera recursos ciegamente — valida contra mejores prácticas, respeta convenciones de nomenclatura y aplica las políticas de tu organización.

La limpieza es igual de sencilla:

```
@git-ape destroy my-resource-group
```

## Mi opinión

Seré honesto — esta es más sobre el patrón que sobre la herramienta específica. Git-APE en sí es una demo/arquitectura de referencia. Pero la idea subyacente — agentes como la interfaz de tu plataforma, MCP como protocolo, GitHub Copilot como host — es hacia donde se dirige la experiencia del desarrollador empresarial.

Si eres un equipo de plataforma buscando cómo hacer tu herramienta interna amigable para agentes, no hay mejor punto de partida. Y si eres un desarrollador .NET preguntándote cómo se conecta esto con tu mundo: el Azure MCP Server y los agentes de GitHub Copilot funcionan con cualquier carga de trabajo de Azure. Tu API ASP.NET Core, tu stack .NET Aspire, tus microservicios contenerizados — todo puede ser el objetivo de un flujo de despliegue agéntico.

## Para cerrar

Git-APE es una mirada temprana pero concreta a la ingeniería de plataformas agéntica en la práctica. Clona el [repo](https://github.com/Azure/git-ape), prueba la demo y empieza a pensar en cómo las APIs y políticas de tu plataforma necesitarían verse para que un agente las use de forma segura.

Lee el [post completo](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) para el walkthrough y videos de demostración.
