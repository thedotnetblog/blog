---
title: "당신의 에이전트는 어디서 기억하나요? 채팅 기록 저장소 실용 가이드"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "서비스 관리형 vs 클라이언트 관리형? 선형 vs 분기형? AI 에이전트가 실제로 무엇을 할 수 있는지 결정하는 아키텍처 결정 — C#과 Python 코드 예제 포함."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*이 게시물은 자동 번역되었습니다. 원문을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

AI 에이전트를 구축할 때 대부분의 에너지를 모델, 도구, 프롬프트에 씁니다. *대화 기록이 어디에 저장되는가*라는 질문은 구현 세부사항처럼 보이지만, 실제로 가장 중요한 아키텍처 결정 중 하나입니다.

이 결정은 사용자가 대화를 분기할 수 있는지, 응답을 취소할 수 있는지, 재시작 후 세션을 재개할 수 있는지, 그리고 데이터가 인프라를 벗어나는지를 결정합니다. [Agent Framework 팀이 심층 분석을 공개했습니다](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## 두 가지 기본 패턴

**서비스 관리형**: AI 서비스가 대화 상태를 저장합니다. 앱은 참조를 유지하고 서비스가 각 요청에 관련 기록을 자동으로 포함시킵니다.

**클라이언트 관리형**: 앱이 전체 기록을 유지하고 각 요청마다 관련 메시지를 보냅니다. 서비스는 무상태입니다. 모든 것을 제어합니다.

## Agent Framework의 추상화 방식

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("내 이름은 Alice입니다.", session);
var second = await agent.RunAsync("내 이름이 뭔가요?", session);
```

```python
session = agent.create_session()
first = await agent.run("내 이름은 Alice입니다.", session=session)
second = await agent.run("내 이름이 뭔가요?", session=session)
```

## 공급자 빠른 참조

| 공급자 | 저장 위치 | 모델 | 압축 |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | 클라이언트 | N/A | 당신 |
| Foundry Agent Service | 서비스 | 선형 | 서비스 |
| Responses API (기본값) | 서비스 | 분기형 | 서비스 |
| Anthropic Claude, Ollama | 클라이언트 | N/A | 당신 |

## 선택 방법

1. **분기 또는 "취소" 기능이 필요한가?** → 서비스 관리형 Responses API
2. **데이터 주권이 필요한가?** → 데이터베이스 백엔드가 있는 클라이언트 관리형
3. **단순 챗봇인가?** → 서비스 관리형 선형으로 충분

전체 의사결정 트리를 보려면 [전체 게시물](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/)을 읽어보세요.
