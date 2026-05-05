---
title: "SQL MCP Server, Copilot dans SSMS et un Database Hub avec des agents IA : Ce qui compte vraiment de SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft a dévoilé une pile d'annonces sur les bases de données à SQLCon 2026. Voici ce qui compte vraiment si vous construisez des apps alimentées par l'IA sur Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft vient de lancer [SQLCon 2026 en parallèle de FabCon à Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/), et il y a beaucoup à décortiquer. L'annonce originale couvre tout, des plans d'économies aux fonctionnalités de conformité enterprise. Je vais passer les slides sur les tarifs enterprise et me concentrer sur les éléments qui comptent si vous êtes un développeur qui construit des choses avec Azure SQL et l'IA.

## SQL MCP Server est en public preview

C'est le titre principal pour moi. Azure SQL Database Hyperscale dispose maintenant d'un **SQL MCP Server** en public preview qui vous permet de connecter vos données SQL de manière sécurisée à des agents IA et des Copilots en utilisant le [Model Context Protocol](https://modelcontextprotocol.io/).

Si vous avez suivi la vague MCP — et honnêtement, c'est difficile de la rater en ce moment — c'est une grosse nouvelle. Au lieu de construire des pipelines de données personnalisés pour alimenter vos agents IA en contexte depuis votre base de données, vous obtenez un protocole standardisé pour exposer les données SQL directement. Vos agents peuvent interroger, raisonner et agir sur des informations de base de données en temps réel.

Pour ceux d'entre nous qui construisent des agents IA avec Semantic Kernel ou le Microsoft Agent Framework, ça ouvre un chemin d'intégration propre. Votre agent a besoin de vérifier l'inventaire ? Chercher un enregistrement client ? Valider une commande ? MCP lui donne une façon structurée de le faire sans que vous écriviez du code de récupération de données sur mesure pour chaque scénario.

## GitHub Copilot dans SSMS 22 est maintenant GA

Si vous passez du temps dans SQL Server Management Studio — et soyons honnêtes, la plupart d'entre nous le font encore — GitHub Copilot est maintenant disponible de manière générale dans SSMS 22. La même expérience Copilot que vous utilisez déjà dans VS Code et Visual Studio, mais pour T-SQL.

La valeur pratique est simple : une assistance par chat pour écrire des requêtes, refactoriser des procédures stockées, résoudre des problèmes de performance et gérer des tâches d'administration. Rien de révolutionnaire dans le concept, mais l'avoir directement dans SSMS signifie que vous n'avez pas besoin de changer de contexte vers un autre éditeur juste pour obtenir de l'aide IA sur votre travail de base de données.

## Les index vectoriels ont reçu une sérieuse mise à jour

Azure SQL Database dispose maintenant d'index vectoriels plus rapides et plus performants avec un support complet pour l'insertion, la mise à jour et la suppression. Ça veut dire que vos données vectorielles restent à jour en temps réel — pas besoin de réindexation par lots.

Voici les nouveautés :
- **Quantification** pour des tailles d'index plus petites sans trop perdre en précision
- **Filtrage itératif** pour des résultats plus précis
- **Intégration plus étroite avec l'optimiseur de requêtes** pour des performances prévisibles

Si vous faites du Retrieval-Augmented Generation (RAG) avec Azure SQL comme vector store, ces améliorations sont directement utiles. Vous pouvez garder vos vecteurs à côté de vos données relationnelles dans la même base de données, ce qui simplifie considérablement votre architecture par rapport à l'exécution d'une base de données vectorielle séparée.

Les mêmes améliorations vectorielles sont également disponibles dans SQL Database in Fabric, puisque les deux tournent sur le même moteur SQL en dessous.

## Database Hub dans Fabric : gestion agentique

Celui-ci est plus tourné vers l'avenir, mais il est intéressant. Microsoft a annoncé le **Database Hub dans Microsoft Fabric** (accès anticipé), qui vous donne une vue unifiée sur Azure SQL, Cosmos DB, PostgreSQL, MySQL et SQL Server via Arc.

L'angle intéressant n'est pas juste la vue unifiée — c'est l'approche agentique de la gestion. Des agents IA surveillent en continu votre parc de bases de données, font remonter ce qui a changé, expliquent pourquoi c'est important et suggèrent quoi faire ensuite. C'est un modèle human-in-the-loop où l'agent fait le gros du travail et vous prenez les décisions.

Pour les équipes qui gèrent plus qu'une poignée de bases de données, ça pourrait vraiment réduire le bruit opérationnel. Au lieu de sauter entre les portails et de vérifier manuellement les métriques, l'agent vous apporte le signal.

## Ce que ça signifie pour les développeurs .NET

Le fil conducteur de toutes ces annonces est clair : Microsoft intègre des agents IA à chaque couche de la pile de bases de données. Pas comme un gadget, mais comme une couche d'outillage pratique.

Si vous construisez des apps .NET adossées à Azure SQL, voici ce que je ferais concrètement :

1. **Essayez le SQL MCP Server** si vous construisez des agents IA. C'est la façon la plus propre de donner à vos agents un accès à la base de données sans plomberie personnalisée.
2. **Activez Copilot dans SSMS** si ce n'est pas déjà fait — un gain de productivité gratuit pour le travail SQL quotidien.
3. **Regardez les index vectoriels** si vous faites du RAG et que vous utilisez actuellement un vector store séparé. Consolider sur Azure SQL signifie un service de moins à gérer.

## Pour conclure

L'annonce complète contient plus — plans d'économies, assistants de migration, fonctionnalités de conformité — mais l'histoire pour les développeurs se trouve dans le MCP Server, les améliorations vectorielles et la couche de gestion agentique. Ce sont les éléments qui changent la façon dont vous construisez, pas juste la façon dont vous budgétisez.

Consultez [l'annonce complète de Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) pour avoir le tableau complet, et [inscrivez-vous pour l'accès anticipé au Database Hub](https://aka.ms/database-hub) si vous voulez essayer la nouvelle expérience de gestion.
