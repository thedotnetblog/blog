---
title: "Verbind Je MCP-servers op Azure Functions met Foundry-agents — Dit Is Hoe"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Bouw je MCP-server eén keer, deploy het naar Azure Functions en verbind het met Microsoft Foundry-agents met juiste authenticatie."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

Er is één ding dat ik geweldig vind aan het MCP-ecosysteem: je bouwt je server één keer en het werkt overal.

Lily Ma van het Azure SDK-team publiceerde een [praktische gids](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) over het verbinden van MCP-servers die zijn geïmplementeerd op Azure Functions met Microsoft Foundry-agents.

## Waarom deze combinatie logisch is

Azure Functions geeft je schaalbare infrastructuur, ingebouwde authenticatie en serverless facturering. Microsoft Foundry geeft je AI-agents die kunnen redeneren en actie ondernemen.

## Authenticatie-opties

| Methode | Gebruikssituatie |
|--------|----------|
| **Sleutelgebaseerd** | Ontwikkeling of servers zonder Entra auth |
| **Microsoft Entra** | Productie met beheerde identiteiten |
| **OAuth identity passthrough** | Productie met gebruikerscontext |
| **Niet-geverifieerd** | Dev/testen of alleen publieke gegevens |

## Instellen

1. **Deploy je MCP-server naar Azure Functions** — voorbeelden beschikbaar voor [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
2. **Schakel ingebouwde MCP-authenticatie in**
3. **Haal de endpoint-URL op** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Voeg de MCP-server toe als tool in Foundry**

Lees de [volledige gids](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/).
