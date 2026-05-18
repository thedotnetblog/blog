---
title: "Aspire 13.3: Kubernetes 지원, 브라우저 로그 및 Aspireify 스킬"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "13.2 이후 5주 만에 Aspire 13.3이 45개의 새 기능과 함께 출시됐습니다. 퍼스트클래스 AKS 배포, AI 지원 온보딩 스킬, 브라우저 로그 캡처, 구조화된 명령 결과가 포함됩니다."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

5주는 릴리스로서 긴 시간이 아니지만 Aspire 13.3은 그렇게 느껴지지 않습니다. 주요 항목들은 의미 있습니다: Helm을 사용한 Kubernetes 및 AKS 퍼스트클래스 배포, Aspireify라는 에이전트 지원 온보딩 스킬, 대시보드에서 직접 브라우저 로그 캡처, 구조화된 명령 결과. 여기에 45개의 새 기능, 134개의 개선 사항, 93개의 버그 수정도 포함됩니다.

하이라이트를 살펴보겠습니다.

## Aspireify: 에이전트 지원 온보딩

기존 프로젝트에 Aspire를 추가하는 것은 간단해 보입니다 — AppHost를 추가하면 끝. 실제로는 많은 조사가 필요합니다: 어떤 포트가 중요한지, 어떤 환경 변수가 실제 의존성인지, 어떤 Docker Compose 서비스를 Aspire 통합에 매핑해야 하는지.

새로운 **Aspireify 스킬**은 코딩 에이전트에게 정확히 이를 위한 가이드 워크플로우를 제공합니다. `aspire init`이 스켈레톤 AppHost를 만들 때, Aspireify 스킬은 에이전트가 저장소를 검사하고, 이미 어떻게 작동하는지 이해하고, 앱에 맞게 AppHost를 연결하는 데 도움을 줍니다 — 반대가 아닙니다.

기본 입장은 "코드 변경을 최소화"입니다. 앱이 이미 `DATABASE_URL`을 읽는다면, 에이전트는 구성을 다시 작성하도록 요청하는 대신 `WithEnvironment()`로 매핑합니다. 포트가 하드코딩된 경우 스킬은 에이전트에게 언제 보존해야 하는지 알려줍니다.

이것이 검토할 작업을 더 생성하는 것이 아니라 실제로 시간을 절약하는 AI 툴링의 유형입니다.

## 퍼스트클래스 Kubernetes 및 AKS 배포

이것은 한동안 위시리스트에 있었습니다. Aspire 13.3은 **Helm을 사용한 Kubernetes 및 AKS 퍼스트클래스 배포 지원**을 제공합니다. 이제 Aspire 도구에서 직접 AKS를 배포 대상으로 지정할 수 있습니다.

AKS에서 이미 프로덕션 워크로드를 실행 중인 팀에게 이것은 중요한 격차를 메웁니다. Aspire 앱 모델은 이제 Helm 차트를 수동으로 작성할 필요 없이 로컬 개발에서 Kubernetes로의 깔끔한 경로를 갖게 됩니다.

## 대시보드의 브라우저 로그

이것은 프론트엔드 문제를 디버깅하기 전까지는 작아 보이는 기능 중 하나입니다.

새로운 `WithBrowserLogs()` API는 엔드포인트를 지원하는 모든 리소스에 추적된 브라우저 리소스를 첨부합니다. Aspire는 개인 CDP 파이프를 사용하여 Chromium을 시작하고 콘솔 로그, 네트워크 요청 및 오류를 리소스의 로그 스트림으로 직접 스트리밍합니다:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost도 동일하게 지원합니다:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

콘솔 오류, 실패한 네트워크 요청, 클라이언트 측 예외 — 이미 트레이스와 메트릭을 관찰하고 있는 동일한 대시보드에서 모두 볼 수 있습니다. 기본적인 것들을 위해 브라우저 DevTools로 탭을 전환할 필요가 없습니다.

## 구조화된 명령 결과

리소스 명령이 중요한 업그레이드를 받았습니다. 이전에는 명령이 성공/실패를 반환했습니다. 이제 구조화된 결과를 반환합니다: 모델, 대시보드 UI, CLI 및 MCP 도구를 통해 흐르는 텍스트, JSON 또는 Markdown입니다.

대시보드는 헤더의 새로운 알림 센터로 이 모든 것을 묶습니다. 명령 결과는 Markdown 렌더링과 "응답 보기" 작업이 있는 타임스탬프된 알림으로 나타납니다.

이는 리소스 명령을 진정으로 조합 가능하게 만듭니다. 이제 통합은 단순히 어딘가의 상태를 변경하는 것이 아니라 터널 URL과 같은 의미 있는 출력을 반환하는 명령을 노출할 수 있습니다.

## 결론

Aspire 13.3은 Kubernetes 지원만으로도 업데이트할 가치가 있습니다. 브라우저 로그와 구조화된 명령 결과는 일상적인 개발 워크플로우에서 빠르게 쌓이는 삶의 질 향상 유형입니다.

전체 릴리스 노트: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
