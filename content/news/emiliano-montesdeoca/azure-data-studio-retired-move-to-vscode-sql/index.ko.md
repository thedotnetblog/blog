---
title: "Azure Data Studio 은 폐기되었습니다: Azure SQL 워크플로를 VS Code로 이전하세요"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio는 2025년 2월 6일에 폐기되었으며, 지원은 2026년 2월 28일에 종료됩니다. MSSQL 확장을 사용한 VS Code로의 전체 마이그레이션 경로를 소개합니다."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[Azure Data Studio는 2025년 2월 6일에 폐기되었습니다](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/). 지원은 2026년 2월 28일에 종료됩니다. 권장 대체 도구는 MSSQL 확장을 갖춘 VS Code입니다.

## 설치할 항목

시작하기 위한 세 가지:

- **MSSQL 확장** — VS Code Marketplace에서 "SQL Server (mssql)" 검색
- **SQL Database Projects 확장** — 코드로서의 스키마, 빌드 유효성 검사, 안내형 게시
- **.NET 8 SDK** — 빌드 시스템에 필요. SDK 누락은 첫 실행 시 가장 흔한 문제

## ADS 연결 및 설정 마이그레이션

MSSQL 확장에는 **ADS Migration Toolkit**이 포함되어 있어 안내형 흐름으로 일회성 마이그레이션을 처리합니다. 저장된 연결, 연결 그룹, 설정, 키 바인딩이 모두 자동으로 가져와집니다.

## F5 단축키 감각 복구

ADS 사용자는 쿼리 실행을 위해 F5에 의존합니다. **MSSQL Database Management Keymap** 확장을 설치하면 F5를 포함한 ADS 스타일 키 바인딩을 복구할 수 있습니다.

## SQL Database Projects: 코드로서의 스키마

프로젝트를 마우스 오른쪽 버튼으로 클릭 → **게시** → 대상 구성 → 생성된 T-SQL 스크립트 검토 → 배포. 배포 전 스크립트 미리 보기가 핵심 안전 기능입니다. 항목 템플릿은 테이블, 저장 프로시저, 뷰에 대한 스텁을 생성합니다. SSDT와 동일한 워크플로입니다.

자주 발생하는 문제: `.sqlproj` 파일의 **대상 플랫폼 불일치**는 프로젝트가 다른 SQL Server 버전에 대해 생성된 경우 빌드 오류를 유발합니다.

## Schema Compare 및 Schema Designer

확장에는 **Schema Compare**(프로젝트와 배포된 데이터베이스 간의 diff)와 **Schema Designer**(수동 DDL 작성 없이 시각적 스키마 편집)도 포함되어 있습니다.

## Microsoft Fabric 개발자

설정은 동일하지만 VS Code에서 열기 전에 **Fabric 포털**에서 시작하여 먼저 데이터베이스를 Git에 연결하세요. Microsoft에는 전용 가이드가 있습니다: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## 마무리

마이그레이션은 수동 재구축이 아닌 일회성 안내형 흐름입니다. 세 가지 도구를 설치하고, ADS Migration Toolkit을 실행하고, 키 바인딩을 복구하면 10분 이내에 정상으로 돌아올 수 있습니다.

단계별 스크린샷과 Fabric 전용 안내는 [전체 기사](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)를 참조하세요.
