---
title: "Un Plugin d'Agent WinUI pour GitHub Copilot et Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft a publié des compétences d'agent pour le développement WinUI : générer un scaffold, compiler, exécuter, tester, itérer, le tout avec GitHub Copilot CLI ou Claude Code. L'innovation clé : des outils dédiés qui ancrent l'agent dans des faits spécifiques à WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft a publié un ensemble de compétences d'agent open source pour le développement d'applications WinUI, disponibles sur [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Installation et Configuration

Installez le plugin avec `/plugin install winui@awesome-copilot`, puis exécutez la configuration initiale avec `/winui:winui-setup`. Le processus de configuration vérifie les prérequis, installe les dépendances nécessaires et configure l'environnement pour le développement d'applications WinUI.

## La Boucle de Développement de Bout en Bout

Les compétences couvrent le cycle de développement complet :

- **Scaffold :** Génère le bon modèle de projet en utilisant `dotnet new WinUI` avec les paramètres appropriés — l'agent connaît les bons modèles et les valeurs de configuration par défaut.
- **Compilation :** Gère le modèle d'exécution packagé que requièrent les applications WinUI, y compris la signature de paquet et les configurations de manifeste.
- **Interaction et validation :** Lance l'application, interagit avec elle et valide le comportement.
- **Correction des erreurs de compilation :** L'agent comprend les messages d'erreur spécifiques à WinUI et sait comment les résoudre.

## Efficacité des Tokens via des Outils Dédiés

L'innovation clé est que les compétences incluent des outils dédiés qui récupèrent des données de référence concrètes à la demande :

- Détails de l'API WinUI et Fluent Design
- Patterns MVVM et meilleures pratiques
- Packaging MSIX, signature de code et soumission au Store
- Accessibilité, thèmes et automatisation de l'UI

Plutôt que d'injecter toute la documentation WinUI dans le contexte, les outils récupèrent exactement ce dont l'agent a besoin au moment où il en a besoin. Cela maintient l'utilisation du contexte efficace et améliore la précision dans les domaines spécialisés.

## Pourquoi les Compétences Dédiées Comptent

Les modèles de langage à usage général ont une connaissance limitée des subtilités spécifiques à WinUI : le modèle d'exécution packagé, les API Fluent Design, l'intégration MSIX ou la façon dont Windows App SDK enveloppe les fonctionnalités Win32. Les outils dédiés résolvent cela en ancrant l'agent dans des faits WinUI vérifiés plutôt que dans des connaissances du modèle potentiellement obsolètes ou incorrectes.

Le même pattern s'applique à tout framework ou SDK spécialisé avec ses propres conventions et exigences qui diffèrent des patterns de développement généraux.

Post original : [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
