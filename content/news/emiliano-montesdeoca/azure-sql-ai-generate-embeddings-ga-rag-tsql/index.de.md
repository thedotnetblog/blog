---
title: "Azure SQL Kann Jetzt Embeddings Generieren — In Reinem T-SQL, Keine Anwendungsschicht Erforderlich"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS und CREATE EXTERNAL MODEL sind jetzt in Azure SQL Database und Managed Instance allgemein verfügbar. RAG-Pipelines vollständig in T-SQL gebaut, kein Datentransport erforderlich."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Wenn Sie jemals eine RAG-Pipeline gebaut haben, kennen Sie die Pipeline-Steuer: Ihre Daten leben in SQL, aber um Embeddings zu generieren, müssen Sie sie extrahieren, eine Embedding-API aufrufen, Batching und Ratenlimits handhaben und die Ergebnisse irgendwo vektorsuchtauglich speichern. Oft in einer völlig anderen Datenbank.

Azure SQL hat das meiste davon gerade mit zwei Features eliminiert, die jetzt allgemein verfügbar sind: `CREATE EXTERNAL MODEL` und `AI_GENERATE_EMBEDDINGS`.

## Was Sie Tun

Diese beiden T-SQL-Features funktionieren als integrierte Pipeline:

**`CREATE EXTERNAL MODEL`** — registriert einen externen KI-Modell-Endpoint als benanntes Datenbankobjekt. Sie legen Ort, API-Format, Modelltyp und Anmeldeinformationen einmal fest. Überall wiederverwendbar.

**`AI_GENERATE_EMBEDDINGS`** — eine skalare T-SQL-Funktion, die das registrierte Modell aufruft und ein JSON-Array von Vektorwerten zurückgibt. Funktioniert in SELECT-, INSERT-, UPDATE- und MERGE-Anweisungen.

Zusammen bilden sie eine End-to-End-Embedding-Pipeline ohne die SQL-Engine zu verlassen.

## Der Vollständige Workflow

```sql
-- Schritt 1: Registrieren Sie Ihren Embedding-Anbieter einmal
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Schritt 2: Embeddings inline in T-SQL generieren
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Schritt 3: Mit Vektorabstand suchen
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Das ist die gesamte Pipeline: Daten in SQL, Embeddings in SQL generiert, Ähnlichkeitssuche in SQL. Keine Orchestrierungsschicht, kein ETL, keine separate Vektordatenbank.

## Unterstützte API-Formate und Optionen

In der GA-Version unterstützt `API_FORMAT` **Azure OpenAI** und **OpenAI**. `MODEL_TYPE` ist derzeit auf `EMBEDDINGS` beschränkt. Das `PARAMETERS`-JSON ermöglicht das Festlegen von Standardwerten auf Modellebene einschließlich der Anzahl der Wiederholungsversuche:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Die Authentifizierung verwendet Datenbankzugangsdaten, sodass Geheimnisse aus Ihrem Anwendungscode herausgehalten werden.

## Was Dies für .NET-Anwendungen Ermöglicht

Für .NET-Entwickler, die KI-Features auf vorhandenen SQL-Daten aufbauen, ist dies bedeutsam. Sie müssen nicht:

- Daten für Embeddings in einen Zwischenspeicher extrahieren
- Eine externe Embedding-Pipeline verwalten
- Eine separate Vektordatenbank einrichten (obwohl Sie Azure AI Search verwenden können, wenn Sie einen vollwertigen Vektorspeicher möchten)
- Die Datenzugriffsschicht Ihrer Anwendung ändern

Sie können semantische Suche zu bestehenden SQL-Anwendungen inkrementell hinzufügen, mit denselben T-SQL-Tools, die Sie bereits haben.

## Fazit

RAG-Muster auf SQL-Daten sind dramatisch einfacher geworden. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` bedeutet, dass Ihre bestehende SQL-Anwendung Vektorsuche-Fähigkeiten ohne neue Infrastruktur erwerben kann.

Beide Features sind heute in Azure SQL Database und Azure SQL Managed Instance allgemein verfügbar.

Originalbeitrag: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
