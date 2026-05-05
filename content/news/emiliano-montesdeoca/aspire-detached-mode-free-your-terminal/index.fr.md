---
title: "Arrêtez de surveiller votre terminal : le mode détaché d'Aspire change la donne"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 vous permet d'exécuter votre AppHost en arrière-plan et de récupérer votre terminal. Combiné aux nouvelles commandes CLI et au support des agents, c'est plus important qu'il n'y paraît."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

À chaque fois que vous lancez un AppHost Aspire, votre terminal disparaît. Verrouillé. Occupé jusqu'à ce que vous fassiez Ctrl+C. Besoin d'exécuter une commande rapide ? Ouvrez un autre onglet. Envie de vérifier les logs ? Encore un onglet. C'est une petite friction qui s'accumule vite.

Aspire 13.2 corrige ça. James Newton-King [a détaillé tout ça](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), et honnêtement, c'est une de ces fonctionnalités qui change immédiatement votre façon de travailler.

## Mode détaché : une commande, terminal récupéré

```bash
aspire start
```

C'est le raccourci pour `aspire run --detach`. Votre AppHost démarre en arrière-plan et vous récupérez votre terminal immédiatement. Pas d'onglets supplémentaires. Pas de multiplexeur de terminal. Juste votre prompt, prêt à l'emploi.

## Gérer ce qui tourne

Le truc, c'est que tourner en arrière-plan n'est utile que si on peut gérer ce qui s'y passe. Aspire 13.2 fournit un ensemble complet de commandes CLI pour exactement ça :

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Ça transforme le CLI d'Aspire en un véritable gestionnaire de processus. Vous pouvez démarrer plusieurs AppHosts, vérifier leur statut, suivre leurs logs et les arrêter — le tout depuis une seule session de terminal.

## Combinez-le avec le mode isolé

Le mode détaché se marie naturellement avec le mode isolé. Vous voulez lancer deux instances du même projet en arrière-plan sans conflits de ports ?

```bash
aspire start --isolated
aspire start --isolated
```

Chacune obtient des ports aléatoires, des secrets séparés et son propre cycle de vie. Utilisez `aspire ps` pour voir les deux, `aspire stop` pour arrêter celle dont vous n'avez plus besoin.

## Pourquoi c'est énorme pour les agents de code

C'est là que ça devient vraiment intéressant. Un agent de code travaillant dans votre terminal peut maintenant :

1. Démarrer l'app avec `aspire start`
2. Interroger son état avec `aspire describe`
3. Vérifier les logs avec `aspire logs` pour diagnostiquer les problèmes
4. L'arrêter avec `aspire stop` quand il a terminé

Tout ça sans perdre la session de terminal. Avant le mode détaché, un agent qui lançait votre AppHost se retrouvait bloqué dans son propre terminal. Maintenant il peut démarrer, observer, itérer et nettoyer — exactement comme on voudrait qu'un agent autonome fonctionne.

L'équipe Aspire a misé là-dessus. Lancer `aspire agent init` met en place un fichier de compétences Aspire qui enseigne ces commandes aux agents. Ainsi, des outils comme l'agent de code de Copilot peuvent gérer vos workloads Aspire directement.

## Pour conclure

Le mode détaché est une amélioration du workflow déguisée en simple flag. Vous arrêtez de jongler entre les terminaux, les agents ne se bloquent plus eux-mêmes, et les nouvelles commandes CLI vous donnent une vraie visibilité sur ce qui tourne. C'est pratique, c'est propre, et ça rend le cycle de développement quotidien nettement plus fluide.

Lisez le [post complet](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) pour tous les détails et récupérez Aspire 13.2 avec `aspire update --self`.
