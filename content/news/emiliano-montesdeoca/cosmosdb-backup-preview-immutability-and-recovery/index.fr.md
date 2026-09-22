---
title: "La sauvegarde immuable pour Cosmos DB est le genre de fonctionnalité qu'on apprécie trop tard"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Backup pour Azure Cosmos DB ajoute désormais des sauvegardes immuables et une rétention à long terme en préversion publique. Le point clé n'est pas seulement la récupération, mais l'amélioration de la résilience et de la préservation des preuves pour les charges de travail réglementées ou à haut risque."
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

Les fonctionnalités de sauvegarde sont faciles à ignorer, jusqu'au moment où elles deviennent la chose la plus importante de la pièce.

C'est pourquoi je pense que le nouvel aperçu d'**Azure Backup pour Azure Cosmos DB** mérite de l'attention.

La partie intéressante ici n'est pas simplement « une autre option de sauvegarde ». C'est l'ajout de **points de récupération immuables** et de **rétention à long terme** dans un modèle bien mieux aligné avec la préparation aux rançongiciels, l'auditabilité et les exigences de récupération réglementées.

## L'immuabilité change la conversation

Quand des attaquants ciblent des systèmes de production, la question suivante n'est plus seulement « avons-nous une sauvegarde ? »

C'est :

- la sauvegarde peut-elle être fiable ?
- peut-elle être altérée ou supprimée ?
- avons-nous encore un point de récupération protégé après le début de l'incident ?

C'est pourquoi les sauvegardes immuables comptent. Elles améliorent le chemin de récupération quand l'environnement autour peut ne plus être digne de confiance.

## Mon avis

Ce n'est pas le genre d'annonce qui enthousiasme tout le monde.

Mais pour les équipes qui exploitent des charges de travail critiques sur Cosmos DB, c'est exactement le genre de capacité qui devient centrale le pire jour du trimestre.

Et ce sont souvent les fonctionnalités les plus importantes à suivre.

Original post: [Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)
