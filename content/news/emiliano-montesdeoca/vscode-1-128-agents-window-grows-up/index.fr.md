---
title: "VS Code 1.128 fait un pari clair : la fenêtre des agents devient la nouvelle surface de travail"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 transforme les workflows d'agents, passant de la nouveauté à l'ergonomie quotidienne avec des sessions multi-chat, le support vision en disponibilité générale et des contrôles hôte/session plus poussés."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 est une version significative, non pas en raison d'une fonctionnalité killer, mais parce que plusieurs changements s'alignent autour d'une direction unique : le développement orienté agent au sein de l'éditeur devient structuré, parallèle et gérable sur le plan opérationnel.

Source originale : https://code.visualstudio.com/updates/v1_128

Le point fort est le comportement multi-chat enrichi dans les sessions hôtes d'agents, incluant les conversations en pair, les forks et les tours concurrents sous une même session parente. C'est exactement ce dont les développeurs expérimentés ont besoin lorsqu'ils explorent des implémentations alternatives ou répartissent des tâches entre plusieurs chemins de vérification. Cela reflète le travail d'ingénierie réel, qui est rarement linéaire.

Mon avis : c'est la première version de VS Code où la fenêtre des agents ressemble moins à un panneau de chat et plus à une surface d'orchestration de l'espace de travail.

Les chats rapides sans espace de travail sélectionné comptent également plus qu'il n'y paraît. Ils réduisent les frictions pour les questions conceptuelles ou architecturales tout en maintenant les sessions liées à un projet distinctes. Cette séparation peut réduire l'encombrement et préserver l'intégrité du contexte pour les workflows de modification de code.

L'arrivée de Copilot Vision en disponibilité générale est un autre point d'inflexion. Une fois que les images et les PDF deviennent des entrées normales dans le chat, les tâches à forte composante documentaire et d'interface utilisateur deviennent considérablement plus fluides. Les équipes doivent désormais considérer le contexte multimodal comme une capacité par défaut, et non comme un module complémentaire avancé.

Il y a aussi des implications de plateforme pratiques. Le support BYOK dans les scénarios hôtes d'agents, les paramètres d'échantillonnage de modèle configurables et les valeurs par défaut des modèles utilitaires indiquent une maturité croissante pour la gouvernance des modèles en entreprise. Les organisations ayant des exigences strictes en matière de fournisseurs peuvent désormais façonner le comportement avec un contrôle plus fin plutôt qu'avec des valeurs par défaut uniformes.

Recommandations pour les équipes adoptant la version 1.128 :

Définissez des conventions pour le branchement et le nommage des chats dans les sessions multi-chat afin que l'exploration parallèle ne devienne pas du bruit conversationnel. Encouragez les développeurs à conserver un chat pour l'implémentation et un pour les tests ou l'analyse des échecs. Utilisez les chats rapides intentionnellement pour les questions non liées au dépôt.

Si vous utilisez des endpoints BYOK, établissez des profils de température/top_p de base par classe de charge de travail et documentez les exceptions. Décidez également si les flux utilitaires doivent s'exécuter sur des modèles fournis par Copilot ou BYOK pour éviter des écarts de comportement silencieux accidentels.

Enfin, considérez les raccourcis au niveau du système d'exploitation de manière stratégique. Pouvoir déclencher des commandes VS Code à l'échelle du système peut améliorer le flux de travail pour les utilisateurs expérimentés, mais une prolifération non gérée de raccourcis peut nuire à la cohérence au sein des équipes.

VS Code 1.128 ne se contente pas d'ajouter des fonctionnalités. Il resserre les mécanismes de collaboration entre agents dans les boucles de développement réelles. Les éditeurs qui gagneront dans le prochain cycle seront ceux qui traiteront les interactions avec les agents comme des primitives de workflow de première classe, et non comme des expériences latérales. Cette version montre que VS Code a compris cette course.