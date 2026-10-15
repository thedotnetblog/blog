---
title: "Aspire + Agent Framework Comença a Semblar-se al Stack Multi-Agent Real"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "La nova mostra d'AlpineAI mostra què passa quan Aspire i Microsoft Agent Framework s'utilitzen per a un sistema multi-agent distribuït real. La part important no és la demo d'esquí. És el patró d'arquitectura que hi ha al darrere."
tags:
  - Aspire
  - Agent Framework
  - .NET
  - Microsoft Foundry
  - Architecture
---

Les demos multi-agent són a tot arreu ara.

El problema és que moltes s'aturen just abans de la part que fa mal a la vida real: la forma de desplegament, el cablejat de serveis, la salut, la telemetria, els límits d'execució i el caos pur dels sistemes distribuïts.

Per això val la pena parar atenció a la nova mostra d'**Aspire + Microsoft Agent Framework**.

No, la part interessant no és l'escenari de conserge d'estació d'esquí.

La part interessant és que la mostra mostra un patró molt més realista per construir un sistema d'agents distribuït amb:

- agents hostatjats personalitzats
- agents prompt
- múltiples runtimes
- referències de servei
- fonts de dades en viu
- observabilitat i estructura de desplegament

Aquesta és la història real.

## Això és més que "un agent que utilitza eines"

L'arquitectura de la mostra va més enllà del model familiar d'agent de bucle únic.

Teniu:

- agents especialistes amb responsabilitats estretes
- agents assessors que els orquestren
- recursos gestionats per Foundry
- serveis .NET, Python i Go al mateix graf
- punts d'entrada de veu i xat

Això està molt més a prop de com seran els sistemes d'agents seriosos a la pràctica.

I aquí és on Aspire es torna de sobte molt important.

## Aspire està fent la part difícil que els humans solen mantenir als seus caps

El que més m'agrada aquí no és ni tan sols la lògica de l'agent. És el fet que el **graf d'aplicació és explícit**.

Aspire s'està utilitzant per descriure:

- quins serveis existeixen
- de què depenen
- quins desplegaments de model necessiten
- quin runtime utilitza cada servei
- quines relacions de salut i desplegament existeixen

Això importa perquè els sistemes d'agents distribuïts es tornen desordenats ràpidament. Si la topologia només existeix als caps de la gent i en documents de configuració aleatoris, el vostre sistema es torna fràgil immediatament.

Posar aquesta topologia a l'AppHost és un gran pas cap a una cosa reproduïble.

## Els agents especialistes com a eines segueix sent el patró a seguir

Una de les meves parts favorites de l'arquitectura és la manera com els agents especialistes es mostren com a capacitats invocables per a un orquestrador.

Aquest patró segueix apareixent per una raó. Us dóna:

- separació de preocupacions
- millors límits de domini
- observabilitat més clara
- substitució més fàcil d'un especialista sense reescriure-ho tot

Per als equips .NET, aquest és un model mental molt més saludable que construir un agent gegant que ho sap tot i esperar que les instruccions del prompt el mantinguin estable.

## La meva opinió

El que aquesta mostra demostra no és que les aplicacions multi-agent siguin possibles. Ja ho sabíem.

Demostra que el stack de Microsoft està començant a oferir una resposta coherent a la següent pregunta:

**com construeixes sistemes multi-agent que encara se sentin operables?**

Aspire per al graf. Agent Framework per a les abstraccions d'execució. Foundry per als recursos d'IA gestionats i l'hostatjament. Aquesta combinació comença a sentir-se menys experimental i més com una història de plataforma real.

Això és el que miraria aquí.

Article original: [Distributed multi-agent systems with Aspire and Microsoft Agent Framework](https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework/)