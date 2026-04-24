---
title: "Foundry Toolboxes: Eén endpoint voor alle tools van je AI-agenten"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry heeft Toolboxes uitgebracht in public preview — een manier om AI-agenttools te beheren en bloot te stellen via één MCP-compatibel endpoint."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Er is een probleem dat triviaal lijkt totdat je het zelf tegenkomt: de organisatie bouwt meerdere AI-agenten, elk heeft tools nodig, en elk team configureert die van de grond af. Dezelfde webzoekintegratie, dezelfde Azure AI Search-configuratie, dezelfde GitHub MCP-serververbinding — maar in een ander repository, door een ander team, met andere credentials en zonder gedeeld beheer.

Microsoft Foundry heeft zojuist [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) uitgebracht in public preview — een directe oplossing voor dit probleem.

## Wat is een Toolbox?

Een Toolbox is een benoemde, herbruikbare toolbundel die je eenmalig definieert in Foundry en beschikbaar stelt via één MCP-compatibel endpoint. Elke agent-runtime die MCP spreekt, kan het consumeren — geen lock-in bij Foundry Agents.

De belofte is eenvoudig: **build once, consume anywhere**. Definieer de tools, configureer authenticatie centraal (OAuth passthrough, Entra beheerde identiteit), publiceer het endpoint. Elke agent die die tools nodig heeft, verbindt zich eenmalig en krijgt ze allemaal.

## De vier pijlers (twee vandaag beschikbaar)

| Pijler | Status | Wat het doet |
|--------|--------|--------------|
| **Discover** | Binnenkort | Goedgekeurde tools vinden zonder handmatig zoeken |
| **Build** | Beschikbaar | Tools samenvoegen in een herbruikbare bundel |
| **Consume** | Beschikbaar | Één MCP-endpoint stelt alle tools beschikbaar |
| **Govern** | Binnenkort | Centrale authenticatie + observability voor alle tool-calls |

## Praktisch voorbeeld

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Zoek in documentatie en reageer op GitHub-issues.",
    tools=[
        {"type": "web_search", "description": "Zoek openbare documentatie"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Na publicatie geeft Foundry een uniform endpoint. Één verbinding, alle tools.

## Geen lock-in bij Foundry Agents

Toolboxes worden **aangemaakt en beheerd** in Foundry, maar het consumptieoppervlak is het open MCP-protocol. Ze zijn bruikbaar vanuit eigen agents (Microsoft Agent Framework, LangGraph), GitHub Copilot en andere MCP-compatibele IDEs.

## Waarom dit nu belangrijk is

De multi-agent golf bereikt productie. Elke nieuwe agent is een nieuw oppervlak voor gedupliceerde configuratie, verlopen credentials en inconsistent gedrag. De Build + Consume-basis is voldoende om met centraliseren te beginnen. Wanneer de Govern-pijler komt, beschikt men over een volledig observeerbare, centraal gestuurde tool-laag voor de gehele agentenvloot.

## Conclusie

Dit is nog vroeg — public preview, Python SDK eerst, met Discover en Govern nog in aantocht. Maar het model is degelijk en het MCP-native design zorgt dat het werkt met de tools die al worden gebouwd. Alle details in de [officiële aankondiging](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
