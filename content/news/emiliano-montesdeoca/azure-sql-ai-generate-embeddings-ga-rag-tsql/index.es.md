---
title: "Azure SQL Puede Generar Embeddings Ahora — En T-SQL Puro, Sin Capa de Aplicación"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS y CREATE EXTERNAL MODEL ahora están en GA en Azure SQL Database y Managed Instance. Pipelines RAG construidos completamente en T-SQL, sin movimiento de datos requerido."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Si alguna vez has construido un pipeline RAG, conoces el impuesto del pipeline: tus datos viven en SQL, pero para generar embeddings necesitas extraerlos, llamar a una API de embeddings, gestionar lotes y límites de velocidad, y almacenar los resultados en algún lugar con búsqueda vectorial. A menudo en una base de datos completamente diferente.

Azure SQL acaba de eliminar la mayor parte de eso con dos características que ahora están generalmente disponibles: `CREATE EXTERNAL MODEL` y `AI_GENERATE_EMBEDDINGS`.

## Qué Hacen

Estas dos características de T-SQL funcionan como un pipeline integrado:

**`CREATE EXTERNAL MODEL`** — registra un endpoint de modelo de IA externo como un objeto de base de datos con nombre. Estableces la ubicación, el formato de API, el tipo de modelo y las credenciales una vez. Lo reutilizas en cualquier lugar.

**`AI_GENERATE_EMBEDDINGS`** — una función T-SQL escalar que llama al modelo registrado y devuelve una matriz JSON de valores vectoriales. Funciona en sentencias SELECT, INSERT, UPDATE y MERGE.

Juntos forman un pipeline de embeddings de extremo a extremo sin salir del motor SQL.

## El Flujo de Trabajo Completo

```sql
-- Paso 1: Registra tu proveedor de embeddings una vez
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Paso 2: Genera embeddings en línea en T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Paso 3: Busca con distancia vectorial
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Ese es todo el pipeline: datos en SQL, embeddings generados en SQL, búsqueda de similitud en SQL. Sin capa de orquestación, sin ETL, sin base de datos vectorial separada.

## Formatos de API y Opciones Soportadas

En GA, `API_FORMAT` soporta **Azure OpenAI** y **OpenAI**. `MODEL_TYPE` está bloqueado a `EMBEDDINGS` por ahora. El JSON `PARAMETERS` te permite establecer valores predeterminados a nivel de modelo incluyendo el conteo de reintentos:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

La autenticación usa credenciales de base de datos, por lo que los secretos se mantienen fuera del código de tu aplicación.

## Qué Habilita Esto para las Aplicaciones .NET

Para los desarrolladores .NET que construyen características de IA sobre datos SQL existentes, esto es significativo. No necesitas:

- Extraer datos a un almacén intermedio para embeddings
- Gestionar un pipeline de embeddings externo
- Configurar una base de datos vectorial separada (aunque puedes usar Azure AI Search si quieres un almacén vectorial completo)
- Cambiar la capa de acceso a datos de tu aplicación

Puedes agregar búsqueda semántica a las aplicaciones SQL existentes de manera incremental, usando las mismas herramientas T-SQL que ya tienes.

## Conclusión

Los patrones RAG sobre datos SQL se han vuelto dramáticamente más simples. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` significa que tu aplicación SQL existente puede ganar capacidades de búsqueda vectorial sin agregar nueva infraestructura.

Ambas características están en GA en Azure SQL Database y Azure SQL Managed Instance hoy.

Post original: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
