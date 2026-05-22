---
title: "Azure SQL Ara Ara Incrustaments — En T-SQL Pur, Sense Capa d'Aplicació"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS i CREATE EXTERNAL MODEL ara estan en GA a Azure SQL Database i Managed Instance. Pipelines RAG construïts completament en T-SQL, sense moviment de dades necessari."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Si alguna vegada has construït un pipeline RAG, coneixes l'impost del pipeline: les teves dades viuen a SQL, però per generar incrustaments has d'extreure-les, cridar una API d'incrustaments, gestionar lots i límits de velocitat, i emmagatzemar els resultats en un lloc de cerca vectorial. Sovint en una base de dades completament diferent.

Azure SQL acaba d'eliminar la major part d'això amb dues funcionalitats que ara estan generalment disponibles: `CREATE EXTERNAL MODEL` i `AI_GENERATE_EMBEDDINGS`.

## Què Fan

Aquestes dues funcionalitats de T-SQL funcionen com un pipeline integrat:

**`CREATE EXTERNAL MODEL`** — registra un punt final de model d'IA extern com a objecte de base de dades anomenat. Establiu la ubicació, el format de l'API, el tipus de model i les credencials una vegada. Reutilitzeu-ho en qualsevol lloc.

**`AI_GENERATE_EMBEDDINGS`** — una funció T-SQL escalar que crida el model registrat i retorna una matriu JSON de valors vectorials. Funciona en sentències SELECT, INSERT, UPDATE i MERGE.

Junts formen un pipeline d'incrustaments d'extrem a extrem sense sortir del motor SQL.

## El Flux de Treball Complet

```sql
-- Pas 1: Registra el teu proveïdor d'incrustaments una vegada
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Pas 2: Genera incrustaments en línia en T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Pas 3: Cerca amb distància vectorial
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Això és tot el pipeline: dades a SQL, incrustaments generats a SQL, cerca de similitud a SQL. Sense capa d'orquestració, sense ETL, sense base de dades vectorial separada.

## Formats d'API i Opcions Suportades

En GA, `API_FORMAT` suporta **Azure OpenAI** i **OpenAI**. `MODEL_TYPE` està bloquejat a `EMBEDDINGS` de moment. El JSON `PARAMETERS` permet establir valors predeterminats a nivell de model inclòs el recompte de reintents:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

L'autenticació utilitza credencials de base de dades, de manera que els secrets queden fora del codi de l'aplicació.

## Què Permet Això per a les Aplicacions .NET

Per als desenvolupadors .NET que construeixen funcionalitats d'IA sobre dades SQL existents, això és significatiu. No necessiteu:

- Extreure dades a un magatzem intermedi per a incrustaments
- Gestionar un pipeline d'incrustaments extern
- Configurar una base de dades vectorial separada (tot i que podeu utilitzar Azure AI Search si voleu un magatzem vectorial complet)
- Canviar la capa d'accés a dades de l'aplicació

Podeu afegir cerca semàntica a les aplicacions SQL existents de manera incremental, utilitzant les mateixes eines T-SQL que ja teniu.

## Conclusió

Els patrons RAG sobre dades SQL s'han tornat dramàticament més simples. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` significa que la vostra aplicació SQL existent pot guanyar capacitats de cerca vectorial sense afegir nova infraestructura.

Ambdues funcionalitats estan en GA a Azure SQL Database i Azure SQL Managed Instance avui.

Post original: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
