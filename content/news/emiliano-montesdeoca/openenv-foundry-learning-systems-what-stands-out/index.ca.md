---
title: "OpenEnv i Foundry empenyen la conversa més enllà dels agents estàtics"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "La nova història d'OpenEnv i Foundry va molt més enllà dels clixés de reinforcement learning. En realitat, impulsa sistemes d'agents que es poden avaluar, optimitzar i millorar amb el temps segons resultats empresarials reals."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

La majoria de converses sobre agents encara s'aturen a la inferència.

El model pot respondre a la petició? Pot cridar l'eina? Pot completar la tasca un cop?

La nova conversa sobre **OpenEnv + Foundry** és interessant perquè intenta portar la discussió cap a una cosa més ambiciosa: **com es construeix un sistema d'agents que realment millora amb el temps?**

Aquesta és una pregunta molt millor.

## El canvi clau és passar de les respostes als bucles d'aprenentatge

La publicació de Foundry emmarca el problema al voltant d'entorns, avaluacions, rúbriques, optimització i post-entrenament.

Es pot resumir tot això en una sola frase:

**l'objectiu ja no és només executar un agent, sinó tenir un bucle que mesuri i millori l'agent contra els teus resultats reals.**

Això és el que crec que els desenvolupadors han de tenir en compte.

Perquè, un cop ho veus així, l'actiu durador no és només el model o la petició. És el sistema que l'envolta:

- l'entorn on actua
- la rúbrica que el puntua
- els traces que expliquen què ha passat
- l'optimitzador que millora la configuració

Aquesta és una manera molt més preparada per a l'empresa de pensar-hi.

## Per què importa fins i tot si no fas recerca en RL

Siguem sincers: termes com OpenEnv, post-entrenament i world-modeling poden fer que molts desenvolupadors desconnectin immediatament.

Però la conclusió pràctica és més simple que la terminologia.

Encara que no toquis mai directament un bucle d'entrenament, aquesta feina modela la història de la plataforma per al desenvolupament futur d'agents:

- les avaluacions passen a ser de primera classe
- l'optimització esdevé contínua en lloc d'ocasional
- els entorns es converteixen en actius reutilitzables
- un millor comportament de l'agent esdevé una cosa mesurable, no només "sembla millor a les demos"

És un gran pas endavant.

## La meva opinió

El més intel·ligent d'aquest anunci no és cap detall de recerca en concret.

És l'enquadrament.

Microsoft està clarament intentant portar l'ecosistema de l'enginyeria d'ordres estàtiques cap a **sistemes d'agents orientats a resultats**. Sistemes que es poden avaluar, ajustar, governar i millorar gradualment.

Aquí és on hi ha el valor seriós de la plataforma.

I si avui estàs construint agents, fins i tot a nivell d'aplicació, val la pena seguir cap a on es dirigeix això.

Publicació original: [Sistemes d'aprenentatge orientats a resultats: RL empresarial amb OpenEnv i Foundry](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)