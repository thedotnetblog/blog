---
title: "Aspire 13.2: Bun 지원, 더 나은 컨테이너, 그리고 적은 디버깅 마찰"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2은 Vite 앱에 일급 Bun 지원을 추가하고, Yarn 안정성을 수정하며, 로컬 개발 동작을 더 예측 가능하게 만드는 컨테이너 개선 사항을 제공합니다."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*이 게시물은 자동 번역되었습니다. 원본 버전은 [여기를 클릭](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/)하세요.*

.NET 백엔드와 JavaScript 프론트엔드를 Aspire에서 구축하고 있다면, 13.2는 조용히 하루를 더 나게 만드는 업데이트입니다.

## Bun이 이제 일급 시민입니다

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

팀이 이미 Bun을 사용한다면, Aspire는 더 이상 역류를 강요하지 않습니다.

## Yarn이 더 안정적으로

`withYarn()`과 `addViteApp()`에서 신비한 실패가 줄어듭니다.

## 컨테이너 개선

`ImagePullPolicy.Never`로 레지스트리 없이 로컬 이미지 사용. PostgreSQL 18+ 데이터 볼륨이 이제 올바르게 작동합니다.

## 디버깅 개선

코어 타입에 `DebuggerDisplayAttribute`, `WaitFor`의 개선된 오류 메시지, 올바른 타이밍에 발화하는 `BeforeResourceStartedEvent`.

David Pine의 원본 포스트: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
