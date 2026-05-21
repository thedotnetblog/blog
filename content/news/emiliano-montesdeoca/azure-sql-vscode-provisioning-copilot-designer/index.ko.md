---
title: "VS Code용 MSSQL 확장은 조용히 훨씬 더 큰 플랫폼이 되고 있다"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "최신 MSSQL 확장 업데이트는 Azure SQL provisioning, Copilot 지원 schema design, Data API builder, notebooks를 추가한다. 흥미로운 점은 이제 얼마나 많은 database 작업을 VS Code 안에 둘 수 있느냐이다."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*이 글은 자동 번역되었습니다. 원본 버전은 [여기]({{< ref "index.md" >}})에서 확인하세요.*

VS Code용 MSSQL 확장은 꽤 오랫동안 성장해 왔지만, 이번 최신 업데이트는 그 방향을 훨씬 더 분명하게 만든다.

이제는 단순히 «연결하고 몇 개의 쿼리를 실행하는 도구»가 아니다.

**Azure SQL provisioning**, **Copilot이 지원하는 Schema Designer**, **SQL Notebooks**, **Data API builder**가 한 번에 앞으로 나아가면서, 이 확장은 database-centric development를 위한 훨씬 더 완전한 workspace가 되고 있다.

## 실용적인 핵심은 editor에서 직접 provisioning 할 수 있다는 점이다

원문은 무료 tier를 사용해 «editor에서 직접, 그리고 비용 없이» fully managed cloud database를 만들 수 있다고 말한다.

이건 setup friction이 얼마나 많은지 깨닫기 전까지는 작아 보이는 기능이다.

많은 개발자에게 data-heavy experimentation에서 성가신 부분은 SQL 자체가 아니다. 그건 다음 사이의 environment gap이다:

- 아이디어
- 데이터베이스
- 스키마
- API
- 테스트 가능한 백엔드

이 gap이 하나의 도구 안에서 짧아지면 전체 workflow가 훨씬 더 매력적으로 된다.

## data work를 위한 더 강한 inner loop는 이렇게 생겼다

이번 릴리스에서 마음에 드는 점은 database workflow의 더 많은 부분을 한곳에 두고 있다는 것이다:

- database provisioning
- schema 설계
- 변경 사항 review
- ORM script 생성
- API 노출
- endpoint 테스트
- notebook으로 문서화하고 쿼리

이건 SQL을 stack 안의 분리된 사이드 툴로 보는 것보다 훨씬 더 설득력 있는 이야기다.

## Copilot 지원 schema workflow는 AI value가 진짜 느껴지는 곳이다

schema designer 추가 기능은 특히 흥미로운데, 좋은 균형을 잡고 있는 것처럼 보이기 때문이다.

가치는 «AI가 data model을 설계하고 당신이 blindly trust한다»가 아니다.

가치는 다음과 같다:

- 더 빠른 시작점
- 시각적 review
- 변경 추적
- migration-oriented output
- 명시적인 accept/undo controls

이건 inspection path가 없는 full auto-generation보다 훨씬 건강한 AI workflow다.

그리고 database work에서는 reviewability가 매우 중요하다.

## Data API builder는 조용한 증폭기다

내가 무시하지 않을 또 다른 기능은 Data API builder 통합이다.

같은 environment 안에서 schema에서 다음으로 갈 수 있다면:

- REST
- GraphQL
- MCP endpoints

그것은 backend prototype와 internal tools를 위한 매우 효율적인 경로를 만든다.

이것이 더 깊은 backend engineering을 대체하는 것은 아니다. 하지만 database 아이디어에서 working interface까지 가는 길을 확실히 줄여준다.

## 내 생각

이번 릴리스는 MSSQL 확장을 단순한 add-on보다 VS Code 안의 작은 platform처럼 느껴지게 만든다.

API, data tool, admin tool, SQL-backed prototype을 만드는 개발자에게 이는 의미 있는 변화다.

그리고 Microsoft가 이 loop를 계속 더 조이면, 확장은 지금 많은 사람들이 생각하는 것보다 훨씬 더 전략적으로 유용해질 것이다.

원문: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)