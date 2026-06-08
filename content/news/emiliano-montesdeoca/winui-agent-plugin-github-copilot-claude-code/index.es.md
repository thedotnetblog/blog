---
title: "Un Plugin de Agente WinUI para GitHub Copilot y Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft ha lanzado habilidades de agente para el desarrollo WinUI: crear scaffolding, compilar, ejecutar, probar e iterar, todo con GitHub Copilot CLI o Claude Code. La innovación clave: herramientas de propósito específico que fundamentan al agente en hechos específicos de WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft publicó un conjunto de habilidades de agente de código abierto para el desarrollo de aplicaciones WinUI, disponibles en [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Instalación y Configuración

Instala el plugin con `/plugin install winui@awesome-copilot`, luego ejecuta la configuración inicial con `/winui:winui-setup`. El proceso de configuración verifica los prerrequisitos, instala las dependencias necesarias y configura el entorno para el desarrollo de aplicaciones WinUI.

## El Bucle de Desarrollo de Extremo a Extremo

Las habilidades cubren el ciclo completo de desarrollo:

- **Scaffolding:** Genera la plantilla de proyecto correcta usando `dotnet new WinUI` con los parámetros apropiados — el agente conoce las plantillas correctas y los valores predeterminados de configuración.
- **Compilación:** Gestiona el modelo de ejecución empaquetado que requieren las aplicaciones WinUI, incluyendo la firma del paquete y las configuraciones de manifiesto.
- **Interacción y validación:** Inicia la aplicación, interactúa con ella y valida el comportamiento.
- **Corrección de errores de compilación:** El agente entiende los mensajes de error específicos de WinUI y sabe cómo resolverlos.

## Eficiencia de Tokens mediante Herramientas de Propósito Específico

La innovación clave es que las habilidades incluyen herramientas de propósito específico que obtienen datos de referencia concretos bajo demanda:

- Detalles de la API de WinUI y Fluent Design
- Patrones MVVM y mejores prácticas
- Empaquetado MSIX, firma de código y envío a la Store
- Accesibilidad, temas y automatización de UI

En lugar de inyectar toda la documentación de WinUI en el contexto, las herramientas obtienen exactamente lo que el agente necesita en el momento en que lo necesita. Esto mantiene el uso del contexto eficiente y mejora la precisión en dominios especializados.

## Por Qué Importan las Habilidades de Propósito Específico

Los modelos de lenguaje de uso general tienen conocimiento limitado sobre los matices específicos de WinUI: el modelo de ejecución empaquetado, las APIs de Fluent Design, la integración de MSIX o la forma específica en que Windows App SDK envuelve la funcionalidad de Win32. Las herramientas de propósito específico resuelven esto fundamentando al agente en hechos verificados de WinUI en lugar de conocimiento del modelo potencialmente desactualizado o incorrecto.

El mismo patrón se aplica a cualquier marco o SDK especializado con sus propias convenciones y requisitos que difieren de los patrones de desarrollo general.

Post original: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
