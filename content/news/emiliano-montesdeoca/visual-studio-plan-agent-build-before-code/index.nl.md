---
title: "De nieuwe Plan agent in Visual Studio lost een heel reëel AI-workflowprobleem op"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "De nieuwe Plan agent in Visual Studio is belangrijk omdat hij vóór de implementatie een gestructureerde planningsfase creëert, precies wat grotere features en refactorings vaak nodig hebben."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Dit artikel is automatisch vertaald. Lees het origineel [hier]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

Een van de frustrerendste AI-coding workflows is wanneer de implementatie te snel begint.

De code kan zelfs technisch prima zijn, maar hij lost de verkeerde versie van het probleem op dat je in gedachten had.

Je wilde een refactor. Het begon met een rewrite.
Je wilde een gerichte verbetering. Het raakte de helft van het project.
Je wilde opties bespreken. Het ging meteen door naar file changes.

Daarom is de nieuwe **Plan agent** in Visual Studio zo'n nuttige toevoeging.

## Dit lost een echt workflowprobleem op, niet alleen een cosmetisch probleem

De originele post beschrijft een heel bekende situatie: "**De code is niet fout... hij is gewoon niet wat je bedoelde.**"

Die zin is perfect.

Want de zwakke plek in veel AI-assisted development is niet of het model code kan maken. Het gaat erom of de workflow genoeg ruimte biedt om het beoogde shape van het werk af te stemmen voordat de implementatie begint.

Dat is vooral belangrijk voor:

- grote features
- onbekende codebases
- niet-triviale refactorings
- architectuurgevoelige veranderingen
- werk dat eerst team review nodig heeft voordat edits beginnen

In zulke situaties is direct naar implementatie springen vaak de verkeerde zet.

## Planning is geen overhead wanneer de taak echt is

Ik denk dat teams soms onderschatten hoeveel tijd ze verliezen door te vroeg met implementeren te beginnen.

Als de agent:

- de verkeerde files aanraakt
- de verkeerde aanpak kiest
- een belangrijke constraint mist
- een noodzakelijke edge case negeert

dan wordt de "snelle" start uiteindelijk een tragere workflow in totaal.

Daarom vind ik deze feature goed.

Hij maakt ruimte voor:

- verhelderende vragen
- het plan opstellen
- het plan direct bewerken
- het plan delen voordat codewijzigingen beginnen

Dat is geen bureaucratie. Het is vaak gewoon goede engineering.

## De markdown plan file is een slimme keuze

Een detail dat ik vooral prettig vind, is dat elk plan wordt opgeslagen in `.copilot/plans/plan-{title}.md`.

Dat maakt de planningsstap tastbaar.

Het betekent dat het plan niet vastzit in een chat transcript. Het wordt iets dat je kunt:

- reviewen
- bewerken
- mentaal versioneren
- met teamleden bespreken
- bewuster doorgeven aan implementatie

Daardoor voelt de feature veel serieuzer dan een tijdelijk voorwoord vóór codegeneratie.

## Hier beginnen AI workflows het teamproces te respecteren

Ik denk dat dit een van de sterkere signalen is dat deze tools aan het rijpen zijn.

De beste AI developer workflows zijn niet degene die alle tussenstappen weghalen. Het zijn degene die de juiste tussenstappen verbeteren.

En planning is een van die stappen.

Als het plan sterk is, wordt implementatie makkelijker.
Als het plan zwak is, wordt implementatie rumoerig.

Deze feature erkent dat direct.

## Mijn mening

Dit is niet zomaar een AI extraatje.

Het is een workflowverbetering.

En voor echte features en echte refactorings is dit precies het soort verbetering dat veel onnodige churn, review noise en "dat bedoelde ik niet"-rework kan besparen.

Ik denk dat steeds meer agent-ervaringen uiteindelijk zoiets nodig zullen hebben.

Visual Studio is daar eerder aangekomen op een manier die nuttig aanvoelt.

Originele publicatie: [Plan before you build: de Plan agent introduceren in Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)