---
title: "SQL MCP Server를 Azure App Service에서 실행하기 — 컨테이너 불필요"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server가 이제 Docker나 Kubernetes 없이 Azure App Service에서 실행됩니다. SQL 데이터베이스와 통신하는 AI 에이전트를 구축하는 .NET 개발자에게 무엇을 의미하는지 살펴봅니다."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기]({{< ref "index.md" >}})를 클릭하세요.*

솔직히 말하면, 튜토리얼에서 "컨테이너 필요"라는 말을 볼 때마다 속으로 한숨이 나옵니다. 컨테이너는 훌륭하지만, 팀에 컨테이너 전략이 없으면 단순해 보이는 기능이 예상치 못한 오케스트레이션 복잡성에 막히게 됩니다.

그래서 이것이 눈에 띄었습니다. SQL MCP Server가 이제 Azure App Service에서 실행될 수 있습니다 — Docker도, Kubernetes도 없이, MCP, REST, GraphQL을 통해 SQL 데이터베이스를 공개하는 동일한 Data API Builder(DAB) 구성 파일만으로 동작합니다.

## SQL MCP Server란?

아직 모르신다면 간단히 설명드립니다. SQL MCP Server는 AI 에이전트와 SQL 데이터베이스 사이에 위치합니다. 에이전트에게 직접적인 데이터베이스 접근 권한을 주는 것(끔찍한 아이디어) 대신, 테이블과 뷰를 정의된 권한이 있는 엔티티 추상화 레이어로 공개합니다.

[Data API Builder](https://learn.microsoft.com/ko-kr/azure/data-api-builder/) 위에 구축되어 있어, 단일 구성 파일이 MCP *와* REST *와* GraphQL을 동시에 관리합니다. 에이전트는 MCP 엔드포인트와 통신하고, 기존 애플리케이션은 REST 또는 GraphQL과 통신합니다. 동일한 설정, 동일한 런타임, 다른 인터페이스.

이것은 정말 유용합니다. 두 개의 별도 API 레이어를 관리할 필요가 없습니다.

## 컨테이너 문제 (및 해결책)

SQL MCP Server의 원래 배포 모델은 컨테이너였습니다. 많은 팀에서는 잘 작동하지만, 모든 팀에 해당하지는 않습니다. 많은 .NET 팀이 Azure App Service나 VM을 표준으로 사용합니다. SQL 엔드포인트 하나를 공개하기 위해 컨테이너 런타임이 필요하다는 것은 불필요한 마찰을 만듭니다.

새로운 연습 가이드는 컨테이너를 완전히 건너뛰는 방법을 보여줍니다. 모든 것이 `dab start` 명령으로 실행되며, 표준 .NET 8 웹 프로세스로 App Service에 호스팅됩니다.

```bash
# Data API Builder 설치
dotnet tool install microsoft.dataapibuilder --prerelease -g

# 구성 초기화
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# 엔티티 추가
dab add products --source dbo.products --permissions "authenticated:*"

# App Service 인증 공급자 구성
dab configure --runtime.host.authentication.provider AppService

# 서버 시작
dab start
```

이 시점에서 `/mcp`에 MCP, 동일한 프로세스에서 REST와 GraphQL을 사용할 수 있으며, 컨테이너에서 실행되는 것은 아무것도 없습니다.

## 공유 API 키 없는 인증

제가 가장 좋아하는 부분입니다. App Service에 배포할 때 Microsoft Entra ID를 인증 공급자로 구성합니다. 구성 파일에 공유 비밀이 없고, API 키를 교체할 필요도 없습니다.

연결 문자열은 App Service 환경 변수에 보관되며(`dab-config.json`에는 없음), MCP 엔드포인트는 플랫폼 인증으로 보호됩니다. Azure 워크로드에서 이미 Entra ID를 사용하고 있다면 자연스럽게 통합됩니다.

로컬 개발 시에는 `Simulator` 모드와 STDIO 전송으로 전환합니다. 배포 전에 `AppService` 모드로 돌아옵니다. 깔끔하고 명확합니다.

## App Service에 배포

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

그런 다음 팀이 이미 사용하는 코드 배포 방법으로 DAB 프로젝트를 배포합니다. 핵심 사항: **코드** 배포이지, 컨테이너 배포가 아닙니다.

## .NET 개발자에게 중요한 이유

.NET에서 AI 에이전트를 구축하고 있다면, 에이전트는 결국 데이터베이스와 통신해야 합니다. SQL MCP Server는 원시 연결 문자열을 노출하거나 커스텀 API 레이어를 작성하지 않고도 이를 수행하는 구조화된 방법을 제공합니다.

[원본 블로그 게시물](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/)과 [GitHub 샘플 저장소](https://github.com/Azure-Samples/SQL-MCP-NoContainer)에서 전체 가이드를 확인하세요.

## 마무리

App Service의 SQL MCP Server는 컨테이너 전략 없이 에이전트에게 구조화된 SQL 데이터 접근을 제공하려는 .NET 팀에게 실용적인 선택입니다. 직접 사용해 보세요 — 에이전트가 깔끔한 API 인터페이스를 좋아할 것입니다.
