---
title: "Azure MCP-tools zijn nu Ingebouwd in Visual Studio 2022 — Geen Extensie Nodig"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP-tools worden meegeleverd als onderdeel van de Azure-ontwikkelworkload in Visual Studio 2022. Meer dan 230 tools, 45 Azure-services, nul te installeren extensies."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

Als je de Azure MCP-tools in Visual Studio hebt gebruikt via de afzonderlijke extensie, ken je de procedure — VSIX installeren, herstarten, hopen dat het niet stukgaat, versieverschillen beheren. Die wrijving is weg.

Yun Jung Choi [kondigde aan](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) dat Azure MCP-tools nu rechtstreeks worden meegeleverd als onderdeel van de Azure-ontwikkelworkload in Visual Studio 2022. Geen extensie. Geen VSIX.

## Hoe in te schakelen

1. Update naar Visual Studio 2022 **17.14.30** of hoger
2. Zorg ervoor dat de workload **Azure development** is geïnstalleerd
3. Open GitHub Copilot Chat
4. Klik op de knop **Tools selecteren** (het pictogram met twee moersleutels)
5. Zet **Azure MCP Server** aan

Blijft ingeschakeld tussen sessies.

## Kanttekening

De tools zijn standaard uitgeschakeld — je moet ze inschakelen. Voor .NET-ontwikkelaars in Visual Studio verwijdert dit nog een reden om context te wisselen naar de Azure-portal.
