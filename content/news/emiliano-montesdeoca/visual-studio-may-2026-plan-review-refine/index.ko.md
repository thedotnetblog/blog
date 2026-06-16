---
title: "Visual Studio의 5월 업데이트는 idea와 change 사이의 더 나은 control에 관한 것이다"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Visual Studio의 5월 업데이트는 Plan agent, 향상된 skill 관리, context window 가시성, 그리고 더 강력한 multi-file diff 경험을 추가합니다. 공통된 주제는 AI-assisted inner loop에 대한 더 나은 control입니다."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}})에서 볼 수 있습니다.*

Visual Studio 5월 업데이트에서 가장 흥미로운 것은 하나의 isolated feature가 아닙니다.

공유된 방향성입니다.

이 릴리스는 다음 사이의 공간을 계속 개선합니다.

- 하나의 idea
- 하나의 plan
- 생성된 change
- review
- 정제된 결과

바로 이것이 AI-assisted development가 trustworthy하게 느껴질지, chaotic하게 느껴질지를 결정하는 부분입니다.

## 기능 목록은 다양하지만 의도는 일관됩니다

종이에 적어 보면 이번 릴리스에는 여러 가지가 들어 있습니다.

- 새로운 Plan agent
- skill management 개선
- context window 가시성
- multi-file summary diff
- Copilot 관련 workflow 정리
- C++ 쪽 MSVC 업데이트

이건 잡다한 모음처럼 보일 수 있습니다.

저는 그렇게 생각하지 않습니다.

핵심 흐름은 꽤 분명합니다. **Visual Studio는 개발자에게 AI-assisted 작업에 대한 더 많은 control을 주면서도 속도는 늦추지 않으려 합니다.**

그게 바로 추구해야 할 올바른 tradeoff입니다.

## Plan agent는 이 릴리스의 철학적 중심입니다

다른 기능들도 중요하지만, 저는 여전히 Plan agent가 이번 업데이트에서 가장 드러내는 부분이라고 생각합니다.

이 기능은 coding agents를 쓰면서 많은 사람이 느꼈던 걸 분명하게 보여 줍니다.

빨리 시작하는 것과 효과적으로 전진하는 것은 같지 않습니다.

이 릴리스는 planning, review, controlled implementation을 더 자연스러운 sequence로 만들어 그 점을 더 강하게 보여 줍니다.

그건 건강합니다.

## multi-file diff 작업은 조용하지만 큰 개선입니다

multi-file summary diff도 아마 받을 평가보다 더 많은 credit을 받아야 한다고 생각합니다.

agents가 한 번에 여러 파일을 바꾸면 review experience가 곧 product가 됩니다.

변경 검토가 지저분하게 느껴지면 developers는 workflow를 덜 신뢰하게 됩니다.

변경 검토가 일관되게 느껴지면 developers는 tool을 계속 사용할 가능성이 더 높아집니다.

그래서 unified summary view가 그렇게 중요합니다. 생성된 작업에 yes 또는 no를 말할 때 드는 cognitive cost를 줄여 줍니다.

## context window indicator는 들리는 것보다 똑똑한 추가입니다

context usage indicator도 마음에 듭니다.

작은 디테일처럼 들릴 수 있지만, 이것은 매우 현실적인 AI workflow 문제를 해결합니다. tool이 대화 앞부분을 언제부터 잊기 시작하는지 모르는 문제입니다.

그걸 visible하게 만드는 것은 좋은 design choice입니다.

model context를 마법처럼 늘려 주지는 않지만, limit을 observable하게 만듭니다. 대개 그게 다음으로 가장 좋은 선택입니다.

## 내 생각

이번 업데이트는 본질적으로 developers에게 AI-assisted loop에 대한 더 많은 visibility와 control을 주는 것입니다.

더 많은 novelty가 아닙니다.
더 많은 chaos도 아닙니다.
더 많은 control입니다.

AI tools를 진지한 IDE workflow 안에서 더 trustworthy하게 만들고 싶다면, 투자해야 할 정확한 지점이 바로 여기입니다.

원문: [Visual Studio 5월 업데이트 — Plan, Review, Refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)