---
title: "OpenEnv와 Foundry는 정적 에이전트를 넘어 대화를 밀어낸다"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "OpenEnv와 Foundry의 새 이야기는 강화 학습의 상투적인 표현을 훨씬 넘어선다. 실제 비즈니스 결과를 기준으로 시간이 지날수록 평가하고 최적화하고 개선할 수 있는 에이전트 시스템을 향한 움직임이기 때문이다."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}})에서 볼 수 있습니다.*

에이전트에 대한 대화는 여전히 추론에서 끝나는 경우가 많습니다.

모델이 프롬프트에 답할 수 있는가? 도구를 호출할 수 있는가? 작업을 한 번이라도 완료할 수 있는가?

새로운 **OpenEnv + Foundry** 이야기가 흥미로운 이유는 대화를 더 야심찬 방향으로 옮기려 하기 때문입니다. **시간이 지날수록 실제로 개선되는 에이전트 시스템을 어떻게 만들 것인가?**

그것은 훨씬 더 좋은 질문입니다.

## 핵심 변화는 응답에서 학습 루프로의 전환이다

Foundry 글은 문제를 environment, evals, rubrics, optimization, post-training을 중심으로 설명합니다.

이를 한 문장으로 요약할 수 있습니다.

**이제 목표는 단순히 에이전트를 실행하는 것이 아니라, 실제 결과를 기준으로 에이전트를 측정하고 개선하는 루프를 갖는 것입니다.**

개발자가 주목해야 할 부분이 바로 이것이라고 생각합니다.

이렇게 보면 지속적인 자산은 model이나 prompt만이 아닙니다. 그 주변의 system입니다.

- 작동하는 environment
- 점수화하는 rubric
- 무슨 일이 있었는지 설명하는 traces
- 구성을 개선하는 optimizer

그것은 훨씬 더 enterprise-ready한 사고 방식입니다.

## RL 연구를 하지 않더라도 이것이 중요한 이유

솔직히 말하면 OpenEnv, post-training, world-modeling 같은 용어는 많은 개발자를 바로 흥미 없게 만들 수 있습니다.

하지만 실제 의미는 용어보다 훨씬 단순합니다.

훈련 루프에 직접 손대지 않더라도, 이 작업은 미래의 에이전트 개발을 위한 플랫폼 스토리를 만듭니다.

- 평가가 first-class가 된다
- 최적화가 가끔이 아니라 지속적으로 이루어진다
- environment가 재사용 가능한 자산이 된다
- 더 나은 에이전트 행동이 "데모에서 더 좋아 보인다"가 아니라 측정 가능한 것이 된다

그것은 큰 도약입니다.

## 내 생각

이 발표에서 가장 똑똑한 부분은 특정 연구 디테일이 아닙니다.

그것은 framing입니다.

Microsoft는 분명히 정적 프롬프트 엔지니어링에서 **outcome-driven 에이전트 시스템**으로 생태계를 옮기려 하고 있습니다. 평가하고, 조정하고, 관리하고, 점진적으로 개선할 수 있는 시스템입니다.

그곳에 진짜 플랫폼 가치가 있습니다.

그리고 지금 에이전트를 만들고 있다면, 애플리케이션 계층이라도 이 흐름이 어디로 가는지 지켜볼 가치가 있습니다.

원문: [결과 주도 학습 시스템: OpenEnv와 Foundry를 활용한 엔터프라이즈 RL](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)