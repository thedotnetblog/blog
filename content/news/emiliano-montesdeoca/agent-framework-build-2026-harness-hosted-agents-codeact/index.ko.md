---
title: "Agent Harness, Hosted Agents, CodeAct: 내가 주목할 Agent Framework 업데이트는 이것이다"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Build 2026의 Agent Framework 발표는 내용이 많지만, 가장 중요한 축은 harness 모델, Foundry hosted agents, 그리고 orchestration 오버헤드를 줄이는 CodeAct다."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Build에서 나온 Agent Framework의 큰 발표는 많은 내용을 담고 있지만, 내 눈에는 세 가지가 바로 들어온다:

- **harness가 runtime 이야기에서 더 1급 시민이 되어 가는 것**
- **Foundry hosted agents가 production으로 가는 경로를 제공하는 것**
- **CodeAct가 여러 단계의 orchestration 오버헤드를 줄이는 것**

나는 이 부분들을 계속 지켜볼 것이다.

## harness가 진짜 중심축이 되고 있다

원문에서는 harness를 모델 추론과 실제 실행이 만나는 계층이라고 설명한다.

그 설명은 정확하고, 그래서 이 부분이 많은 개별 기능 항목보다 더 중요하다고 생각한다.

agent가 다음을 필요로 하는 순간:

- 파일 접근
- 셸 실행
- 계획 모드
- 할 일 목록
- 세션 메모리
- 승인 워크플로

이제는 prompt와 model만 이야기하는 것이 아니다.

런타임 동작을 이야기하는 것이다.

프레임워크가 유용해지느냐, 아니면 장난감에 머무르느냐는 바로 그 지점에서 갈린다.

그리고 Microsoft Agent Framework는 분명히 그 계층을 더 유용하게 만들려고 하고 있다.

## Hosted agents는 로컬에서 프로덕션으로 가는 이야기를 현실로 만드는 지점이다

나도 hosted agents 부분이 이번 발표에서 전략적으로 가장 중요한 축 중 하나라고 생각한다.

원문도 이 기능이 그 agent에게 production home을 주는 가장 쉬운 방법이라고 분명히 말한다.

대부분의 agent framework가 여전히 운영 배포보다 로컬 실험에 훨씬 강하기 때문에, 이 표현이 중요하다.

Foundry hosted agents가 로컬 개발에서 다음 단계로 옮겨 가는 일을 훨씬 쉽게 만든다면:

- 스케일링
- 관찰 가능성
- 관리형 ID
- 세션 처리
- 버전 관리

현재 agent 생태계의 가장 큰 gaps 중 하나를 메우게 된다.

그건 의미 있는 개선이다.

## CodeAct는 이번 업데이트에서 가장 흥미로운 기술 아이디어다

내가 이 게시물에서 가장 흥미로운 기술 개념을 고르라면, 아마 CodeAct를 고를 것이다.

이게 해결하려는 문제는 매우 현실적이다. 너무 많은 다단계 agent 워크플로는 orchestration 루프 자체가 너무 많은 model turn을 소모해서 비싸진다.

그래서 원문에 이런 결과가 나오면:

- 52.4% faster
- 63.9% fewer tokens

바로 눈에 들어온다.

물론 이것은 대표적인 작업 부하에 묶인 benchmark 수치이지, 보편적인 법칙은 아니다. 그래도 더 큰 아이디어는 여전히 꽤 설득력 있다.

모델이 tool-calling 체인을 더 효율적인 실행 형태로 압축할 수 있다면, agent 시스템의 경제성이 꽤 달라질 수 있다.

## 개발자가 이 업데이트에서 실제로 받아들여야 할 것

중요한 교훈은 기능이 얼마나 나왔는지가 아니다.

중요한 건 framework가 실제 애플리케이션이 가장 필요로 하는 지점에서 강해지고 있다는 점이다:

- runtime shell
- 배포 경로
- 실행 효율
- 내장된 운영 패턴

이런 성숙도 신호는, 또 하나의 얕은 AI 기능 목록보다 훨씬 중요하다.

## 내 생각

이 업데이트가 중요한 이유는 단순히 표면적 기능을 더한 것이 아니기 때문이다.

실제 애플리케이션이 필요로 하는 지점, 특히 로컬 실험에서 실제로 운영하고 유지할 수 있는 시스템으로 옮기려는 팀에 중요한 지점에서 agent를 둘러싼 runtime과 deployment 이야기를 강화하고 있다.

그 지점에서 framework가 더 설득력 있어진다.

이 릴리스를 자세히 따라간다면, harness, hosted agents, CodeAct가 내가 가장 주목할 부분일 것이다.

원문: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
