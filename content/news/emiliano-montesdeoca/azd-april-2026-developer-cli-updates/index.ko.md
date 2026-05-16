---
title: "Azure Developer CLI (azd) 2026년 4월 업데이트"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd는 2026년 4월에 5개의 릴리스를 출시했습니다. Python, JavaScript, TypeScript, .NET에 대한 다중 언어 훅 지원, azd update 공개 미리 보기, AI 할당량 프리플라이트 검사 등이 포함되어 있습니다."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd)는 2026년 4월에 5개의 릴리스를 출시했습니다](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14에서 1.24.2). 큰 주제는 Bash와 PowerShell뿐만 아니라 Python, JavaScript, TypeScript, .NET에서도 실행되는 훅입니다.

## azure.yaml의 다중 언어 훅

훅은 이제 셸 스크립트 외에도 `.py`, `.js`, `.ts`, `.cs` 파일을 가리킬 수 있습니다. 각 언어에 대해 자동 종속성 해결이 제공됩니다.

- **Python** — `requirements.txt` 또는 `pyproject.toml`을 감지하고, virtualenv를 생성하며, 실행 전에 종속성을 설치합니다. `virtualEnvName`으로 환경 이름을 구성합니다.
- **JavaScript / TypeScript** — `package.json`을 감지하고 자동으로 `npm install`을 실행합니다. TypeScript는 컴파일 단계 없이 `npx tsx`를 통해 실행됩니다. `packageManager` 구성 블록으로 패키지 관리자를 선택합니다.
- **.NET** — `dotnet run`으로 `.cs` 파일을 실행합니다. .NET 10+에서 단일 파일 스크립트를 지원합니다. `configuration/framework` 블록을 통해 대상 프레임워크를 구성합니다.

이는 이미 이러한 언어 중 하나에서 작업하는 팀이 프로비저닝 수명 주기 이벤트를 연결하기 위해 별도의 Bash 또는 PowerShell 훅을 유지할 필요가 없음을 의미합니다.

## azd update 공개 미리 보기 출시

`azd update`가 이제 모든 플랫폼에서 공개 미리 보기로 제공됩니다. azd가 처음 설치된 방법에 관계없이 단일 명령으로 업데이트를 처리합니다. Homebrew, WinGet, MSI 경로를 개별적으로 추적할 필요가 없습니다.

## AZD_NON_INTERACTIVE를 통한 비대화형 모드

`AZD_NON_INTERACTIVE=true`를 설정하거나 `--non-interactive` / `--no-prompt`를 사용하면 필요한 입력을 자동으로 해결할 수 없을 때 CI/CD 파이프라인에서 일관되고 결정론적인 오류가 발생합니다. 이전에는 명령 간에 동작이 일치하지 않았습니다.

## AI 모델 할당량 프리플라이트 검사

`azd provision`은 AI 모델 리소스를 프로비저닝하기 전에 Azure Cognitive Services 할당량을 검증합니다. 할당량 제한으로 실패할 배포는 이제 프로비저닝 도중이 아니라 프로세스 초기에 오류를 표시합니다.

## Copilot 문제 해결의 "이 오류 수정"

azd Copilot 문제 해결 통합이 제안된 수정 사항을 직접 적용하는 기능을 갖추었습니다. 단순히 설명하는 것이 아니라, 에이전트가 수정 가능한 문제를 식별하면 그 자리에서 변경을 적용할 수 있습니다.

## 사용자 지정 프로비저닝 공급자 및 Key Vault 비밀 확인자

확장 작성자는 이제 `WithProvisioningProvider()`를 사용하여 대체 인프라 백엔드를 등록할 수 있습니다. 별도로, azd는 확장에 구성을 전달하기 전에 `@Microsoft.KeyVault(...)` 참조를 자동으로 해결하여 사용자 지정 공급자에서 수동 비밀 확인이 필요 없어집니다.

## 템플릿 및 감시 모드 제외

두 개의 새로운 ignore 파일이 파일 처리에 대한 세밀한 제어를 제공합니다.
- **`.azdignore`** — 기여자 전용 파일(문서, CI 구성)을 템플릿 복사본에서 제외하여 최종 사용자가 깔끔한 프로젝트 스캐폴드를 얻을 수 있도록 합니다.
- **`.azdxignore`** — `azd x watch` 중 재빌드 트리거에서 디렉터리를 제외하여 반복 개발 중 노이즈를 줄입니다.

## 예약된 이름 프리플라이트 및 docker.network 옵션

azd는 프로비저닝이 시작되기 전에 예측된 리소스 이름에 Azure 예약어(`MICROSOFT`, `WINDOWS`, 또는 `LOGIN` 접두사)가 포함될 경우 경고합니다. 새로운 `docker.network` 옵션은 `docker build`에 `--network`를 전달하며, 특정 Docker 네트워크가 필요한 기업 프록시 환경에서 유용합니다.

## 보안 수정

Windows MSI 패키지에 코드 서명 검증이 포함됩니다. 별도의 수정으로 확장 명령 경계를 넘어 값을 노출할 수 있는 환경 변수 누수가 해결되었습니다.

---

바쁜 달이었습니다. 다중 언어 훅 지원은 특히 주로 Bash로 작업하지 않는 팀의 실질적인 마찰 지점을 없애줍니다. 5개 릴리스 전체의 완전한 변경 내역은 [전체 릴리스 노트](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/)를 참조하세요.
