---
title: "SQL MCP Server — AI 에이전트에게 데이터베이스 접근을 제공하는 올바른 방법"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Data API builder의 SQL MCP Server는 스키마를 노출하거나 NL2SQL에 의존하지 않고 AI 에이전트에게 안전하고 결정론적인 데이터베이스 접근을 제공합니다. RBAC, 캐싱, 다중 데이터베이스 지원 — 모두 기본 제공."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "sql-mcp-server-data-api-builder.md" >}})에서 확인하세요.*

솔직히 말합시다: 오늘날 사용 가능한 대부분의 데이터베이스 MCP 서버는 무섭습니다. 자연어 쿼리를 받아서 즉석에서 SQL을 생성하고 프로덕션 데이터에 대해 실행합니다. 뭐가 잘못될 수 있을까요? (전부요. 전부 잘못될 수 있습니다.)

Azure SQL 팀이 방금 [SQL MCP Server를 발표](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)했는데, 근본적으로 다른 접근 방식을 취합니다. Data API builder(DAB) 2.0의 기능으로 구축되어, AI 에이전트에게 구조화되고 결정론적인 데이터베이스 작업 접근을 제공합니다 — NL2SQL 없이, 스키마 노출 없이, 매 단계마다 완전한 RBAC와 함께.

## 왜 NL2SQL이 아닌가?

이것이 가장 흥미로운 설계 결정입니다. 모델은 결정론적이지 않으며, 복잡한 쿼리가 미묘한 오류를 생성할 가능성이 가장 높습니다. 사용자가 AI가 생성해주길 바라는 바로 그 쿼리가 비결정론적으로 생성될 때 가장 많은 검토가 필요한 쿼리이기도 합니다.

대신, SQL MCP Server는 **NL2DAB** 접근 방식을 사용합니다. 에이전트는 Data API builder의 엔티티 추상화 레이어와 내장 쿼리 빌더로 작업하여 정확하고 잘 형성된 T-SQL을 결정론적으로 생성합니다. 사용자에게는 같은 결과이지만, 환각된 JOIN이나 우발적인 데이터 노출 위험이 없습니다.

## 7개의 도구, 700개가 아닌

SQL MCP Server는 데이터베이스 크기에 관계없이 정확히 7개의 DML 도구를 노출합니다:

- `describe_entities` — 사용 가능한 엔티티 및 작업 발견
- `create_record` — 행 삽입
- `read_records` — 테이블 및 뷰 쿼리
- `update_record` — 행 수정
- `delete_record` — 행 삭제
- `execute_entity` — 저장 프로시저 실행
- `aggregate_records` — 집계 쿼리

이것은 현명합니다. 컨텍스트 윈도우는 에이전트의 사고 공간이기 때문입니다. 수백 개의 도구 정의로 채우면 추론을 위한 공간이 줄어듭니다. 7개의 고정 도구는 에이전트를 *탐색*이 아닌 *사고*에 집중하게 합니다.

각 도구는 개별적으로 활성화하거나 비활성화할 수 있습니다:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## 세 가지 명령으로 시작

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

이것으로 Customers 테이블을 노출하는 SQL MCP Server가 실행됩니다. 엔티티 추상화 레이어는 이름과 열에 별칭을 지정하고, 역할별로 필드를 제한하며, 에이전트가 보는 것을 정확히 제어할 수 있게 합니다 — 내부 스키마 세부 정보를 노출하지 않으면서.

## 보안 이야기는 탄탄합니다

여기서 Data API builder의 성숙도가 빛을 발합니다:

- **모든 계층에서 RBAC** — 각 엔티티가 어떤 역할이 읽기, 생성, 업데이트, 삭제할 수 있는지, 어떤 필드가 표시되는지 정의
- **Azure Key Vault 통합** — 연결 문자열과 비밀을 안전하게 관리
- **Microsoft Entra + 커스텀 OAuth** — 프로덕션 등급 인증
- **Content Security Policy** — 에이전트는 원시 SQL이 아닌 통제된 계약을 통해 상호작용

스키마 추상화는 특히 중요합니다. 내부 테이블 및 열 이름은 에이전트에게 절대 노출되지 않습니다. AI 상호작용에 의미 있는 엔티티, 별칭, 설명을 정의합니다 — 데이터베이스 ERD 다이어그램이 아니라.

## 멀티 데이터베이스 및 멀티 프로토콜

SQL MCP Server는 Microsoft SQL, PostgreSQL, Azure Cosmos DB, MySQL을 지원합니다. DAB의 기능이므로 동일한 구성에서 REST, GraphQL, MCP 엔드포인트를 동시에 얻을 수 있습니다. 동일한 엔티티 정의, 동일한 RBAC 규칙, 동일한 보안 — 세 가지 프로토콜 모두에서.

DAB 2.0의 자동 구성은 빠른 프로토타이핑을 위해 추상화를 줄이고 싶다면 데이터베이스를 검사하고 구성을 동적으로 빌드할 수도 있습니다.

## 제 의견

이것이 AI 에이전트를 위한 엔터프라이즈 데이터베이스 접근이 작동해야 하는 방식입니다. "LLM아, SQL 좀 써줘, 프로덕션에 YOLO 할게"가 아닙니다. 대신: 잘 정의된 엔티티 레이어, 결정론적 쿼리 생성, 매 단계의 RBAC, 캐싱, 모니터링, 텔레메트리. 최고의 의미로 지루합니다.

.NET 개발자에게 통합 이야기는 깔끔합니다 — DAB는 .NET 도구이고, MCP Server는 컨테이너로 실행되며, 대부분이 이미 사용하고 있는 Azure SQL과 함께 작동합니다. 데이터 접근이 필요한 AI 에이전트를 구축한다면 여기서 시작하세요.

## 마무리

SQL MCP Server는 무료, 오픈소스이며 어디서나 실행됩니다. AI 에이전트에게 안전한 데이터베이스 접근을 제공하기 위한 Microsoft의 규범적 접근 방식입니다. 시작하려면 [전체 게시물](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)과 [문서](https://aka.ms/sql/mcp)를 확인하세요.
