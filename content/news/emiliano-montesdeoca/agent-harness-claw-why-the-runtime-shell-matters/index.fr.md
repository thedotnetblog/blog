---
title: "Les harnais d'agents comptent parce que les prompts ne suffisent pas"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "Le nouveau tour d'horizon claw et harnais du Microsoft Agent Framework est un rappel utile que les vrais agents ont besoin d'une coquille d'exécution autour du modèle : outils, planification, mémoire, sessions et une boucle d'exécution pratique."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

L'une des erreurs les plus faciles à commettre dans le développement d'agents est de penser que le prompt est le produit.

Ce n'est pas le cas.

Le nouveau tour d'horizon **harnais et claw d'agent** de l'équipe Microsoft Agent Framework est précieux parce qu'il garde le focus sur la partie qui détermine vraiment si un agent semble utilisable : la coquille d'exécution autour du modèle.

Cela inclut :

- les outils
- la planification
- l'état de session
- la mémoire
- les modes d'exécution
- une console ou une interface utilisable pour l'itération

C'est là que les agents cessent d'être de simples démos ingénieuses et commencent à ressembler à du logiciel.

## Le modèle de harnais est un modèle pratique

Ce que j'apprécie ici, c'est à quel point l'idée est accessible.

Vous commencez avec un client de chat.

Puis vous l'enveloppez dans un harnais avec des instructions et des outils.

Puis vous l'exécutez à travers une coquille qui prend en charge la planification, les todos, les sessions et l'interaction en streaming.

C'est un modèle sain parce qu'il sépare clairement les préoccupations :

- le modèle gère le raisonnement
- le harnais gère le comportement d'exécution
- l'application décide quels outils et expériences comptent

## Cela colle très bien avec la façon dont les développeurs .NET construisent des systèmes

L'idée du harnais correspond aussi bien à l'état d'esprit .NET.

Nous réussissons généralement mieux quand le comportement d'exécution est explicite et composable. Middleware, pipelines, options, providers et adaptateurs, tout cela semble naturel dans ce monde.

C'est pourquoi je pense qu'Agent Framework a de bonnes chances de séduire les développeurs .NET. Il ne force pas tout le monde dans une seule abstraction magique. Il vous donne des pièces d'exécution structurées que vous pouvez assembler.

## Mon avis

La partie la plus utile de ce billet est le rappel que les agents ont besoin de plus qu'un bon modèle et d'une chaîne d'instructions astucieuse.

Ils ont besoin d'une coquille d'exécution qui leur donne structure, mémoire, accès aux outils, planification et une boucle de développement viable.

C'est ce que le harnais vous donne.

Et honnêtement, c'est pourquoi ce modèle mérite qu'on lui prête attention.

Original post: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)
