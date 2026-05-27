---
title: "dotnet new WinUI: Crea apps de Windows sin tocar Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Las plantillas de proyectos WinUI ahora funcionan con dotnet new — apps en blanco, patrones NavigationView y más. Soporte para VS Code, sin necesidad de Visual Studio, con diseño Fluent incluido por defecto."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

El desarrollo con WinUI solía requerir Visual Studio. Eso está cambiando: Microsoft ha publicado plantillas de proyectos y elementos de código abierto para WinUI que funcionan con `dotnet new`, incorporando el desarrollo de aplicaciones Windows al flujo de trabajo estándar de la CLI.

## Empezar en tres comandos

```shell
# Instalar las plantillas
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Crear una app NavigationView
dotnet new winui-navview -n MyApp

# Ejecutarla
cd MyApp
dotnet run
```

Sin Visual Studio, sin configuración manual del proyecto. La aplicación se ejecuta con `dotnet run`.

## Qué incluye

**Plantilla en blanco** (`dotnet new winui`) — un punto de partida moderno con una barra de título Fluent ya configurada, icono de app actualizado con recurso `.ico`, y valores predeterminados correctos para modo claro/oscuro. Mejor que la antigua plantilla en blanco que te dejaba configurar lo básico tú mismo.

**Plantilla NavigationView** (`dotnet new winui-navview`) — el patrón de navegación maestro-detalle, completamente configurado con un NavigationView, barra de título moderna y estructura de navegación multipágina. Sigue la silueta estándar de apps Windows para aplicaciones basadas en navegación. Si estás construyendo algo con navegación lateral, empieza aquí.

Ambas plantillas siguen las [siluetas de apps Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — patrones modernos de Fluent Design para diseño, navegación y estructura visual — desde el primer momento.

## Por qué importa para desarrolladores que no usan Visual Studio

Los desarrolladores de WinUI que usan VS Code, Rider o herramientas de línea de comandos han estado desatendidos. Las plantillas existentes de Visual Studio no se podían usar fuera de VS — había que recrear manualmente la estructura del proyecto y configurar lo básico.

Estas plantillas son de código abierto (ver [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), desarrolladas a partir de [comentarios de la comunidad](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), y disponibles ahora. El soporte para Visual Studio está en curso — estas mismas plantillas eventualmente funcionarán allí también.

Para equipos que quieran automatizar la configuración de sus proyectos WinUI, integrarla en CI, o simplemente usar un editor diferente a Visual Studio, esta es una mejora significativa.

Post original: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
