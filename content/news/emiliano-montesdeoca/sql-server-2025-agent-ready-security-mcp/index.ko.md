---
title: "SQL Server 2025: 에이전트 준비 데이터베이스 — 하나의 엔진에서 보안, 백업, MCP"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Polyglot Tax 시리즈의 마지막 편은 어려운 프로덕션 문제를 다룹니다: 관계형, JSON, 그래프, 벡터 데이터 전반에 걸친 통합 Row-Level Security, 그리고 MCP 통합."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*이 게시물은 자동 번역되었습니다. 원본 버전은 [여기를 클릭](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/)하세요.*

Aditya Badramraju의 Polyglot Tax 시리즈를 많은 관심으로 팔로우해왔습니다. 파트 4는 이 아키텍처를 프로덕션에서 신뢰할지 실제로 결정하는 부분으로 시리즈를 마무리합니다.

## 모든 데이터 모델을 위한 단일 보안 모델

하나의 Row-Level Security 정책으로 모든 데이터 모델을 커버. 감사인에게 하나의 정책, 하나의 증명.

## 통합 백업 = 원자적 복구

폴리글롯 스택에서 5개 데이터베이스의 특정 시점 복구를 조율하는 것은 일관성 악몽입니다. 하나의 데이터베이스로는 정의상 원자적입니다.

## MCP 통합: 수동 코딩된 미들웨어 없이

SQL Server 2025는 SQL MCP 서버를 직접 지원합니다. 에이전트가 도구를 호출하면, 엔진이 자동으로 테넌트 격리와 컬럼 마스킹을 강제합니다.

Aditya Badramraju의 원본 포스트: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
