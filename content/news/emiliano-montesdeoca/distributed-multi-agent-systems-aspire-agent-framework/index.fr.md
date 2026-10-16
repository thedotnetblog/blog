---
title: "Aspire + Agent Framework commence à ressembler à la vraie pile multi-agents"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "Le nouvel exemple AlpineAI montre ce qui se passe quand Aspire et Microsoft Agent Framework sont utilisés pour un vrai système multi-agents distribué. La partie importante n'est pas la démo de ski. C'est le modèle architectural derrière."
tags:
  - Aspire
  - Agent Framework
  - .NET
  - Microsoft Foundry
  - Architecture
---

Les démos multi-agents sont partout en ce moment.

Le problème, c'est que beaucoup d'entre elles s'arrêtent juste avant la partie qui fait mal dans la vraie vie : la forme du déploiement, le câblage des services, la santé, la télémétrie, les limites d'exécution, et le simple chaos des systèmes distribués.

C'est pourquoi le nouvel exemple **Aspire + Microsoft Agent Framework** mérite qu'on lui prête attention.

Non, la partie intéressante n'est pas le scénario de concierge de station de ski.

La partie intéressante, c'est que l'exemple montre un modèle bien plus réaliste pour construire un système d'agents distribué avec :

- des agents hébergés personnalisés
- des agents de prompt
- plusieurs runtimes
- des références de service
- des sources de données en direct
- de l'observabilité et une structure de déploiement

C'est la vraie histoire.

## C'est plus qu'« un agent qui utilise des outils »

L'architecture de l'exemple va au-delà du modèle familier d'agent à boucle unique.

Vous avez :

- des agents spécialistes aux responsabilités étroites
- des agents conseillers qui les orchestrent
- des ressources gérées par Foundry
- des services .NET, Python et Go dans le même graphe
- des points d'entrée vocaux et de chat

C'est bien plus proche de ce à quoi ressembleront réellement les systèmes d'agents sérieux en pratique.

Et c'est là qu'Aspire devient soudainement très important.

## Aspire fait la partie difficile que les humains gardent habituellement dans leur tête

Ce que j'apprécie le plus ici, ce n'est même pas la logique de l'agent. C'est le fait que **le graphe applicatif est explicite**.

Aspire est utilisé pour décrire :

- quels services existent
- de quoi ils dépendent
- quels déploiements de modèle il leur faut
- quel runtime chaque service utilise
- quelles relations de santé et de déploiement existent

Cela compte parce que les systèmes d'agents distribués deviennent vite chaotiques. Si la topologie n'existe que dans la tête des gens et dans des documents de configuration aléatoires, votre système devient immédiatement fragile.

Mettre cette topologie dans l'AppHost est un pas immense vers quelque chose de reproductible.

## Les agents spécialistes en tant qu'outils restent le modèle à surveiller

L'une de mes parties préférées de l'architecture, c'est la façon dont les agents spécialistes sont exposés comme des capacités appelables pour un orchestrateur.

Ce modèle revient sans cesse pour une raison. Il vous donne :

- une séparation des préoccupations
- de meilleures limites de domaine
- une observabilité plus claire
- un remplacement plus facile d'un spécialiste sans tout réécrire

Pour les équipes .NET, c'est un modèle mental bien plus sain que de construire un gigantesque agent omniscient et d'espérer que les instructions de prompt le maintiennent stable.

## Mon avis

Ce que cet exemple prouve d'important, ce n'est pas que les applications multi-agents soient possibles. On le savait déjà.

Il prouve que la pile Microsoft commence à offrir une réponse cohérente à la prochaine question :

**comment construit-on des systèmes multi-agents qui restent exploitables ?**

Aspire pour le graphe. Agent Framework pour les abstractions d'exécution. Foundry pour les ressources IA gérées et l'hébergement. Cette combinaison commence à sembler moins expérimentale et davantage comme une vraie histoire de plateforme.

C'est ce que je surveillerais ici.

Original post: [Distributed multi-agent systems with Aspire and Microsoft Agent Framework](https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework/)
