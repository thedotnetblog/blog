---
title: ".NET Aspire 13.2는 AI 에이전트의 가장 친한 친구가 되고 싶어한다"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2가 에이전틱 개발에 올인합니다 — 구조화된 CLI 출력, 격리된 실행, 자동 복구 환경, 그리고 완전한 OpenTelemetry 데이터로 AI 에이전트가 실제로 앱을 빌드, 실행, 관찰할 수 있게 합니다."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "aspire-agentic-development-build-run-observe" >}})에서 확인하세요.*

AI 코딩 에이전트가 꽤 괜찮은 코드를 작성해서 기대했는데, 그것을 실제로 *실행*하려고 하면 전부 무너지는 그 순간 아시죠? 포트 충돌, 고스트 프로세스, 잘못된 환경 변수 — 갑자기 에이전트가 기능을 만드는 대신 시작 문제를 디버깅하느라 토큰을 소모합니다.

Aspire 팀이 바로 이 문제에 대한 [정말 사려 깊은 글](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/)을 발표했고, 그들의 답은 설득력이 있습니다: Aspire 13.2는 인간만을 위한 것이 아니라 AI 에이전트를 위해서도 설계되었습니다.

## 문제는 현실입니다

AI 에이전트는 코드 작성에 놀라운 능력을 보여줍니다. 하지만 작동하는 풀스택 앱을 배포하려면 파일 생성 이상의 것이 필요합니다. 서비스를 올바른 순서로 시작하고, 포트를 관리하고, 환경 변수를 설정하고, 데이터베이스를 연결하고, 문제가 생겼을 때 피드백을 받아야 합니다. 현재 대부분의 에이전트는 이 모든 것을 시행착오로 처리합니다 — 명령 실행, 에러 출력 읽기, 재시도.

Markdown 지침, 커스텀 스킬, 프롬프트를 쌓아올려 가이드하려 하지만, 이것들은 예측 불가능하고 컴파일할 수 없으며 파싱하는 것만으로도 토큰이 듭니다. Aspire 팀은 핵심 인사이트를 정확히 짚었습니다: 에이전트에게 필요한 것은 **컴파일러와 구조화된 API**이지, 더 많은 Markdown이 아닙니다.

## 에이전트 인프라로서의 Aspire

Aspire 13.2가 에이전틱 개발 테이블에 가져오는 것들:

**전체 스택을 타입이 있는 코드로.** AppHost가 앱의 전체 토폴로지 — API, 프론트엔드, 데이터베이스, 캐시 — 를 컴파일 가능한 TypeScript 또는 C#로 정의합니다:

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

에이전트는 이것을 읽어 앱 토폴로지를 이해하고, 리소스를 추가하고, 연결을 설정하고, *검증을 위해 빌드*할 수 있습니다. 컴파일러가 뭔가 잘못되면 즉시 알려줍니다. 추측 불필요, 설정 파일에 대한 시행착오 불필요.

**하나의 명령으로 모두 지배.** 에이전트가 `docker compose up`, `npm run dev`, 데이터베이스 시작 스크립트를 저글링하는 대신, 모든 것이 `aspire start` 하나입니다. 모든 리소스가 올바른 순서로, 올바른 포트에, 올바른 설정으로 시작됩니다. 장시간 실행 프로세스도 에이전트를 멈추지 않습니다 — Aspire가 관리합니다.

**병렬 에이전트를 위한 격리 모드.** `--isolated`를 사용하면 각 Aspire 실행이 자체 랜덤 포트와 별도의 사용자 시크릿을 갖습니다. 여러 에이전트가 git worktree에서 작업 중인가요? 충돌하지 않습니다. 이것은 VS Code의 백그라운드 에이전트처럼 병렬 환경을 생성하는 도구에 매우 중요합니다.

**텔레메트리를 통한 에이전트의 눈.** 여기서 정말 강력해집니다. Aspire CLI는 개발 중 완전한 OpenTelemetry 데이터를 노출합니다 — 트레이스, 메트릭, 구조화된 로그. 에이전트가 콘솔 출력을 읽고 최선을 바라는 것이 아닙니다. 서비스 간 실패한 요청을 추적하고, 느린 엔드포인트를 프로파일링하고, 정확히 어디서 문제가 발생하는지 파악할 수 있습니다. 개발 루프에 프로덕션급 관찰 가능성이 있는 것입니다.

## 볼링 범퍼 비유

Aspire 팀은 훌륭한 비유를 사용합니다: Aspire를 AI 에이전트를 위한 볼링 레인 범퍼라고 생각하세요. 에이전트가 완벽하지 않다면 (그리고 완벽하지 않을 것입니다), 범퍼가 거터볼을 치지 않도록 막아줍니다. 스택 정의가 잘못된 구성을 방지하고, 컴파일러가 오류를 잡고, CLI가 프로세스 관리를 담당하고, 텔레메트리가 피드백 루프를 제공합니다.

이것을 Playwright CLI 같은 것과 결합하면, 에이전트가 실제로 앱을 *사용*할 수 있습니다 — 플로우를 클릭하고, DOM을 확인하고, 텔레메트리에서 깨진 것을 보고, 코드를 수정하고, 재시작하고, 다시 테스트합니다. 빌드, 실행, 관찰, 수정. 이것이 우리가 추구해온 자율 개발 루프입니다.

## 시작하기

Aspire가 처음이세요? [get.aspire.dev](https://get.aspire.dev)에서 CLI를 설치하고 [시작 가이드](https://aspire.dev/get-started/first-app)를 따르세요.

이미 Aspire를 사용 중이세요? `aspire update --self`를 실행하여 13.2를 받고, 좋아하는 코딩 에이전트를 레포에 연결하세요. Aspire의 가드레일이 있으면 에이전트가 얼마나 더 멀리까지 갈 수 있는지 놀라실 수 있습니다.

## 마무리

Aspire 13.2는 더 이상 단순한 분산 앱 프레임워크가 아닙니다 — 필수적인 에이전트 인프라가 되고 있습니다. 구조화된 스택 정의, 원커맨드 시작, 격리된 병렬 실행, 실시간 텔레메트리가 AI 에이전트에게 코드 작성에서 앱 배포로 넘어가는 데 필요한 모든 것을 제공합니다.

Aspire 팀의 [전체 포스트](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/)에서 모든 세부사항과 데모 비디오를 확인하세요.
