---
title: "El Azure MCP Server Ahora es un .mcpb — Instálalo sin Ningún Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "El Azure MCP Server ya está disponible como MCP Bundle (.mcpb) — descárgalo, arrástralo a Claude Desktop y listo. Sin Node.js, Python ni .NET requeridos."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

¿Sabes qué era molesto de configurar servidores MCP? Necesitabas un runtime. Node.js para la versión npm, Python para pip/uvx, .NET SDK para la variante dotnet, Docker si querías contenedores. Solo para conectar una herramienta a tu cliente IA.

El [Azure MCP Server acaba de cambiar eso](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Ahora está disponible como `.mcpb` — un MCP Bundle — y la configuración es arrastrar y soltar.

## ¿Qué es un MCP Bundle?

Piénsalo como una extensión de VS Code (`.vsix`) o una extensión de navegador (`.crx`), pero para servidores MCP. Un archivo `.mcpb` es un archivo ZIP autónomo que incluye el binario del servidor y todas sus dependencias. Todo lo necesario para ejecutarlo en tu plataforma, empaquetado junto.

El resultado: descargas un archivo, lo abres en un cliente compatible y el servidor funciona. Sin runtime que instalar, sin `package.json` que gestionar, sin conflictos de versiones.

## Cómo instalarlo

**1. Descarga el bundle para tu plataforma**

Ve a la [página de GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) y descarga el archivo `.mcpb` para tu OS y arquitectura. Asegúrate de elegir el correcto — `osx-arm64` para Apple Silicon, `osx-x64` para Mac Intel, etc.

**2. Instala en Claude Desktop**

La forma más fácil: arrastra y suelta el archivo `.mcpb` en la ventana de Claude Desktop mientras estás en la página de configuración de Extensiones (`☰ → Archivo → Configuración → Extensiones`). Revisa los detalles del servidor, haz clic en Instalar y confirma.

**3. Autentícate en Azure**

```bash
az login
```

Eso es todo. El Azure MCP Server usa tus credenciales de Azure existentes.

## Qué puedes hacer con él

Una vez instalado, tienes acceso a más de 100 herramientas de servicios Azure directamente desde tu cliente IA:

- Consultar y administrar Cosmos DB, Storage, Key Vault, App Service, Foundry
- Generar comandos `az` CLI para cualquier tarea
- Crear plantillas Bicep y Terraform
- Obtener recomendaciones de arquitectura y diagnósticos

Prueba prompts como:
- "Lista todos los grupos de recursos en mi suscripción"
- "Genera una plantilla Bicep para una app web con base de datos SQL"

## ¿Qué método de instalación usar?

| Método | Ideal para |
|--------|----------|
| `.mcpb` | Usuarios de Claude Desktop que quieren cero configuración |
| Extensión VS Code | Desarrolladores en VS Code + GitHub Copilot |
| npm/npx | Desarrolladores que ya tienen Node.js |
| Docker | Pipelines CI/CD y contenedores |

## Para empezar

- **Descarga**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repositorio**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Consulta el [post completo](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/) para consejos de solución de problemas.
