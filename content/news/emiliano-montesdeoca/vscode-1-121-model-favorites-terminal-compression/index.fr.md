---
title: "VS Code 1.121 : Modèles Favoris, Compression des Sorties Terminal, SSH pour Agent"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 ajoute les modèles favoris, une compression étendue des sorties terminal pour les exécuteurs de tests et les outils de compilation, un minuteur de silence inactif pour les terminaux en arrière-plan et l'authentification SSH interactive par clavier dans l'agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continue les améliorations de qualité de l'agent Copilot de 1.120, avec un accent sur la gestion des modèles et le comportement des terminaux.

## Épingler les Modèles Favoris

Le sélecteur de modèle prend désormais en charge l'épinglage. Si vous utilisez toujours le même modèle ou deux, épinglez-les en haut de la liste. Réduit le défilement quand vous avez accès à de nombreux modèles chez plusieurs fournisseurs.

## Compression Étendue des Sorties Terminal

L'outil terminal de l'agent compressait déjà la sortie pour les commandes courantes. 1.121 étend cela pour couvrir les exécuteurs de tests et les outils de compilation :

- **Exécuteurs de tests :** `pytest`, `jest`, `cargo test`
- **Outils de compilation :** `tsc`, `cargo build`, `make`
- **Linters, Docker, gestionnaires de paquets**

Les longues sorties de compilation et les rapports d'échecs de tests sont compressés en extraits pertinents avant d'être transmis au modèle. Cela maintient l'utilisation du contexte gérable quand l'agent exécute des cycles de compilation ou des suites de tests, qui peuvent produire des milliers de lignes de sortie.

## Minuteur de Silence Inactif pour les Terminaux en Arrière-plan

Un nouveau minuteur de silence inactif pour l'outil `run_in_terminal` : si une commande synchrone ne produit aucune sortie pendant une période configurable, elle est automatiquement promue en exécution en arrière-plan. Cela empêche les commandes longues de bloquer l'agent quand elles traitent silencieusement. Vous obtenez un ID de terminal pour vérifier plus tard.

## Variable d'Environnement VSCODE_AGENT

Quand Copilot Chat exécute des commandes dans le terminal, une variable d'environnement `VSCODE_AGENT` est maintenant définie. Utile si vous avez des scripts ou des outils qui se comportent différemment quand ils sont appelés depuis une session d'agent par rapport à de façon interactive.

## Ajouter au Chat depuis le Navigateur

Un clic droit dans le navigateur intégré affiche maintenant une option "Ajouter au Chat". Sélectionnez du contenu d'une page web et ajoutez-le directement à votre contexte Copilot Chat sans copier-coller.

## Corrigé : Commandes Shell Multi-lignes dans Agent Host

Une correction de bug attendue : les commandes shell multi-lignes dans l'outil terminal de l'Agent Host fonctionnent maintenant correctement. Précédemment, elles pouvaient échouer ou produire un comportement incorrect.

## Authentification SSH Interactive par Clavier

Les connexions SSH de l'Agent Host prennent désormais en charge l'authentification interactive par clavier — la méthode d'authentification de secours utilisée par certains serveurs SSH (y compris certaines configurations d'entreprise plus anciennes). Les agents travaillant sur des hôtes SSH distants sont moins susceptibles de rencontrer des échecs d'authentification.

Post original : [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
