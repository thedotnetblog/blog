---
title: "Le serveur MCP Azure DevOps débarque dans Microsoft Foundry : ce que ça signifie pour vos agents IA"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Le serveur MCP Azure DevOps est maintenant disponible dans Microsoft Foundry. Connectez vos agents IA directement aux workflows DevOps — work items, repos, pipelines — en quelques clics."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) a le vent en poupe. Si vous suivez l'écosystème des agents IA, vous avez probablement remarqué que les serveurs MCP apparaissent partout — donnant aux agents la capacité d'interagir avec des outils et services externes via un protocole standardisé.

Maintenant le [serveur MCP Azure DevOps est disponible dans Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), et c'est une de ces intégrations qui fait réfléchir aux possibilités pratiques.

## Ce qui se passe réellement ici

Microsoft a déjà publié le serveur MCP Azure DevOps en [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — c'est le serveur MCP lui-même. La nouveauté, c'est l'intégration Foundry. Vous pouvez maintenant ajouter le serveur MCP Azure DevOps à vos agents Foundry directement depuis le catalogue d'outils.

Pour ceux qui ne connaissent pas encore Foundry : c'est la plateforme unifiée de Microsoft pour construire et gérer des applications et agents alimentés par l'IA à grande échelle. Accès aux modèles, orchestration, évaluation, déploiement — tout au même endroit.

## La mise en place

La configuration est étonnamment simple :

1. Dans votre agent Foundry, allez dans **Add Tools** > **Catalog**
2. Cherchez "Azure DevOps"
3. Sélectionnez le Azure DevOps MCP Server (preview) et cliquez sur **Create**
4. Entrez le nom de votre organisation et connectez

C'est tout. Votre agent a maintenant accès aux outils Azure DevOps.

## Contrôler ce à quoi votre agent peut accéder

C'est la partie que j'apprécie : vous n'êtes pas coincé avec une approche tout-ou-rien. Vous pouvez spécifier quels outils sont disponibles pour votre agent. Si vous voulez qu'il ne lise que les work items sans toucher aux pipelines, vous pouvez configurer ça. Principe du moindre privilège, appliqué à vos agents IA.

C'est important pour les scénarios enterprise où vous ne voulez pas qu'un agent déclenche accidentellement un pipeline de déploiement parce que quelqu'un lui a demandé d'"aider avec la release."

## Pourquoi c'est intéressant pour les équipes .NET

Pensez à ce que ça permet en pratique :

- **Assistants de planification de sprint** — des agents qui peuvent récupérer les work items, analyser les données de vélocité et suggérer la capacité du sprint
- **Bots de code review** — des agents qui comprennent le contexte de votre PR parce qu'ils peuvent réellement lire vos repos et work items liés
- **Réponse aux incidents** — des agents qui peuvent créer des work items, interroger les déploiements récents et corréler les bugs avec les changements récents
- **Onboarding des développeurs** — "Sur quoi devrais-je travailler ?" obtient une vraie réponse basée sur les données réelles du projet

Pour les équipes .NET qui utilisent déjà Azure DevOps pour leurs pipelines CI/CD et la gestion de projet, avoir un agent IA qui peut interagir directement avec ces systèmes est un pas significatif vers une automatisation utile.

## La vision plus large de MCP

Cela fait partie d'une tendance plus large : les serveurs MCP deviennent le moyen standard par lequel les agents IA interagissent avec le monde extérieur. On les voit pour GitHub, Azure DevOps, les bases de données, les APIs SaaS — et Foundry devient le hub où toutes ces connexions convergent.

Si vous construisez des agents dans l'écosystème .NET, MCP mérite votre attention. Le protocole est standardisé, l'outillage mûrit, et l'intégration Foundry le rend accessible sans avoir à câbler manuellement les connexions serveur.

## Pour conclure

Le serveur MCP Azure DevOps dans Foundry est en preview, alors attendez-vous à ce qu'il évolue. Mais le workflow de base est solide : connecter, configurer l'accès aux outils, et laisser vos agents travailler avec vos données DevOps. Si vous êtes déjà dans l'écosystème Foundry, c'est à quelques clics. Essayez et voyez quels workflows vous pouvez construire.

Consultez l'[annonce complète](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) pour la configuration étape par étape et plus de détails.
