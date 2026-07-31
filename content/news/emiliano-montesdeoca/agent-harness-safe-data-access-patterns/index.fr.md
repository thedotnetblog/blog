---
title: "La vraie victoire UX pour les agents, c'est l'autonomie sûre, pas l'autonomie maximale"
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: "L'accès aux fichiers, les approbations et la conception de la mémoire forment le trio pratique pour un comportement d'agent digne de confiance en production."
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Original source: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

C'est l'un des billets d'ingénierie d'agents les plus utiles de l'année parce qu'il refuse le piège habituel de l'autonomie orientée démo. Il se concentre plutôt sur la manière dont les agents devraient opérer autour de vraies données utilisateur et de vraies conséquences.

Les trois blocs de construction mis en avant ici sont exactement les bons.

L'accès aux fichiers donne aux agents un ancrage utile dans les données appartenant à l'utilisateur.

Le verrouillage par approbation empêche l'exécution silencieuse d'actions à conséquences.

La mémoire durable évite les interactions répétitives sans sacrifier le contrôle.

La plupart des équipes surinvestissent dans l'étendue des outils et sous-investissent dans la sémantique des permissions. C'est à l'envers. Un agent avec dix outils et des limites d'approbation faibles vaut moins qu'un agent avec trois outils et des points de contrôle prévisibles.

Le meilleur modèle pratique de cet article est la stratégie d'approbation par couches :

Exigez toujours une approbation pour les outils à fort impact comme le trading ou les opérations destructrices.

Approuvez automatiquement les lectures à faible risque pour préserver la fluidité.

Utilisez des approbations permanentes et limitées pour les actions de confiance répétitives au sein d'une session.

Cela crée un gradient de risque sain. Les utilisateurs ne sont pas interrompus pour des lectures inoffensives, mais ils restent dans la boucle quand les conséquences deviennent coûteuses ou irréversibles.

J'apprécie aussi la séparation explicite entre la mémoire fichier et la mémoire Foundry. Les équipes devraient arrêter d'essayer de forcer un seul modèle de mémoire à résoudre tous les problèmes. Des artefacts fichiers grossiers et explicites sont excellents pour l'état visible par l'utilisateur comme les rapports et les listes de surveillance. L'extraction de mémoire au niveau des faits est meilleure pour les préférences et le contexte conversationnel. Combiner les deux donne de meilleurs résultats que de prétendre que l'un ou l'autre suffit.

Mon avis tranché : la future qualité des agents se mesurera moins à des prompts astucieux qu'à l'ergonomie de sécurité. Si vos invites d'approbation sont bruyantes, les utilisateurs cliquent sans réfléchir. Si vos limites de mémoire sont floues, les utilisateurs cessent de faire confiance à l'assistant. Si vos accès aux données sont permissifs par défaut, les équipes de sécurité fermeront le projet.

Pour les équipes .NET et Python qui adoptent ce modèle, la clé est de traiter les callbacks de politique et les règles d'approbation comme de la logique métier centrale, versionnée et testée comme tout autre code critique. Ne les laissez pas traîner comme des lambdas ad hoc enfouies dans des exemples.

Les systèmes d'agents qui gagnent la confiance ne sont pas ceux qui en font le plus. Ce sont ceux qui font exactement ce que les utilisateurs voulaient, ni plus ni moins, avec des points d'interruption clairs quand le risque augmente.

C'est la différence entre une démo impressionnante et un logiciel auquel les gens sont prêts à déléguer du vrai travail.
