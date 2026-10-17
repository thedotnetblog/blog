---
title: "Aspire + Agent Framework begint eruit te zien als de echte multi-agentstack"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "Het nieuwe AlpineAI-voorbeeld laat zien wat er gebeurt wanneer Aspire en Microsoft Agent Framework worden gebruikt voor een echt gedistribueerd multi-agentsysteem. Het belangrijke deel is niet de skidemo. Het is het architectuurpatroon erachter."
tags:
  - Aspire
  - Agent Framework
  - .NET
  - Microsoft Foundry
  - Architecture
---

Multi-agentdemo's zijn momenteel overal.

Het probleem is dat velen ervan stoppen net vóór het deel dat pijn doet in het echte leven: deploymentvorm, servicebekabeling, gezondheid, telemetrie, runtimegrenzen en de gewone chaos van gedistribueerde systemen.

Daarom is het nieuwe **Aspire + Microsoft Agent Framework**-voorbeeld de moeite van het opletten waard.

Nee, het interessante deel is niet het conciërgescenario voor het skiresort.

Het interessante deel is dat het voorbeeld een veel realistischer patroon laat zien voor het bouwen van een gedistribueerd agentsysteem met:

- aangepaste hosted agents
- prompt agents
- meerdere runtimes
- servicereferenties
- livegegevensbronnen
- observability en deploymentstructuur

Dat is het echte verhaal.

## Dit is meer dan "een agent die tools gebruikt"

De architectuur in het voorbeeld gaat verder dan het vertrouwde single-loop-agentmodel.

Je hebt:

- specialistagents met smalle verantwoordelijkheden
- adviesagents die ze orchestreren
- door Foundry beheerde resources
- .NET-, Python- en Go-services in dezelfde graaf
- spraak- en chattoegangspunten

Dit ligt veel dichter bij hoe serieuze agentsystemen er in de praktijk daadwerkelijk uit zullen zien.

En daar wordt Aspire ineens heel belangrijk.

## Aspire doet het lastige deel dat mensen meestal in hun hoofd houden

Wat ik hier het meest waardeer, is niet eens de agentlogica. Het is het feit dat de **applicatiegraaf expliciet is**.

Aspire wordt gebruikt om te beschrijven:

- welke services bestaan
- waarvan ze afhankelijk zijn
- welke modeldeployments ze nodig hebben
- welke runtime elke service gebruikt
- welke gezondheids- en deploymentrelaties bestaan

Dat is belangrijk omdat gedistribueerde agentsystemen snel rommelig worden. Als de topologie alleen bestaat in de hoofden van mensen en willekeurige setupdocumenten, wordt je systeem direct broos.

Die topologie in de AppHost plaatsen is een enorme stap richting iets reproduceerbaars.

## Specialistagents als tools blijft het patroon om te volgen

Een van mijn favoriete onderdelen van de architectuur is de manier waarop specialistagents worden blootgesteld als aanroepbare mogelijkheden voor een orchestrator.

Dat patroon blijft om een reden opduiken. Het geeft je:

- scheiding van verantwoordelijkheden
- betere domeingrenzen
- duidelijkere observability
- makkelijkere vervanging van één specialist zonder alles te herschrijven

Voor .NET-teams is dit een veel gezonder mentaal model dan het bouwen van één gigantische alwetende agent en hopen dat promptinstructies hem stabiel houden.

## Mijn standpunt

Het belangrijke dat dit voorbeeld bewijst, is niet dat multi-agent-apps mogelijk zijn. Dat wisten we al.

Het bewijst dat de Microsoft-stack begint een samenhangend antwoord te bieden op de volgende vraag:

**hoe bouw je multi-agentsystemen die nog steeds bestuurbaar aanvoelen?**

Aspire voor de graaf. Agent Framework voor de runtime-abstracties. Foundry voor beheerde AI-resources en hosting. Die combinatie begint minder experimenteel aan te voelen en meer als een echt platformverhaal.

Dat is wat ik hier zou volgen.

Oorspronkelijke post: [Distributed multi-agent systems with Aspire and Microsoft Agent Framework](https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework/)