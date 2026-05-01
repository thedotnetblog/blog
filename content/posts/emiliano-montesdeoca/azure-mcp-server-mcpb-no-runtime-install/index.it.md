---
title: "Azure MCP Server Ora è un .mcpb — Installalo senza Nessun Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server è ora disponibile come MCP Bundle (.mcpb) — scaricalo, trascinalo in Claude Desktop e il gioco è fatto. Nessun Node.js, Python o .NET richiesto."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Sai cosa era fastidioso nella configurazione dei server MCP? Avevi bisogno di un runtime. Node.js per la versione npm, Python per pip/uvx, .NET SDK per la variante dotnet.

L'[Azure MCP Server ha appena cambiato questo](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). È ora disponibile come `.mcpb` — un MCP Bundle — e la configurazione è drag-and-drop.

## Cos'è un MCP Bundle?

Pensaci come a un'estensione VS Code (`.vsix`) o un'estensione browser (`.crx`), ma per i server MCP. Un file `.mcpb` è un archivio ZIP autonomo che include il binario del server e tutte le sue dipendenze.

## Come installarlo

**1. Scarica il bundle per la tua piattaforma**

Vai alla [pagina GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) e scarica il file `.mcpb` per il tuo OS e architettura.

**2. Installa in Claude Desktop**

Il modo più semplice: trascina il file `.mcpb` nella finestra di Claude Desktop sulla pagina delle impostazioni Estensioni (`☰ → File → Impostazioni → Estensioni`). Rivedi i dettagli del server, clicca su Installa, conferma.

**3. Autenticati su Azure**

```bash
az login
```

Fatto. Azure MCP Server usa le tue credenziali Azure esistenti.

## Cosa puoi fare

Oltre 100 strumenti di servizi Azure direttamente dal tuo client AI:
- Interrogare e gestire Cosmos DB, Storage, Key Vault, App Service, Foundry
- Generare comandi `az` CLI per qualsiasi attività
- Creare template Bicep e Terraform

## Per iniziare

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repository**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Consulta il [post completo](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
