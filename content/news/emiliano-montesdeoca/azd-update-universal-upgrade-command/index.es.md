---
title: "azd update — Un solo comando para gobernar todos tus gestores de paquetes"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ahora tiene un comando de actualización universal que funciona sin importar cómo lo instalaste — winget, Homebrew, Chocolatey o script de instalación."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "azd-update-universal-upgrade-command.md" >}}).*

¿Conoces ese mensaje de "Hay una nueva versión de azd disponible" que aparece cada pocas semanas? ¿Ese que ignoras porque no recuerdas si instalaste `azd` con winget, Homebrew o ese script de curl que ejecutaste hace seis meses? Bueno, eso por fin tiene solución.

Microsoft acaba de lanzar [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — un único comando que actualiza Azure Developer CLI a la última versión sin importar cómo lo instalaste originalmente. Windows, macOS, Linux — da igual. Un solo comando.

## Cómo funciona

```bash
azd update
```

Eso es todo. Si quieres acceso anticipado a nuevas funcionalidades, puedes cambiar a la build diaria de insiders:

```bash
azd update --channel daily
azd update --channel stable
```

El comando detecta tu método de instalación actual y usa el mecanismo de actualización apropiado internamente. Se acabó el "espera, ¿usé winget o choco en esta máquina?"

## El pequeño detalle

`azd update` viene a partir de la versión 1.23.x. Si estás en una versión anterior, necesitarás hacer una última actualización manual usando tu método de instalación original. Después de eso, `azd update` se encarga de todo en adelante.

Comprueba tu versión actual con `azd version`. Si necesitas una instalación desde cero, la [documentación de instalación](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) te cubre.

## Por qué importa

Es una pequeña mejora de calidad de vida, pero para los que usamos `azd` a diario para desplegar agentes de IA y apps de Aspire en Azure, estar actualizado significa menos momentos de "ese bug ya estaba corregido en la última versión". Una cosa menos en la que pensar.

Lee el [anuncio completo](https://devblogs.microsoft.com/azure-sdk/azd-update/) y el [análisis más detallado](https://blog.jongallant.com/2026/04/azd-update) de Jon Gallant para más contexto.
