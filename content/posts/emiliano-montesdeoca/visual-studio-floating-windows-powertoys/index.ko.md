---
title: "몰랐던 Visual Studio 플로팅 윈도우 설정 (하지만 알아야 할)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Visual Studio의 숨겨진 설정으로 플로팅 윈도우를 완벽하게 제어하세요 — 독립적인 작업 표시줄 항목, 적절한 멀티 모니터 동작, 그리고 완벽한 FancyZones 통합. 드롭다운 하나로 모든 것이 바뀝니다."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "visual-studio-floating-windows-powertoys.md" >}})에서 확인하세요.*

Visual Studio에서 여러 모니터를 사용한다면 (솔직히 요즘 누가 안 쓰겠어요?), 아마 이런 불편함을 경험했을 겁니다: 플로팅 도구 창이 메인 IDE를 최소화하면 사라지고, 항상 다른 모든 것 위에 표시되며, 작업 표시줄에 별도의 버튼으로 나타나지 않습니다. 일부 워크플로에서는 괜찮지만 멀티 모니터 설정에서는 정말 답답합니다.

Visual Studio 팀의 Mads Kristensen이 플로팅 윈도우의 동작을 완전히 바꾸는 [잘 알려지지 않은 설정을 공유했습니다](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/). 드롭다운 하나. 그게 전부입니다.

## 설정

**Tools > Options > Environment > Windows > Floating Windows**

드롭다운 "These floating windows are owned by the main window"에는 세 가지 옵션이 있습니다:

- **None** — 완전한 독립. 모든 플로팅 윈도우가 자체 작업 표시줄 항목을 가지며 일반 Windows 창처럼 동작합니다.
- **Tool Windows** (기본값) — 문서는 자유롭게 플로팅, 도구 창은 IDE에 연결됩니다.
- **Documents and Tool Windows** — 클래식 Visual Studio 동작, 모든 것이 메인 창에 연결됩니다.

## 멀티 모니터 설정에서 "None"이 최적인 이유

**None**으로 설정하면 갑자기 모든 플로팅 도구 창과 문서가 진짜 Windows 애플리케이션처럼 동작합니다. 작업 표시줄에 나타나고, Visual Studio 메인 창을 최소화해도 보이며, 더 이상 모든 것 앞으로 강제되지 않습니다.

이것을 **PowerToys FancyZones**와 결합하면 완전히 달라집니다. 모니터 전체에 커스텀 레이아웃을 만들고, 솔루션 탐색기를 한 존에, 디버거를 다른 존에, 코드 파일을 원하는 곳에 배치하세요. 모든 것이 제자리에 있고, 모든 것이 독립적으로 접근 가능하며, 작업 공간이 혼란스럽지 않고 정돈된 느낌입니다.

## 빠른 추천

- **멀티 모니터 파워 유저**: **None**으로 설정하고 FancyZones와 함께 사용
- **가끔 플로팅하는 분**: **Tool Windows** (기본값)가 좋은 중간 지점
- **전통적인 워크플로**: **Documents and Tool Windows**가 클래식한 방식 유지

프로 팁: 아무 도구 창의 제목 표시줄에서 **Ctrl + 더블 클릭**으로 즉시 플로팅 또는 도킹할 수 있습니다. 설정 변경 후 재시작이 필요 없습니다.

## 마무리

전형적인 "이걸 왜 몰랐지" 설정입니다. Visual Studio의 플로팅 윈도우가 한 번이라도 불편했다면, 지금 바로 바꾸러 가세요.

자세한 내용과 스크린샷은 [전체 포스트](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/)에서 확인하세요.
