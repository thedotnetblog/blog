---
title: "Deja de vigilar tu terminal: el modo desacoplado de Aspire cambia el flujo de trabajo"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 te permite ejecutar tu AppHost en segundo plano y recuperar tu terminal. Combinado con los nuevos comandos CLI y el soporte para agentes, esto es más importante de lo que parece."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Cada vez que ejecutas un AppHost de Aspire, tu terminal desaparece. Bloqueada. Ocupada hasta que presionas Ctrl+C. ¿Necesitas ejecutar un comando rápido? Abre otra pestaña. ¿Quieres revisar los logs? Otra pestaña. Es una pequeña fricción que se acumula rápido.

Aspire 13.2 soluciona esto. James Newton-King [escribió todos los detalles](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), y honestamente, esta es una de esas funcionalidades que cambia inmediatamente tu forma de trabajar.

## Modo desacoplado: un comando, terminal de vuelta

```bash
aspire start
```

Ese es el atajo para `aspire run --detach`. Tu AppHost arranca en segundo plano y recuperas tu terminal de inmediato. Sin pestañas extra. Sin multiplexor de terminal. Solo tu prompt, listo para usar.

## Gestionando lo que está en ejecución

La cuestión es que ejecutar en segundo plano solo es útil si puedes gestionar lo que hay ahí fuera. Aspire 13.2 incluye un conjunto completo de comandos CLI para exactamente eso:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Esto convierte el CLI de Aspire en un gestor de procesos completo. Puedes iniciar múltiples AppHosts, verificar su estado, seguir sus logs y apagarlos — todo desde una sola sesión de terminal.

## Combínalo con el modo aislado

El modo desacoplado se combina naturalmente con el modo aislado. ¿Quieres ejecutar dos instancias del mismo proyecto en segundo plano sin conflictos de puertos?

```bash
aspire start --isolated
aspire start --isolated
```

Cada uno obtiene puertos aleatorios, secretos separados y su propio ciclo de vida. Usa `aspire ps` para ver ambos, `aspire stop` para detener el que ya no necesites.

## Por qué esto es enorme para los agentes de código

Aquí es donde se pone realmente interesante. Un agente de código trabajando en tu terminal ahora puede:

1. Iniciar la app con `aspire start`
2. Consultar su estado con `aspire describe`
3. Revisar logs con `aspire logs` para diagnosticar problemas
4. Detenerla con `aspire stop` cuando termine

Todo sin perder la sesión de terminal. Antes del modo desacoplado, un agente que ejecutara tu AppHost se bloqueaba a sí mismo en su propia terminal. Ahora puede iniciar, observar, iterar y limpiar — exactamente como querrías que funcione un agente autónomo.

El equipo de Aspire se volcó en esto. Ejecutar `aspire agent init` configura un archivo de habilidades de Aspire que enseña estos comandos a los agentes. Así, herramientas como el agente de código de Copilot pueden gestionar tus cargas de trabajo de Aspire directamente.

## Para cerrar

El modo desacoplado es una mejora de flujo de trabajo disfrazada de un simple flag. Dejas de cambiar contexto entre terminales, los agentes dejan de bloquearse a sí mismos, y los nuevos comandos CLI te dan visibilidad real de lo que está en ejecución. Es práctico, es limpio, y hace que el ciclo de desarrollo diario sea notablemente más fluido.

Lee el [post completo](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) para todos los detalles y obtén Aspire 13.2 con `aspire update --self`.
