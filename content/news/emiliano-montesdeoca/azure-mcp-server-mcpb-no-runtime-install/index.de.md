---
title: "Der Azure MCP Server ist jetzt ein .mcpb — Ohne Runtime Installieren"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Der Azure MCP Server ist jetzt als MCP Bundle (.mcpb) verfügbar — herunterladen, in Claude Desktop ziehen, fertig. Kein Node.js, Python oder .NET Runtime erforderlich."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Weißt du, was an der Einrichtung von MCP-Servern lästig war? Du brauchtest eine Runtime. Node.js für die npm-Version, Python für pip/uvx, .NET SDK für die dotnet-Variante.

Der [Azure MCP Server hat das gerade geändert](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Er ist jetzt als `.mcpb` — ein MCP Bundle — verfügbar, und die Einrichtung ist Drag-and-Drop.

## Was ist ein MCP Bundle?

Denk daran wie an eine VS Code-Erweiterung (`.vsix`) oder eine Browser-Erweiterung (`.crx`), aber für MCP-Server. Eine `.mcpb`-Datei ist ein eigenständiges ZIP-Archiv mit dem Server-Binary und allen Abhängigkeiten.

## Installation

**1. Bundle für deine Plattform herunterladen**

Gehe auf die [GitHub Releases-Seite](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) und lade die `.mcpb`-Datei für dein OS und deine Architektur herunter. Stelle sicher, dass du die richtige wählst — `osx-arm64` für Apple Silicon, `win-x64` für Windows, usw.

**2. In Claude Desktop installieren**

Am einfachsten: Ziehe die `.mcpb`-Datei in das Claude Desktop-Fenster während du auf der Erweiterungsseite bist (`☰ → Datei → Einstellungen → Erweiterungen`). Serverdetails überprüfen, Installieren klicken, bestätigen. Fertig.

**3. Bei Azure authentifizieren**

```bash
az login
```

Das war's. Der Azure MCP Server nutzt deine vorhandenen Azure-Anmeldeinformationen.

## Was du damit machen kannst

Über 100 Azure-Service-Tools direkt von deinem KI-Client:
- Cosmos DB, Storage, Key Vault, App Service, Foundry abfragen und verwalten
- `az` CLI-Befehle für beliebige Aufgaben generieren
- Bicep- und Terraform-Vorlagen erstellen

## Erste Schritte

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repository**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Siehe den [vollständigen Beitrag](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
