---
title: "Microsoft Agent Framework의 계층형 설계가 실제로 중요한 이유"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework의 새로운 계층형 SDK 설명은 단순한 아키텍처 이야기가 아닙니다. Microsoft가 개발자들에게 단순한 루프에서 프로덕션 수준의 오케스트레이션으로, 모든 것을 다시 만들지 않고도 옮겨 가길 바란다는 뜻을 보여 줍니다."
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "index.md" >}})에서 확인하세요.*

프레임워크 발표는 보통 기능으로 시작합니다.

이번에는 **설계 철학**으로 시작했습니다. 그리고 저는 바로 그 점 때문에 이 글이 중요하다고 생각합니다.

Microsoft Agent Framework가 **agent loops**, **workflows**, **harnesses**를 중심으로 어떻게 구성되는지에 대한 새 설명은 또 다른 기능 목록보다 훨씬 더 많은 신호를 줍니다. 팀이 실제 애플리케이션이 어떻게 성장하기를 기대하는지 보여 주기 때문입니다.

그리고 .NET으로 agent를 만드는 사람에게는 그 부분이 가장 가치 있습니다.

## 대부분의 agent 앱은 첫 번째 아키텍처를 아주 빨리 넘어서게 된다

모델 호출부터 시작합니다.

그다음 도구를 추가합니다.

그다음 메모리.

그다음 플래너.

그다음에는 재시도, telemetry, 승인, 특화된 agent, 그리고 워크플로 로직까지 필요해집니다. 한 번의 loop만으로는 더 이상 충분하지 않기 때문입니다.

여기서 많은 AI 앱이 지저분해집니다. 첫 버전은 잘 동작했지만, 새 기능이 추가될 때마다 서로 다른 추상화 계층에서 덧붙여졌기 때문입니다.

Agent Framework 설명에서 마음에 드는 점은 계층을 명시적으로 보여 준다는 것입니다:

- **loops** 는 핵심 실행 사이클
- **workflows** 는 구조화된 오케스트레이션
- **harnesses** 는 agent 주변에서 재사용할 수 있는 runtime 기능

처음엔 다소 학술적으로 들릴 수 있지만, 실제로는 아주 실용적인 문제를 해결합니다. **앱이 더 복잡해질 때마다 마음속 모델을 다시 쓰지 않고도 진화시킬 수 있기 때문입니다**.

## harness 개념은 특히 중요하다

앞으로 더 중요해질 부분을 하나 고르라면, 저는 **harness**라는 아이디어를 꼽겠습니다.

harness는 agent 개발이 prompt 작성이 아니라 engineering이 되는 지점입니다.

여기서부터는 다음을 신경 쓰게 됩니다:

- tools와 middleware
- planning 동작
- memory 통합
- observability
- controls와 governance
- 반복 가능한 runtime 동작

이것이 Microsoft 스택의 나머지 부분과도 잘 맞아떨어지는 이유입니다. Foundry, governance 도구, hosted agents, 평가, 그리고 tool 생태계는 모델 주변의 runtime shell을 일급 요소로 다룰 때 훨씬 더 자연스러워집니다.

## .NET 개발자에게는 좋은 신호다

이런 생태계에서 제가 항상 보는 것은 첫 데모 이후에도 framework가 여전히 쓰기 편한지 여부입니다.

계층형 접근은 Microsoft가 전체 경로를 생각하고 있음을 보여 줍니다:

1. 단순한 agent loop를 만든다
2. 혼란 없이 구조화된 기능을 추가한다
3. 앱이 필요로 할 때 더 공식적인 workflows로 옮긴다
4. enterprise 시스템과 통합할 수 있을 만큼 runtime을 조합 가능하게 유지한다

그것은 `여기 거대한 단일 추상화가 있습니다, 행운을 빕니다`보다 훨씬 건강한 성장 경로입니다.

그리고 그것은 .NET 개발자들이 보통 일하는 방식과도 잘 맞습니다. 계층화된 시스템, 명시적 composition, 테스트 가능한 경계, 강력한 runtime 제어 말입니다.

## 내 생각

이 글은 화려한 스크린샷도, 거대한 API 덤프도 없어서 쉽게 과소평가됩니다.

하지만 이런 아키텍처 노트는 framework가 6개월 뒤에도 버틸지 예측하는 데 훨씬 좋은 संकेत입니다.

Microsoft Agent Framework는 분명 model call을 감싼 장난감 수준의 래퍼가 되려는 것이 아닙니다. 계층형 SDK 이야기는 팀이 지저분한 중간 지대, 즉 agent가 orchestration, tools, runtime services, production discipline을 필요로 하는 지점을 위해 만들고 있음을 말해 줍니다.

그곳이 հենց 제가 신경 쓰는 곳입니다.

원문: [ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
