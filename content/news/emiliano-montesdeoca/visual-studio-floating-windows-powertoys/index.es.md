---
title: "Esa Configuración de Ventanas Flotantes de Visual Studio Que No Conocías (Pero Deberías)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Una configuración oculta de Visual Studio te da control total sobre las ventanas flotantes — entradas independientes en la barra de tareas, comportamiento adecuado con múltiples monitores e integración perfecta con FancyZones. Un desplegable lo cambia todo."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "visual-studio-floating-windows-powertoys.md" >}}).*

Si usas múltiples monitores con Visual Studio (y honestamente, ¿quién no lo hace hoy en día?), probablemente hayas experimentado la molestia: las ventanas flotantes de herramientas desaparecen cuando minimizas el IDE principal, siempre se quedan encima de todo lo demás, y no aparecen como botones separados en la barra de tareas. Funciona para algunos flujos de trabajo, pero para configuraciones con múltiples monitores es frustrante.

Mads Kristensen del equipo de Visual Studio [compartió una configuración poco conocida](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) que cambia completamente cómo se comportan las ventanas flotantes. Un desplegable. Eso es todo.

## La configuración

**Tools > Options > Environment > Windows > Floating Windows**

El desplegable "These floating windows are owned by the main window" tiene tres opciones:

- **None** — independencia total. Cada ventana flotante tiene su propia entrada en la barra de tareas y se comporta como una ventana normal de Windows.
- **Tool Windows** (predeterminado) — los documentos flotan libremente, las ventanas de herramientas quedan vinculadas al IDE.
- **Documents and Tool Windows** — comportamiento clásico de Visual Studio, todo vinculado a la ventana principal.

## Por qué "None" es la mejor opción para configuraciones con múltiples monitores

Configúralo en **None** y de repente todas tus ventanas flotantes de herramientas y documentos se comportan como aplicaciones reales de Windows. Aparecen en la barra de tareas, permanecen visibles cuando minimizas la ventana principal de Visual Studio, y dejan de forzarse al frente de todo.

Combina esto con **PowerToys FancyZones** y es un cambio total. Crea diseños personalizados a través de tus monitores, coloca tu Explorador de Soluciones en una zona, el depurador en otra, y los archivos de código donde quieras. Todo se mantiene en su lugar, todo es accesible de forma independiente, y tu espacio de trabajo se siente organizado en lugar de caótico.

## Recomendaciones rápidas

- **Usuarios avanzados con múltiples monitores**: Configura en **None**, combina con FancyZones
- **Flotadores ocasionales**: **Tool Windows** (predeterminado) es un buen punto medio
- **Flujo de trabajo tradicional**: **Documents and Tool Windows** mantiene todo clásico

Consejo pro: **Ctrl + doble clic** en la barra de título de cualquier ventana de herramientas para flotarla o anclarla instantáneamente. No se necesita reiniciar después de cambiar la configuración.

## Conclusión

Es una de esas configuraciones de "no puedo creer que no lo sabía". Si las ventanas flotantes en Visual Studio alguna vez te han molestado, ve a cambiar esto ahora mismo.

Lee el [post completo](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) para los detalles y capturas de pantalla.
