---
title: "하루 68분을 코드 재설명에 낭비하고 있나요? 해결책이 있습니다"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "컨텍스트 로트는 현실입니다 — AI 에이전트는 30턴 후에 길을 잃고, 매시간 컴팩션 세금을 냅니다. auto-memory는 GitHub Copilot CLI에 수천 개의 토큰을 소모하지 않고 외과적인 기억을 제공합니다."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*이 게시물은 자동 번역되었습니다. 원본 버전은 [여기를 클릭](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/)하세요.*

Copilot 세션이 `/compact`에 도달하여 에이전트가 무엇을 하고 있었는지 완전히 잊어버리는 순간을 아시나요? 다음 5분 동안 파일 구조, 실패한 테스트, 이미 시도한 세 가지 접근 방식을 다시 설명합니다. 그리고 또 일어납니다.

Desi Villanueva가 측정했습니다: **하루 68분** — 재오리엔테이션에만. 코드 작성도 아니고, PR 리뷰도 아니고, AI가 이미 알고 있던 것들을 다시 알려주는 데만.

## 컨텍스트 윈도우의 거짓말

실제 계산: 200K 총 컨텍스트에서 MCP 도구 65K, 인스트럭션 파일 10K를 빼면, **한 글자 입력 전에 이미 125K만 남습니다**. LLM은 60% 용량에서 벽에 부딪히므로, 실효 한계는 **45K 토큰**입니다.

## 컴팩션 세금

잔인한 부분: **기억은 이미 존재합니다.** Copilot CLI는 `~/.copilot/session-store.db`에 모든 세션을 기록합니다. 에이전트가 읽지 못할 뿐입니다.

## auto-memory: 리콜 레이어, 메모리 시스템이 아님

```bash
pip install auto-memory
```

~1,900줄의 Python. 의존성 없음. 30초 설치.

grep 결과로 컨텍스트를 범람시키는 대신, **10,000 토큰이 아닌 50 토큰**으로 정말 중요한 것에 대한 외과적 접근을 제공합니다.

## 마무리

컨텍스트 로트는 실제 아키텍처 제약입니다. auto-memory는 에이전트에게 저렴하고 정확한 리콜 메커니즘을 제공하여 이를 우회합니다.

확인해보세요: [GitHub의 auto-memory](https://github.com/dezgit2025/auto-memory). Desi Villanueva의 원본 포스트: [I Wasted 68 Minutes a Day](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).
