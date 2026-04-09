---
title: "Le Mode Isolé d'Aspire Résout le Cauchemar des Conflits de Ports pour le Développement Parallèle"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduit le mode --isolated : ports aléatoires, secrets séparés et zéro collision lors de l'exécution de plusieurs instances du même AppHost. Parfait pour les agents IA, les worktrees et les workflows parallèles."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Si tu as déjà essayé d'exécuter deux instances du même projet en même temps, tu connais la douleur. Le port 8080 est déjà utilisé. Le port 17370 est pris. Tuer quelque chose, redémarrer, jongler avec les variables d'environnement — c'est un tueur de productivité.

Ce problème empire, il ne s'améliore pas. Les agents IA créent des git worktrees pour travailler indépendamment. Les agents en arrière-plan démarrent des environnements séparés. Les développeurs font des checkout du même repo deux fois pour des branches de fonctionnalités. Chacun de ces scénarios frappe le même mur : deux instances de la même app qui se battent pour les mêmes ports.

Aspire 13.2 résout ça avec un seul flag. James Newton-King de l'équipe Aspire a [écrit tous les détails](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), et c'est une de ces fonctionnalités « pourquoi on n'avait pas ça avant ? ».

## La solution : `--isolated`

```bash
aspire run --isolated
```

C'est tout. Chaque exécution obtient :

- **Des ports aléatoires** — plus de collisions entre instances
- **Des secrets utilisateur isolés** — les chaînes de connexion et clés API restent séparées par instance

Pas de réattribution manuelle de ports. Pas de jonglage avec les variables d'environnement. Chaque exécution obtient un environnement propre et sans collision automatiquement.

## Scénarios réels où ça brille

**Checkouts multiples.** Tu as une branche de fonctionnalité dans un répertoire et un bugfix dans un autre :

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Les deux tournent sans conflit. Le dashboard montre ce qui tourne et où.

**Agents en arrière-plan dans VS Code.** Quand l'agent en arrière-plan de Copilot Chat crée un git worktree pour travailler sur ton code indépendamment, il peut avoir besoin d'exécuter ton AppHost Aspire. Sans `--isolated`, c'est un conflit de ports avec ton worktree principal. Avec, les deux instances fonctionnent tout simplement.

Le skill Aspire livré avec `aspire agent init` instruit automatiquement les agents d'utiliser `--isolated` quand ils travaillent dans des worktrees. Donc l'agent en arrière-plan de Copilot devrait gérer ça nativement.

**Tests d'intégration en parallèle du développement.** Besoin d'exécuter des tests contre un AppHost live tout en continuant à développer des fonctionnalités ? Le mode isolé donne à chaque contexte ses propres ports et sa propre config.

## Comment ça fonctionne sous le capot

Quand tu passes `--isolated`, la CLI génère un ID d'instance unique pour l'exécution. Cela pilote deux comportements :

1. **Randomisation des ports** — au lieu de se lier à des ports prévisibles définis dans la config de ton AppHost, le mode isolé choisit des ports aléatoires disponibles pour tout — le dashboard, les endpoints de services, tout. Le service discovery s'ajuste automatiquement, pour que les services se trouvent mutuellement quel que soit le port attribué.

2. **Isolation des secrets** — chaque exécution isolée obtient son propre store de secrets utilisateur, indexé par l'ID d'instance. Les chaînes de connexion et clés API d'une exécution ne fuient pas dans une autre.

Ton code n'a besoin d'aucun changement. Le service discovery d'Aspire résout les endpoints au runtime, donc tout se connecte correctement quelle que soit l'attribution des ports.

## Quand l'utiliser

Utilise `--isolated` quand tu exécutes plusieurs instances du même AppHost simultanément — que ce soit pour du développement parallèle, des tests automatisés, des agents IA ou des git worktrees. Pour du développement mono-instance où tu préfères des ports prévisibles, le `aspire run` classique fonctionne toujours très bien.

## Pour conclure

Le mode isolé est une petite fonctionnalité qui résout un problème réel et de plus en plus courant. Alors que le développement assisté par IA nous pousse vers plus de workflows parallèles — agents multiples, worktrees multiples, contextes multiples — la capacité de simplement lancer une autre instance sans se battre pour les ports est essentielle.

Lis le [post complet](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) pour tous les détails techniques et essaie-le avec `aspire update --self` pour obtenir la 13.2.
