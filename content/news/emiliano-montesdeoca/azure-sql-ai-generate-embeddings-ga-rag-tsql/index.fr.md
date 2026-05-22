---
title: "Azure SQL Peut Maintenant Générer des Embeddings — En T-SQL Pur, Sans Couche Applicative"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS et CREATE EXTERNAL MODEL sont maintenant en GA dans Azure SQL Database et Managed Instance. Des pipelines RAG entièrement construits en T-SQL, sans déplacement de données requis."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Si vous avez déjà construit un pipeline RAG, vous connaissez la taxe pipeline : vos données vivent dans SQL, mais pour générer des embeddings vous devez les extraire, appeler une API d'embeddings, gérer le traitement par lots et les limites de débit, et stocker les résultats quelque part avec une recherche vectorielle. Souvent dans une base de données entièrement différente.

Azure SQL vient d'éliminer la majeure partie de cela avec deux fonctionnalités désormais généralement disponibles : `CREATE EXTERNAL MODEL` et `AI_GENERATE_EMBEDDINGS`.

## Ce Qu'elles Font

Ces deux fonctionnalités T-SQL fonctionnent comme un pipeline intégré :

**`CREATE EXTERNAL MODEL`** — enregistre un endpoint de modèle d'IA externe comme un objet de base de données nommé. Vous définissez l'emplacement, le format d'API, le type de modèle et les identifiants une seule fois. Réutilisez-les partout.

**`AI_GENERATE_EMBEDDINGS`** — une fonction T-SQL scalaire qui appelle le modèle enregistré et renvoie un tableau JSON de valeurs vectorielles. Fonctionne dans les instructions SELECT, INSERT, UPDATE et MERGE.

Ensemble, ils forment un pipeline d'embeddings de bout en bout sans quitter le moteur SQL.

## Le Flux de Travail Complet

```sql
-- Étape 1 : Enregistrez votre fournisseur d'embeddings une fois
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Étape 2 : Générez des embeddings en ligne en T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Étape 3 : Recherche avec la distance vectorielle
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

C'est tout le pipeline : données dans SQL, embeddings générés dans SQL, recherche de similarité dans SQL. Pas de couche d'orchestration, pas d'ETL, pas de base de données vectorielle séparée.

## Formats d'API et Options Supportés

En GA, `API_FORMAT` supporte **Azure OpenAI** et **OpenAI**. `MODEL_TYPE` est verrouillé sur `EMBEDDINGS` pour l'instant. Le JSON `PARAMETERS` vous permet de définir des valeurs par défaut au niveau du modèle, notamment le nombre de tentatives :

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

L'authentification utilise les identifiants de la base de données, donc les secrets restent hors de votre code applicatif.

## Ce Que Cela Permet pour les Applications .NET

Pour les développeurs .NET qui construisent des fonctionnalités d'IA sur des données SQL existantes, c'est significatif. Vous n'avez pas besoin de :

- Extraire des données vers un magasin intermédiaire pour les embeddings
- Gérer un pipeline d'embeddings externe
- Configurer une base de données vectorielle séparée (bien que vous puissiez utiliser Azure AI Search si vous voulez un magasin vectoriel complet)
- Modifier la couche d'accès aux données de votre application

Vous pouvez ajouter la recherche sémantique aux applications SQL existantes de manière incrémentale, en utilisant les mêmes outils T-SQL que vous avez déjà.

## Conclusion

Les patterns RAG sur les données SQL sont devenus dramatiquement plus simples. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` signifie que votre application SQL existante peut acquérir des capacités de recherche vectorielle sans ajouter de nouvelle infrastructure.

Les deux fonctionnalités sont en GA dans Azure SQL Database et Azure SQL Managed Instance aujourd'hui.

Post original : [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
