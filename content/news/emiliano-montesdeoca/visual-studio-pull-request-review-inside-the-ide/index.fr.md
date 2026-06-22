---
title: "Revoir les pull requests dans Visual Studio, c'est exactement le genre de réduction de friction que j'aime"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio peut maintenant revoir les pull requests de bout en bout sans quitter l'IDE. Cela peut sembler incrémental, mais pour les équipes qui vivent toute la journée dans Visual Studio, cela supprime beaucoup de changements de contexte inutiles."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *Cet article a été traduit automatiquement. Lisez l'original [ici]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}}).* 

Le navigateur a trop longtemps volé une trop grande partie du workflow de code review.

C'est pourquoi je suis très heureux de voir Visual Studio aller plus loin dans la **revue de pull requests de bout en bout directement dans l'IDE**.

C'est l'une de ces fonctionnalités qui ne feront peut-être pas les gros titres, mais qui peuvent absolument améliorer le développement au quotidien.

## La valeur principale est simple : moins de changements de contexte

Quand votre boucle de review se trouve en partie dans l'IDE et en partie dans le navigateur, la friction s'accumule :

- ouvrir le PR ailleurs
- inspecter les changements dans un outil
- revenir à la solution pour creuser davantage
- recommencer le changement pour commenter ou approuver

Ce n'est pas catastrophique. C'est simplement inefficace.

Si Visual Studio peut vous permettre d'ouvrir, d'inspecter, de commenter, d'approuver et de merger depuis le même environnement de travail, c'est un vrai gain de productivité.

## L'option de revue sans checkout est particulièrement appréciable

Un point que j'aime particulièrement est la possibilité de revoir sans checkout la branche du PR.

Cela paraît petit, mais c'est parfait pour :

- des passes de revue rapides
- des demandes de feedback déclenchées par des interruptions
- conserver intacte la branche actuelle et l'état local

C'est exactement le genre de flexibilité dont les bons outils de code review ont besoin.

## Mon avis

Ce n'est pas une fonctionnalité révolutionnaire.

C'est quelque chose de mieux : quelque chose de pratique.

Pour les équipes qui passent la majeure partie de leur journée dans Visual Studio, un support plus étroit de la revue de PR signifie moins de ruptures dans le workflow et un chemin plus fluide de l'inspection à l'action.

C'est, à mes yeux, une amélioration qui en vaut la peine.

Publication originale : [Revoir des pull requests sans quitter Visual Studio](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)