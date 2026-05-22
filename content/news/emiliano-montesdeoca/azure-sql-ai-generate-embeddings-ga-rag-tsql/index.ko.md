---
title: "Azure SQL이 이제 임베딩을 생성할 수 있습니다 — 순수 T-SQL로, 앱 레이어 없이"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS와 CREATE EXTERNAL MODEL이 Azure SQL Database와 Managed Instance에서 GA가 되었습니다. 데이터 이동 없이 T-SQL만으로 구축된 RAG 파이프라인."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

RAG 파이프라인을 구축해본 적이 있다면 파이프라인 세금을 알 것입니다: 데이터는 SQL에 있지만 임베딩을 생성하려면 데이터를 추출하고, 임베딩 API를 호출하고, 배치 처리와 속도 제한을 처리하고, 벡터 검색이 가능한 곳에 결과를 저장해야 합니다. 종종 완전히 다른 데이터베이스에.

Azure SQL은 현재 일반 공개된 두 가지 기능으로 그 대부분을 제거했습니다: `CREATE EXTERNAL MODEL`과 `AI_GENERATE_EMBEDDINGS`.

## 무엇을 하는가

이 두 T-SQL 기능은 통합 파이프라인으로 작동합니다:

**`CREATE EXTERNAL MODEL`** — 외부 AI 모델 엔드포인트를 명명된 데이터베이스 객체로 등록합니다. 위치, API 형식, 모델 유형, 자격 증명을 한 번 설정합니다. 어디서나 재사용하세요.

**`AI_GENERATE_EMBEDDINGS`** — 등록된 모델을 호출하고 벡터 값의 JSON 배열을 반환하는 스칼라 T-SQL 함수입니다. SELECT, INSERT, UPDATE, MERGE 문에서 작동합니다.

함께 SQL 엔진을 벗어나지 않고 엔드투엔드 임베딩 파이프라인을 형성합니다.

## 전체 워크플로우

```sql
-- 1단계: 임베딩 공급자를 한 번 등록
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- 2단계: T-SQL에서 인라인으로 임베딩 생성
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- 3단계: 벡터 거리로 검색
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

이것이 전체 파이프라인입니다: SQL의 데이터, SQL에서 생성된 임베딩, SQL에서의 유사성 검색. 오케스트레이션 레이어 없음, ETL 없음, 별도의 벡터 데이터베이스 없음.

## 지원되는 API 형식과 옵션

GA에서 `API_FORMAT`은 **Azure OpenAI**와 **OpenAI**를 지원합니다. `MODEL_TYPE`은 현재 `EMBEDDINGS`로 고정되어 있습니다. `PARAMETERS` JSON을 통해 재시도 횟수를 포함한 모델 수준의 기본값을 설정할 수 있습니다:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

인증은 데이터베이스 자격 증명을 사용하므로 비밀은 애플리케이션 코드 외부에 보관됩니다.

## .NET 애플리케이션에서 무엇이 가능해지는가

기존 SQL 데이터 위에 AI 기능을 구축하는 .NET 개발자에게 이것은 중요합니다. 다음이 필요하지 않습니다:

- 임베딩을 위해 중간 저장소로 데이터 추출
- 외부 임베딩 파이프라인 관리
- 별도의 벡터 데이터베이스 설정 (완전한 기능의 벡터 저장소가 필요하면 Azure AI Search를 사용할 수 있지만)
- 애플리케이션의 데이터 액세스 레이어 변경

이미 보유한 동일한 T-SQL 도구를 사용하여 기존 SQL 애플리케이션에 의미 검색을 점진적으로 추가할 수 있습니다.

## 마무리

SQL 데이터에 대한 RAG 패턴이 극적으로 단순해졌습니다. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL`은 기존 SQL 애플리케이션이 새로운 인프라를 추가하지 않고도 벡터 검색 기능을 얻을 수 있음을 의미합니다.

두 기능 모두 오늘 Azure SQL Database와 Azure SQL Managed Instance에서 GA입니다.

원본 게시물: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
