---
title: "VS Code 1.120 : Invites de Mot de Passe, Sélecteur de Taille de Contexte, Métadonnées GitHub dans Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 est une version axée sur les utilisateurs de Copilot : gestion sécurisée des invites de mot de passe, sélecteur de taille de contexte du modèle, métadonnées de PR GitHub dans les sessions d'agent et gestion des archives de sessions."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 a été livré avec un ensemble d'améliorations de l'agent Copilot qui sont petites individuellement mais nettement meilleures au quotidien.

## Détection Sécurisée des Invites de Mot de Passe dans les Terminaux de l'Agent

Lorsqu'un agent Copilot exécute une commande de terminal qui déclenche une invite de mot de passe ou de phrase secrète, VS Code le détecte maintenant et affiche un dialogue de confirmation. Le dialogue met le focus sur le terminal pour que vous puissiez taper le secret directement — et de manière cruciale, les secrets ne sont jamais acheminés via le modèle.

C'est une amélioration de sécurité significative. Auparavant, les agents exécutant des commandes qui déclenchaient des invites d'authentification pouvaient créer des situations où les utilisateurs pourraient exposer involontairement des identifiants. L'annonce du lecteur d'écran signifie que les utilisateurs de l'accessibilité reçoivent également la notification.

## Sélecteur de Taille de Contexte dans le Sélecteur de Modèle

Un nouveau sélecteur de taille de contexte vous permet de choisir combien de contexte le modèle utilise pour une session. Différents modèles ont différentes tailles de fenêtre de contexte, et certains workflows bénéficient de la contraindre (latence plus faible, coût plus faible) ou de la maximiser (bases de code complexes, sessions de longue durée).

## Métadonnées de PR GitHub dans les Sessions Agent Host

Pour les sessions adossées à un dépôt GitHub, VS Code affiche maintenant les métadonnées GitHub — y compris un bouton de pull request — dans l'interface utilisateur de l'agent host. Moins de changements de contexte vers le navigateur ou l'extension GitHub quand vous travaillez sur une PR.

## Gestion des Archives de Sessions de Chat

Deux améliorations pour le Quick Pick des sessions :
- Les sessions archivées sont masquées par défaut (moins d'encombrement visuel)
- La recherche correspond toujours aux sessions archivées, pour que vous puissiez en retrouver une par titre

Les sessions sont également regroupées par récence par défaut, facilitant la recherche du travail récent.

## Découverte de Plugins CLI Copilot

VS Code découvre maintenant automatiquement les plugins Copilot CLI installés par l'utilisateur depuis `~/.copilot/installed-plugins/`. Si vous avez configuré WinUI ou d'autres compétences d'agent spécifiques au domaine, elles sont récupérées sans configuration manuelle.

## API de l'Éditeur de Diff Personnalisé (Préversion)

Pour les auteurs d'extensions : une nouvelle API proposée `customDiffEditorProvider` permet aux extensions de rendre un diff unifié dans une seule webview avec accès aux documents originaux et modifiés, au lieu de deux vues d'éditeur personnalisées côte à côte.

Post original : [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
