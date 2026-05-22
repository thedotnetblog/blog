---
title: "Azure SQL Kan Nu Embeddings Genereren — In Puur T-SQL, Geen Applicatielaag Nodig"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS en CREATE EXTERNAL MODEL zijn nu GA in Azure SQL Database en Managed Instance. RAG-pipelines volledig gebouwd in T-SQL, geen gegevensverplaatsing vereist."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Als u ooit een RAG-pipeline hebt gebouwd, kent u de pipeline-belasting: uw gegevens leven in SQL, maar om embeddings te genereren moet u ze extraheren, een embedding-API aanroepen, batching en snelheidslimieten beheren, en de resultaten ergens opslaan met vector-zoekfunctionaliteit. Vaak in een geheel andere database.

Azure SQL heeft het meeste daarvan zojuist geëlimineerd met twee functies die nu algemeen beschikbaar zijn: `CREATE EXTERNAL MODEL` en `AI_GENERATE_EMBEDDINGS`.

## Wat Ze Doen

Deze twee T-SQL-functies werken als een geïntegreerde pipeline:

**`CREATE EXTERNAL MODEL`** — registreert een extern AI-modelendpoint als een benoemd databaseobject. U stelt locatie, API-indeling, modeltype en referenties eenmalig in. Overal herbruikbaar.

**`AI_GENERATE_EMBEDDINGS`** — een scalaire T-SQL-functie die het geregistreerde model aanroept en een JSON-array van vectorwaarden retourneert. Werkt in SELECT-, INSERT-, UPDATE- en MERGE-instructies.

Samen vormen ze een end-to-end embedding-pipeline zonder het SQL-engine te verlaten.

## De Complete Workflow

```sql
-- Stap 1: Registreer uw embedding-provider eenmalig
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Stap 2: Genereer embeddings inline in T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Stap 3: Zoek met vectorafstand
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Dat is de volledige pipeline: gegevens in SQL, embeddings gegenereerd in SQL, gelijkenis zoeken in SQL. Geen orchestratielaag, geen ETL, geen aparte vectordatabase.

## Ondersteunde API-indelingen en Opties

Bij GA ondersteunt `API_FORMAT` **Azure OpenAI** en **OpenAI**. `MODEL_TYPE` is voorlopig vergrendeld op `EMBEDDINGS`. De `PARAMETERS` JSON laat u standaardwaarden op modelniveau instellen, inclusief het aantal pogingen:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Verificatie gebruikt databasereferenties, zodat geheimen buiten uw applicatiecode blijven.

## Wat Dit Mogelijk Maakt voor .NET-toepassingen

Voor .NET-ontwikkelaars die AI-functies bouwen op bestaande SQL-gegevens is dit significant. U hoeft niet:

- Gegevens te extraheren naar een tussenopslag voor embeddings
- Een externe embedding-pipeline te beheren
- Een aparte vectordatabase in te stellen (u kunt Azure AI Search gebruiken als u een volwaardige vectoropslag wilt)
- De gegevenstoegangslaag van uw toepassing te wijzigen

U kunt semantisch zoeken incrementeel toevoegen aan bestaande SQL-toepassingen, met dezelfde T-SQL-tools die u al heeft.

## Conclusie

RAG-patronen op SQL-gegevens zijn dramatisch eenvoudiger geworden. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` betekent dat uw bestaande SQL-toepassing vectorzoekmogelijkheden kan krijgen zonder nieuwe infrastructuur toe te voegen.

Beide functies zijn vandaag GA in Azure SQL Database en Azure SQL Managed Instance.

Originele post: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
