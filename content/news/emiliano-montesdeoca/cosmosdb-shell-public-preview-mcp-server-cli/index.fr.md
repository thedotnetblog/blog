---
title: "Cosmos DB Shell Est en Préversion Publique — Et Il a un Serveur MCP Intégré"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell est un nouveau CLI open source qui expose les commandes de base de données comme outils MCP. Vos agents IA peuvent naviguer dans les conteneurs, exécuter des requêtes et gérer des données en utilisant la même interface que vous."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Si vous avez déjà dû naviguer entre un onglet de portail, un exemple de SDK et un script à moitié terminé juste pour répondre à une question Cosmos DB, vous connaissez déjà la friction que ce projet est conçu pour éliminer.

Azure Cosmos DB Shell vient d'entrer en préversion publique. C'est un CLI open source avec une syntaxe de type bash et — la partie qui le rend intéressant — un serveur MCP intégré.

## Ce Qui le Différencie des Autres CLIs de Base de Données

Le CLI lui-même est utile : commandes familières, support de script, intégration CI/CD. Cette partie est le minimum attendu pour un outil de base de données orienté développeur.

La partie intéressante est l'intégration du serveur MCP. Chaque commande que le CLI expose devient disponible comme outil MCP que vos agents IA peuvent appeler. Il n'y a pas de couche API personnalisée, pas de code d'intégration à écrire. Votre agent peut :

- Naviguer dans les hiérarchies de bases de données avec `cd`, `ls`, `pwd`
- Exécuter des requêtes SQL avec `query` et obtenir des résultats structurés
- Créer et modifier des éléments avec `create item`, `update`, `rm`
- Gérer des bases de données et des conteneurs avec `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Inspecter le contexte actuel avec `endpoint`, `pwd`

Le changement clé : votre agent ne parle pas à une API Cosmos DB — il parle à la même interface shell que vous utilisez. Les commandes sont déterministes, auditables et open source pour que vous puissiez inspecter exactement ce qui se passe.

## La Base Open Source Compte

Ce n'est pas un service géré boîte noire. Le shell est open source, ce qui signifie :

- Les équipes de sécurité peuvent auditer l'implémentation
- Les équipes de plateforme peuvent le forker et l'étendre pour leurs standards spécifiques
- Les développeurs peuvent contribuer des améliorations qui bénéficient à tous

Pour les équipes d'entreprise adoptant des outils IA, "peut-on voir exactement comment ça fonctionne" est de plus en plus une exigence non optionnelle. L'open source ici est un différenciateur significatif.

## Trois Scénarios Qui Deviennent Plus Faciles

**Analyse intelligente des données** — connectez un agent au shell, posez des questions en langage naturel, obtenez des résultats de requêtes structurés. L'agent gère la construction de la requête ; le shell gère l'exécution.

**Gestion autonome des données** — les workflows qui doivent créer, mettre à jour ou supprimer des données dans Cosmos DB peuvent le faire via les outils MCP sans avoir besoin d'une intégration personnalisée.

**Surveillance et alertes en temps réel** — un agent peut interroger périodiquement des conteneurs, comparer les résultats et signaler des anomalies via le canal de notification approprié.

L'interface MCP rend ces scénarios composables avec n'importe quelle plateforme IA qui parle MCP — pas seulement les outils Microsoft.

## Pour Commencer

Le shell est en préversion publique. Installez-le, configurez votre connexion Cosmos DB et activez le serveur MCP. De là, tout hôte d'agent compatible MCP peut découvrir et utiliser les outils.

Post original : [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
