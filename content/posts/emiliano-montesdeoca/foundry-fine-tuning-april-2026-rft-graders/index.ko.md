---
title: "Foundry의 RFT가 더 저렴하고 스마트해졌습니다 — 변경된 내용 정리"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry가 이번 달 세 가지 RFT 업데이트를 출시했습니다: o4-mini 글로벌 트레이닝, 새로운 GPT-4.1 모델 그레이더, 그리고 디버깅 시간을 크게 줄여줄 모범 사례 가이드."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}})에서 확인하세요.*

파인튜닝된 모델에 의존하는 .NET 앱을 개발하고 있다면, 이번 달 Foundry 업데이트에 주목할 필요가 있습니다. Reinforcement Fine-Tuning이 더 접근하기 쉬워지고 비용이 크게 낮아졌습니다.

자세한 내용은 [공식 발표](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/)에 있지만, 여기서 실용적인 요약을 정리해 드리겠습니다.

## o4-mini 글로벌 트레이닝

o4-mini는 추론 중심 및 에이전트 워크로드에 가장 적합한 모델입니다. 큰 소식: 이제 13개 이상의 Azure 리전에서 파인튜닝 작업을 시작할 수 있으며, Standard 트레이닝 대비 토큰당 트레이닝 비용이 더 낮습니다. 동일한 인프라, 동일한 품질, 더 넓은 범위.

팀이 여러 지역에 분산되어 있다면 이것은 중요합니다. 더 이상 트레이닝을 위해 소수의 리전에 묶여 있을 필요가 없습니다.

글로벌 트레이닝 작업을 시작하는 REST API 호출은 다음과 같습니다:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

`trainingType: globalstandard` 플래그가 핵심적인 차이점입니다.

## 새로운 모델 그레이더: GPT-4.1 패밀리

그레이더는 모델이 최적화하는 보상 신호를 정의합니다. 지금까지 모델 기반 그레이더는 소수의 모델로 제한되어 있었습니다. 이제 세 가지 새로운 옵션이 추가되었습니다: GPT-4.1, GPT-4.1-mini, GPT-4.1-nano.

결정적 그레이더 대신 모델 그레이더를 사용해야 할 때는? 태스크 출력이 개방형일 때, 여러 차원에서 부분 점수가 필요할 때, 또는 도구 호출의 정확성이 의미적 맥락에 따라 달라지는 에이전트 워크플로를 구축할 때입니다.

핵심은 티어링 전략이 실용적이라는 것입니다:

- **GPT-4.1-nano** 초기 반복용. 낮은 비용, 빠른 피드백 루프.
- **GPT-4.1-mini** 평가 기준이 안정되고 더 높은 정확도가 필요할 때.
- **GPT-4.1** 프로덕션 평가 또는 모든 점수 결정이 중요한 복잡한 기준용.

단일 RFT 작업에서 그레이더 유형을 혼합할 수도 있습니다. "정답" 차원에는 string-match를 사용하고 추론 품질 평가에는 모델 그레이더를 사용하세요. 솔직히 이 유연성이 실제 워크로드에서 유용한 이유입니다.

## RFT 데이터 형식 주의사항

많은 사람들이 여기서 실수합니다. RFT 데이터 형식은 SFT와 다릅니다. 각 행의 마지막 메시지는 User 또는 Developer 역할이어야 합니다 — Assistant가 아닙니다. 예상 답변은 그레이더가 직접 참조하는 `reference_answer`와 같은 최상위 키에 넣습니다.

지금까지 지도 파인튜닝을 해왔고 RFT로 전환하고 싶다면, 트레이닝 데이터를 재구성해야 합니다. 이 단계를 건너뛰면 작업이 조용히 실패합니다.

## .NET 개발자에게 왜 중요한가

Azure OpenAI SDK를 통해 .NET 앱에서 파인튜닝된 모델을 호출하고 있다면, 더 저렴한 트레이닝은 더 공격적으로 반복할 수 있다는 뜻입니다. 모델 그레이더 옵션은 정확 일치 시나리오뿐만 아니라 미묘한 태스크에 대해서도 파인튜닝할 수 있다는 것을 의미합니다. 그리고 [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md)의 모범 사례 가이드는 실제 디버깅 시간을 절약해 줄 것입니다.

작게 시작하세요. 10개에서 100개 샘플. 간단한 그레이더. 루프를 검증하세요. 그다음 확장하세요.
