---
title: "VS Code 1.120: Contraseñas Seguras, Selector de Contexto, Metadatos de GitHub en Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 es una versión enfocada para usuarios de Copilot: manejo seguro de prompts de contraseña, selector de tamaño de contexto del modelo, metadatos de PRs de GitHub en sesiones de agente y gestión de archivos de sesión."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 llegó con un conjunto de mejoras para el agente de Copilot que son pequeñas individualmente pero notablemente mejores en el uso diario.

## Detección Segura de Prompts de Contraseña en Terminales de Agente

Cuando un agente de Copilot ejecuta un comando de terminal que desencadena un prompt de contraseña o passphrase, VS Code ahora lo detecta y muestra un diálogo de confirmación. El diálogo enfoca el terminal para que puedas escribir el secreto directamente — y de manera crucial, los secretos nunca se enrutan a través del modelo.

Esta es una mejora de seguridad significativa. Anteriormente, los agentes que ejecutaban comandos que desencadenaban prompts de autenticación podían crear situaciones donde los usuarios podrían exponer inadvertidamente credenciales. El anuncio del lector de pantalla significa que los usuarios de accesibilidad también reciben la notificación.

## Selector de Tamaño de Contexto en el Selector de Modelo

Un nuevo selector de tamaño de contexto te permite elegir cuánto contexto usa el modelo para una sesión. Los diferentes modelos tienen diferentes tamaños de ventana de contexto, y algunos flujos de trabajo se benefician de limitarlo (menor latencia, menor costo) o maximizarlo (bases de código complejas, sesiones de larga duración).

## Metadatos de PRs de GitHub en Sesiones de Agent Host

Para sesiones respaldadas por un repositorio de GitHub, VS Code ahora muestra metadatos de GitHub — incluyendo un botón de pull request — en la interfaz de usuario de agent host. Menos cambios de contexto al navegador o la extensión de GitHub cuando estás trabajando en un PR.

## Gestión del Archivo de Sesiones de Chat

Dos mejoras para el Quick Pick de sesiones:
- Las sesiones archivadas están ocultas por defecto (menos desorden visual)
- La búsqueda todavía coincide con las sesiones archivadas, para que puedas recuperar una por título

Las sesiones también se agrupan por recencia por defecto, facilitando encontrar el trabajo reciente.

## Descubrimiento de Plugins de CLI de Copilot

VS Code ahora descubre automáticamente los plugins de usuario de CLI de Copilot instalados desde `~/.copilot/installed-plugins/`. Si has configurado WinUI u otras habilidades de agente específicas del dominio, se capturan sin configuración manual.

## API de Editor de Diff Personalizado (Vista Previa)

Para autores de extensiones: una nueva API propuesta `customDiffEditorProvider` permite a las extensiones renderizar un diff unificado en un único webview con acceso tanto a documentos originales como modificados, en lugar de dos vistas de editor personalizadas lado a lado.

Post original: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
