---
title: "Mise à jour de juin de Visual Studio : la visibilité d'utilisation et la confiance MCP sont les fonctionnalités les plus importantes"
date: 2026-07-24
author: 'Emiliano Montesdeoca'
description: 'Les éléments les plus importants de cette version ne sont pas cosmétiques ; ils améliorent la gouvernance et la confiance dans les workflows assistés par IA.'
tags:
  - visual-studio
  - github-copilot
  - mcp
  - cplusplus
  - developer-experience
---

Source originale : [Visual Studio June Update – Track Your Usage, Trust Your Tools](https://devblogs.microsoft.com/visualstudio/visual-studio-june-update-track-your-usage-trust-your-tools/)

Cette version de Visual Studio comporte de nombreuses améliorations agréables de la qualité de vie, mais deux mises à jour se démarquent pour les équipes sérieuses : la transparence d'utilisation de Copilot et la validation de confiance MCP.

Alors que le développement assisté par IA évolue vers une facturation à l'utilisation, la visibilité n'est plus une simple métrique de commodité. C'est une exigence de planification. Les fenêtres d'utilisation en temps réel et les alertes de seuil aident les équipes à éviter les pics de coûts surprise et à instaurer des normes d'utilisation plus saines. Sans cette visibilité, les discussions sur les gains de productivité deviennent rapidement des conjectures.

Le flux de validation de confiance MCP est encore plus crucial sur le plan stratégique. Les écosystèmes d'outillage deviennent dynamiques, et les systèmes dynamiques nécessitent des frontières de confiance explicites. Comparer la configuration de démarrage et les empreintes de capacité aux références de confiance est exactement la posture par défaut appropriée.

Mon opinion est ferme : chaque IDE intégré à l'IA devrait le faire par défaut. La dérive silencieuse des capacités dans les serveurs d'outils est un risque inacceptable pour les environnements d'entreprise.

L'agent de modernisation C++ GA pour les mises à niveau MSVC est un autre gain pratique. Le travail de mise à niveau est généralement différé parce qu'il est fastidieux et risqué. Disposer de parcours guidés et automatisés au sein de l'IDE abaisse la barrière pour rester à jour, en particulier pour les bases de code legacy de grande taille.

Les suggestions d'édition à longue distance sont une bonne amélioration de productivité, mais elles sont mieux traitées comme une accélération optionnelle. Les fonctionnalités de confiance et de gouvernance doivent être activées et comprises en premier ; les fonctionnalités de confort peuvent suivre.

Recommandations pratiques pour les équipes déployant cette version :

Activez les alertes d'utilisation Copilot avec des seuils alignés sur la gestion budgétaire interne.

Formez les développeurs aux invites de confiance MCP afin que les approbations soient intentionnelles, et non des clics habituels.

Testez les workflows de l'agent de modernisation sur une solution C++ représentative avant un déploiement généralisé.

Recueillez des retours sur les suggestions étendues, mais conditionnez l'activation par défaut à un taux d'acceptation mesurable.

Le support des emoji couleur est mineur sur le papier, mais il améliore la lisibilité dans les contextes de texte mixte comme le chat, le markdown et les volets de sortie. Les petites améliorations UX finissent par compter lorsqu'elles sont utilisées quotidiennement.

Dans l'ensemble, cette version reflète une philosophie d'outillage qui mûrit : l'assistance IA ne concerne plus seulement la vitesse de génération. Elle concerne le contrôle, la responsabilité et la confiance dans ce qui s'exécute dans votre environnement de développement.

Si votre organisation standardise les workflows Visual Studio améliorés par l'IA, priorisez d'abord les fonctionnalités de confiance opérationnelle. Elles constituent le fondement qui permet au reste de la pile de productivité de passer à l'échelle en toute sécurité.