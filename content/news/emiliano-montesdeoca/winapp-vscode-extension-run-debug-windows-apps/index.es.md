---
title: "Extensión WinApp para VS Code: Ejecuta, Depura y Empaqueta Apps Windows Sin Salir del Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "La extensión WinApp para VS Code trae el CLI completo de Desarrollo de Apps Windows directamente a VS Code — ejecuta, depura con identidad de paquete, empaqueta y firma apps Windows sin tocar Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Si alguna vez has intentado desarrollar una app Windows en VS Code, ya conoces ese momento. Estás trabajando fluidamente, editando código en tu editor preferido, y de repente necesitas identidad de paquete para una API de Windows. O necesitas crear un MSIX. O firmar un paquete. Y de repente estás abriendo Visual Studio, o buscando en Google "msix packaging without visual studio" a las 11 de la noche.

Ese fricción ya no existe. La [extensión WinApp para VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) está en preview pública — y es el [CLI de Desarrollo de Apps Windows](https://github.com/microsoft/WinAppCli) completo integrado directamente en VS Code. Sin instalación separada, sin Visual Studio requerido.

## Identidad de Paquete desde F5

El tema con las APIs de Windows — notificaciones, tareas en segundo plano, funciones de IA on-device, share targets — es que muchas requieren que tu app tenga **identidad de paquete**. Sin ella, esas APIs simplemente no funcionan.

Conseguir identidad de paquete tradicionalmente significaba construir un instalador MSIX completo o ejecutar desde Visual Studio. La extensión WinApp cambia esto completamente con un tipo de depuración `winapp` personalizado.

Agrega esto a tu `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Presiona F5. La extensión localiza tu build output y manifiesto, da a tu app identidad de paquete mediante `winapp run`, y adjunta el depurador. Para apps .NET es `coreclr` (requiere C# Dev Kit). C/C++ usa `cppvsdbg`. Node/Electron usa el depurador incorporado.

Puedes configurar un `preLaunchTask` para que el proyecto compile automáticamente antes de cada F5 — mismo flujo que Visual Studio, pero en VS Code.

## Todo en la Paleta de Comandos

Abre `Ctrl+Shift+P`, escribe `WinApp`, y obtienes el kit de herramientas completo:

- **Initialize Project** — configura tu proyecto con Windows SDK y/o Windows App SDK
- **Run Application** — lanza como app empaquetada con identidad de paquete
- **Create MSIX Package** — empaqueta tu app con opciones de certificado y runtime
- **Update Manifest Assets** — genera automáticamente todos los iconos requeridos desde una imagen fuente
- **Generate / Install Certificate** — gestión de certificados de desarrollo
- **Sign Package** — firma un MSIX o ejecutable
- **Run SDK Tool** — ejecuta `makeappx`, `signtool`, `mt` o `makepri` directamente

No se necesita instalar el CLI de WinApp tampoco. Viene incluido con la extensión.

## Funciona con Múltiples Frameworks

No es solo una herramienta para .NET WPF/WinUI. La extensión funciona con:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Esa amplitud es deliberada. VS Code es donde viven los desarrolladores web y multiplataforma. Si estás construyendo una app Tauri o Electron que necesita empaquetado Windows, esta extensión te cubre sin que tengas que adoptar Visual Studio.

## Por Qué Importa para Desarrolladores .NET

Trabajo mucho en VS Code — es donde escribo Markdown, gestiono configuraciones, edito proyectos pequeños y ejecuto terminales. Pero para trabajo de escritorio Windows en .NET, Visual Studio ha sido la única opción real en el momento que necesitas algo relacionado con empaquetado.

Esta extensión cierra esa brecha. Ahora puedes tener un ciclo completo de desarrollo de escritorio Windows en .NET — editar, compilar, ejecutar con identidad de paquete, depurar, empaquetar, firmar — sin salir de VS Code. Es una mejora genuina de calidad de vida.

## Empezando

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

O busca **WinApp** en la vista de Extensiones (`Ctrl+Shift+X`).

Requisitos:
- Windows 10 o posterior
- VS Code 1.109.0 o posterior
- La extensión de depurador para el lenguaje de tu app

Lee el [anuncio completo de Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) para más detalles.

## Conclusión

La extensión WinApp para VS Code es una bienvenida adición para desarrolladores de escritorio Windows en .NET que viven en VS Code pero han tenido que cambiar a Visual Studio para trabajo de empaquetado. Identidad de paquete desde F5, empaquetado MSIX desde la paleta de comandos, gestión de certificados integrada — es el conjunto correcto de funcionalidades.

Pruébalo en tu próximo proyecto WPF o WinUI. La fricción que has estado sorteando acaba de reducirse considerablemente.
