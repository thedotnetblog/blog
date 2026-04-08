---
title: "SQL MCP Server — La bonne façon de donner accès aux bases de données aux agents IA"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server de Data API builder donne aux agents IA un accès sécurisé et déterministe aux bases de données sans exposer les schémas ni dépendre de NL2SQL. RBAC, cache, support multi-bases — tout est intégré."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "sql-mcp-server-data-api-builder.md" >}}).*

Soyons honnêtes : la plupart des serveurs MCP de bases de données disponibles aujourd'hui sont effrayants. Ils prennent une requête en langage naturel, génèrent du SQL à la volée et l'exécutent contre vos données de production. Qu'est-ce qui pourrait mal tourner ? (Tout. Absolument tout.)

L'équipe Azure SQL vient de [présenter SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), et il adopte une approche fondamentalement différente. Construit comme une fonctionnalité de Data API builder (DAB) 2.0, il donne aux agents IA un accès structuré et déterministe aux opérations de base de données — sans NL2SQL, sans exposer votre schéma, et avec un RBAC complet à chaque étape.

## Pourquoi pas de NL2SQL ?

C'est la décision de conception la plus intéressante. Les modèles ne sont pas déterministes, et les requêtes complexes sont les plus susceptibles de produire des erreurs subtiles. Les requêtes exactes que les utilisateurs espèrent que l'IA peut générer sont aussi celles qui nécessitent le plus de vérification quand elles sont produites de manière non déterministe.

À la place, SQL MCP Server utilise une approche **NL2DAB**. L'agent travaille avec la couche d'abstraction d'entités de Data API builder et son constructeur de requêtes intégré pour produire du T-SQL précis et bien formé de manière déterministe. Même résultat pour l'utilisateur, mais sans le risque de JOINs hallucinés ou d'exposition accidentelle de données.

## Sept outils, pas sept cents

SQL MCP Server expose exactement sept outils DML, quelle que soit la taille de la base de données :

- `describe_entities` — découvrir les entités et opérations disponibles
- `create_record` — insérer des lignes
- `read_records` — interroger des tables et vues
- `update_record` — modifier des lignes
- `delete_record` — supprimer des lignes
- `execute_entity` — exécuter des procédures stockées
- `aggregate_records` — requêtes d'agrégation

C'est malin, car les fenêtres de contexte sont l'espace de réflexion de l'agent. Les inonder de centaines de définitions d'outils laisse moins de place au raisonnement. Sept outils fixes gardent l'agent concentré sur la *réflexion* plutôt que la *navigation*.

Chaque outil peut être activé ou désactivé individuellement :

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Démarrage en trois commandes

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Voilà un SQL MCP Server en fonctionnement qui expose votre table Customers. La couche d'abstraction d'entités vous permet de créer des alias pour les noms et colonnes, de limiter les champs par rôle et de contrôler exactement ce que les agents voient — sans exposer les détails internes du schéma.

## L'aspect sécurité est solide

C'est là que la maturité de Data API builder porte ses fruits :

- **RBAC à chaque couche** — chaque entité définit quels rôles peuvent lire, créer, mettre à jour ou supprimer, et quels champs sont visibles
- **Intégration Azure Key Vault** — chaînes de connexion et secrets gérés de manière sécurisée
- **Microsoft Entra + OAuth personnalisé** — authentification de niveau production
- **Content Security Policy** — les agents interagissent via un contrat contrôlé, pas du SQL brut

L'abstraction du schéma est particulièrement importante. Vos noms internes de tables et colonnes ne sont jamais exposés à l'agent. Vous définissez des entités, des alias et des descriptions qui ont du sens pour l'interaction IA — pas votre diagramme ERD de base de données.

## Multi-bases et multi-protocoles

SQL MCP Server supporte Microsoft SQL, PostgreSQL, Azure Cosmos DB et MySQL. Et comme c'est une fonctionnalité de DAB, vous obtenez des endpoints REST, GraphQL et MCP simultanément depuis la même configuration. Mêmes définitions d'entités, mêmes règles RBAC, même sécurité — sur les trois protocoles.

L'auto-configuration dans DAB 2.0 peut même inspecter votre base de données et construire la configuration dynamiquement, si vous êtes à l'aise avec moins d'abstraction pour du prototypage rapide.

## Mon avis

C'est ainsi que l'accès base de données d'entreprise pour les agents IA devrait fonctionner. Pas « hey LLM, écris-moi du SQL et YOLO sur la prod ». À la place : une couche d'entités bien définie, une génération de requêtes déterministe, RBAC à chaque étape, cache, monitoring et télémétrie. C'est ennuyeux de la meilleure façon possible.

Pour les développeurs .NET, l'histoire d'intégration est propre — DAB est un outil .NET, le MCP Server tourne en conteneur, et il fonctionne avec Azure SQL, que la plupart d'entre nous utilisent déjà. Si vous construisez des agents IA qui ont besoin d'accéder aux données, commencez ici.

## Pour conclure

SQL MCP Server est gratuit, open-source et tourne partout. C'est l'approche prescriptive de Microsoft pour donner aux agents IA un accès sécurisé aux bases de données. Consultez le [post complet](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) et la [documentation](https://aka.ms/sql/mcp) pour commencer.
