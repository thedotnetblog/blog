---
title: "Aspire 13.3: Kubernetes-ondersteuning, browserlogboeken en de Aspireify-skill"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Vijf weken na 13.2 verschijnt Aspire 13.3 met 45 nieuwe functies, waaronder eersteklas AKS-implementatie, een AI-ondersteunde onboarding-skill, browserlogboekopname en gestructureerde opdrachtresultaten."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Vijf weken is niet lang voor een release, maar Aspire 13.3 voelt niet zo. De hoofdpunten zijn significant: eersteklas Kubernetes- en AKS-implementatie met Helm, een agent-ondersteunde onboarding-skill genaamd Aspireify, browserlogboekopname direct in het dashboard en gestructureerde opdrachtresultaten. Plus 45 nieuwe functies, 134 verbeteringen en 93 bugfixes.

Laten we de hoogtepunten bekijken.

## Aspireify: Agent-ondersteunde onboarding

Aspire toevoegen aan een bestaand project klinkt eenvoudig — voeg een AppHost in, klaar. In de praktijk vereist het veel onderzoek: welke poorten belangrijk zijn, welke omgevingsvariabelen echte afhankelijkheden zijn, welke Docker Compose-services moeten worden toegewezen aan Aspire-integraties.

De nieuwe **Aspireify-skill** geeft uw coderingsagent een begeleide workflow precies daarvoor. Wanneer `aspire init` een skeletten AppHost maakt, helpt de Aspireify-skill de agent het repository te inspecteren, te begrijpen hoe het al werkt en de AppHost te verbinden zodat het bij de app past — niet andersom.

De standaardhouding is "minimaliseer wijzigingen aan uw code." Als uw app al `DATABASE_URL` leest, wijst de agent dat toe met `WithEnvironment()` in plaats van u te vragen uw configuratie te herschrijven. Als een poort hard is gecodeerd, vertelt de skill de agent wanneer hij die moet bewaren.

Dit is het soort AI-tooling dat echt tijd bespaart in plaats van meer werk te genereren om te beoordelen.

## Eersteklas Kubernetes- en AKS-implementatie

Dit stond al een tijdje op de verlanglijst. Aspire 13.3 levert **eersteklas Kubernetes- en AKS-implementatieondersteuning met Helm**. U kunt nu AKS direct vanuit de Aspire-tools als implementatiedoel kiezen.

Voor teams die al productieworkloads op AKS uitvoeren, sluit dit een belangrijke kloof. Uw Aspire-appmodel heeft nu een schoon pad van lokale ontwikkeling naar Kubernetes zonder handmatig Helm-charts te hoeven schrijven.

## Browserlogboeken in het dashboard

Dit is een van die functies die klein lijken totdat u een frontend-probleem debugt.

De nieuwe `WithBrowserLogs()` API koppelt een getrackt browserresource aan elke resource die endpoints ondersteunt. Aspire start Chromium met een privé CDP-pipe en streamt consolelogboeken, netwerkaanvragen en fouten direct naar de logstroom van de resource:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

De TypeScript AppHost ondersteunt hetzelfde:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Consolefouten, mislukte netwerkaanvragen, client-side uitzonderingen — alles zichtbaar in hetzelfde dashboard waar u al traces en metrieken bekijkt. Niet meer wisselen naar browser DevTools voor de basisprincipes.

## Gestructureerde opdrachtresultaten

Resourceopdrachten hebben een significante upgrade gekregen. Tot nu toe gaven opdrachten succes/mislukking terug. Nu geven ze gestructureerde resultaten terug: tekst, JSON of Markdown dat door het model, de dashboard-UI, de CLI en de MCP-tools stroomt.

Het dashboard verbindt dit alles met een nieuw notificatiecentrum in de header. Opdrachtresultaten verschijnen als tijdgestempelde meldingen met Markdown-rendering en een actie "Antwoord bekijken".

Dit maakt resourceopdrachten echt composeerbaar. Een integratie kan nu een opdracht blootstellen die een betekenisvolle uitvoer retourneert — zoals een tunnel-URL — in plaats van simpelweg ergens de status te wijzigen.

## Conclusie

Aspire 13.3 is de update waard al was het alleen maar voor de Kubernetes-ondersteuning. De browserlogboeken en gestructureerde opdrachtresultaten voelen aan als het soort verbeteringen van levenskwaliteit die snel ophopen in een alledaagse ontwikkelingsworkflow.

Volledige release-opmerkingen: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
