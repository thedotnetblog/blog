---
title: "Hooks de azd en Python, TypeScript y .NET: adiós a los scripts de shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "La CLI de Azure Developer ahora permite escribir hooks en Python, JavaScript, TypeScript o .NET. Se acabó el cambio de contexto a Bash solo para ejecutar un script de migración."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Si alguna vez has tenido un proyecto completamente en .NET y aun así tuviste que escribir scripts Bash solo para los hooks de azd, conoces bien ese dolor. ¿Por qué cambiar a sintaxis de shell en un paso de pre-provisioning cuando todo lo demás en el proyecto es C#?

Esa frustración tiene solución oficial. La Azure Developer CLI [acaba de lanzar soporte multi-lenguaje para hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), y es exactamente tan bueno como suena.

## Hooks, brevemente, por si no los conoces

Los hooks son scripts que se ejecutan en puntos clave del ciclo de vida de `azd` — antes del provisioning, después del despliegue, y más. Se definen en `azure.yaml` y permiten inyectar lógica personalizada sin modificar la CLI.

Antes solo se admitían Bash y PowerShell. Ahora puedes usar **Python, JavaScript, TypeScript o .NET** — y `azd` se encarga del resto automáticamente.

## Cómo funciona la detección

Simplemente apuntas el hook a un archivo y `azd` infiere el lenguaje por la extensión:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Eso es todo. Sin config adicional. Si la extensión es ambigua, puedes añadir `kind: python` (o el que corresponda) para especificarlo explícitamente.

## Detalles importantes por lenguaje

### Python

Coloca un `requirements.txt` o `pyproject.toml` junto al script (o en cualquier directorio padre) y `azd` crea un entorno virtual, instala dependencias y ejecuta el script:

```
hooks/
├── setup.py
└── requirements.txt
```

Sin gestión manual de virtualenv. `azd` busca hacia arriba desde el script el archivo de proyecto más cercano.

### JavaScript y TypeScript

El mismo patrón — pon un `package.json` cerca del script y `azd` ejecutará `npm install` primero. Para TypeScript, usa `npx tsx` sin paso de compilación ni `tsconfig.json`:

```
hooks/
├── seed.ts
└── package.json
```

¿Quieres usar pnpm o yarn? Hay una opción `config.packageManager` para eso.

### .NET

Dos modos disponibles:

- **Modo proyecto**: Si hay un `.csproj` junto al script, `azd` ejecuta `dotnet restore` y `dotnet build` automáticamente.
- **Modo single-file**: En .NET 10+, puedes poner un archivo `.cs` independiente y se ejecuta directamente con `dotnet run script.cs`. Sin archivo de proyecto.

```yaml
hooks:
  postprovision:
    run: ./hooks/migrate.cs
```

Si ya estás en .NET 10, el modo single-file es la opción más limpia para scripts simples de migración o seeding. Sin scaffolding, sin `.csproj` que mantener.

## Config por ejecutor

Cada lenguaje soporta un bloque `config` opcional para ajustar los valores por defecto:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postdeploy:
    run: ./hooks/seed.py
    config:
      virtualEnvName: .venv
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

También puedes mezclar formatos en el mismo bloque `hooks:` — distintos lenguajes para distintos eventos del ciclo de vida, overrides por plataforma para Windows vs. Linux, lo que necesites.

## Por qué importa para desarrolladores .NET

La respuesta aburrida es "consistencia". Pero en la práctica va más allá. Los hooks eran el último lugar de un proyecto basado en azd que te obligaba a usar otro lenguaje. Ahora todo el pipeline de despliegue — código de app, scripts de infraestructura y hooks del ciclo de vida — puede vivir en un solo lenguaje.

Más concreto: puedes reutilizar tus utilidades .NET existentes en los hooks. ¿Tienes una librería compartida para gestión de esquemas de base de datos? Simplemente referencíala en el proyecto del hook. ¿Tienes un script Python de seeding que ya escribiste? Ponlo directamente en `azure.yaml`.

## Conclusión

Es uno de esos cambios que parecen pequeños pero que eliminan mucha fricción del día a día con azd. El soporte multi-lenguaje para hooks ya está disponible — revisa el [post oficial](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) para la documentación completa y el [repositorio de azd en GitHub](https://github.com/Azure/azure-dev) para probarlo en tu próximo proyecto.
