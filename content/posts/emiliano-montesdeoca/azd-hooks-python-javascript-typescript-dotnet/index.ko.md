---
title: "Python, TypeScript, .NET으로 azd 훅 작성하기: 셸 스크립트와의 작별"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI가 이제 Python, JavaScript, TypeScript, .NET으로 훅 작성을 지원합니다. 마이그레이션 스크립트 하나 때문에 Bash로 전환할 필요가 없어집니다."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

완전히 .NET으로 구성된 프로젝트에서 azd 훅을 위해 Bash 스크립트를 작성해야 했던 경험이 있다면, 그 불편함을 잘 알 것이다. 프로젝트의 모든 것이 C#인데, 왜 pre-provisioning 단계 하나 때문에 셸 문법으로 전환해야 하는가.

그 불만이 이제 공식적으로 해결됐다. Azure Developer CLI가 [훅의 멀티 언어 지원을 출시](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)했으며, 기대했던 것만큼 훌륭하다.

## 훅이란

훅은 `azd` 라이프사이클의 핵심 지점에서 실행되는 스크립트다 — 프로비저닝 전, 배포 후 등. `azure.yaml`에 정의되며 CLI를 수정하지 않고 커스텀 로직을 주입할 수 있게 해준다.

기존에는 Bash와 PowerShell만 지원됐다. 이제 **Python, JavaScript, TypeScript 또는 .NET**을 사용할 수 있으며, `azd`가 나머지를 자동으로 처리한다.

## 감지 방식

훅을 파일로 가리키기만 하면 `azd`가 파일 확장자에서 언어를 추론한다:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

추가 설정이 필요 없다. 확장자가 모호한 경우 `kind: python` (또는 해당 언어)을 명시적으로 지정할 수 있다.

## 언어별 주요 세부 사항

### Python

스크립트 옆 (또는 상위 디렉토리)에 `requirements.txt`나 `pyproject.toml`을 놓으면 `azd`가 자동으로 가상 환경을 생성하고 의존성을 설치한 후 스크립트를 실행한다.

### JavaScript와 TypeScript

같은 패턴 — 스크립트 근처에 `package.json`을 두면 `azd`가 먼저 `npm install`을 실행한다. TypeScript의 경우 컴파일 단계나 `tsconfig.json` 없이 `npx tsx`를 사용한다.

### .NET

두 가지 모드 지원:

- **프로젝트 모드**: 스크립트 옆에 `.csproj`가 있으면 `azd`가 자동으로 `dotnet restore`와 `dotnet build`를 실행한다.
- **단일 파일 모드**: .NET 10+에서 독립 `.cs` 파일을 `dotnet run script.cs`로 직접 실행 가능하다. 프로젝트 파일 불필요.

## 실행기별 설정

각 언어는 선택적 `config` 블록을 지원한다:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## .NET 개발자에게 중요한 이유

훅은 azd 기반 프로젝트에서 언어 전환을 강제하는 마지막 장소였다. 이제 앱 코드, 인프라 스크립트, 라이프사이클 훅을 포함한 전체 배포 파이프라인이 하나의 언어로 살 수 있다. 기존 .NET 유틸리티를 훅에서 재사용하고, 공유 라이브러리를 참조하고, 셸 스크립트 유지보수에서 해방될 수 있다.

## 마무리

작은 변화처럼 보이지만 azd 일상 워크플로우에서 많은 마찰을 제거하는 변화 중 하나다. 훅의 멀티 언어 지원은 지금 바로 사용 가능하다 — [공식 게시물](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)에서 전체 문서를 확인해 보자.
