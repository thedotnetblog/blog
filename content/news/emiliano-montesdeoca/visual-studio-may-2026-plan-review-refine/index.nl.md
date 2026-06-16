---
title: "De Visual Studio-update van mei gaat eigenlijk over betere controle tussen idee en verandering"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "De Visual Studio-update van mei voegt de Plan agent, verbeteringen in skillbeheer, zichtbaarheid van het contextvenster en sterkere multi-file diff-ervaringen toe. Het gemeenschappelijke thema is betere controle over de AI-assisted inner loop."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *Dit artikel is automatisch vertaald. Lees het origineel [hier]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}).* 

Het interessantste aan de Visual Studio-update van mei is niet één geïsoleerde functie.

Het is de gedeelde richting.

Deze release verbetert steeds verder de ruimte tussen:

- een idee
- een plan
- een gegenereerde wijziging
- een review
- een verfijnd resultaat

Dat is het deel van AI-assisted development dat bepaalt of de workflow betrouwbaar of chaotisch aanvoelt.

## De functieset is divers, maar de intentie is consistent

Op papier bevat deze release een mix van dingen:

- de nieuwe Plan agent
- verbeteringen in skillbeheer
- zichtbaarheid van het contextvenster
- multi-file summary diff
- opschoning van de Copilot-gerelateerde workflow
- MSVC-updates aan de C++-kant

Dat kan eruitzien als een grab bag.

Ik denk van niet.

De rode draad is vrij duidelijk: **Visual Studio probeert ontwikkelaars meer controle te geven over AI-assisted werk zonder hen af te remmen.**

Dat is precies de juiste trade-off om na te streven.

## De Plan agent is het filosofische centrum van deze release

Ook al zijn andere functies belangrijk, ik blijf denken dat de Plan agent het meest onthullende onderdeel van deze update is.

Het maakt expliciet iets wat veel van ons hebben gevoeld bij het gebruik van coding agents:

snel beginnen is niet altijd hetzelfde als effectief vooruitkomen.

De release zet dat kracht bij door planning, review en gecontroleerde implementatie een natuurlijkere volgorde te maken.

Dat is gezond.

## Het multi-file diff-werk is stilletjes een grote verbetering

Ik denk ook dat de multi-file summary diff meer credit verdient dan het waarschijnlijk zal krijgen.

Wanneer agents meerdere bestanden tegelijk wijzigen, wordt de review-ervaring het product.

Als het reviewen van wijzigingen rommelig voelt, vertrouwen ontwikkelaars de workflow minder.

Als het reviewen van wijzigingen samenhangend voelt, blijven ontwikkelaars het tool eerder gebruiken.

Daarom is een uniforme summary-view zo belangrijk. Die verlaagt de cognitieve kost van ja of nee zeggen tegen gegenereerd werk.

## De contextvenster-indicator is slimmer dan hij klinkt

Ik vind de contextgebruik-indicator ook goed.

Het klinkt misschien als een klein detail, maar het lost een heel reëel AI-workflowprobleem op: niet weten wanneer het tool het eerdere deel van het gesprek begint te vergeten.

Dat zichtbaar maken is een goede designkeuze.

Het vergroot het modelcontextvenster niet magisch. Maar het maakt de limiet observeerbaar, en dat is vaak het op één na beste.

## Mijn mening

Deze update gaat eigenlijk over ontwikkelaars meer zichtbaarheid en controle geven over de AI-assisted loop.

Niet meer nieuwigheid.
Niet meer chaos.
Meer controle.

Dat is precies de juiste plek om in te investeren als het doel is om AI-tools betrouwbaarder te laten voelen binnen een serieuze IDE-workflow.

Originele publicatie: [Visual Studio-update van mei — plannen, reviewen, verfijnen](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)