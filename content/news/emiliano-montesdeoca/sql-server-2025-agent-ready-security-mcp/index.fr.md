---
title: "SQL Server 2025 comme Base de Données Prête pour les Agents : Sécurité, Backup et MCP dans un Seul Moteur"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "La partie finale de la série Polyglot Tax aborde les problèmes de production difficiles : sécurité Row-Level unifiée sur les données relationnelles, JSON, graphes et vecteurs, plus intégration MCP."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

J'ai suivi la série Polyglot Tax d'Aditya Badramraju avec beaucoup d'intérêt. La partie 4 clôt la série avec les parties qui déterminent vraiment si vous feriez confiance à cette architecture en production.

## Un Modèle de Sécurité pour Tous les Modèles de Données

Une seule politique Row-Level Security couvre toutes les tables — relationnelles, JSON, graphes, vecteurs. Une politique, une preuve pour l'auditeur.

## Backup Unifié = Récupération Atomique

Dans un stack polyglottes, la récupération point-in-time sur cinq bases de données est un cauchemar de cohérence. Avec une seule base de données, c'est atomique par définition.

## Intégration MCP : Agents Sans Middleware

SQL Server 2025 supporte directement le SQL MCP Server. Les agents appellent des outils, le moteur impose l'isolation tenant et le masquage des colonnes automatiquement.

## Conclusion

Pour les développeurs .NET qui construisent des applications agent-first sur Azure SQL, cette architecture mérite une sérieuse considération. Post original d'Aditya Badramraju : [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
