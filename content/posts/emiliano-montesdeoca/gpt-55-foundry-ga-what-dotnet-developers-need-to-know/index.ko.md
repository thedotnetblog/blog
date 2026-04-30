---
title: "GPT-5.5가 Azure Foundry에 출시됐다 — .NET 개발자가 알아야 할 것들"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5가 Microsoft Foundry에서 일반 출시됐습니다. GPT-5에서 5.5로의 발전, 실제로 무엇이 개선됐는지, 오늘 에이전트에서 사용하는 방법."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*이 게시물은 자동 번역되었습니다. 원문을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

Microsoft가 [GPT-5.5가 Microsoft Foundry에서 일반 출시됐다고 발표했습니다](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Azure에서 에이전트를 구축해 왔다면, 이것이 기다리던 업데이트입니다.

## GPT-5 발전 과정

- **GPT-5**: 추론과 속도를 단일 시스템으로 통합
- **GPT-5.4**: 더 강력한 다단계 추론, 기업용 초기 에이전트 기능
- **GPT-5.5**: 더 깊은 장문맥 추론, 더 신뢰할 수 있는 에이전트 실행, 향상된 토큰 효율성

## 실제로 무엇이 바뀌었나

**향상된 에이전트 코딩**: GPT-5.5는 대규모 코드베이스 전체에서 컨텍스트를 유지하고, 아키텍처 수준 오류를 진단하며, 테스트 요구사항을 예측합니다. 수정이 *다른 무엇에* 영향을 미치는지 행동 전에 추론합니다.

**토큰 효율성**: 더 적은 토큰과 더 적은 재시도로 더 높은 품질의 출력. 프로덕션 배포에서 비용과 지연이 직접 감소합니다.

## 가격

| 모델 | 입력 ($/M tokens) | 캐시 입력 | 출력 ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## Foundry가 중요한 이유

Foundry Agent Service를 사용하면 YAML로 에이전트를 정의하거나 Microsoft Agent Framework, GitHub Copilot SDK, LangGraph 또는 OpenAI Agents SDK와 연결할 수 있습니다. 영구 파일시스템, 별도의 Microsoft Entra 아이덴티티, 제로 스케일 가격으로 격리된 호스팅 에이전트로 실행합니다.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "당신은 유용한 어시스턴트입니다.", name: "내에이전트");
```

[전체 발표](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)를 확인하세요.
