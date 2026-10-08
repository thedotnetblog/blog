---
title: "Les chemins personnalisés de Data API Builder vous permettent de concevoir des API pour les humains, pas pour les tables"
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: "Les chemins REST composés dans DAB sont une petite fonctionnalité avec un grand impact architectural pour la conception d'API orientée domaine."
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Original source: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

Le nouveau support des chemins REST composés dans Data API Builder peut sembler une amélioration de configuration mineure, mais il résout en réalité une tension de conception d'API de longue date : la topologie de base de données qui s'infiltre dans la conception des points de terminaison publics.

Les routes par défaut basées sur les entités sont excellentes pour des démarrages rapides. Elles sont souvent inadéquates pour des API produit à long terme. Les vrais systèmes ont besoin de structures de route qui correspondent aux concepts métier, aux limites de propriété et aux modèles mentaux des consommateurs.

C'est pourquoi ce changement de DAB compte. Vous pouvez garder la commodité d'API générée tout en présentant une surface plus propre et orientée domaine.

Mon avis tranché est simple : si la structure de chemin de votre API reflète les noms de table brutes en production, vous optimisez généralement pour la commodité du back-end au détriment de la clarté pour le client.

Avec les chemins personnalisés, les équipes peuvent modéliser de meilleures limites, comme des surfaces ventes, facturation, support, ou spécifiques à un partenaire. Cela ne remplace pas une bonne gouvernance d'API, mais cela donne aux utilisateurs de DAB un moyen pratique d'aligner la conception des routes avec le langage produit.

Conseils pratiques pour les équipes qui adoptent cette fonctionnalité :

Définissez une politique de nommage avant d'ajouter des chemins de manière ad hoc. Des sous-segments incohérents deviennent un fouillis à long terme.

Faites correspondre les points de terminaison à des contextes délimités, pas à des organigrammes. Les équipes changent ; la sémantique de domaine devrait être stable.

Traitez la structure des chemins comme faisant partie de votre stratégie de versionnage et documentez explicitement les changements cassants.

Validez le comportement d'autorisation le long des structures de routes personnalisées afin que la clarté des routes soit associée à la clarté de sécurité.

Ce que j'apprécie dans DAB en général, c'est le modèle d'effet de levier : vous obtenez pagination, filtrage, projection et autres mécaniques de point de terminaison sans écrire de code de contrôleur répétitif. Les chemins personnalisés rendent cet effet de levier plus prêt pour la production en réduisant l'une des plus grandes objections des architectes d'API.

Il y a une mise en garde. Une meilleure composition de chemin peut tenter les équipes d'exposer trop rapidement trop de choses parce que la génération semble facile. Les garde-fous comptent encore : gardez l'exposition d'entité délibérée, appliquez la politique de manière centralisée, et évitez de construire accidentellement des contrats publics à partir d'expérimentations de schéma interne.

Pour les organisations .NET sous pression de livraison, cette fonctionnalité est un déblocage de productivité si elle est utilisée avec discipline. Vous pouvez avancer plus vite que des couches d'API faites à la main tout en préservant une surface de point de terminaison cohérente et adaptée au métier.

En résumé : les chemins personnalisés de DAB ne consistent pas à enjoliver les URL. Ils consistent à reprendre le contrôle de l'intention de conception d'API tout en conservant l'efficacité opérationnelle des points de terminaison générés.
