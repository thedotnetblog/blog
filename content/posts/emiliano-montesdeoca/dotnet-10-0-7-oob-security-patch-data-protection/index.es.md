---
title: "Parchea Esto Ahora: Actualización de Seguridad OOB .NET 10.0.7 para ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 es un lanzamiento fuera de banda que corrige una vulnerabilidad de seguridad en Microsoft.AspNetCore.DataProtection — el encriptador autenticado computaba HMAC sobre bytes incorrectos, llevando a posible elevación de privilegios."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Esta no es opcional. Si tu aplicación usa `Microsoft.AspNetCore.DataProtection`, necesitas actualizar a 10.0.7.

## Qué Pasó

Después del lanzamiento de Patch Tuesday `.NET 10.0.6`, algunos usuarios reportaron que el descifrado fallaba. Mientras investigaban la regresión, el equipo descubrió que también exponía una vulnerabilidad de seguridad: **CVE-2026-40372**.

En versiones `10.0.0` a `10.0.6` de `Microsoft.AspNetCore.DataProtection`, el encriptador autenticado calculaba su etiqueta de validación HMAC sobre los **bytes incorrectos** del payload. Resultado: posible elevación de privilegios.

## Cómo Solucionarlo

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Luego **reconstruye y redespliega** tu aplicación.

## El Panorama General

Los lanzamientos OOB son poco comunes — ocurren cuando una vulnerabilidad es lo suficientemente seria para no esperar al próximo Patch Tuesday.

Anuncio original de Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
