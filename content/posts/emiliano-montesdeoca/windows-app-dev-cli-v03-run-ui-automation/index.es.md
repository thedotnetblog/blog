---
title: "Windows App Dev CLI v0.3: F5 desde la terminal y automatización de UI para agentes"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 llega con winapp run para lanzar y depurar desde la terminal, winapp ui para automatización de UI, y un paquete NuGet que hace que dotnet run funcione con apps empaquetadas."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

La experiencia F5 de Visual Studio es fantástica. Pero tener que abrir VS solo para lanzar y depurar una app Windows empaquetada es excesivo cuando estás en un pipeline de CI, ejecutando un workflow automatizado, o — cada vez más — cuando un agente de IA está haciendo las pruebas.

Windows App Development CLI v0.3 acaba de [salir](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) y lo aborda directamente con dos funciones destacadas: `winapp run` y `winapp ui`.

## winapp run: F5 desde cualquier sitio

`winapp run` toma una carpeta de app sin empaquetar y un manifiesto, y hace todo lo que VS hace en un debug launch: registra un paquete loose, lanza la app y preserva el `LocalState` entre re-deploys.

```bash
# Construye tu app, luego ejecútala como app empaquetada
winapp run ./bin/Debug
```

Funciona para WinUI, WPF, WinForms, Console, Avalonia y más. Los modos están pensados tanto para desarrolladores como para workflows automatizados:

- **`--detach`**: Lanza y devuelve el control a la terminal inmediatamente. Perfecto para CI/automation.
- **`--unregister-on-exit`**: Limpia el paquete registrado al cerrar la app. Ejecuciones de test limpias.
- **`--debug-output`**: Captura mensajes `OutputDebugString` y excepciones en tiempo real. Añade `--symbols` para PDBs del Microsoft Symbol Server.

## Nuevo paquete NuGet: dotnet run para apps empaquetadas

Para desarrolladores .NET hay un nuevo paquete NuGet: `Microsoft.Windows.SDK.BuildTools.WinApp`.

Añádelo al proyecto (o deja que `winapp init` lo haga), y `dotnet run` maneja todo el inner loop: build, preparar un paquete loose-layout, registrar en Windows y lanzar — todo en un paso.

```bash
# Deja que winapp init lo configure
winapp init

# O instala directamente
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

Funciona con WinUI, WPF, WinForms, Console, Avalonia. Sin comandos adicionales, sin registro manual. Solo `dotnet run`.

## winapp ui: UI Automation desde la línea de comandos

Este es el que abre los escenarios agénticos. `winapp ui` te da acceso completo de UI Automation a cualquier app Windows en ejecución — WPF, WinForms, Win32, Electron, WinUI3 — todo desde la terminal.

Lo que puedes hacer:

- Listar todas las ventanas de nivel superior
- Navegar el árbol completo de UI Automation de cualquier ventana
- Buscar elementos por nombre, tipo o ID de automatización
- Hacer clic, invocar y establecer valores
- Tomar capturas de pantalla
- Esperar a que aparezcan elementos — ideal para sincronización de tests

Combina `winapp ui` con `winapp run` y tienes un workflow completo build → lanzar → verificar desde la terminal. Un agente puede ejecutar tu app, inspeccionar el estado de UI, interactuar con ella programáticamente y validar el resultado.

## Otras novedades

- **`winapp unregister`**: Elimina un paquete sideloaded cuando terminas.
- **`winapp manifest add-alias`**: Añade un `uap5:AppExecutionAlias` para lanzar la app por nombre desde la terminal.
- **Tab completion**: Configura completado con un solo comando para PowerShell.
- **`Package.appxmanifest` por defecto**: Ahora `winapp init` crea `Package.appxmanifest` (convención VS) en lugar de `appxmanifest.xml`.

## Cómo obtenerlo

```bash
winget install Microsoft.WinAppCli
# o
npm install -g @microsoft/winappcli
```

La CLI está en preview pública. Consulta el [repositorio en GitHub](https://github.com/microsoft/WinAppCli) para documentación completa y el [anuncio original](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) para todos los detalles.
