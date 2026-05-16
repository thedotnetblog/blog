---
title: "Azure Data Studio est retraité : migrez votre flux Azure SQL vers VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio a été retraité le 6 février 2025, le support se termine le 28 février 2026. Voici le chemin de migration complet vers VS Code avec l'extension MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Azure Data Studio a été retraité le 6 février 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), le support se termine le 28 février 2026 — le remplacement recommandé est VS Code avec l'extension MSSQL.

## Ce qu'il faut installer

Trois éléments pour commencer :

- **Extension MSSQL** — cherchez « SQL Server (mssql) » dans le Marketplace VS Code
- **Extension SQL Database Projects** — schéma en tant que code, validation de build, publication guidée
- **.NET 8 SDK** — requis par le système de build ; SDK manquant est le problème le plus fréquent au premier démarrage

## Migrer vos connexions et paramètres ADS

L'extension MSSQL inclut l'**ADS Migration Toolkit**, qui gère la migration unique dans un flux guidé : connexions enregistrées, groupes de connexions, paramètres et raccourcis clavier sont tous importés automatiquement.

## Retrouver le réflexe F5

Les utilisateurs d'ADS utilisent F5 pour exécuter des requêtes. Installez l'extension **MSSQL Database Management Keymap** pour retrouver les raccourcis clavier de type ADS, y compris F5.

## SQL Database Projects : schéma en tant que code

Clic droit sur un projet → **Publier** → configurer la cible → examiner le script T-SQL généré → déployer. La prévisualisation du script avant le déploiement est la fonctionnalité de sécurité clé. Les modèles d'éléments génèrent des stubs pour les tables, procédures stockées et vues — le même flux de travail que SSDT.

Problème courant : une **incompatibilité de plateforme cible** dans le fichier `.sqlproj` provoquera des erreurs de build si le projet a été créé pour une version différente de SQL Server.

## Schema Compare et Schema Designer

L'extension inclut également **Schema Compare** (diff entre votre projet et la base de données déployée) et **Schema Designer** (édition visuelle du schéma sans écrire du DDL à la main).

## Développeurs Microsoft Fabric

La configuration est identique, mais commencez depuis le **portail Fabric** et connectez la base de données à Git avant de l'ouvrir dans VS Code. Microsoft dispose d'un guide dédié : *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## En résumé

La migration est un flux guidé en une seule fois, pas une reconstruction manuelle. Installez les trois outils, exécutez l'ADS Migration Toolkit, restaurez vos raccourcis clavier, et vous êtes de retour à la normale en moins de 10 minutes.

Consultez l'[article complet](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) pour les captures d'écran étape par étape et le tutoriel spécifique à Fabric.
