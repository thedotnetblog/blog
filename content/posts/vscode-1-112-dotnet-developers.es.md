---
title: "VS Code 1.112: Lo que los desarrolladores .NET realmente deberían importarles"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 acaba de salir y viene cargado con mejoras de agentes, un depurador de navegador integrado, sandboxing MCP y soporte para monorepos. Esto es lo que realmente importa si desarrollas con .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 acaba de aterrizar, y ¿honestamente? Este pega diferente si pasas tus días en territorio .NET. Hay mucho en las [notas de la versión oficial](https://code.visualstudio.com/updates/v1_112), pero déjame ahorrarte algo de scroll y enfocarme en lo que realmente nos importa.

## Copilot CLI se volvió mucho más útil

El gran tema de esta versión es la **autonomía del agente** — dar a Copilot más espacio para hacer lo suyo sin que tengas que supervisar cada paso.

### Direccionamiento y cola de mensajes

¿Conoces ese momento cuando Copilot CLI va a la mitad de una tarea y te das cuenta de que olvidaste mencionar algo? Antes, tenías que esperar. Ahora puedes enviar mensajes mientras una solicitud aún está en progreso — ya sea para dirigir la respuesta actual o encolar instrucciones de seguimiento.

Esto es enorme para esas tareas más largas de scaffolding con `dotnet` donde estás viendo a Copilot configurar un proyecto y piensas "oh espera, también necesito MassTransit ahí".

### Niveles de permisos

Este es el que más me emociona. Las sesiones de Copilot CLI ahora soportan tres niveles de permisos:

- **Permisos por defecto** — el flujo usual donde las herramientas piden confirmación antes de ejecutarse
- **Omitir aprobaciones** — auto-aprueba todo y reintenta en errores
- **Autopiloto** — totalmente autónomo: aprueba herramientas, responde sus propias preguntas, y sigue hasta que la tarea está completa

Si estás haciendo algo como crear desde cero una nueva API ASP.NET Core con Entity Framework, migraciones, y un setup de Docker — el modo Autopiloto significa que describes lo que quieres y vas por un café. Él lo resolverá.

Puedes habilitar Autopiloto con la configuración `chat.autopilot.enabled`.

### Previsualizar cambios antes de delegar

Cuando delegas una tarea a Copilot CLI, crea un worktree. Antes, si tenías cambios sin commit, tenías que revisar el Control de Código Fuente para ver qué se afectaría. Ahora la vista de Chat muestra los cambios pendientes ahí mismo antes de que decidas si copiarlos, moverlos o ignorarlos.

Algo pequeño, pero te salva de ese momento de "espera, ¿qué tenía en staging?".

## Depura apps web sin salir de VS Code

El navegador integrado ahora soporta **depuración completa**. Puedes poner breakpoints, hacer step through del código, e inspeccionar variables — todo dentro de VS Code. Se acabó cambiar a Edge DevTools.

Hay un nuevo tipo de depuración `editor-browser`, y si ya tienes configuraciones de lanzamiento `msedge` o `chrome` existentes, migrar es tan simple como cambiar el campo `type` en tu `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Para desarrolladores de Blazor, esto es un game changer. Ya estás ejecutando `dotnet watch` en la terminal — ahora tu depuración se queda en la misma ventana también.

El navegador también obtuvo niveles de zoom independientes (por fin), menús de contexto con clic derecho apropiados, y el zoom se recuerda por sitio web.

## Sandboxing de servidores MCP

Esto importa más de lo que podrías pensar. Si estás usando servidores MCP — quizás has configurado uno personalizado para tus recursos de Azure o consultas de base de datos — han estado ejecutándose con los mismos permisos que tu proceso de VS Code. Eso significa acceso total a tu sistema de archivos, red, todo.

Ahora puedes ponerlos en sandbox. En tu `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Cuando un servidor en sandbox necesita acceso a algo que no tiene, VS Code te solicita que otorgues permiso. Mucho mejor que el enfoque de "esperar que nadie haga nada raro".

> **Nota:** El sandboxing está disponible en macOS y Linux por ahora. El soporte para Windows viene pronto — aunque los escenarios remotos como WSL sí funcionan.

## Descubrimiento de personalizaciones en monorepos

Si trabajas en un monorepo (y seamos honestos, muchas soluciones empresariales .NET terminan siendo uno), esto resuelve un punto de dolor real.

Anteriormente, si abrías una subcarpeta de tu repo, VS Code no encontraba tu `copilot-instructions.md`, `AGENTS.md`, o skills personalizados ubicados en la raíz del repositorio. Ahora con la configuración `chat.useCustomizationsInParentRepositories`, sube hasta la raíz `.git` y descubre todo.

Esto significa que tu equipo puede compartir instrucciones de agente, archivos de prompt y herramientas personalizadas a través de todos los proyectos en un monorepo sin que todos tengan que abrir la carpeta raíz.

## /troubleshoot para depuración de agentes

¿Alguna vez configuraste instrucciones personalizadas o skills y te preguntaste por qué no se están detectando? El nuevo skill `/troubleshoot` lee los logs de depuración del agente y te dice qué pasó — qué herramientas se usaron o se saltaron, por qué las instrucciones no cargaron, y qué está causando respuestas lentas.

Habilítalo con:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Luego simplemente escribe `/troubleshoot why is my custom skill not loading?` en el chat.

También puedes exportar e importar estos logs de depuración ahora, lo cual es genial para compartir con tu equipo cuando algo no funciona como se esperaba.

## Soporte para archivos de imagen y binarios

Los agentes ahora pueden leer archivos de imagen desde disco y archivos binarios de forma nativa. Los archivos binarios se presentan en formato hexdump, y las salidas de imagen (como capturas de pantalla del navegador integrado) aparecen en una vista de carrusel.

Para desarrolladores .NET, piensa: pega una captura de pantalla de un bug de UI en el chat y haz que el agente entienda qué está mal, o haz que analice la salida del renderizado de un componente Blazor.

## Referencias automáticas de símbolos

Pequeña mejora de calidad de vida: cuando copias el nombre de un símbolo (una clase, método, etc.) y lo pegas en el chat, VS Code ahora lo convierte automáticamente en una referencia `#sym:Name`. Esto le da al agente contexto completo sobre ese símbolo sin que tengas que agregarlo manualmente.

Si quieres texto plano en su lugar, usa `Ctrl+Shift+V`.

## Los plugins ahora se pueden habilitar/deshabilitar

Anteriormente, deshabilitar un servidor MCP o plugin significaba desinstalarlo. Ahora puedes activarlos y desactivarlos — tanto globalmente como por workspace. Clic derecho en la vista de Extensiones o la vista de Personalizaciones y listo.

Los plugins de npm y pypi también pueden auto-actualizarse ahora, aunque pedirán aprobación primero ya que las actualizaciones significan ejecutar código nuevo en tu máquina.

## Para cerrar

VS Code 1.112 está claramente empujando fuerte en la experiencia del agente — más autonomía, mejor depuración, seguridad más ajustada. Para desarrolladores .NET, la depuración del navegador integrado y las mejoras de Copilot CLI son las características destacadas.

Si aún no has probado ejecutar una sesión completa de Copilot CLI en modo Autopiloto para un proyecto .NET, esta versión es un buen momento para empezar. Solo recuerda configurar tus permisos y dejarlo cocinar.

[Descarga VS Code 1.112](https://code.visualstudio.com/updates/v1_112) o actualiza desde dentro de VS Code vía **Ayuda > Buscar actualizaciones**.
