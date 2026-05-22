---
title: "Azure SQL Może Teraz Generować Embeddingi — W Czystym T-SQL, Bez Warstwy Aplikacji"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS i CREATE EXTERNAL MODEL są teraz w GA w Azure SQL Database i Managed Instance. Pipelines RAG zbudowane całkowicie w T-SQL, bez konieczności przenoszenia danych."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Jeśli kiedykolwiek zbudowałeś pipeline RAG, znasz podatek pipeline'u: twoje dane żyją w SQL, ale żeby generować embeddingi musisz je wyodrębnić, wywołać API embeddingów, obsługiwać przetwarzanie wsadowe i limity szybkości, i przechowywać wyniki gdzieś, gdzie można wyszukiwać wektory. Często w zupełnie innej bazie danych.

Azure SQL właśnie wyeliminował większość z tego dzięki dwóm funkcjom, które są teraz ogólnie dostępne: `CREATE EXTERNAL MODEL` i `AI_GENERATE_EMBEDDINGS`.

## Co Robią

Te dwie funkcje T-SQL działają jako zintegrowany pipeline:

**`CREATE EXTERNAL MODEL`** — rejestruje zewnętrzny punkt końcowy modelu AI jako nazwany obiekt bazy danych. Ustawiasz lokalizację, format API, typ modelu i poświadczenia raz. Ponownie używasz wszędzie.

**`AI_GENERATE_EMBEDDINGS`** — skalarna funkcja T-SQL, która wywołuje zarejestrowany model i zwraca tablicę JSON wartości wektorowych. Działa w instrukcjach SELECT, INSERT, UPDATE i MERGE.

Razem tworzą end-to-end pipeline embeddingów bez opuszczania silnika SQL.

## Pełny Przepływ Pracy

```sql
-- Krok 1: Zarejestruj dostawcę embeddingów raz
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Krok 2: Generuj embeddingi inline w T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Krok 3: Wyszukuj z odległością wektorową
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

To jest cały pipeline: dane w SQL, embeddingi generowane w SQL, wyszukiwanie podobieństw w SQL. Bez warstwy orkiestracji, bez ETL, bez oddzielnej bazy danych wektorów.

## Obsługiwane Formaty API i Opcje

W GA `API_FORMAT` obsługuje **Azure OpenAI** i **OpenAI**. `MODEL_TYPE` jest na razie zablokowany na `EMBEDDINGS`. JSON `PARAMETERS` pozwala ustawić wartości domyślne na poziomie modelu, w tym liczbę ponownych prób:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Uwierzytelnianie używa poświadczeń bazy danych, więc sekrety pozostają poza kodem aplikacji.

## Co To Umożliwia dla Aplikacji .NET

Dla programistów .NET budujących funkcje AI na istniejących danych SQL, to jest znaczące. Nie potrzebujesz:

- Wyodrębniać danych do pośredniego magazynu dla embeddingów
- Zarządzać zewnętrznym pipeline embeddingów
- Konfigurować oddzielnej bazy danych wektorów (choć możesz użyć Azure AI Search jeśli chcesz pełnofunkcjonalny magazyn wektorów)
- Zmieniać warstwy dostępu do danych aplikacji

Możesz stopniowo dodawać wyszukiwanie semantyczne do istniejących aplikacji SQL, używając tych samych narzędzi T-SQL, które już masz.

## Podsumowanie

Wzorce RAG na danych SQL stały się dramatycznie prostsze. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` oznacza, że Twoja istniejąca aplikacja SQL może zyskać możliwości wyszukiwania wektorów bez dodawania nowej infrastruktury.

Obie funkcje są dziś w GA w Azure SQL Database i Azure SQL Managed Instance.

Oryginalny post: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
