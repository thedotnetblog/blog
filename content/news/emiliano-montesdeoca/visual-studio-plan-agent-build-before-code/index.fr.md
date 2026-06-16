---
title: "Le nouvel agent Plan dans Visual Studio résout un vrai problème de workflow IA"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Le nouvel agent Plan de Visual Studio compte parce qu'il crée une étape de planification structurée avant l'implémentation, exactement ce dont les grosses fonctionnalités et les refactorings ont souvent besoin."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Cet article a été traduit automatiquement. Lisez l'original [ici]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

L'un des workflows de codage IA les plus frustrants, c'est quand l'implémentation démarre trop vite.

Le code peut même être techniquement correct, mais il résout la mauvaise version du problème que vous aviez en tête.

Vous vouliez un refactoring. Cela a lancé un rewrite.
Vous vouliez une amélioration ciblée. Cela a touché la moitié du projet.
Vous vouliez discuter des options. Cela est passé directement aux changements de fichiers.

C'est pourquoi le nouvel **agent Plan** dans Visual Studio est un ajout si utile.

## Cela résout un vrai problème de workflow, pas seulement un problème cosmétique

Le billet original décrit une situation très familière : "**Le code n'est pas faux... il n'est juste pas ce que vous vouliez.**"

Cette phrase est parfaite.

Parce que le point faible de beaucoup de développement assisté par IA n'est pas de savoir si le modèle peut produire du code. C'est de savoir si le workflow crée assez d'espace pour s'accorder sur la forme voulue du travail avant de commencer l'implémentation.

Cela compte surtout pour :

- les grosses fonctionnalités
- les bases de code inconnues
- les refactorings non triviaux
- les changements sensibles à l'architecture
- le travail qui nécessite une revue d'équipe avant le début des modifications

Dans ces situations, aller directement à l'implémentation est souvent le mauvais choix.

## La planification n'est pas du surcoût quand la tâche est réelle

Je pense que les équipes sous-estiment parfois le temps perdu à commencer l'implémentation trop tôt.

Si l'agent :

- modifie les mauvais fichiers
- choisit la mauvaise approche
- ignore une contrainte essentielle
- passe à côté d'un cas limite requis

alors le démarrage "rapide" devient, au final, un workflow plus lent.

C'est pour cela que j'aime cette fonctionnalité.

Elle laisse de la place pour :

- des questions de clarification
- la rédaction du plan
- l'édition directe du plan
- le partage du plan avant le début des changements de code

Ce n'est pas de la bureaucratie. C'est souvent juste de la bonne ingénierie.

## Le fichier de plan en markdown est un choix intelligent

Un détail que j'aime particulièrement est que chaque plan est enregistré dans `.copilot/plans/plan-{title}.md`.

Cela rend l'étape de planification tangible.

Le plan n'est pas prisonnier d'un fil de discussion. Il devient quelque chose que vous pouvez :

- relire
- modifier
- versionner mentalement
- discuter avec l'équipe
- transmettre à l'implémentation plus délibérément

Cela donne à la fonctionnalité un côté bien plus sérieux qu'un simple préambule temporaire avant la génération de code.

## C'est là que les workflows IA commencent à respecter le processus d'équipe

Je pense que c'est l'un des signes les plus forts de la maturité de ces outils.

Les meilleurs workflows IA pour développeurs ne sont pas ceux qui suppriment toutes les étapes intermédiaires. Ce sont ceux qui améliorent les bonnes étapes intermédiaires.

Et la planification est l'une de ces étapes.

Si le plan est solide, l'implémentation devient plus facile.
Si le plan est faible, l'implémentation devient bruyante.

Cette fonctionnalité l'assume directement.

## Mon avis

Ce n'est pas juste un confort IA.

C'est une amélioration du workflow.

Et pour les vraies fonctionnalités et les vrais refactorings, c'est exactement le genre d'amélioration qui peut éviter beaucoup de churn inutile, de bruit de revue et de rework du type "ce n'est pas ce que je voulais dire".

Je pense que de plus en plus d'expériences d'agents finiront par avoir besoin de quelque chose comme cela.

Visual Studio y est arrivé plus tôt, d'une manière utile.

Publication originale : [Planifier avant de construire : présentation de l'agent Plan dans Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)