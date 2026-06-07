---
title: "Intelligent Terminal 0.1은 AI-네이티브 셸 경험을 향한 진지한 첫 시도다"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Intelligent Terminal 0.1은 네이티브 agent pane, 오류를 인지하는 지원, 백그라운드 작업, command palette에서 시작되는 agent 흐름을 추가합니다. 아직 실험 단계이지만, 방향성은 매우 매력적입니다."
tags:
  - Terminal
  - AI
  - GitHub Copilot
  - Developer Tools
  - Windows Terminal
---

> *이 글은 자동 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

저는 여전히 터미널이 AI 지원 개발이 실제로 유용해지기에 가장 자연스러운 장소 중 하나라고 생각합니다.

그래서 **Intelligent Terminal 0.1**은 실험 단계임에도 꽤 진지한 발표처럼 느껴집니다.

흥미로운 점은 단순히 "터미널에서 채팅"하는 것이 아닙니다. 다음의 네이티브 통합입니다.

- agent pane
- 오류 감지
- 세션 관리
- 백그라운드 작업
- command palette에서 시작되는 agent 작업

이제는 옆에 덧붙인 부가 기능이 아니라, 진짜 shell 경험처럼 느껴지기 시작합니다.

## 원문은 실제 고통 지점을 이해합니다

원문에서 가장 좋은 부분 중 하나는 추상적인 AI 야망으로 시작하지 않는다는 점입니다.

매우 평범한 개발자 경험에서 시작합니다.

> "**PowerShell 명령을 입력했는데 오류가 나고, 그걸 복사해 브라우저를 열고 붙여넣은 뒤, 여러 포럼 글을 돌아다니며 고쳐본 적이 있나요?**"

이 질문이 먹히는 이유는 너무나 익숙하고 고통스럽기 때문입니다.

터미널에는 이런 작은 중단이 가득합니다.

따라서 AI가 있어야 할 곳이 있다면, 바로 이런 중단들 옆입니다.

## 왜 이게 대부분의 터미널 AI 데모보다 더 강하게 느껴지는가

이것이 흥미로운 이유는 agent가 있기 때문만은 아닙니다.

개발자가 실제로 어떻게 일하는지를 중심으로 터미널 경험을 다시 생각하고 있기 때문입니다.

- 지속되는 agent surface
- shell output에서 오는 context
- 오류가 발생했을 때 빠른 도움
- 백그라운드 작업 시작
- session resumption
- 진입점으로서의 command palette

이건 떠다니는 chatbot이 shell 창에 붙어 있는 것보다 훨씬 더 쓸 수 있는 workflow에 가깝습니다.

## 여기서 진짜 제품은 agent pane입니다

디자인에서 가장 중요한 부분을 하나 고르라면 아마 agent pane일 것입니다.

왜일까요? 두 가지 불편한 모드 사이에 중간 지점을 만들어주기 때문입니다.

- 터미널을 완전히 떠나는 것
- 혹은 모든 상호작용을 inline shell text 안에 밀어 넣는 것

이것은 좋은 설계 선택입니다.

터미널을 작업 공간으로 존중하면서도, agent가 autocomplete 이상의 존재가 되기에 충분한 공간을 줍니다.

## 오류 감지는 가치가 드러나기 시작하는 지점입니다

자동 오류 감지도 여기에서는 정확히 맞는 기능입니다.

터미널은 이미 context를 가지고 있습니다.
오류는 이미 발생했습니다.
그리고 개발자는 아직 flow 안에 있습니다.

이것은 shell을 다음과 같은 일에 가장 좋은 장소 중 하나로 만듭니다.

- 즉각적인 진단
- 수정 제안
- 빠른 반복
- 현재 환경을 떠나지 않는 추가 사고

이건 마법이 아닙니다. workflow를 올바른 곳에 배치하는 것일 뿐입니다.

## 제 생각

아직 초기 단계이지만, 지금까지 본 터미널 AI 방향 중 가장 설득력 있는 것 중 하나입니다.

마법을 약속해서가 아닙니다.
개발자가 이미 shell 안에서 일하는 방식에 가깝게 머무르기 때문입니다.

그리고 이 방향으로 계속 발전한다면, Microsoft 툴링 포트폴리오에서 가장 흥미로운 AI 네이티브 개발 경험 중 하나가 될 수 있다고 생각합니다.

원문: [Announcing Intelligent Terminal 0.1](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)
