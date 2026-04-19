---
title: "Azure DevOps finalment soluciona l'UX de l'editor de Markdown de què es va queixar tothom"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'editor d'Azure DevOps Markdown per a elements de treball obté una distinció més clara entre el mode de previsualització i el d'edició. És un petit canvi que soluciona un problema de flux de treball realment molest."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

Si utilitzeu Azure Boards, probablement haureu experimentat això: esteu llegint la descripció d'un element de treball, potser revisant els criteris d'acceptació i accidentalment feu doble clic. Boom: esteu en mode d'edició. No volies editar res. Només estaves llegint.

Dan Hellem [va anunciar la correcció](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), i és un d'aquests canvis que sona minúscul però que en realitat elimina la fricció real del vostre flux de treball diari.

## Què va canviar

L'editor Markdown per als camps de text d'elements de treball ara s'obre en **mode de vista prèvia de manera predeterminada**. Podeu llegir i interactuar amb el contingut (seguir enllaços, revisar el format) sense preocupar-vos d'entrar accidentalment al mode d'edició.

Quan realment voleu editar, feu clic a la icona d'edició a la part superior del camp. Quan hàgiu acabat, torneu al mode de previsualització explícitament. Simple, intencionat, previsible.

Això és tot. Aquest és el canvi.

## Per què això importa més del que sembla

El [fil de comentaris de la comunitat](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) sobre això era llarg. El comportament de fer doble clic per editar es va introduir amb l'editor Markdown el juliol de 2025 i les queixes van començar gairebé immediatament. El problema no eren només les edicions accidentals, sinó que tota la interacció semblava impredictible. Mai no sabíeu si fer clic es llegiria o editaria.

Per als equips que fan planificació d'esprints, preparació de backlog o revisió de codi amb Azure Boards, aquest tipus de compostos de microfricció. Cada entrada accidental del mode d'edició és un canvi de context. Cada "espera, he canviat alguna cosa?" moment és una atenció perduda.

El nou valor predeterminat respecta el patró d'interacció més comú: llegiu els elements de treball amb molta més freqüència que no els editeu.

## Estat de llançament

Això ja s'està implementant a un subconjunt de clients i s'ampliarà a tothom durant les properes dues o tres setmanes. Si encara no ho veus, aviat ho faràs.

## Tancant

No totes les millores han de ser una característica de titular. De vegades, la millor actualització és simplement eliminar alguna cosa molesta. Aquest és un d'ells: una petita correcció d'UX que fa que Azure Boards se senti menys hostil a les persones que només volen llegir els seus elements de treball amb tranquil·litat.
