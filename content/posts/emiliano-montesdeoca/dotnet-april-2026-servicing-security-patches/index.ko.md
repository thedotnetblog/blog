---
title: ".NET 2026년 4월 서비싱 — 오늘 바로 적용해야 할 보안 패치"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "2026년 4월 서비싱 릴리스는 .NET 10, .NET 9, .NET 8, .NET Framework에 걸쳐 6개의 CVE를 패치합니다 — 원격 코드 실행 취약점 2건을 포함합니다."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}})를 참조하세요.*

.NET과 .NET Framework의 [2026년 4월 서비싱 업데이트](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/)가 출시되었습니다. 이번에는 빨리 적용하고 싶은 보안 수정 사항이 포함되어 있습니다. 6개의 CVE가 패치되었으며, 그 중 2개는 원격 코드 실행(RCE) 취약점입니다.

## 패치된 내용

빠른 요약은 다음과 같습니다:

| CVE | 유형 | 영향 범위 |
|-----|------|-----------|
| CVE-2026-26171 | 보안 기능 우회 | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **원격 코드 실행** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **원격 코드 실행** | .NET 10, 9, 8 |
| CVE-2026-32203 | 서비스 거부 | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | 서비스 거부 | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | 서비스 거부 | .NET Framework 2.0–4.8.1 |

2개의 RCE CVE(CVE-2026-32178 및 CVE-2026-33116)는 가장 넓은 범위의 .NET 버전에 영향을 미치며 우선적으로 대응해야 합니다.

## 업데이트된 버전

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

모두 일반적인 채널을 통해 사용할 수 있습니다 — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), MCR의 컨테이너 이미지, Linux 패키지 관리자.

## 해야 할 일

프로젝트와 CI/CD 파이프라인을 최신 패치 버전으로 업데이트하세요. 컨테이너를 실행 중이라면 최신 이미지를 풀하세요. .NET Framework를 사용 중이라면 해당 패치에 대해 [.NET Framework 릴리스 노트](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes)를 확인하세요.

.NET 10을 프로덕션에서 실행하고 있다면(현재 릴리스입니다), 10.0.6은 필수 업데이트입니다. LTS 트랙의 .NET 9.0.15와 .NET 8.0.26도 마찬가지입니다. 2개의 RCE 취약점은 미룰 수 있는 것이 아닙니다.
