---
title: "Visual Studio의 Agent Skills: Copilot에게 팀이 실제로 일하는 방법 가르치기"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio는 이제 Agent Skills를 지원합니다 — Copilot에게 팀의 특정 워크플로, 코딩 표준 및 규칙을 가르치는 재사용 가능한 명령 세트입니다. 한 번 정의하고 자동으로 적용하세요."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

AI 코딩 어시스턴트에 대한 지속적인 불만 중 하나: 일반 프로그래밍은 잘 알지만 *팀*의 특정 규칙, 내부 API 또는 선호하는 패턴은 알지 못합니다. 매 세션마다 컨텍스트를 다시 설명해야 합니다. Visual Studio의 Agent Skills는 이 문제를 해결하도록 설계되었습니다.

## Agent Skills란

`SKILL.md` 파일로 정의된 재사용 가능한 명령 세트 — Copilot 에이전트에게 특정 작업 처리 방법을 가르칩니다. "빌드 파이프라인 실행 방법", "서비스 레이어의 보일러플레이트 생성 방법" 또는 "코드 리뷰 체크리스트"를 위한 스킬을 정의합니다. 에이전트는 관련성이 있을 때 스킬을 자동으로 적용합니다.

이것은 새로운 개념이 아닙니다(`.github/copilot-instructions.md`는 한동안 존재했습니다), 하지만 Visual Studio 통합은 이를 발견 UI가 있는 일급 객체로 만듭니다.

## Visual Studio에서 Skills 만들기

통합 UI 흐름: Copilot Chat의 도구 아이콘을 클릭하고 스킬 패널을 열고 `+`를 클릭합니다. 글로벌(개인) 또는 솔루션 레벨 범위를 선택하고 이름을 선택하면 Visual Studio가 템플릿을 생성합니다. 그런 다음 Copilot 에이전트 모드가 템플릿 작성을 도와줄 수 있습니다 — 에이전트를 사용해 에이전트용 스킬을 작성하세요.

현재 Insiders 채널에서 사용 가능하며, 곧 Release에 출시 예정.

스킬을 수동으로 만들 수도 있습니다:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## 검색 위치

스킬은 표준 경로에서 자동으로 검색됩니다:

**솔루션 레벨(리포지토리를 통해 공유):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**글로벌/개인(사용자 프로필, 어디서나 사용 가능):** `~/.copilot/skills/`, `~/.agents/skills/`

다중 위치 지원은 동일한 규칙이 GitHub Copilot, Claude Code 및 기타 에이전트 프레임워크와 작동한다는 것을 의미합니다 — 스킬을 한 번 정의하고 어디서나 사용하세요.

## 형식

스킬은 [agentskills.io/specification](https://agentskills.io/specification) 형식을 따릅니다 — 인간이 읽을 수 있고 기계가 파싱할 수 있는 Markdown 기반 사양. `SKILL.md` 옆에 스크립트, 템플릿 및 예제를 포함할 수 있습니다.

## 실용적 가치

진정한 힘은 개별 기능에 있는 것이 아니라 — 팀 공유 스킬(`.github/skills/`를 통해)과 개인 스킬(`~/.agents/skills/`를 통해)의 조합에 있습니다. 팀 스킬은 조직이 어떻게 일을 처리하는지 인코딩합니다. 개인 스킬은 특별히 당신이 어떻게 일하는지 인코딩합니다. 에이전트는 두 컨텍스트를 자동으로 가져옵니다.

이미 Copilot을 많이 사용하는 조직의 경우, 이는 도구가 일반적인 조언을 제공하는 대신 코드베이스의 특정 규칙을 실제로 인식하게 만드는 중요한 단계입니다.

원본 게시물: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
