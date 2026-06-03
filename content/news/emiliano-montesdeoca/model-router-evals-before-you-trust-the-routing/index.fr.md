---
title: "Les évaluations du model router sont l'étape que trop d'équipes sautent"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Le nouveau dépôt d'évaluation du model router dans Foundry est important, car les décisions de routage doivent être mesurées en fonction de la qualité, de la latence et du coût avant que les équipes ne traitent la sélection automatique de modèles comme de la magie."
tags:
  - Microsoft Foundry
  - AI
  - Evaluations
  - Model Router
  - Cost Optimization
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Le routage automatique des modèles semble génial jusqu'au moment où l'on réalise qu'il faut encore prouver que c'est le bon choix pour votre charge de travail.

C'est pourquoi le nouveau **dépôt d'évaluation du model router** est utile.

Il donne aux équipes une façon plus concrète de répondre aux questions qui comptent vraiment :

- le routage préserve-t-il la qualité ?
- améliore-t-il le coût ?
- qu'en est-il de la latence ?
- que se passe-t-il si je restreins le sous-ensemble de modèles ?

## L'article source pose les bonnes questions

Ce que j'aime particulièrement dans l'article original, c'est qu'il ne traite pas le model router comme étant évidemment bon.

À la place, il pose les questions inconfortables mais justes :

- "**Sur mes prompts, le modèle sélectionné automatiquement par le model router égalise-t-il ou dépasse-t-il le modèle unique que je choisirais sinon ?**"
- "**Est-ce que j'économise réellement de l'argent de bout en bout, ou est-ce que je ne fais que déplacer les dépenses d'un endroit à un autre ?**"

C'est exactement la bonne attitude.

Parce que le routage automatique est attrayant, mais cela reste une décision de système. Et les décisions de système doivent être mesurées, pas admirées.

## Pourquoi ce dépôt compte plus qu'il n'y paraît au premier abord

À un niveau, il ne s'agit que d'un dépôt d'évaluation.

À un autre niveau, c'est un signe de maturité.

Cela dit : si vous voulez adopter le routage automatique, voici une façon plus disciplinée de tester :

- la qualité
- le coût
- la latence
- les compromis liés au sous-ensemble
- le comportement de distribution des modèles

C'est bien mieux que de traiter le routage comme une boîte noire avec une bonne image de marque.

## Mon avis

C'est un bon exemple du type d'outils dont les plateformes d'IA ont besoin davantage : pas plus de magie, mais davantage de moyens de valider la magie avant de lui faire confiance.

C'est ainsi que les équipes évitent de bâtir une confiance coûteuse sur des hypothèses non testées.

Article original : [How to run evals for the model router](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)
