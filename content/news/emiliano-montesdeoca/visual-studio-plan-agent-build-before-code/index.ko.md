---
title: "Visual Studio의 새로운 Plan agent는 매우 실제적인 AI 워크플로 문제를 해결한다"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Visual Studio의 새로운 Plan agent는 구현 전에 구조화된 계획 단계를 만들기 때문에 중요합니다. 이는 큰 기능과 리팩터링에 정확히 필요한 것입니다."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "visual-studio-plan-agent-build-before-code.md" >}})에서 볼 수 있습니다.*

AI 코딩 workflow에서 가장 답답한 것 중 하나는 구현이 너무 빨리 시작될 때입니다.

코드는 기술적으로는 괜찮을 수 있지만, 머릿속에 있던 문제의 잘못된 버전을 해결하고 있을 수 있습니다.

리팩터링을 원했는데 rewrite가 시작됐다.
범위를 좁힌 개선을 원했는데 프로젝트 절반을 건드렸다.
옵션을 같이 이야기하고 싶었는데 바로 file changes로 넘어갔다.

그래서 Visual Studio의 새로운 **Plan agent**가 아주 유용한 추가 기능인 것입니다.

## 이것은 단순한 외형 문제가 아니라 실제 workflow 문제를 해결한다

원문은 아주 익숙한 상황을 이렇게 설명합니다. "**코드가 틀린 건 아니다... 다만 당신이 원한 것이 아닐 뿐이다.**"

이 문장은 정말 정확합니다.

왜냐하면 AI-assisted development의 약점은 model이 code를 만들 수 있느냐가 아니기 때문입니다. 문제는 implementation이 시작되기 전에 작업의 의도한 shape에 대해 합의할 수 있을 만큼 workflow가 충분한 공간을 주느냐입니다.

이것은 특히 다음과 같은 경우에 중요합니다.

- 큰 features
- 익숙하지 않은 codebase
- 단순하지 않은 refactor
- architecture에 민감한 변경
- editing을 시작하기 전에 팀 review가 필요한 작업

이런 상황에서는 바로 implementation으로 들어가는 것이 보통 잘못된 선택입니다.

## task가 진짜라면 planning은 overhead가 아니다

팀이 너무 빨리 implementation을 시작해서 얼마나 많은 시간을 잃는지 종종 과소평가한다고 생각합니다.

agent가:

- 잘못된 file을 건드리고
- 잘못된 approach를 선택하고
- 중요한 constraint를 놓치고
- 필요한 edge case를 무시하면

"빠른" 시작은 결국 전체적으로 더 느린 workflow가 됩니다.

그래서 이 기능이 좋습니다.

이 기능은 다음을 위한 공간을 만듭니다.

- 명확화 질문
- 계획 초안 작성
- 계획을 직접 수정하기
- 코드 변경이 시작되기 전에 계획을 공유하기

그건 bureaucracy가 아닙니다. 보통은 그냥 좋은 engineering입니다.

## markdown plan file은 smart choice다

특히 마음에 드는 점은 모든 plan이 `.copilot/plans/plan-{title}.md`에 저장된다는 것입니다.

이로써 planning 단계가 tangible해집니다.

plan이 chat transcript 안에 갇혀 있지 않습니다. 대신 다음이 가능한 것이 됩니다.

- review
- edit
- mentally version 관리
- 팀과 논의
- 더 의도적으로 implementation에 넘기기

이 덕분에 기능이 단순한 임시 서문이 아니라 훨씬 진지하게 느껴집니다.

## 여기서 AI workflow는 팀 프로세스를 존중하기 시작한다

이것은 이런 도구들이 성숙하고 있다는 강한 신호 중 하나라고 생각합니다.

가장 좋은 AI developer workflow는 중간 단계를 전부 없애는 것이 아닙니다. 올바른 중간 단계를 개선하는 것입니다.

그리고 planning은 그런 단계 중 하나입니다.

plan이 강하면 implementation이 쉬워집니다.
plan이 약하면 implementation이 시끄러워집니다.

이 기능은 그것을 직접 인정합니다.

## 내 생각

이것은 단순한 AI nicety가 아닙니다.

workflow 개선입니다.

그리고 실제 기능과 실제 리팩터링에서, 이것은 불필요한 churn, review noise, 그리고 "그 뜻이 아니었는데"식 rework를 크게 줄여 주는 종류의 개선입니다.

앞으로 더 많은 agent 경험이 이런 종류의 것을 필요로 하게 될 거라고 생각합니다.

Visual Studio는 그것을 유용한 방식으로 더 일찍 해냈습니다.

원문: [빌드하기 전에 계획하기: Visual Studio의 Plan agent 소개](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)