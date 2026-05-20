---
title: "Uw AI-agent heeft een identiteitsprobleem (en dit is de template die het oplost)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Een nieuwe azd-template van Curity en Microsoft laat zien hoe je AI-agents bouwt die kortlevende OAuth-tokens gebruiken met gedetailleerde scopes — zodat agents nooit gegevens kunnen zien die ze niet zouden moeten zien."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

In elk AI-agentproject is er een moment dat ongeveer zo verloopt: de demo werkt perfect, de agent interpreteert natuurlijke taal, roept de juiste API's aan, geeft de juiste gegevens terug. Dan begint u aan echte gebruikers te denken.

Wat verhindert dat de agentsessie van één gebruiker de gegevens van een andere gebruiker ziet? Wat als de agent wordt misleid via promptinjectie? Wat als hij een tool op een onverwachte manier aanroept?

Dit zijn geen randgevallen. Dit zijn ontwerpbeslissingen die u vóór de release moet nemen.

Een nieuwe `azd`-template van Curity en Microsoft geeft u een werkende referentie voor precies dit probleem.

## Het kernprobleem: Authenticatie ≠ Autorisatie

De meeste agentsamples gaan goed om met gebruikersauthenticatie. Ze gaan slecht om met autorisatie. Weten *wie* de gebruiker is, vertelt u niet *welke gegevens* ze zouden moeten zien.

Een traditionele clientapp maakt voorspelbare API-aanroepen. Een AI-agent is niet-deterministisch — hij interpreteert natuurlijke taal en beslist wat hij aanroept. Hij kan creatief zijn. Hij kan ook ongelijk hebben. En als hij via promptinjectie wordt gemanipuleerd, hebt u regels nodig die niet afhankelijk zijn van goed gedrag van de AI.

De oplossing die deze template demonstreert: **kortlevende tokens die precies de juiste informatie bij elke hop dragen**.

## Hoe de tokenketen werkt

De template gebruikt OAuth 2.0-toegangstokens met tokenuitwisseling om machtigingen bij elke stap te beperken. Het gebruikerstoken wordt twee keer uitgewisseld voordat het de MCP-server bereikt:

1. **Eerste uitwisseling** — versmalt de scope en converteert het ondoorzichtige token naar een JWT
2. **Tweede uitwisseling** — voegt agentidentiteit en een nieuw publiek toe voor de MCP-server hop

Hoe het MCP-servertoken eruit ziet:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

`customer_id` wordt door de autorisatieserver in het token ingebed, niet doorgegeven als een parameter die de agent beheert. De API controleert het token, niet de instructies van de agent.

Dat betekent: zelfs als iemand de agent misleidt om gegevens van een andere klant op te halen, zal het token dat niet autoriseren.

## Wat de template implementeert

Met een paar `azd`-commando's krijgt u:

- Een backend-agent op Microsoft Foundry (C#, Microsoft A2A- en MCP-SDK's)
- Een MCP-server die een voorbeeld portfolio-API blootstelt
- Curity Identity Server als autorisatieserver, samen met Entra ID voor authenticatie
- Externe en interne API-gateways die tokenuitwisseling en auditlogging afhandelen
- Bicep voor alle Azure-infrastructuur: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, opslag

Het volledige patroon is inspecteerbaar en aanpasbaar.

## Het ontwerpprincipe dat het waard is te lenen

Zelfs als u Curity niet gebruikt, is het patroon overdraagbaar: **agents mogen nooit permanente API-toegang hebben**. Elke actie zou een kortlevend token moeten gebruiken met de minimale scope die nodig is voor die specifieke aanroep, uitgegeven voor de specifieke agentidentiteit, met de claims die de API nodig heeft om autorisatiebeslissingen te nemen.

Dit bestand het tegen creatieve agents, fouten en promptinjectie op manieren die "zorg er gewoon voor dat de agent geen slechte dingen doet" nooit zal.

## Conclusie

Beveiligingspatronen voor AI-agents worden nog steeds in de gehele industrie uitgewerkt. Deze template is een van de meest complete referentie-implementaties die ik heb gezien — het behandelt de daadwerkelijke autorisatiestroom, niet alleen authenticatie.

Originele post: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
