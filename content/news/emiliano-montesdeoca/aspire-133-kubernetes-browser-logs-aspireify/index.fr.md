---
title: "Aspire 13.3 : Support Kubernetes, Journaux du Navigateur et la Compétence Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Cinq semaines après 13.2, Aspire 13.3 arrive avec 45 nouvelles fonctionnalités, notamment le déploiement AKS de première classe, une compétence d'intégration assistée par IA, la capture des journaux du navigateur et des résultats de commandes structurés."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Cinq semaines, ce n'est pas beaucoup pour une version, mais Aspire 13.3 ne le semble pas. Les éléments principaux sont significatifs : déploiement Kubernetes et AKS de première classe avec Helm, une compétence d'intégration assistée par agent appelée Aspireify, la capture des journaux du navigateur directement dans le dashboard et des résultats de commandes structurés. En plus, 45 nouvelles fonctionnalités, 134 améliorations et 93 corrections de bugs.

Passons aux points saillants.

## Aspireify : Intégration Assistée par Agent

Ajouter Aspire à un projet existant semble simple — ajoutez un AppHost, c'est fait. En pratique, cela implique beaucoup d'archéologie : quels ports comptent, quelles variables d'environnement sont de vraies dépendances, quels services Docker Compose doivent correspondre aux intégrations Aspire.

La nouvelle **compétence Aspireify** donne à votre agent de code un flux de travail guidé précisément pour cela. Quand `aspire init` crée un AppHost squelette, la compétence Aspireify aide l'agent à inspecter le dépôt, à comprendre comment il fonctionne déjà et à câbler l'AppHost pour s'adapter à l'application — pas l'inverse.

La posture par défaut est "minimiser les modifications de votre code." Si votre application lit déjà `DATABASE_URL`, l'agent le mappe avec `WithEnvironment()` au lieu de vous demander de réécrire votre configuration. Si un port est codé en dur, la compétence indique à l'agent quand le préserver.

C'est le type d'outillage IA qui fait réellement gagner du temps plutôt que de générer plus de travail à revoir.

## Déploiement Kubernetes et AKS de Première Classe

Celui-là était sur la liste de souhaits depuis un moment. Aspire 13.3 inclut le **support de déploiement Kubernetes et AKS de première classe avec Helm**. Vous pouvez maintenant cibler AKS comme destination de déploiement directement depuis les outils Aspire.

Pour les équipes qui exécutent déjà des charges de travail de production sur AKS, cela comble un écart significatif. Votre modèle d'application Aspire a maintenant un chemin propre du développement local vers Kubernetes sans rédaction manuelle de charts Helm.

## Journaux du Navigateur dans le Dashboard

C'est une de ces fonctionnalités qui semblent mineures jusqu'à ce que vous déboguiez un problème frontend.

La nouvelle API `WithBrowserLogs()` attache une ressource de navigateur suivie à toute ressource capable d'endpoints. Aspire lance Chromium en utilisant un pipe CDP privé et diffuse les journaux de console, les requêtes réseau et les erreurs directement dans le flux de journaux de la ressource :

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

L'AppHost TypeScript prend en charge la même chose :

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Erreurs de console, requêtes réseau échouées, exceptions côté client — tout visible dans le même dashboard où vous regardez déjà les traces et métriques. Plus besoin de changer d'onglet vers les DevTools du navigateur pour les bases.

## Résultats de Commandes Structurés

Les commandes de ressources ont reçu une mise à niveau significative. Jusqu'à présent, les commandes renvoyaient succès/échec. Maintenant elles retournent des résultats structurés : texte, JSON ou markdown qui circule à travers le modèle, l'interface du dashboard, la CLI et les outils MCP.

Le dashboard relie tout cela avec un nouveau centre de notifications dans l'en-tête. Les résultats des commandes apparaissent sous forme de notifications horodatées avec rendu markdown et une action "Voir la réponse".

Cela rend les commandes de ressources véritablement composables. Une intégration peut maintenant exposer une commande qui renvoie une sortie significative — comme une URL de tunnel — plutôt que de simplement changer d'état quelque part.

## En Résumé

Aspire 13.3 vaut la mise à jour ne serait-ce que pour le support Kubernetes. Les journaux du navigateur et les résultats de commandes structurés ressemblent au type d'améliorations de qualité de vie qui s'accumulent rapidement dans un flux de travail de développement quotidien.

Notes de version complètes : [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
