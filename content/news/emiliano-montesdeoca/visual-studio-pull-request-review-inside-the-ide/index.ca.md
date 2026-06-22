---
title: "Revisar pull requests dins de Visual Studio és exactament el tipus de reducció de fricció que m'agrada"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio ara pot revisar pull requests de principi a fi sense sortir de l'IDE. Pot semblar incremental, però per als equips que viuen tot el dia dins de Visual Studio, elimina molt de canvi de context innecessari."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}}).* 

El navegador ha estat robant massa part del flux de treball de code review durant massa temps.

Per això em fa molta il·lusió veure Visual Studio avançar encara més cap a la **revisió de pull requests de principi a fi dins de l'IDE**.

Aquesta és una d'aquelles funcions que pot no generar grans titulars, però que pot millorar molt el desenvolupament quotidià.

## El valor principal és simple: menys canvi de context

Quan el teu bucle de review viu parcialment dins de l'IDE i parcialment al navegador, la fricció s'acumula:

- obre el PR en un altre lloc
- inspecciona els canvis en una eina
- torna a la solució per investigar més a fons
- canvia una altra vegada per comentar o aprovar

No és catastròfic. Només és ineficient.

Si Visual Studio et permet obrir, inspeccionar, comentar, aprovar i fer merge des del mateix entorn de treball, això és un guany de productivitat real.

## L'opció de "review sense checkout" és especialment bona

Una part que m'agrada especialment és poder revisar sense fer checkout de la branca del PR.

Pot semblar petit, però és perfecte per a:

- passades ràpides de review
- sol·licituds de feedback interrompudes
- mantenir intactes la branca actual i l'estat local

Això és exactament el tipus de flexibilitat que necessiten les bones eines de code review.

## La meva opinió

Això no és una funció revolucionària.

És una cosa millor: una funció pràctica.

Per als equips que passen la major part del dia a Visual Studio, un suport més estret per al review de PR significa menys interrupcions del flux de treball i un camí més suau de la inspecció a l'acció.

És una millora que val la pena, al meu parer.

Publicació original: [Revisa pull requests sense sortir de Visual Studio](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)