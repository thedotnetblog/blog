---
title: "VS Code 1.121: Fijar Modelos Favoritos, Compresión de Salida de Terminal, SSH en Agent"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 agrega modelos favoritos, compresión expandida de salida de terminal para ejecutores de pruebas y herramientas de compilación, temporizador de silencio inactivo para terminales en segundo plano y autenticación SSH interactiva por teclado en agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continúa las mejoras de calidad del agente Copilot de 1.120, con un enfoque en la gestión de modelos y el comportamiento del terminal.

## Fijar Modelos Favoritos

El selector de modelos ahora admite fijar. Si siempre buscas el mismo modelo o dos, fíjalos en la parte superior de la lista. Reduce el desplazamiento cuando tienes acceso a muchos modelos de múltiples proveedores.

## Compresión Expandida de Salida de Terminal

La herramienta de terminal del agente ya comprimía la salida para comandos comunes. 1.121 amplía esto para cubrir ejecutores de pruebas y herramientas de compilación:

- **Ejecutores de pruebas:** `pytest`, `jest`, `cargo test`
- **Herramientas de compilación:** `tsc`, `cargo build`, `make`
- **Linters, Docker, gestores de paquetes**

Las salidas largas de compilación y los informes de fallas de pruebas se comprimen en fragmentos relevantes antes de pasarse al modelo. Esto mantiene el uso de contexto manejable cuando el agente ejecuta ciclos de compilación o suites de pruebas, que pueden producir miles de líneas de salida.

## Temporizador de Silencio Inactivo para Terminales en Segundo Plano

Un nuevo temporizador de silencio inactivo para la herramienta `run_in_terminal`: si un comando sincrónico no produce salida durante un período configurable, se promueve automáticamente a ejecución en segundo plano. Esto evita que los comandos de larga duración bloqueen al agente cuando están procesando en silencio. Obtienes un ID de terminal para verificar más tarde.

## Variable de Entorno VSCODE_AGENT

Cuando Copilot Chat ejecuta comandos en el terminal, ahora se establece una variable de entorno `VSCODE_AGENT`. Útil si tienes scripts o herramientas que se comportan de manera diferente cuando se llaman desde una sesión de agente frente a de forma interactiva.

## Agregar al Chat desde el Navegador

Hacer clic con el botón derecho en el navegador integrado ahora muestra una opción "Agregar al Chat". Selecciona contenido de una página web y agrégalo directamente a tu contexto de Copilot Chat sin copiar y pegar.

## Corregido: Comandos de Shell de Múltiples Líneas en Agent Host

Una corrección de errores esperada: los comandos de shell de múltiples líneas en la herramienta de terminal de Agent Host ahora funcionan correctamente. Anteriormente, podían fallar o producir comportamiento incorrecto.

## Autenticación SSH Interactiva por Teclado

Las conexiones SSH de Agent Host ahora admiten autenticación interactiva por teclado — el método de autenticación de reserva utilizado por algunos servidores SSH (incluyendo algunas configuraciones corporativas más antiguas). Es menos probable que los agentes que trabajan en hosts SSH remotos experimenten fallos de autenticación.

Post original: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
