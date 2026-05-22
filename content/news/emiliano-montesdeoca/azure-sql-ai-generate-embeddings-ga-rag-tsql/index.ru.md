---
title: "Azure SQL Теперь Может Генерировать Эмбеддинги — На Чистом T-SQL, Без Слоя Приложения"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS и CREATE EXTERNAL MODEL теперь находятся в GA в Azure SQL Database и Managed Instance. RAG-пайплайны, построенные полностью на T-SQL, без необходимости перемещения данных."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Если вы когда-нибудь создавали RAG-пайплайн, вы знаете налог пайплайна: ваши данные живут в SQL, но для генерации эмбеддингов нужно их извлечь, вызвать API эмбеддингов, обработать пакетную обработку и ограничения скорости, и сохранить результаты где-то с поддержкой векторного поиска. Часто в совершенно другой базе данных.

Azure SQL только что устранил большую часть этого с двумя функциями, которые теперь стали общедоступными: `CREATE EXTERNAL MODEL` и `AI_GENERATE_EMBEDDINGS`.

## Что Они Делают

Эти две функции T-SQL работают как интегрированный пайплайн:

**`CREATE EXTERNAL MODEL`** — регистрирует внешний эндпоинт модели ИИ как именованный объект базы данных. Вы устанавливаете расположение, формат API, тип модели и учётные данные один раз. Повторно используете везде.

**`AI_GENERATE_EMBEDDINGS`** — скалярная функция T-SQL, которая вызывает зарегистрированную модель и возвращает JSON-массив векторных значений. Работает в инструкциях SELECT, INSERT, UPDATE и MERGE.

Вместе они формируют сквозной пайплайн эмбеддингов без выхода из SQL-движка.

## Полный Рабочий Процесс

```sql
-- Шаг 1: Зарегистрируйте провайдера эмбеддингов один раз
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Шаг 2: Генерируйте эмбеддинги встроенно в T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Шаг 3: Поиск с векторным расстоянием
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Это весь пайплайн: данные в SQL, эмбеддинги генерируются в SQL, поиск по сходству в SQL. Без слоя оркестрации, без ETL, без отдельной векторной базы данных.

## Поддерживаемые Форматы API и Параметры

В GA `API_FORMAT` поддерживает **Azure OpenAI** и **OpenAI**. `MODEL_TYPE` пока ограничен значением `EMBEDDINGS`. JSON `PARAMETERS` позволяет устанавливать значения по умолчанию на уровне модели, включая количество повторных попыток:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Аутентификация использует учётные данные базы данных, поэтому секреты остаются вне кода приложения.

## Что Это Открывает для Приложений .NET

Для разработчиков .NET, создающих функции ИИ на основе существующих данных SQL, это значительно. Вам не нужно:

- Извлекать данные в промежуточное хранилище для эмбеддингов
- Управлять внешним пайплайном эмбеддингов
- Настраивать отдельную векторную базу данных (хотя можно использовать Azure AI Search для полнофункционального векторного хранилища)
- Изменять слой доступа к данным приложения

Вы можете постепенно добавлять семантический поиск в существующие SQL-приложения, используя те же инструменты T-SQL, которые у вас уже есть.

## Заключение

Паттерны RAG на SQL-данных стали значительно проще. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` означает, что ваше существующее SQL-приложение может получить возможности векторного поиска без добавления новой инфраструктуры.

Обе функции сегодня доступны в GA в Azure SQL Database и Azure SQL Managed Instance.

Оригинальная публикация: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
