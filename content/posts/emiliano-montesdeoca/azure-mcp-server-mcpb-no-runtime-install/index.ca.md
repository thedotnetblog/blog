---
title: "El Azure MCP Server Ara és un .mcpb — Instal·la'l sense Cap Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "L'Azure MCP Server ja està disponible com a MCP Bundle (.mcpb) — descarrega'l, arrossega'l a Claude Desktop i ja està. Sense Node.js, Python ni .NET requerits."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Saps el que era molest de configurar servidors MCP? Necessitaves un runtime. Node.js per a la versió npm, Python per a pip/uvx, .NET SDK per a la variant dotnet.

L'[Azure MCP Server acaba de canviar això](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Ara està disponible com a `.mcpb` — un MCP Bundle — i la configuració és arrossegar i deixar anar.

## Què és un MCP Bundle?

Pensa-hi com una extensió de VS Code (`.vsix`) o una extensió de navegador (`.crx`), però per a servidors MCP. Un fitxer `.mcpb` és un arxiu ZIP autònom que inclou el binari del servidor i totes les seves dependències.

## Com instal·lar-lo

**1. Descarrega el bundle per a la teva plataforma**

Ves a la [pàgina de GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) i descarrega el fitxer `.mcpb` per al teu OS i arquitectura.

**2. Instal·la a Claude Desktop**

La manera més fàcil: arrossega i deixa anar el fitxer `.mcpb` a la finestra de Claude Desktop mentre estàs a la pàgina de configuració d'Extensions. Revisa els detalls del servidor, fes clic a Instal·la i confirma.

**3. Autentifica't a Azure**

```bash
az login
```

## Per a començar

- **Descarrega**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repositori**: [aka.ms/azmcp](https://aka.ms/azmcp)

Consulta el [post complet](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/) per a més detalls.
