---
title: "Microsoft Foundry juin 2026 : des annonces de fonctionnalités à une plateforme d'agents gouvernée"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Les mises à jour de Foundry en juin signalent une transition de plateforme : distribution, outillage, mémoire, observabilité et optimisation convergent vers une pile d'opérations d'agents prête pour l'entreprise."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

La vague Foundry de juin 2026 n'est pas juste un digest mensuel de plus. Elle marque une transition de maturité, passant de « construire des agents cool » à « exploiter des agents comme des systèmes d'entreprise gouvernés ». Cette distinction compte plus que n'importe quelle fonctionnalité isolée.

Original source: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Trois mises à jour définissent ce virage. D'abord, la publication d'agents vers Microsoft 365 Copilot et Teams a atteint la disponibilité générale, ce qui fait passer la distribution de projets d'intégration personnalisés à une voie de déploiement opinionated. Ensuite, les Toolboxes ont gagné des contrôles de découverte et d'exécution plus forts, y compris la recherche d'outils et les routines. Enfin, l'observabilité plus l'optimisation sont devenues une boucle fermée délibérée, pas une réflexion après coup.

Mon avis : c'est le modèle le plus important de cette sortie. Le traçage, l'évaluation, l'optimisation et le déploiement contrôlé forment le modèle opérationnel minimum viable pour des systèmes non déterministes. Si vous n'avez qu'une seule de ces pièces, vous avez de la télémétrie ou du réglage, pas de la gouvernance.

Claude en GA dans Foundry est aussi stratégique, mais pas principalement à cause de la qualité du modèle. La plus grande valeur, c'est l'intégration d'entreprise : auth Entra, RBAC, continuité de facturation, et alignement des politiques. Les équipes qui passent de points de terminaison de modèle directs à Foundry devraient présenter cela comme une consolidation opérationnelle, pas juste un changement de fournisseur.

Les agents Autopilot sont prometteurs, mais les organisations devraient les aborder avec des choix architecturaux sobres. La collaboration en espace partagé dans Teams peut débloquer de la productivité, mais elle soulève rapidement une complexité d'identité, de permission et de responsabilité. Commencez avec des portées limitées et des points de contrôle d'approbation stricts avant un déploiement large.

Recommandations pratiques :

Si vous êtes déjà en pilote, priorisez l'instrumentation avant l'expansion des capacités. Câblez d'abord le traçage GenAI. Puis établissez des suites d'évaluateurs liées aux résultats métier, pas à des métriques de modèle génériques. Ce n'est qu'après cela que vous devriez exécuter des boucles d'optimiseur et des workflows de promotion.

Pour les agents chargés de toolboxes, activez la recherche d'outils tôt pour réduire le bruit de contexte et le risque de mauvaise sélection d'outil à mesure que les catalogues grandissent. Pour les agents à mémoire activée, définissez la politique de TTL et de rétention en amont. La mémoire sans contrôles de cycle de vie devient de la dette de conformité.

La conclusion la plus tranchée que je puisse tirer, c'est celle-ci : Foundry concerne désormais moins « quel modèle je choisis ? » et davantage « puis-je exécuter le comportement de l'agent comme un cycle de vie géré ? ». Les équipes qui répondent bien à la seconde question s'adapteront facilement à la rotation des modèles. Les équipes fixées sur les classements de modèles continueront de reconstruire des piles fragiles chaque trimestre.

La sortie de juin rend une chose claire. Foundry devient une plateforme d'opérations pour les systèmes IA, pas juste une boîte à outils de développement. C'est un produit plus difficile à construire, et bien plus précieux à adopter.
