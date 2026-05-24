---
title: "La réduction des paquets NuGet dans .NET 10 est le genre d'amélioration que l'on ressent partout"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "La nouvelle réduction des paquets NuGet dans .NET 10 diminue les faux positifs dans les rapports de vulnérabilités, simplifie le graphe de restore et améliore les performances de restore. C'est l'un de ces changements de plateforme qui améliorent discrètement le travail quotidien."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Certaines améliorations de plateforme sont enthousiasmantes parce qu'elles ouvrent de nouveaux scénarios.

D'autres le sont parce qu'elles rendent les workflows existants moins bruyants, moins fragiles et moins agaçants.

**La réduction des paquets NuGet dans .NET 10** appartient clairement à la deuxième catégorie, et je le dis comme un compliment.

## Pourquoi c'est important

Si vous avez déjà dû gérer du bruit de vulnérabilités transitives, des graphes de restore inutilement volumineux ou des paquets qui sont techniquement présents mais qui ne sont pas réellement pertinents pour le runtime utilisé par votre application, ce changement répond à un vrai point de douleur.

La réduction aide en retirant du graphe effectif des dépendances les paquets fournis par la plateforme lorsque le runtime les fournit déjà.

Cela signifie :

- moins de faux positifs dans les rapports de vulnérabilités
- des graphes de dépendances transitives plus propres
- moins de surcharge de restore
- des résultats d'audit plus exploitables

## Mon avis

C'est exactement le genre d'amélioration .NET que j'aime.

Elle améliore les valeurs par défaut, réduit la charge mentale et améliore à la fois la qualité du signal de sécurité et le comportement quotidien des outils.

C'est une victoire, même si cela n'atteint jamais une slide de keynote.

Article original : [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
