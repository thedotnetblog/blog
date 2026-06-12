---
title: "FIDES는 내가 더 많이 보고 싶은 결정론적 에이전트 보안 이야기다"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Agent Framework의 새로운 FIDES 기능은 prompt injection 방어를 휴리스틱에서 벗어나, 레이블이 붙은 콘텐츠와 middleware 검사를 기반으로 한 실행 가능한 정책 쪽으로 옮긴다는 점에서 중요하다."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "index.md" >}})를 클릭하세요.*

prompt injection 방어는 종종 불안정한 땅 위에 서 있는 것처럼 느껴진다.

더 강한 system prompt를 추가한다. 필터를 추가한다. 몇 개의 allowlist를 만든다. 그리고 다음 이상한 입력이 가정을 깨지 않기를 바란다.

그래서 **FIDES**가 흥미롭다.

이 이야기의 강점은 보안을 더 결정론적인 무언가로 옮긴다는 점이다.

- 콘텐츠에 대한 레이블
- workflow 전반으로 레이블이 전달됨
- 권한이 있는 도구가 실행되기 전 middleware를 통한 enforcement
- 신뢰할 수 없는 context가 무엇에 영향을 줄 수 있는지에 대한 명확한 policy 경계

## 원문은 적절하게 직설적이다

시작부터 prompt injection이 "**OWASP LLM Top 10의 1위 위험**"이라고 말한다.

좋다.

여기서 이런 직설적인 표현이 마음에 든다. 너무 많은 팀이 agent security를 지금 당장의 runtime design 문제가 아니라 미래의 걱정거리처럼 다루고 있기 때문이다.

그리고 글은 이를 실용적인 대비로 이어 간다. 현재의 방어 대부분은 heuristic이지만, FIDES는 시스템을 policy와 enforcement 쪽으로 움직이려 한다.

그것이 정확히 올바른 변화다.

## 다른 security whitepaper보다 설득력 있는 이유

AI security에 대한 많은 글은 추상적인 수준에 머문다.

이 글은 더 나은 일을 한다. GitHub issue triage agent, 악의적인 issue 본문, 권한이 있는 파일 읽기, 공개 comment 유출 시도라는 아주 구체적인 예를 따라간다.

이것은 논의를 실제 workflow에 묶어 주기 때문에 유용하다.

그리고 그 시나리오를 보면 결정론적 제어의 가치를 훨씬 더 쉽게 이해할 수 있다.

## 핵심은 "모델을 더 똑똑하게 만들어라"가 아니다

여기서 가장 중요한 점은 FIDES가 모델에게 공격을 마법처럼 더 잘 알아내라고 요구하지 않는다는 것이다.

대신 runtime contract를 바꾸고 있다.

즉:

- 콘텐츠에 레이블을 붙인다
- 레이블이 전달된다
- 도구는 자신이 받는 것을 선언한다
- middleware가 실행 전에 안전하지 않은 경로를 막는다

이것은 훨씬 더 건강한 접근이다.

왜냐하면 agent가 실제 결과를 만들어내는 도구를 호출할 수 있게 되면, 보안은 모델의 컨디션이 좋은지 아닌지에만 의존할 수 없기 때문이다.

## 내 생각

이것이 내가 더 많이 보고 싶은 agent security의 방향이다.

"모델이 나쁜 지시를 무시할 거라고 믿자"가 아니라, "policy fence를 runtime 안에 만들어 넣자"는 것이다.

이쪽이 훨씬 더 건강한 모델이다.

그리고 agent framework가 production에서 진지하게 받아들여지려면, 이런 이야기가 더 필요하다.

원문: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)