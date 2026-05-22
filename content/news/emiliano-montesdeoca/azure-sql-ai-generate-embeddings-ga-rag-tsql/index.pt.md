---
title: "Azure SQL Agora Pode Gerar Embeddings — Em T-SQL Puro, Sem Camada de Aplicação"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS e CREATE EXTERNAL MODEL estão agora em GA no Azure SQL Database e Managed Instance. Pipelines RAG construídas inteiramente em T-SQL, sem movimentação de dados necessária."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Se você já construiu uma pipeline RAG, conhece o imposto da pipeline: seus dados vivem no SQL, mas para gerar embeddings você precisa extraí-los, chamar uma API de embeddings, lidar com batching e limites de taxa, e armazenar os resultados em algum lugar com busca vetorial. Muitas vezes em um banco de dados completamente diferente.

O Azure SQL acabou de eliminar a maior parte disso com duas funcionalidades que agora estão geralmente disponíveis: `CREATE EXTERNAL MODEL` e `AI_GENERATE_EMBEDDINGS`.

## O Que Elas Fazem

Essas duas funcionalidades T-SQL funcionam como uma pipeline integrada:

**`CREATE EXTERNAL MODEL`** — registra um endpoint de modelo de IA externo como um objeto de banco de dados nomeado. Você define a localização, o formato da API, o tipo de modelo e as credenciais uma vez. Reutilize em qualquer lugar.

**`AI_GENERATE_EMBEDDINGS`** — uma função T-SQL escalar que chama o modelo registrado e retorna um array JSON de valores vetoriais. Funciona em instruções SELECT, INSERT, UPDATE e MERGE.

Juntos formam uma pipeline de embeddings de ponta a ponta sem sair do motor SQL.

## O Fluxo de Trabalho Completo

```sql
-- Passo 1: Registre seu provedor de embeddings uma vez
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Passo 2: Gere embeddings inline em T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Passo 3: Pesquise com distância vetorial
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Esse é o pipeline inteiro: dados no SQL, embeddings gerados no SQL, busca por similaridade no SQL. Sem camada de orquestração, sem ETL, sem banco de dados vetorial separado.

## Formatos de API e Opções Suportadas

Em GA, `API_FORMAT` suporta **Azure OpenAI** e **OpenAI**. `MODEL_TYPE` está bloqueado em `EMBEDDINGS` por enquanto. O JSON `PARAMETERS` permite definir padrões a nível de modelo incluindo o número de tentativas:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

A autenticação usa credenciais do banco de dados, portanto os segredos ficam fora do código da aplicação.

## O Que Isso Habilita para Aplicações .NET

Para desenvolvedores .NET construindo funcionalidades de IA em dados SQL existentes, isso é significativo. Você não precisa:

- Extrair dados para um armazenamento intermediário para embeddings
- Gerenciar uma pipeline de embeddings externa
- Configurar um banco de dados vetorial separado (embora você possa usar Azure AI Search se quiser um armazenamento vetorial completo)
- Alterar a camada de acesso a dados da sua aplicação

Você pode adicionar busca semântica a aplicações SQL existentes de forma incremental, usando as mesmas ferramentas T-SQL que você já tem.

## Conclusão

Os padrões RAG em dados SQL ficaram dramaticamente mais simples. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` significa que sua aplicação SQL existente pode ganhar capacidades de busca vetorial sem adicionar nova infraestrutura.

Ambas as funcionalidades estão em GA no Azure SQL Database e Azure SQL Managed Instance hoje.

Post original: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
