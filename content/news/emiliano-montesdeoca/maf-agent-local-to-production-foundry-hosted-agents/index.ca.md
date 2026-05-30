---
title: "El Vostre Agent MAF Local Acaba de Trobar una Llar en Producció"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents dóna al vostre agent Microsoft Agent Framework identitat, escalat, persistència de sessió i observabilitat sense configuració addicional. Aquí és com es veu a la pràctica."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Aconseguir que un agent funcioni localment és la part divertida. La part complicada és tot el que ve després: desplegar-lo sense perdre el cap, gestionar sessions, configurar la identitat, connectar la observabilitat. Normalment això significa molta infraestructura personalitzada.

Foundry Hosted Agents ha eliminat la major part d'aquesta infraestructura per als usuaris de Microsoft Agent Framework (MAF).

## Què Fa Realment Foundry Hosted Agents

Quan desplegueu un agent MAF a Foundry Hosted Agents, la plataforma gestiona una llista sorprenentment llarga de coses que altrament hauríeu de construir vosaltres mateixos:

- **Escalar a zero** — el vostre agent no costa res quan és inactiu i torna a arrencar automàticament
- **Sandboxes aïllats per VM per sessió** — cada sessió d'usuari obté el seu propi sandbox amb persistència del sistema de fitxers que sobreviu als esdeveniments de reducció d'escala
- **Entra ID integrat** — cada agent obté la seva pròpia identitat per cridar models Foundry, Toolbox i serveis Azure sense secrets codificats a la imatge
- **Desplegaments versionats** — cada desplegament és un snapshot immutable, amb suport de desplegament blue/green i canary
- **Observabilitat sense configuració** — `APPLICATIONINSIGHTS_CONNECTION_STRING` s'injecta en temps d'execució perquè les traces OpenTelemetry de MAF flueixin automàticament a App Insights

L'últim és genuïnament pràctic. Sense connexió addicional, sense configuració extra. Les traces simplement apareixen.

## La Diferència en el Codi És Mínima

Això és el que més aprecio d'aquesta integració. No reescriviu el vostre agent. Simplement l'emboliqueu:

**En .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**En Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Això és tot. La mateixa lògica que vau provar localment és la que s'executa en producció. La plataforma l'embolica amb la infraestructura de gestió de sessions, identitat i escalat.

## Dos Protocols, Un Agent

Els Hosted Agents suporten dos estils d'endpoint:

- **Responses** (`/responses`) — compatible amb OpenAI, gestiona l'historial de conversa i l'streaming. Bon valor predeterminat per a agents amb forma de xat.
- **Invocations** (`/invocations`) — vosaltres definiu l'esquema de sol·licitud/resposta. Bo per a fluxos de treball no conversacionals.

Si esteu construint quelcom que sembla una conversa, comenceu amb Responses. Si esteu construint un agent amb forma d'API que pren entrada estructurada i retorna sortida estructurada, Invocations us dóna la flexibilitat.

## El Flux de Desplegament amb `azd`

Quan executeu `azd up` amb un agent MAF:

1. Opcionalment crea un projecte Foundry i desplega un model
2. Empaqueta el vostre codi i envia una imatge a Azure Container Registry
3. Aprovisiona còmput des de la imatge ACR
4. Assigna un Entra ID dedicat a l'agent
5. Exposa un endpoint estable (`https://{project_endpoint}/agents/{agent_name}`)
6. Gestiona tot el resta a partir d'aquell punt

Les sessions persisteixen fins a 30 dies. El còmput inactiu es desaprovisiona després de 15 minuts i es restaura de manera transparent a la propera sol·licitud. Des de la perspectiva de l'agent, res no ha canviat.

## Conclusió

La distància entre "funciona localment" i "s'executa en producció" ha estat històricament llarga i dolorosa per als agents d'IA. Foundry Hosted Agents + MAF tanca significativament aquesta bretxa. Si ja teniu un agent local construït amb Agent Framework, val la pena provar-ho avui.

L'equip diu que GA arribarà aviat — actualment està en preview. Consulteu els [docs d'integració MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) i els [exemples .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) per començar.

Article original: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
