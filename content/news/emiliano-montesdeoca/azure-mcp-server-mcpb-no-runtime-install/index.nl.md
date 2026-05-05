---
title: "Azure MCP Server Is Nu een .mcpb — Installeer het Zonder Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server is nu beschikbaar als MCP Bundle (.mcpb) — download, sleep naar Claude Desktop en klaar. Geen Node.js, Python of .NET vereist."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

Weet je wat vervelend was aan het instellen van MCP-servers? Je had een runtime nodig. Node.js voor de npm-versie, Python voor pip/uvx, .NET SDK voor de dotnet-variant.

De [Azure MCP Server heeft dat net veranderd](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Het is nu beschikbaar als `.mcpb` — een MCP Bundle — en de installatie is slepen en neerzetten.

## Wat is een MCP Bundle?

Denk eraan als een VS Code-extensie (`.vsix`) of een browserextensie (`.crx`), maar voor MCP-servers. Een `.mcpb`-bestand is een zelfstandig ZIP-archief met de serverbinary en alle afhankelijkheden.

## Hoe te installeren

**1. Download de bundle voor uw platform**

Ga naar de [GitHub Releases-pagina](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) en download het `.mcpb`-bestand voor uw OS en architectuur.

**2. Installeer in Claude Desktop**

Het gemakkelijkst: sleep het `.mcpb`-bestand naar het Claude Desktop-venster terwijl u op de pagina Extensie-instellingen bent (`☰ → Bestand → Instellingen → Extensies`). Bekijk de serverdetails, klik op Installeren, bevestig.

**3. Verifieer bij Azure**

```bash
az login
```

## Aan de slag

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repository**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Bekijk het [volledige bericht](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
