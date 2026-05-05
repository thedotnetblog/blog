---
title: "VS Code 1.115 — Notificaciones de Terminal en Segundo Plano, Modo Agente SSH y Más"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 trae notificaciones de terminal en segundo plano para agentes, hosting remoto de agentes por SSH, pegado de archivos en terminales y seguimiento de ediciones con reconocimiento de sesión. Esto es lo que importa para desarrolladores .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "vscode-1-115-agent-improvements.md" >}}).*

VS Code 1.115 acaba de [lanzarse](https://code.visualstudio.com/updates/v1_115), y aunque es una versión más ligera en cuanto a funcionalidades destacadas, las mejoras relacionadas con agentes son genuinamente útiles si trabajás con asistentes de código con IA todos los días.

Déjame resaltar lo que realmente vale la pena saber.

## Las terminales en segundo plano ahora se comunican con los agentes

Esta es la funcionalidad estrella. Las terminales en segundo plano ahora notifican automáticamente a los agentes cuando los comandos terminan, incluyendo el código de salida y la salida de la terminal. Las solicitudes de entrada en terminales en segundo plano también se detectan y se muestran al usuario.

¿Por qué importa esto? Si usaste el modo agente de Copilot para ejecutar comandos de compilación o suites de tests en segundo plano, conocés el dolor del "¿ya terminó eso?" — las terminales en segundo plano eran básicamente disparar-y-olvidar. Ahora el agente recibe una notificación cuando tu `dotnet build` o `dotnet test` termina, ve la salida y puede reaccionar en consecuencia. Es un cambio pequeño que hace que los flujos de trabajo impulsados por agentes sean significativamente más confiables.

También hay una nueva herramienta `send_to_terminal` que permite a los agentes enviar comandos a terminales en segundo plano con confirmación del usuario, solucionando el problema donde `run_in_terminal` con un timeout movía las terminales al segundo plano y las dejaba como solo lectura.

## Hosting remoto de agentes por SSH

VS Code ahora soporta conectarse a máquinas remotas por SSH, instalando automáticamente el CLI e iniciándolo en modo host de agentes. Esto significa que tus sesiones de agentes de IA pueden apuntar a entornos remotos directamente — útil para desarrolladores .NET que compilan y prueban en servidores Linux o VMs en la nube.

## Seguimiento de ediciones en sesiones de agentes

Las ediciones de archivos realizadas durante sesiones de agentes ahora se rastrean y restauran, con diffs, deshacer/rehacer y restauración de estado. Si un agente hace cambios en tu código y algo sale mal, podés ver exactamente qué cambió y revertirlo. Tranquilidad para dejar que los agentes modifiquen tu codebase.

## Reconocimiento de pestañas del navegador y otras mejoras

Algunas mejoras adicionales de calidad de vida:

- **Seguimiento de pestañas del navegador** — el chat ahora puede rastrear y enlazar a pestañas del navegador abiertas durante una sesión, para que los agentes puedan referenciar páginas web que estás viendo
- **Pegado de archivos en la terminal** — pegá archivos (incluyendo imágenes) en la terminal con Ctrl+V, arrastrar y soltar, o clic derecho
- **Cobertura de tests en el minimapa** — los indicadores de cobertura de tests ahora se muestran en el minimapa para una vista visual rápida
- **Pellizcar para zoom en Mac** — el navegador integrado soporta gestos de pellizcar para zoom
- **Derechos de Copilot en Sesiones** — la barra de estado muestra información de uso en la vista de Sesiones
- **Favicon en Ir a Archivo** — las páginas web abiertas muestran favicons en la lista de selección rápida

## Conclusión

VS Code 1.115 es una versión incremental, pero las mejoras de agentes — notificaciones de terminal en segundo plano, hosting de agentes por SSH y seguimiento de ediciones — se suman a una experiencia notablemente más fluida para el desarrollo asistido por IA. Si estás usando el modo agente de Copilot para proyectos .NET, estos son el tipo de mejoras de calidad de vida que reducen la fricción diaria.

Mirá las [notas de la versión completas](https://code.visualstudio.com/updates/v1_115) para cada detalle.
