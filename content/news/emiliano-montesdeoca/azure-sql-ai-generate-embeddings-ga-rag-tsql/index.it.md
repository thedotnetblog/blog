---
title: "Azure SQL Può Ora Generare Embedding — In T-SQL Puro, Senza Livello Applicativo"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS e CREATE EXTERNAL MODEL sono ora in GA in Azure SQL Database e Managed Instance. Pipeline RAG costruite interamente in T-SQL, senza spostamento di dati richiesto."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Se hai mai costruito una pipeline RAG, conosci la tassa della pipeline: i tuoi dati vivono in SQL, ma per generare embedding devi estrarli, chiamare un'API di embedding, gestire il batching e i limiti di velocità, e archiviare i risultati da qualche parte con ricerca vettoriale. Spesso in un database completamente diverso.

Azure SQL ha appena eliminato la maggior parte di questo con due funzionalità ora generalmente disponibili: `CREATE EXTERNAL MODEL` e `AI_GENERATE_EMBEDDINGS`.

## Cosa Fanno

Queste due funzionalità T-SQL lavorano come una pipeline integrata:

**`CREATE EXTERNAL MODEL`** — registra un endpoint di modello AI esterno come oggetto di database con nome. Imposti la posizione, il formato API, il tipo di modello e le credenziali una volta sola. Riutilizzalo ovunque.

**`AI_GENERATE_EMBEDDINGS`** — una funzione T-SQL scalare che chiama il modello registrato e restituisce un array JSON di valori vettoriali. Funziona nelle istruzioni SELECT, INSERT, UPDATE e MERGE.

Insieme formano una pipeline di embedding end-to-end senza lasciare il motore SQL.

## Il Flusso di Lavoro Completo

```sql
-- Passo 1: Registra il tuo fornitore di embedding una volta
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Passo 2: Genera embedding inline in T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Passo 3: Cerca con la distanza vettoriale
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Questa è l'intera pipeline: dati in SQL, embedding generati in SQL, ricerca per similarità in SQL. Nessun livello di orchestrazione, nessun ETL, nessun database vettoriale separato.

## Formati API e Opzioni Supportate

In GA, `API_FORMAT` supporta **Azure OpenAI** e **OpenAI**. `MODEL_TYPE` è bloccato su `EMBEDDINGS` per ora. Il JSON `PARAMETERS` consente di impostare valori predefiniti a livello di modello incluso il conteggio dei tentativi:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

L'autenticazione usa le credenziali del database, quindi i segreti rimangono fuori dal codice dell'applicazione.

## Cosa Questo Abilita per le Applicazioni .NET

Per gli sviluppatori .NET che costruiscono funzionalità AI su dati SQL esistenti, questo è significativo. Non hai bisogno di:

- Estrarre dati in un archivio intermedio per gli embedding
- Gestire una pipeline di embedding esterna
- Configurare un database vettoriale separato (anche se puoi usare Azure AI Search se vuoi un archivio vettoriale completo)
- Modificare il livello di accesso ai dati della tua applicazione

Puoi aggiungere la ricerca semantica alle applicazioni SQL esistenti in modo incrementale, usando gli stessi strumenti T-SQL che hai già.

## Conclusione

I pattern RAG sui dati SQL sono diventati drammaticamente più semplici. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` significa che la tua applicazione SQL esistente può acquisire capacità di ricerca vettoriale senza aggiungere nuova infrastruttura.

Entrambe le funzionalità sono in GA in Azure SQL Database e Azure SQL Managed Instance oggi.

Post originale: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
