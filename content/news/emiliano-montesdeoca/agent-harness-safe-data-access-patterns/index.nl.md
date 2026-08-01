---
title: 'De echte winst in agent-UX is veilige autonomie, niet maximale autonomie'
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: 'Bestandstoegang, goedkeuringen en geheugenontwerp vormen de praktische drie-eenheid voor betrouwbaar agentgedrag in productie.'
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Oorspronkelijke bron: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

Dit is een van de nuttigere agent-engineeringposts dit jaar omdat het de gebruikelijke valkuil van demo-eerst-autonomie weigert. In plaats daarvan richt het zich op hoe agents zouden moeten opereren rond echte gebruikersdata en echte consequenties.

De drie bouwstenen die hier worden belicht, zijn precies juist.

Bestandstoegang geeft agents nuttige verankering in data die van de gebruiker is.

Goedkeuringspoorten voorkomen stille uitvoering van consequentiële acties.

Duurzaam geheugen voorkomt repetitieve interacties zonder controle op te offeren.

De meeste teams investeren te veel in tool-breedte en te weinig in permissiesemantiek. Dat is achterstevoren. Een agent met tien tools en zwakke goedkeuringsgrenzen is minder waardevol dan een agent met drie tools en voorspelbare controlepunten.

Het beste praktische patroon in dit artikel is een gelaagde goedkeuringsstrategie:

Vereis altijd goedkeuring voor high-impact tools zoals handelen of destructieve operaties.

Keur automatisch risicoarme leesacties goed om de flow te behouden.

Gebruik afgebakende staande goedkeuringen voor repetitieve vertrouwde acties binnen een sessie.

Dit creëert een gezonde risicogradiënt. Gebruikers worden niet onderbroken voor onschadelijke leesacties, maar blijven wel betrokken wanneer consequenties duur of onomkeerbaar worden.

Ik waardeer ook de expliciete splitsing tussen bestandsgeheugen en Foundry-geheugen. Teams zouden moeten stoppen met proberen één geheugenmodel te forceren om elk probleem op te lossen. Grove, expliciete bestandsartefacten zijn uitstekend voor gebruikerszichtbare status zoals rapporten en watchlists. Feitniveau-geheugenextractie is beter voor voorkeuren en gespreekscontext. Beide combineren geeft betere resultaten dan doen alsof een van beide voldoende is.

Mijn eigenzinnige mening: de toekomst van agentkwaliteit zal minder gemeten worden aan slimme prompts en meer aan veiligheidsergonomie. Als je goedkeuringspromts rommelig zijn, klikken gebruikers er blindelings doorheen. Als je geheugengrenzen onduidelijk zijn, stoppen gebruikers met het vertrouwen van de assistent. Als je databank-toegangsdefaults te permissief zijn, sluiten beveiligingsteams het project.

Voor .NET- en Python-teams die dit patroon toepassen, is de belangrijkste stap om policy-callbacks en goedkeuringsregels te behandelen als kernbedrijfslogica, versiebeheerd en getest zoals elke andere kritieke code. Laat ze niet als ad-hoc lambda's begraven in voorbeelden.

Agentsystemen die vertrouwen verdienen, zijn niet degene die het meeste doen. Het zijn degene die precies doen wat gebruikers bedoelden, niet meer, niet minder, met duidelijke onderbrekingspunten wanneer risico toeneemt.

Dat is het verschil tussen een indrukwekkende demo en software waaraan mensen bereid zijn echt werk te delegeren.
