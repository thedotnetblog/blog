---
title: "OpenEnv en Foundry duwen het gesprek voorbij statische agents"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "Het nieuwe OpenEnv-en-Foundry-verhaal gaat veel verder dan de buzzwords rond reinforcement learning. Het is eigenlijk een zet richting agentsystemen die in de loop van de tijd kunnen worden geëvalueerd, geoptimaliseerd en verbeterd op basis van echte bedrijfsresultaten."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *Dit artikel is automatisch vertaald. Lees het origineel [hier]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

De meeste gesprekken over agents stoppen nog steeds bij inferentie.

Kan het model de prompt beantwoorden? Kan het de tool aanroepen? Kan het de taak één keer voltooien?

De nieuwe **OpenEnv + Foundry**-discussie is interessant omdat die het gesprek naar iets ambitieuzers wil verschuiven: **hoe bouw je een agentsysteem dat in de loop van de tijd echt beter wordt?**

Dat is een veel betere vraag.

## De belangrijkste verschuiving is van reacties naar leerloops

Het Foundry-artikel kadert het probleem rond omgevingen, evals, rubrics, optimalisatie en post-training.

Je kunt dat in één zin samenvatten:

**het doel is niet langer alleen een agent draaien, maar een lus bezitten die de agent meet en verbetert op basis van je echte resultaten.**

Dat is volgens mij het deel waar ontwikkelaars op moeten letten.

Want zodra je het zo ziet, is het duurzame bezit niet alleen het model of de prompt. Het is het systeem eromheen:

- de omgeving waarin het handelt
- de rubric die het beoordeelt
- de traces die uitleggen wat er gebeurde
- de optimizer die de configuratie verbetert

Dat is een veel enterprise-vriendelijkere manier van denken.

## Waarom dit belangrijk is, zelfs als je geen RL-onderzoek doet

Laten we eerlijk zijn: termen als OpenEnv, post-training en world-modeling kunnen veel ontwikkelaars meteen doen afhaken.

Maar de praktische conclusie is eenvoudiger dan de terminologie.

Zelfs als je nooit direct een trainingslus aanraakt, vormt dit werk de platformstory voor toekomstige agentontwikkeling:

- evaluaties worden first-class
- optimalisatie wordt continu in plaats van af en toe
- omgevingen worden herbruikbare assets
- beter agentgedrag wordt iets meetbaars, niet alleen "voelt beter in demo's"

Dat is een grote stap vooruit.

## Mijn mening

Het slimste aan deze aankondiging is niet één specifiek onderzoeksdetail.

Het is de framing.

Microsoft probeert duidelijk het ecosysteem te verplaatsen van statische prompt engineering naar **outcome-driven agentsystemen**. Systemen die kunnen worden geëvalueerd, afgesteld, bestuurd en geleidelijk verbeterd.

Dáár zit de serieuze platformwaarde.

En als je vandaag agents bouwt, zelfs op applicatielaag, is het de moeite waard om te volgen waar dit heen gaat.

Originele publicatie: [Resultaatgerichte leersystemen: Enterprise RL met OpenEnv en Foundry](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)