---
title: "Du laptop à la production : déployer des agents IA sur Microsoft Foundry en deux commandes"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI dispose maintenant de commandes 'azd ai agent' qui amènent votre agent IA du développement local à un endpoint Foundry en production en quelques minutes. Voici le workflow complet."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

Vous connaissez ce fossé entre "ça marche sur ma machine" et "c'est déployé et sert du trafic" ? Pour les agents IA, ce fossé a été douloureusement large. Il faut provisionner des ressources, déployer des modèles, configurer l'identité, mettre en place le monitoring — et tout ça avant que quiconque puisse réellement appeler votre agent.

L'Azure Developer CLI vient d'en faire une [affaire de deux commandes](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## Le nouveau workflow `azd ai agent`

Laissez-moi vous montrer ce que ça donne concrètement. Vous avez un projet d'agent IA — disons un agent concierge d'hôtel. Il fonctionne en local. Vous voulez qu'il tourne sur Microsoft Foundry.

```bash
azd ai agent init
azd up
```

C'est tout. Deux commandes. `azd ai agent init` génère l'infrastructure-as-code dans votre repo, et `azd up` provisionne tout sur Azure et publie votre agent. Vous obtenez un lien direct vers votre agent dans le portail Foundry.

## Ce qui se passe sous le capot

La commande `init` génère de vrais templates Bicep inspectables dans votre repo :

- Une **Foundry Resource** (conteneur de niveau supérieur)
- Un **Foundry Project** (où vit votre agent)
- Configuration du **déploiement de modèle** (GPT-4o, etc.)
- **Identité managée** avec les attributions de rôles RBAC appropriées
- `azure.yaml` pour la carte des services
- `agent.yaml` avec les métadonnées de l'agent et les variables d'environnement

Le point clé : tout cela vous appartient. C'est du Bicep versionné dans votre repo. Vous pouvez l'inspecter, le personnaliser et le commiter aux côtés du code de votre agent. Pas de boîtes noires magiques.

## La boucle interne de développement

Ce que j'aime vraiment, c'est l'expérience de développement local. Quand vous itérez sur la logique de l'agent, vous ne voulez pas redéployer à chaque modification d'un prompt :

```bash
azd ai agent run
```

Cela démarre votre agent localement. Combinez-le avec `azd ai agent invoke` pour envoyer des prompts de test, et vous avez une boucle de feedback rapide. Modifier le code, redémarrer, invoquer, répéter.

La commande `invoke` est intelligente pour le routage aussi — quand un agent local tourne, elle le cible automatiquement. Sinon, elle va vers l'endpoint distant.

## Monitoring en temps réel

C'est la fonctionnalité qui m'a convaincu. Une fois votre agent déployé :

```bash
azd ai agent monitor --follow
```

Chaque requête et réponse transitant par votre agent est streamée vers votre terminal en temps réel. Pour déboguer des problèmes en production, c'est inestimable. Plus besoin de fouiller dans les Log Analytics, plus d'attente pour l'agrégation des métriques — vous voyez ce qui se passe maintenant.

## L'ensemble complet des commandes

Voici la référence rapide :

| Commande | Ce qu'elle fait |
|----------|----------------|
| `azd ai agent init` | Scaffold d'un projet agent Foundry avec IaC |
| `azd up` | Provisionne les ressources Azure et déploie l'agent |
| `azd ai agent invoke` | Envoie des prompts à l'agent distant ou local |
| `azd ai agent run` | Exécute l'agent localement pour le développement |
| `azd ai agent monitor` | Streame les logs en temps réel de l'agent publié |
| `azd ai agent show` | Vérifie la santé et le statut de l'agent |
| `azd down` | Nettoie toutes les ressources Azure |

## Pourquoi c'est important pour les développeurs .NET

Même si l'exemple de l'annonce est basé sur Python, l'histoire de l'infrastructure est agnostique au langage. Votre agent .NET bénéficie du même scaffolding Bicep, de la même configuration d'identité managée, du même pipeline de monitoring. Et si vous utilisez déjà `azd` pour vos apps .NET Aspire ou vos déploiements Azure, ça s'intègre directement dans votre workflow existant.

Le fossé de déploiement pour les agents IA a été l'un des plus grands points de friction dans l'écosystème. Passer d'un prototype fonctionnel à un endpoint de production avec identité, réseau et monitoring appropriés ne devrait pas nécessiter une semaine de travail DevOps. Maintenant il faut deux commandes et quelques minutes.

## Pour conclure

`azd ai agent` est disponible maintenant. Si vous avez repoussé le déploiement de vos agents IA parce que la mise en place de l'infrastructure semblait trop de travail, essayez. Consultez le [walkthrough complet](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) pour le guide étape par étape incluant l'intégration d'une app de chat frontend.
