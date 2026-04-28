---
title: "Agent Framework의 CodeAct: 에이전트 지연 시간을 절반으로 줄이는 방법"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct는 다단계 도구 체인을 단일 샌드박스 코드 블록으로 압축합니다 — 지연 시간 52% 감소, 토큰 사용량 64% 감소. 에이전트에 미치는 영향과 사용 시기를 알아보세요."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭]({{< ref "index.md" >}})하세요.*

모든 에이전트 프로젝트에서 트레이스를 보며 "왜 이렇게 오래 걸리는 거야?"라고 생각하는 순간이 있습니다. 모델은 괜찮고, 도구도 작동합니다. 하지만 한 번에 계산할 수 있는 결과를 위해 일곱 번의 왕복이 발생합니다.

이것이 바로 CodeAct가 해결하는 문제입니다. [Agent Framework 팀이 새 `agent-framework-hyperlight` 패키지를 통해 알파 지원을 출시](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)했습니다.

## CodeAct란?

[CodeAct 패턴](https://arxiv.org/abs/2402.01030)은 우아하게 단순합니다. 모델에 도구 목록을 주고 하나씩 호출하게 하는 대신, 단일 `execute_code` 도구를 주고 *전체 계획*을 짧은 Python 프로그램으로 표현하게 합니다.

| 방식 | 시간 | 토큰 |
|--------|------|--------|
| 기존 방식 | 27.81초 | 6,890 |
| CodeAct | 13.23초 | 2,489 |
| **개선** | **52.4%** | **63.9%** |

## 보안: Hyperlight 마이크로 VM

`agent-framework-hyperlight` 패키지는 [Hyperlight](https://github.com/hyperlight-dev/hyperlight) 마이크로 VM을 사용합니다. 각 `execute_code` 호출은 자체 새로운 마이크로 VM을 받습니다. 시작 시간은 밀리초 단위입니다. 격리는 사실상 무료입니다.

도구는 계속 호스트에서 실행됩니다. 모델이 생성한 *글루 코드*는 샌드박스에서 실행됩니다. 올바른 분리입니다.

## 최소 설정

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## CodeAct 사용 시기 (그리고 사용하지 않을 때)

**CodeAct를 사용하는 경우:**
- 많은 소규모 도구 호출을 연결하는 작업 (조회, 조인, 계산)
- 지연 시간과 토큰 비용이 중요한 경우
- 모델 생성 코드에 강력한 격리가 필요한 경우

**기존 도구 호출을 사용하는 경우:**
- 에이전트가 턴당 한두 번만 도구를 호출하는 경우
- 각 호출에 개별 승인이 필요한 부작용이 있는 경우
- 도구 설명이 부족하거나 모호한 경우

## 지금 시도해보세요

```bash
pip install agent-framework-hyperlight --pre
```

[Agent Framework 블로그의 전체 게시물](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)에서 심층적인 내용을 확인하세요.
