---
title: "L'évaluation de modernisation de GitHub Copilot est le meilleur outil de migration que vous n'utilisez pas encore"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "L'extension de modernisation de GitHub Copilot ne se contente pas de suggérer des modifications de code — elle produit une évaluation complète de migration avec des issues actionnables, des comparaisons de cibles Azure et un workflow collaboratif. Voici pourquoi le document d'évaluation est la clé de tout."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}}).*

Migrer une application legacy .NET Framework vers .NET moderne est l'une de ces tâches que tout le monde sait devoir faire mais que personne ne veut commencer. Ce n'est jamais juste « changer le framework cible ». Ce sont des API qui ont disparu, des packages qui n'existent plus, des modèles d'hébergement qui fonctionnent totalement différemment, et un million de petites décisions sur ce qu'il faut containeriser, réécrire ou laisser tel quel.

Jeffrey Fritz vient de publier une [plongée approfondie dans l'évaluation de modernisation de GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), et honnêtement ? C'est le meilleur outillage de migration que j'ai vu pour .NET. Pas à cause de la génération de code — c'est devenu standard maintenant. À cause du document d'évaluation qu'il produit.

## Ce n'est pas qu'un moteur de suggestions de code

L'extension VS Code suit un modèle **Évaluer → Planifier → Exécuter**. La phase d'évaluation analyse l'intégralité de votre codebase et produit un document structuré qui capture tout : ce qui doit changer, quelles ressources Azure provisionner, quel modèle de déploiement utiliser. Tout en aval — infrastructure as code, containerisation, manifestes de déploiement — découle de ce que l'évaluation trouve.

L'évaluation est stockée sous `.github/modernize/assessment/` dans votre projet. Chaque exécution produit un rapport indépendant, vous construisez ainsi un historique et pouvez suivre l'évolution de votre posture de migration au fur et à mesure que vous corrigez les issues.

## Deux façons de commencer

**Évaluation Recommandée** — la voie rapide. Choisissez parmi des domaines curatés (Mise à jour Java/.NET, Cloud Readiness, Sécurité) et obtenez des résultats significatifs sans toucher à la configuration. Idéal pour un premier regard sur l'état de votre application.

**Évaluation Personnalisée** — la voie ciblée. Configurez exactement ce qu'il faut analyser : compute cible (App Service, AKS, Container Apps), OS cible, analyse de containerisation. Choisissez plusieurs cibles Azure pour comparer les approches de migration côte à côte.

Cette vue de comparaison est véritablement utile. Une app avec 3 issues obligatoires pour App Service pourrait en avoir 7 pour AKS. Voir les deux aide à prendre la décision d'hébergement avant de s'engager sur un chemin de migration.

## Le détail des issues est actionnable

Chaque issue est accompagné d'un niveau de criticité :

- **Obligatoire** — doit être corrigé sinon la migration échoue
- **Potentiel** — pourrait impacter la migration, nécessite un jugement humain
- **Optionnel** — améliorations recommandées, ne bloque pas la migration

Et chaque issue renvoie aux fichiers affectés et numéros de lignes, fournit une description détaillée de ce qui ne va pas et pourquoi c'est important pour votre plateforme cible, donne des étapes concrètes de remédiation (pas juste « corrigez ceci ») et inclut des liens vers la documentation officielle.

Vous pouvez confier des issues individuelles à des développeurs et ils ont tout ce dont ils ont besoin pour agir. C'est la différence entre un outil qui vous dit « il y a un problème » et un qui vous dit comment le résoudre.

## Les chemins de mise à jour couverts

Pour .NET spécifiquement :
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Chaque chemin de mise à jour a des règles de détection qui savent quelles API ont été supprimées, quels patterns n'ont pas d'équivalent direct et quels problèmes de sécurité nécessitent une attention particulière.

Pour les équipes gérant plusieurs applications, il y a aussi un CLI qui supporte les évaluations batch multi-repo — clonez tous les repos, évaluez-les tous, obtenez des rapports par application plus une vue agrégée du portfolio.

## Mon avis

Si vous êtes assis sur des applications legacy .NET Framework (et soyons honnêtes, la plupart des équipes enterprise le sont), c'est *l'outil* par lequel commencer. Le document d'évaluation seul vaut le temps — il transforme un vague « on devrait moderniser » en une liste concrète et priorisée d'éléments de travail avec des chemins clairs vers l'avant.

Le workflow collaboratif est malin aussi : exportez les évaluations, partagez-les avec votre équipe, importez-les sans relancer. Revues d'architecture où les décideurs ne sont pas ceux qui exécutent les outils ? Couvert.

## Pour conclure

L'évaluation de modernisation de GitHub Copilot transforme la migration .NET d'un projet effrayant et indéfini en un processus structuré et traçable. Commencez avec une évaluation recommandée pour voir où vous en êtes, puis utilisez des évaluations personnalisées pour comparer les cibles Azure et construire votre plan de migration.

Lisez le [walkthrough complet](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) et récupérez l'[extension VS Code](https://aka.ms/ghcp-appmod/vscode-ext) pour l'essayer sur votre propre codebase.
