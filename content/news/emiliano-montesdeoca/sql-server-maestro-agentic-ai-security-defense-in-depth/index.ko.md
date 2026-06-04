---
title: "MAESTRO, 심층 방어, 그리고 SQL Server가 AI의 보안 경계가 된 이유"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "에이전트 AI는 전통적인 STRIDE 모델이 설계되지 않은 위협을 도입합니다. Microsoft SQL이 MAESTRO 프레임워크에 어떻게 매핑되어 거버넌스된 실행 경계를 제공하는지 살펴봅니다."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

보안 위협 모델은 누가 또는 무엇이 요청을 하는지에 대한 가정 위에 구축됩니다. STRIDE는 정의된 인터페이스를 통해 시스템과 상호작용하는 인간 행위자를 가정합니다. AI 에이전트는 그런 방식으로 작동하지 않습니다.

## STRIDE는 AI 에이전트를 위해 설계되지 않았다

에이전트 시스템은 자율적으로 작동하며, API 호출을 통해 도구를 연결하고, 어떤 데이터를 검색하고 어떤 조치를 취할지 결정하며, 여러 소스(사용자 프롬프트, 도구 결과, 검색된 데이터)에서 지시를 받을 수 있습니다. STRIDE 위협 모델(Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)은 프롬프트 인젝션, 컨텍스트 오염, 도구 남용과 같은 에이전트별 공격 벡터를 적절히 포착하지 못합니다.

Cloud Security Alliance는 AI 에이전트 위험을 위해 특별히 MAESTRO 프레임워크를 발표했습니다.

## MAESTRO 프레임워크

MAESTRO는 에이전트 AI 위험을 7개 레이어로 구성합니다:

1. **Foundation Models** — 기반 LLM과 훈련 취약점
2. **Data Operations** — 데이터 검색, 저장 및 조작
3. **Agent Frameworks** — 에이전트 오케스트레이션 및 조정 미들웨어
4. **Deployment & Infrastructure** — 에이전트가 실행되는 위치와 구성 방법
5. **Evaluation & Observability** — 시간에 따른 에이전트 행동 모니터링
6. **Security & Compliance** — 접근 제어, 감사 및 규제 준수
7. **Agent Ecosystem** — 에이전트가 서로 및 외부 도구와 상호작용하는 방법

각 레이어에는 기존 보안 제어가 직접 해결하지 않는 특정 공격 벡터가 있습니다.

## 거버넌스된 실행 경계로서의 Microsoft SQL

SQL Server 2025는 구체적인 방식으로 MAESTRO 레이어에 매핑됩니다:

**Data Operations 레이어**: T-SQL에 통합된 `AI_GENERATE_EMBEDDINGS`는 벡터 작업을 데이터베이스의 거버넌스된 경계 내에 유지합니다. 임베딩 처리를 위해 데이터가 모델 서비스로 이동할 필요가 없습니다.

**Security & Compliance 레이어**: 행 수준 보안(RLS)과 동적 데이터 마스킹(DDM)은 요청이 어떻게 왔는지에 관계없이 적용됩니다 — 인간 사용자에서든 AI 에이전트에서든. 에이전트는 데이터베이스 자체에 의해 적용되는 제어를 우회할 수 없습니다.

**Agent Frameworks 레이어**: 저장 프로시저가 도구 경계 역할을 합니다. 에이전트에게 임의의 SQL 접근을 부여하는 대신, 허용된 작업을 프로시저로 정의하고 에이전트 도구로 노출합니다. 매개변수화된 쿼리는 실행 수준에서 인젝션을 방지합니다.

**Evaluation & Observability 레이어**: 감사 로깅과 Query Store는 각 에이전트가 실제로 실행한 것을 포착합니다 — 수행하도록 요청된 것만이 아닙니다. 이 추적 가능성은 귀속이 복잡한 에이전트 시스템에서 인시던트 조사에 중요합니다.

## 에이전트 AI를 위한 심층 방어

원칙은 전통적인 보안과 동일합니다: 단일 제어로는 충분하지 않습니다. 변하는 것은 에이전트에게 가장 중요한 제어가 무엇인가입니다:

**폭발 반경 줄이기**: 저장 프로시저를 통한 도구 경계는 침해된 에이전트가 사전 정의된 작업만 실행할 수 있음을 의미합니다. 임의의 쿼리로 전환할 수 없습니다.

**관찰 가능성**: 인시던트 후 "이 에이전트는 정확히 무엇을 했는가?"에 답할 수 있어야 합니다. 데이터베이스 수준의 추적 가능성이 없는 에이전트 AI 시스템에는 애플리케이션 로깅이 커버하지 않는 사각지대가 있습니다.

**제약된 실행**: 매개변수화, RLS 및 DDM은 호출자가 인간인지에 관계없이 보안 자산입니다. 에이전트를 수용하기 위해 약화시키지 마세요.

**책임**: SQL Server 감사 로깅은 누가(어떤 에이전트가, 어떤 자격 증명을 사용하여) 언제 무엇을 실행했는지 기록을 만듭니다. 이것은 에이전트 시스템이 실제 세계에서 결과를 초래하는 행동을 취할 때 중요합니다.

SQL Server 2025는 에이전트 위험을 추상적으로 해결하기 위해 구축된 것이 아니라 관계형 데이터베이스로 구축되었습니다. 하지만 엔터프라이즈 데이터베이스를 신뢰할 수 있게 만드는 거버넌스가 바로 에이전트 실행 경계를 안전하게 만드는 것이기도 합니다.

원본 게시물: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
