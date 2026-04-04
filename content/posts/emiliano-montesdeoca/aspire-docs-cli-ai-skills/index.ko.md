---
title: "Aspire 13.2에 문서 CLI가 탑재 — AI 에이전트도 사용할 수 있습니다"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2에 aspire docs가 추가되었습니다. 터미널을 떠나지 않고 공식 문서를 검색, 탐색, 읽을 수 있는 CLI입니다. AI 에이전트의 도구로도 작동합니다. 이것이 왜 중요한지 알려드립니다."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *이 글은 자동 번역되었습니다. 원문은 [여기를 클릭]({{< ref "aspire-docs-cli-ai-skills.md" >}})하세요.*

Aspire AppHost 깊숙이 들어가서 통합을 연결하는 중에, Redis 통합이 정확히 어떤 파라미터를 기대하는지 확인해야 하는 그 순간을 아시죠? Alt-Tab으로 브라우저로 전환하고, aspire.dev를 뒤지고, API 문서를 눈을 가늘게 뜨고 보다가, 다시 에디터로 돌아옵니다. 컨텍스트를 잃었고, 플로우가 끊겼습니다.

Aspire 13.2가 바로 [그 해결책을 출시했습니다](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). `aspire docs` CLI를 사용하면 터미널에서 직접 Aspire 공식 문서를 검색하고, 탐색하고, 읽을 수 있습니다. 그리고 재사용 가능한 서비스에 기반하고 있어서, AI 에이전트와 스킬이 같은 명령어를 사용해 문서를 조회할 수 있습니다. 존재하지 않는 API를 환각하는 대신에요.

## 이것이 실제로 해결하는 문제

David Pine이 원문에서 정확히 짚었습니다: AI 에이전트는 개발자가 Aspire 앱을 구축하는 것을 돕는 데 *끔찍했습니다*. `aspire run` 대신 `dotnet run`을 추천하고, aspire.dev에 있는 문서에 대해 learn.microsoft.com을 참조하고, 오래된 NuGet 패키지를 제안하고, 그리고 — 개인적으로 가장 좋아하는 — 존재하지 않는 API를 환각했습니다.

왜 그럴까요? Aspire가 폴리글랏이 된 것보다 .NET 전용이었던 기간이 훨씬 길었고, LLM은 최신 기능보다 앞선 학습 데이터로 작동하기 때문입니다. AI 에이전트에게 현재 문서를 실제로 조회할 수 있는 능력을 주면, 추측을 멈추고 유용해지기 시작합니다.

## 세 가지 명령어, 브라우저 탭은 제로

CLI는 상쾌할 정도로 간단합니다:

### 모든 문서 나열

```bash
aspire docs list
```

aspire.dev에서 사용 가능한 모든 문서 페이지를 반환합니다. 기계가 읽을 수 있는 출력이 필요하세요? `--format Json`을 추가하세요.

### 주제 검색

```bash
aspire docs search "redis"
```

가중 관련성 점수로 제목과 콘텐츠 모두를 검색합니다. 내부적으로 문서 도구를 구동하는 것과 같은 검색 엔진입니다. 제목, 슬러그, 관련성 점수가 포함된 순위별 결과를 얻을 수 있습니다.

### 전체 페이지 읽기 (또는 한 섹션만)

```bash
aspire docs get redis-integration
```

전체 페이지를 마크다운으로 터미널에 스트리밍합니다. 한 섹션만 필요하세요?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

외과적 정밀도. 500줄을 스크롤할 필요 없습니다. 필요한 부분만.

## AI 에이전트 관점

AI 도구로 개발하는 우리 개발자들에게 흥미로워지는 부분입니다. 같은 `aspire docs` 명령어가 스킬, MCP 서버, 또는 간단한 CLI 래퍼를 통해 AI 에이전트의 도구로 작동합니다.

AI 어시스턴트가 오래된 학습 데이터를 기반으로 Aspire API를 지어내는 대신, `aspire docs search "postgres"`를 호출하고, 공식 통합 문서를 찾고, 올바른 페이지를 읽고, 문서화된 접근 방식을 제공할 수 있습니다. 실시간이고 최신인 문서 — 모델이 6개월 전에 기억한 것이 아닙니다.

이 뒤의 아키텍처는 의도적입니다. Aspire 팀은 일회성 통합 대신 재사용 가능한 서비스(`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`)를 구축했습니다. 이는 같은 검색 엔진이 터미널의 사람, 에디터의 AI 에이전트, CI 파이프라인의 자동화를 위해 작동한다는 의미입니다.

## 실제 시나리오

**터미널에서 빠른 조회:** 파일 세 개 깊이에 있고 Redis 설정 파라미터가 필요합니다. 두 개의 명령어, 90초, 다시 작업으로:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**AI 지원 개발:** VS Code 스킬이 CLI 명령어를 래핑합니다. "내 AppHost에 PostgreSQL 데이터베이스를 추가해"라고 물으면 에이전트가 답변하기 전에 실제 문서를 조회합니다. 환각 없음.

**CI/CD 검증:** 파이프라인이 공식 문서에 대해 AppHost 설정을 프로그래밍 방식으로 검증합니다. `--format Json` 출력은 `jq` 및 다른 도구와 깔끔하게 연결됩니다.

**커스텀 지식 베이스:** 자체 AI 도구를 구축하고 있나요? 구조화된 JSON 출력을 지식 베이스에 직접 파이프:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

웹 스크래핑 없음. API 키 없음. 문서 도구가 내부적으로 사용하는 것과 같은 구조화된 데이터.

## 문서는 항상 최신 상태

이것이 제가 가장 높이 평가하는 부분입니다. CLI는 스냅샷을 다운로드하지 않습니다 — ETag 기반 캐싱으로 aspire.dev를 조회합니다. 문서가 업데이트되는 순간, CLI와 그 위에 구축된 모든 스킬이 이를 반영합니다. 오래된 복사본도 없고, "하지만 위키에는..."하는 순간도 없습니다.

## 마무리

`aspire docs`는 실제 문제를 깔끔하게 해결하는 작은 기능 중 하나입니다. 사람은 터미널 네이티브 문서 접근을 얻습니다. AI 에이전트는 추측을 멈추고 실제 문서를 참조할 수 있는 방법을 얻습니다. 그리고 모든 것이 같은 진실의 원천에 의해 뒷받침됩니다.

.NET Aspire로 개발하고 있고 아직 CLI를 시도해보지 않았다면, `aspire docs search "여러분의-주제"` 를 실행하고 어떤 느낌인지 확인해 보세요. 그런 다음 사용 중인 AI 스킬이나 자동화 설정에 이 명령어들을 래핑하는 것을 고려해 보세요 — 여러분의 에이전트가 감사할 것입니다.

문서 도구가 어떻게 만들어졌는지에 대한 [David Pine의 심층 분석](https://davidpine.dev/posts/aspire-docs-mcp-tools/)과 모든 세부 사항이 담긴 [공식 CLI 레퍼런스](https://aspire.dev/reference/cli/commands/aspire-docs/)를 확인해 보세요.
