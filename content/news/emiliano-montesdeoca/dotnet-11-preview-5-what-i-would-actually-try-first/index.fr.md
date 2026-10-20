---
title: ".NET 11 Preview 5 : ce que j'essaierais réellement en premier"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 apporte des améliorations à travers le SDK, le runtime, C#, ASP.NET Core et EF Core. Voici les mises à jour que je pense les plus dignes d'être testées tôt si vous construisez de vraies applications .NET."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

Les billets de préversion .NET sont toujours denses.

C'est une bonne nouvelle pour la plateforme, mais cela signifie aussi que la question pratique se retrouve enterrée : **qu'est-ce que vous devriez réellement tester en premier ?**

.NET 11 Preview 5 apporte beaucoup à travers le SDK, le runtime, les bibliothèques, ASP.NET Core, C#, MAUI et EF Core. Plutôt que de transformer ceci en un gigantesque résumé de changelog, je veux me concentrer sur les parties qui, je pense, méritent une vraie attention des développeurs dès maintenant.

## Le modèle de serveur MCP dans `dotnet new` est un signal

C'est probablement l'élément le plus stratégique de la section SDK.

Quand un modèle de projet atterrit directement dans le SDK, cela signifie que la plateforme ne traite plus le scénario comme niche. Avoir un **modèle de serveur MCP** intégré à `dotnet new` réduit le coût d'essai du modèle et envoie un message clair sur la direction de l'écosystème.

Si vous construisez de l'outillage d'agents, des assistants internes, ou des utilitaires de développement intégrant l'IA en .NET, c'est l'une des premières choses que je testerais.

## Les vérifications de vulnérabilité et de fin de vie au moment de la compilation sont exactement le genre de valeurs par défaut que j'apprécie

La sécurité et la conscience du cycle de vie sont bien meilleures quand la plateforme vous aide *pendant la compilation*, pas après coup dans un rapport séparé que personne ne lit.

Les nouvelles vérifications du SDK pour les vulnérabilités et les packages en fin de vie pendant la compilation sont le genre de fonctionnalité que j'adore parce qu'elles font du meilleur comportement la norme par défaut.

Ce n'est pas tape-à-l'œil, mais c'est le genre d'amélioration qui vieillit vraiment bien.

## C# continue de devenir plus expressif aux bons endroits

Les éléments C# de la Preview 5 sont intéressants, en particulier :

- les hiérarchies de classes fermées
- les déclarations et motifs d'union
- le travail continu d'évolution du unsafe

Je n'adopterais pas aveuglément tout cela en code de production pour l'instant, parce que les fonctionnalités de langage en préversion méritent toujours un cycle de test sobre. Mais la direction est bonne. C# continue d'évoluer vers une modélisation plus riche sans perdre son identité.

## ASP.NET Core et EF Core ont des mises à jour pratiques dignes d'être testées tôt

Deux domaines que je mettrais définitivement à l'épreuve dans un spike :

### Améliorations Blazor

La validation côté client pour Blazor SSR et les améliorations de QuickGrid sans interactivité sont toutes les deux le genre de fonctionnalités de qualité de vie qui peuvent simplifier de vraies applications.

### Valeurs par défaut et avertissements EF Core

EF Core faisant passer la compatibilité SQL Server 2022 en valeur par défaut et ajoutant des avertissements pour les requêtes EF asynchrones exécutées de manière synchrone sont exactement le genre de changements qui peuvent révéler des problèmes cachés dans de vraies bases de code.

Cela signifie que ça vaut la peine de tester plus tôt que plus tard.

## Ma liste courte pour un premier passage

Si j'avais une demi-journée pour explorer la Preview 5, voici ce que je ferais :

1. essayer le modèle de serveur MCP
2. exécuter des builds et inspecter les nouvelles vérifications de vulnérabilité/fin de vie
3. tester toute base de code qui pourrait bénéficier des nouvelles fonctionnalités de modélisation C#
4. valider les scénarios Blazor SSR si vous êtes sur cette pile
5. exécuter des chemins fortement EF Core et surveiller les changements d'avertissement ou les différences SQL

C'est là que je pense que se trouve la valeur précoce.

## Mon avis

.NET 11 Preview 5 ressemble à l'une de ces sorties où la plateforme continue de pousser dans deux directions à la fois :

- des capacités développeur plus ambitieuses
- de meilleures valeurs par défaut pour les équipes orientées production

Cette combinaison est ce que je veux d'un cycle de préversion.

Essayez-le, mais essayez-le avec un but.

Original post: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)
