---
title: "Aspire dans VS Code 13.4 resserre la boucle de développement de la bonne façon"
date: 2026-06-16
author: "Emiliano Montesdeoca"
description: "Aspire dans VS Code 13.4 n'est pas qu'une mise à jour de fonctionnalité. C'est une véritable amélioration de la boucle de développement quotidienne avec un meilleur débogage, une meilleure visibilité des ressources, une intégration de panneau et le support de TypeScript AppHost."
tags:
  - Aspire
  - VS Code
  - .NET
  - Developer Experience
  - TypeScript
---

Les meilleures mises à jour d'outillage sont celles que vous ressentez après quelques jours, pas celles qui semblent seulement bonnes dans les notes de version.

C'est ainsi que **Aspire dans VS Code 13.4** se présente à mes yeux.

Cette mise à jour porte entièrement sur le resserrement de la boucle interne : créer des projets plus vite, déboguer des ressources multi-langage plus naturellement, faire remonter la santé et les commandes directement dans l'éditeur, et garder le tableau de bord à portée de main sans en faire le seul endroit où travailler.

C'est une très bonne direction.

## La grande victoire, c'est moins de changement de contexte

Si vous utilisez Aspire sérieusement, vous naviguez habituellement entre plusieurs surfaces :

- le code AppHost
- le terminal
- le tableau de bord
- les logs
- les sessions de débogage
- les points de terminaison de service

Ce que la 13.4 fait bien, c'est réduire la friction entre ces surfaces.

La nouvelle expérience VS Code rend plus d'état d'application visible exactement là où vous travaillez déjà :

- la santé des ressources dans l'éditeur
- des commandes à côté des déclarations de ressources
- un accès plus facile au tableau de bord
- l'accès aux logs depuis le contexte de l'AppHost
- un panneau qui reste utile même avant le début complet du débogage

Cela semble anodin jusqu'à ce que vous le fassiez tous les jours.

## Déboguer des piles mixtes compte plus que les gens ne le pensent

L'une des parties les plus fortes de cette mise à jour est l'histoire plus naturelle pour déboguer **C#, TypeScript, Python, Go, les applications navigateur et Azure Functions** dans un flux piloté par Aspire.

Cela reflète bien mieux la forme réelle des applications modernes que de prétendre que tout vit dans un seul runtime.

Pour les développeurs .NET en particulier, c'est précieux parce que beaucoup d'entre nous construisent désormais des systèmes qui mélangent des projets API, des frontends, des workers et des services adjacents à l'IA dans différents langages.

Le fait qu'Aspire rende cela plus unifié à l'intérieur de VS Code est une amélioration très pratique.

## L'arrivée en GA du support TypeScript AppHost est aussi significative

Je n'ignorerais pas le volet TypeScript AppHost de cette sortie.

Aspire devenant plus naturel à la fois pour C# et TypeScript élargit qui peut travailler dans le même modèle de système sans workflows étranges de seconde classe. Cela compte pour les équipes où le code de plateforme, le code frontend et l'orchestration de service vivent tous proches.

## Mon avis

Aspire 13.4 dans VS Code ne repose pas sur une seule fonctionnalité phare. Il s'agit de lisser les aspérités de la boucle quotidienne :

- démarrer plus vite
- voir plus d'état là où vous codez
- déboguer plus naturellement
- accéder aux logs et au tableau de bord seulement quand nécessaire

C'est exactement comment un bon outillage devrait évoluer.

Si vous utilisez déjà Aspire, cette mise à jour vaut la peine d'être installée. Si vous vous demandez encore si VS Code est un vrai foyer pour le développement basé sur Aspire, la réponse devient de plus en plus évidente.

Original post: [Aspire in VS Code: the 13.4 developer loop](https://devblogs.microsoft.com/aspire/aspire-vscode-extension-13-4/)
