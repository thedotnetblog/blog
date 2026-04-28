---
title: "Azure SDK april 2026: AI Foundry 2.0 en wat .NET-ontwikkelaars moeten weten"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "De Azure SDK-release van april 2026 brengt Azure.AI.Projects 2.0.0 stable met belangrijke breaking changes, kritieke beveiligingsfixes voor Cosmos DB en een golf aan nieuwe Provisioning-bibliotheken voor .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "index.md" >}}).*

Maandelijkse SDK-releases zijn vaak makkelijk over te slaan. Deze heeft een paar dingen waar je op wilt letten — vooral als je bouwt met AI Foundry, met Cosmos DB in Java, of infrastructuur provisiont vanuit .NET-code.

## Azure.AI.Projects 2.0.0 — Breaking changes die logisch zijn

Het `Azure.AI.Projects` NuGet-pakket bereikt stable 2.0.0 met een aantal belangrijke architectuurwijzigingen. Als je al de preview gebruikt, is dit wat er veranderd is:

- **Namespace-splitsing**: Evaluations zijn verhuisd naar `Azure.AI.Projects.Evaluation`, en memory operations naar `Azure.AI.Projects.Memory`. Je moet je `using`-statements bijwerken.
- **Hernoemde types**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Naamconventies**: booleaanse properties volgen nu consequent de `Is*`-conventie

Dit zijn precies het soort breaking changes die één keer pijn doen en daarna gewoon goed voelen. Als je op de preview hebt gebouwd, werk je imports bij en laat de compiler de rest aanwijzen.

Het goede nieuws: het is nu stable. Je kunt nu echt op deze API vertrouwen.

## Cosmos DB Java: kritieke beveiligingsfix (RCE)

Dit is serieus. De Java Cosmos DB-bibliotheek (`azure-cosmos`) versie 4.79.0 bevat een kritieke beveiligingsfix voor een **Remote Code Execution vulnerability (CWE-502)**.

Het probleem zat in Java-deserialisatie in `CosmosClientMetadataCachesSnapshot`, `AsyncCache` en `DocumentCollection`. De fix vervangt Java-deserialisatie door JSON-gebaseerde serialisatie, waarmee de hele klasse deserialisatie-aanvallen verdwijnt.

Als je Java-services hebt die Azure Cosmos DB gebruiken, update dan meteen naar 4.79.0. Dit is niet optioneel.

## Nieuwe Provisioning-bibliotheken voor .NET

Deze maand zijn er verschillende stabiele Provisioning-bibliotheken naar 1.0.0 gegaan — dit zijn de bibliotheken waarmee je Azure-infrastructuur in C#-code definieert in plaats van ARM-templates of Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Er zitten er nog meerdere in beta.1, voor API Management, Batch, Compute, Monitor, MySQL en Security Center. Als je infrastructure-as-code vanuit .NET doet — vooral met Aspire-deployments — dan zijn deze bibliotheken je startpunt.

## Azure AI Agents Java: 2.0.0 GA

De Java Azure AI Agents-bibliotheek bereikt deze maand ook general availability. De belangrijkste breaking changes:

- Verschillende enum-types zijn omgezet naar klassen op basis van `ExpandableStringEnum` (flexibeler voor nieuwe waarden)
- `*Param`-modelklassen zijn hernoemd naar `*Parameter`
- `MCPToolConnectorId` → `McpToolConnectorId` (consistent hoofdlettergebruik)
- Nieuwe convenience overload voor `beginUpdateMemories`

## Afronding

De headline voor .NET-ontwikkelaars deze maand is dat `Azure.AI.Projects 2.0.0` stable wordt — als je met AI Foundry bouwt, is dit het moment om naar stable te pinnen en je imports bij te werken. Voor Java-teams die Cosmos DB gebruiken is de beveiligingsupdate urgent.

De volledige release notes staan op [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). Oorspronkelijk bericht: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).