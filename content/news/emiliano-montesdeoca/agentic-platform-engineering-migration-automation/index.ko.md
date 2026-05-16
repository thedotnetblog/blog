---
title: "Agentic Platform Engineering으로 마이그레이션의 반복 작업 제거하기"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape가 실제 AWS Terraform 배포를 Azure Bicep으로 마이그레이션하는 과정을 안내합니다 — 1:1 구문 변환이 아닌 배포 의도를 추출하고 아키텍처를 재매핑합니다."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — Git-Ape(git 에이전틱 플랫폼 엔지니어링 도구)가 실제 AWS Terraform 리포지토리를 Azure로 마이그레이션하는 과정을 보여주며, 줄 단위 변환이 아닌 배포 의도 추출에 초점을 맞춥니다.

## 입력: contoso-migration

소스는 AWS에서 Next.js 앱을 배포하는 실제 Terraform 프로젝트(`contoso-migration`)입니다 — 컴퓨팅에 EC2, 로드 밸런싱에 ALB, 아티팩트에 S3, 아이덴티티에 IAM 키. 비용: 월 ~$34. 목표는 Azure에서 동일한 인프라를 재현하는 것이 아닙니다. 배포가 실제로 무엇을 하려는지 파악하고 Azure 네이티브 서비스로 재구축하는 것입니다.

## 1단계: 검증 및 인증

Git-Ape는 무언가를 건드리기 전에 모든 필수 CLI 도구 — `az`, `aws`, `gh`, `jq`, `git` — 를 검증하고 활성 인증 세션을 확인하는 것으로 시작합니다. 부분 실행은 없습니다.

## 2단계: 의도 추출

에이전트는 GitHub API를 통해 전체 소스 리포지토리를 읽고 배포 의도를 추출합니다: 런타임(Node.js), 컴퓨팅 유형, 인그레스 패턴, 아티팩트 처리, 아이덴티티 모델, 네트워킹, 모니터링. 이것이 핵심 단계입니다 — Terraform 키워드가 아니라 배포가 무엇을 하는지의 시맨틱 모델을 구축합니다.

## 3단계: 서비스 매핑

AWS 서비스가 Azure 동등물로 매핑됩니다:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → App Service 내장 로드 밸런싱
- IAM 역할/키 → Managed Identity
- Terraform → Bicep + GitHub Actions

## 4단계: 비평 에이전트

출력을 생성하기 전에 비평 에이전트가 실행되어 두 가지 차단 문제를 발견합니다:

1. **시작 시 빌드 안티패턴** — 원래 Terraform이 EC2 시작 시 `npm install && npm run build`를 실행하고 있었습니다. 수정: CI에서 빌드하고 준비된 아티팩트를 배포합니다.
2. **불필요한 Blob Storage** — S3가 적절한 CI/CD로 제거할 수 있는 아티팩트 스테이징에 사용되었습니다. 비평 에이전트가 이를 완전히 제거했습니다.

## 5단계: 생성된 출력

결과는 원래 200줄 이상의 Terraform 대신 약 80줄의 Bicep입니다. 에이전트는 `infra/main.bicep` 및 `.github/workflows/deploy.yml`이 포함된 새 GitHub 리포지토리를 생성하고 모든 AWS 전용 파일을 제거했습니다.

## 보안 태세 비교

마이그레이션은 또한 의미 있는 보안 개선을 가져왔습니다:

| AWS 원본 | Azure 출력 |
|---|---|
| HTTP만 | HTTPS만, TLS 1.2 |
| SSH가 0.0.0.0/0에 열려 있음 | SSH 노출 없음 |
| IAM 액세스 키 | OIDC + Managed Identity |
| 모니터링 없음 | Application Insights |

비용: 원래 $34/월 대비 ~$13/월.

## 구문 변환기와의 차이점

비평 에이전트 단계가 이것을 기계적 번역과 구별시키는 것입니다. AWS에서는 작동하지만 Azure에서는 잘못될 패턴을 발견하고 복제 대신 수정했습니다. 출력은 "Azure 구문의 AWS"가 아닙니다. 동일한 목표를 더 깔끔하게 달성하는 Azure 네이티브 배포입니다.

완전한 에이전트 추적 및 생성된 파일은 [전체 가이드](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/)를 참조하세요.
