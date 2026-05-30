---
title: "Uw Lokale MAF-agent Heeft Eindelijk Een Thuis in Productie"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents geeft uw Microsoft Agent Framework-agent identiteit, schaling, sessiepersistentie en observabiliteit zonder extra configuratie. Zo ziet het er in de praktijk uit."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Een agent lokaal laten werken is het leuke deel. Het lastige deel is alles wat daarna komt: het deployen zonder uw verstand te verliezen, sessies beheren, identiteit instellen, observabiliteit aansluiten. Dat betekent gewoonlijk veel aangepaste infrastructuurlijm.

Foundry Hosted Agents heeft het grootste deel van die lijm net verwijderd voor gebruikers van Microsoft Agent Framework (MAF).

## Wat Foundry Hosted Agents Werkelijk Doet

Wanneer u een MAF-agent deployt naar Foundry Hosted Agents, verwerkt het platform een verrassend lange lijst van dingen die u anders zelf zou moeten bouwen:

- **Schalen naar nul** — uw agent kost niets in idle en start automatisch opnieuw op
- **Per-sessie VM-geïsoleerde sandboxen** — elke gebruikerssessie krijgt zijn eigen sandbox met bestandssysteempersistentie die scale-down-gebeurtenissen overleeft
- **Ingebouwde Entra ID** — elke agent krijgt zijn eigen identiteit om Foundry-modellen, Toolbox en Azure-services aan te roepen zonder geheimen in de image
- **Versioned deployments** — elke deployment is een onveranderlijke snapshot, met ondersteuning voor blue/green en canary-uitrol
- **Observabiliteit zonder configuratie** — `APPLICATIONINSIGHTS_CONNECTION_STRING` wordt bij runtime geïnjecteerd zodat MAF's OpenTelemetry-traces automatisch naar App Insights vloeien

Die laatste is echt fijn. Geen extra bedrading, geen extra configuratie. Traces verschijnen gewoon.

## Het Codeverschil Is Minimaal

Dit is wat ik het meest waardeer aan deze integratie. U herschrijft uw agent niet. U omhult hem gewoon:

**In .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**In Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Dat is alles. Dezelfde logica die u lokaal testte, is wat in productie draait. Het platform omhult het met sessiebeheers-, identiteits- en schalinginfrastructuur.

## Twee Protocollen, Één Agent

Hosted Agents ondersteunen twee endpoint-stijlen:

- **Responses** (`/responses`) — OpenAI-compatibel, beheert gespreksgeschiedenis en streaming. Goed standaard voor chat-achtige agents.
- **Invocations** (`/invocations`) — u definieert het verzoek/antwoord-schema. Goed voor niet-conversationele workflows.

Als u iets bouwt dat eruit ziet als een gesprek, begin dan met Responses. Als u een API-achtige agent bouwt die gestructureerde invoer neemt en gestructureerde uitvoer retourneert, geeft Invocations u de flexibiliteit.

## De Deployment-flow met `azd`

Wanneer u `azd up` uitvoert met een MAF-agent:

1. Maakt optioneel een Foundry-project en deployt een model
2. Pakt uw code en pusht een image naar Azure Container Registry
3. Voorziet compute vanuit de ACR-image
4. Wijst een toegewijd Entra ID toe aan de agent
5. Stelt een stabiel endpoint bloot (`https://{project_endpoint}/agents/{agent_name}`)
6. Verwerkt al het andere vanaf dat punt

Sessies blijven tot 30 dagen bestaan. Idle compute wordt na 15 minuten gede-provisioneerd en transparant hersteld bij het volgende verzoek. Vanuit het perspectief van de agent is er niets veranderd.

## Afsluiting

De afstand tussen "lokaal werkend" en "in productie draaiend" was historisch lang en pijnlijk voor AI-agents. Foundry Hosted Agents + MAF verkleint die kloof aanzienlijk. Als u al een lokale agent heeft gebouwd met Agent Framework, is dit het proberen waard vandaag.

Het team zegt dat GA binnenkort komt — dit is momenteel in preview. Bekijk de [MAF Hosted Agent integratie-documentatie](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) en de [.NET-voorbeelden](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) om te beginnen.

Origineel artikel: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
