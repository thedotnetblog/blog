---
title: "고생하는 종속성을 계속 두드리지 마세요: Azure Functions + Service Bus의 재시도 패턴"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "지수 백오프와 서킷 브레이커 패턴이 이제 Service Bus로 트리거되는 Azure Functions에서 기본 지원됩니다 — 작동 방식과 둘 다 필요한 이유를 설명합니다."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Functions 앱에서 복구 가능한 오류가 장애로 변하는 방식은 이렇습니다: 종속성이 타임아웃하기 시작하고, 모든 Functions 인스턴스가 즉시 무기한으로 재시도하고, 종속성은 수백 개의 동시 실패 요청으로 두드려 맞고, 일시적인 문제로 시작한 것이 시스템 전체 백프레셔 이벤트가 됩니다.

이 이야기를 알고 있을 것입니다. Azure Functions는 빠르게 스케일 아웃됩니다 — 그것이 핵심입니다. 그러나 "빠른 스케일 아웃"과 "즉각적인 재시도"가 함께하면 장애를 극적으로 악화시킬 수 있습니다.

두 가지 패턴이 도움이 됩니다. 지수 백오프와 서킷 브레이커. 둘 다 이제 Service Bus로 트리거되는 Azure Functions에서 기본 지원됩니다.

## 두 가지 패턴, 다른 역할

이 패턴들은 대안이 아닌 보완적입니다:

**지수 백오프**는 답합니다: *언제 다시 시도해야 하는가?*
종속성이 복구할 시간을 확보하기 위해 재시도 사이의 지연을 증가시킵니다. 메시지 수준에서 재시도 타이밍을 조절합니다.

**서킷 브레이커**는 답합니다: *지금 이 종속성을 호출해야 하는가?*
오류 임계값에 도달한 후 비정상적인 종속성에 대한 반복 호출을 중단하고, 쿨다운 기간 후 신중하게 탐색합니다. 시스템 수준에서 재시도 폭풍을 방지합니다.

둘 다 필요합니다. 백오프는 메시지별 재시도 페이싱을 처리합니다. 서킷 브레이커는 집계 상태 결정을 처리합니다.

## Service Bus에 특히 중요한 이유

큐는 버스트 트래픽을 흡수합니다, 이는 좋은 일입니다. 그러나 제어 없이는 워커가 실패할 호출에 컴퓨팅 리소스를 계속 낭비하는 동안 큐가 증가할 수 있습니다. 포이즌 메시지가 있어야 할 시간보다 더 오래 활성 상태를 유지합니다. 핫 파티션이나 제한된 다운스트림 용량이 계단식 문제를 일으킵니다.

더 안전한 설계:

1. 일시적인 오류 감지
2. 지수 백오프로 다음 시도 지연
3. 오류 임계값에 도달하면 종속성 호출 중단 (서킷 오픈)
4. 쿨다운 기간 후 신중하게 재개 (서킷 탐색)
5. 복구 불가능한 작업을 dead-letter 또는 격리 경로로 이동

## 네이티브 지원의 모습

새로운 지원은 기존 Azure Functions 호스트 모델과 통합됩니다 — 추가 라이브러리 없음, 사용자 정의 구현 없음. 구성은 `host.json`에 들어갑니다:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

서킷 브레이커 구성은 비정상 종속성이 복구 중에 두드려 맞지 않도록 오류 임계값과 재설정 간격을 설정합니다.

## 지원되는 언어

.NET만을 위한 것이 아닙니다. 이 기능은 dotnet, JavaScript, TypeScript, Python을 포함합니다 — Azure Functions의 Service Bus 트리거에서 지원되는 전체 언어 세트입니다.

## 마무리

재시도 패턴은 다운스트림 장애가 Functions를 우아하게 저하되는 대신 문제를 악화시키는 첫 번째 사태가 발생할 때까지 설정하기에 흥미롭지 않습니다. 이를 사전에 설정하는 것은 저렴합니다. 인시던트 중에 개조하는 것은 그렇지 않습니다.

원본 게시물: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
