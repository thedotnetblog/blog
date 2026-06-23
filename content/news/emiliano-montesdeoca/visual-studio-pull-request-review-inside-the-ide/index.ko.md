---
title: "Visual Studio 안에서 pull request를 리뷰하는 것은 내가 좋아하는 종류의 friction reduction이다"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio는 이제 IDE를 떠나지 않고도 pull request를 처음부터 끝까지 리뷰할 수 있습니다. 이는 점진적으로 보일 수 있지만, 하루 종일 Visual Studio 안에서 일하는 팀에게는 불필요한 context switching을 크게 줄여 줍니다."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}})에서 볼 수 있습니다.*

브라우저가 code review workflow의 너무 많은 부분을 너무 오래 가져가고 있었습니다.

그래서 Visual Studio가 **IDE 안에서 end-to-end pull request review** 쪽으로 더 나아가는 모습을 보는 것이 정말 반갑습니다.

이건 큰 헤드라인을 만들지는 않을 수 있지만, 일상적인 development를 확실히 개선할 수 있는 기능입니다.

## 핵심 가치는 간단합니다: context switching이 줄어든다

review loop가 일부는 IDE에, 일부는 browser에 있을 때 friction은 쌓입니다.

- 다른 곳에서 PR을 연다
- 한 tool에서 변경 사항을 검사한다
- 더 깊게 조사하기 위해 solution으로 돌아간다
- comment나 approve를 위해 다시 전환한다

치명적이지는 않습니다. 그냥 비효율적일 뿐입니다.

Visual Studio가 같은 working environment에서 PR을 열고, inspect하고, comment하고, approve하고, merge할 수 있게 해 준다면, 그것은 진짜 productivity win입니다.

## "checkout 없이 review" 옵션은 특히 좋습니다

제가 특히 좋아하는 부분은 PR branch를 checkout하지 않고 review할 수 있다는 점입니다.

작아 보일 수 있지만, 다음과 같은 경우에 완벽합니다.

- 빠른 review pass
- interrupt-driven feedback 요청
- 현재 branch와 local state를 그대로 유지

이게 바로 좋은 code review tool이 필요한 유연성입니다.

## 내 생각

이건 혁신적인 기능은 아닙니다.

그보다 더 좋은 것입니다: 실용적인 기능.

하루 대부분을 Visual Studio에서 보내는 팀에게 더 강한 PR review 지원은 workflow break를 줄이고 inspection에서 action까지의 경로를 더 부드럽게 만듭니다.

저는 이걸 충분히 가치 있는 개선이라고 봅니다.

원문: [Visual Studio를 떠나지 않고 pull request 리뷰하기](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)