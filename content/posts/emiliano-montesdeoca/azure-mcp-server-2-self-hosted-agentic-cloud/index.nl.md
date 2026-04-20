---
title: "Azure MCP Server 2.0 Net Uitgebracht — Self-Hosted Agentic Cloud Automatisering is er"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 wordt stabiel met self-hosted remote deployments, 276 tools in 57 Azure-services en enterprise-beveiliging."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

Als je recentelijk iets hebt gebouwd met MCP en Azure, weet je waarschijnlijk al dat de lokale ervaring goed werkt. Maar wanneer je die setup met je hele team moet delen? Daar werd het ingewikkeld.

Niet meer. Azure MCP Server [heeft 2.0 stabiel bereikt](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), en de headlinefunctie is precies wat enterprise-teams hebben gevraagd: **self-hosted remote MCP-serverondersteuning**.

## Wat is Azure MCP Server?

Azure MCP Server implementeert de [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)-specificatie en exposeert Azure-mogelijkheden als gestructureerde, vindbare tools. De cijfers spreken voor zich: **276 MCP-tools in 57 Azure-services**.

## Het grote nieuws: self-hosted remote deployments

In een echt teamscenario heb je nodig:
- Gedeelde toegang voor ontwikkelaars en interne agentsystemen
- Gecentraliseerde configuratie
- Enterprise-netwerk- en beleidslimieten
- Integratie in CI/CD-pipelines

Azure MCP Server 2.0 pakt dit allemaal aan. Voor authenticatie zijn er twee opties:
1. **Managed Identity** — bij gebruik met [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **On-Behalf-Of (OBO)-stroom** — OpenID Connect-delegatie met de werkelijke rechten van de gebruiker

## Beveiligingsverbetering

Versie 2.0 voegt sterkere endpointvalidatie, bescherming tegen injectiepatronen en strikter isolatiebeheer toe.

## Aan de slag

- **[GitHub Repo](https://aka.ms/azmcp)** — broncode, documentatie
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — containerimplementatie
- **[VS Code-extensie](https://aka.ms/azmcp/download/vscode)** — IDE-integratie
- **[Zelfhostinghandleiding](https://aka.ms/azmcp/self-host)** — 2.0's vlaggenschipfunctie
