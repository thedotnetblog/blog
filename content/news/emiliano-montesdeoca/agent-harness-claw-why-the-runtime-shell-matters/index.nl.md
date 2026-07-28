---
title: "Agent-harnassen zijn belangrijk omdat prompts niet genoeg zijn"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "De nieuwe Microsoft Agent Framework claw- en harness-walkthrough is een nuttige herinnering dat echte agents een runtime-schil rond het model nodig hebben: tools, planning, geheugen, sessies en een praktische uitvoeringslus."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Een van de makkelijkste fouten in agent-ontwikkeling is denken dat de prompt het product is.

Dat is het niet.

De nieuwe **agent harness- en claw**-walkthrough van het Microsoft Agent Framework-team is waardevol omdat de focus blijft liggen op het deel dat echt bepaalt of een agent bruikbaar aanvoelt: de runtime-schil rond het model.

Dat omvat:

- tools
- planning
- sessiestatus
- geheugen
- uitvoeringsmodi
- een bruikbare console of interface om te itereren

Dat is waar agents ophouden slimme demo's te zijn en beginnen aan te voelen als software.

## Het harness-patroon is een praktisch patroon

Wat ik hier waardeer, is hoe toegankelijk het idee is.

Je begint met een chatclient.

Vervolgens verpak je die in een harness met instructies en tools.

Daarna voer je het uit via een shell die planning, todo's, sessies en streaminginteractie ondersteunt.

Dat is een gezond patroon omdat het de verantwoordelijkheden duidelijk scheidt:

- het model verzorgt de redenering
- de harness verzorgt het runtimegedrag
- de app bepaalt welke tools en ervaringen ertoe doen

## Dit past heel goed bij hoe .NET-ontwikkelaars systemen bouwen

Het harness-idee sluit ook goed aan bij de .NET-mindset.

We doen het meestal beter wanneer runtimegedrag expliciet en samenstelbaar is. Middleware, pijplijnen, opties, providers en adapters voelen allemaal natuurlijk aan in deze wereld.

Daarom denk ik dat Agent Framework een goede kans heeft om aan te slaan bij .NET-ontwikkelaars. Het dwingt niet iedereen in één magische abstractie. Het geeft je gestructureerde runtime-onderdelen die je samen kunt bekabelen.

## Mijn standpunt

Het nuttigste deel van deze post is de herinnering dat agents meer nodig hebben dan een goed model en een slimme instructiestring.

Ze hebben een runtime-schil nodig die ze structuur, geheugen, tooltoegang, planning en een werkbare ontwikkelaarslus geeft.

Dat is wat de harness je geeft.

En eerlijk gezegd, daarom is dit patroon de moeite van het opletten waard.

Oorspronkelijke post: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)