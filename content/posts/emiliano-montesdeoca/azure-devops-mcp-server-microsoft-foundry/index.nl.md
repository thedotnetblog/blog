---
title: "Azure DevOps MCP Server Beschikbaar in Microsoft Foundry: Wat Dit Betekent voor je AI-Agents"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "De Azure DevOps MCP Server is nu beschikbaar in Microsoft Foundry. Verbind je AI-agents rechtstreeks met DevOps-workflows — werkitems, repos, pipelines — met een paar klikken."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) heeft z'n moment. Als je het AI-agent-ecosysteem volgt, heb je waarschijnlijk MCP-servers overal zien opduiken.

Nu is de [Azure DevOps MCP Server beschikbaar in Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), en dit is een van die integraties die je laat nadenken over de praktische mogelijkheden.

## Wat er eigenlijk gebeurt

Microsoft heeft de Azure DevOps MCP Server al uitgebracht als [publieke preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview). Nieuw is de Foundry-integratie. Je kunt de Azure DevOps MCP Server nu toevoegen aan je Foundry-agents rechtstreeks vanuit de toolcatalogus.

## Instellen

De instelling is verrassend eenvoudig:

1. Ga in je Foundry-agent naar **Tools toevoegen** > **Catalogus**
2. Zoek op "Azure DevOps"
3. Selecteer de Azure DevOps MCP Server (preview) en klik op **Aanmaken**
4. Voer je organisatienaam in en verbind

## Toegang beheren

Je kunt opgeven welke tools beschikbaar zijn voor je agent. Principe van minste privileges, toegepast op je AI-agents.

## Waarom dit interessant is voor .NET-teams

- **Sprint-planningsassistenten** — agents die werkitems ophalen en sprintcapaciteit voorstellen
- **Code review-bots** — agents die PR-context begrijpen
- **Incident response** — agents die werkitems aanmaken en bugs correleren
- **Onboarding** — echte antwoorden gebaseerd op projectdata

## Samenvatting

Bekijk de [volledige aankondiging](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) voor details.
