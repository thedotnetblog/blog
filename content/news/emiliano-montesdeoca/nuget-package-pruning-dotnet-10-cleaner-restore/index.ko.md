---
title: ".NET 10의 NuGet 패키지 pruning은 어디서나 체감되는 개선이다"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10의 새로운 NuGet 패키지 pruning은 false-positive vulnerability reports를 줄이고, restore graph를 단순화하며, restore 성능을 향상한다. 이것은 조용히 일상을 더 좋게 만드는 종류의 platform change다."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "index.md" >}})에서 확인하세요.*

어떤 platform improvements는 새로운 scenarios를 열어 주기 때문에 흥미롭습니다.

다른 것들은 기존 workflows를 더 조용하게, 더 덜 취약하게, 더 덜 성가시게 만들어 주기 때문에 흥미롭습니다.

**.NET 10의 NuGet 패키지 pruning**은 분명히 두 번째 범주에 속하며, 저는 그것을 칭찬으로 말하고 있습니다.

## 왜 중요한가

transitive vulnerability noise, 불필요하게 큰 restore graph, 또는 기술적으로는 존재하지만 앱이 사용하는 runtime에는 실제로 관련이 없는 package들 때문에 어려움을 겪어 본 적이 있다면, 이 변경은 실제 pain point를 정확히 건드립니다.

pruning은 runtime이 이미 제공하는 platform-provided packages를 effective dependency graph에서 제거함으로써 도움이 됩니다.

그 결과는 다음과 같습니다.

- false-positive vulnerability reports 감소
- 더 깔끔한 transitive dependency graph
- restore overhead 감소
- 더 실행 가능한 audit 결과

## 내 생각

이것이야말로 제가 좋아하는 .NET improvement입니다.

기본값을 더 좋게 만들고, mental overhead를 줄이며, security signal quality와 일상적인 tooling behavior를 모두 개선합니다.

keynote slide에 올라가지 않더라도, 그것은 충분한 승리입니다.

원문: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
