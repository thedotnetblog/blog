---
title: ".NET 11 Preview 4: MCP 서버 템플릿, Runtime-Async 라이브러리, 프로세스 API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4가 출시되었습니다. 주요 내용: SDK의 MCP 서버 템플릿, runtime-async로 컴파일된 런타임 라이브러리, 모바일용 dotnet watch, 그리고 프로세스 API의 주요 확장."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4가 출시되었습니다. .NET 주요 미리 보기의 각 릴리스는 런타임, SDK, 라이브러리, ASP.NET Core, MAUI, C#, Entity Framework에 걸쳐 긴 변경 목록을 추가합니다. 전체 목록을 반복하는 대신, 제가 주목한 항목들을 소개합니다.

## .NET SDK에 MCP 서버 템플릿 추가

가장 흥미로운 항목: MCP 서버 프로젝트 템플릿이 이제 SDK에 포함됩니다. 이는 `dotnet new mcp-server`(또는 최종 커맨드 이름)가 바로 작동한다는 의미입니다. .NET에서 MCP 도구를 구축하는 분들에게 이는 초기 설정의 번거로움을 크게 줄여줍니다. 플랫폼 toolchain에의 MCP 통합은 생태계가 향하는 방향을 보여줍니다.

## Runtime-Async로 컴파일된 런타임 라이브러리

런타임 자체가 이제 runtime-async 기능을 사용하여 표준 라이브러리를 컴파일합니다. 이것은 성능에 영향을 미치는 내부 변경입니다 — 런타임의 async 상태 머신이 더 효율적이 됩니다. 여기서 중요한 것은 사용자에게 보이는 API 변경이 아니라, runtime-async가 BCL 자체에 사용될 만큼 성숙했다는 것으로, 기능의 준비 상태에 대한 의미 있는 신호입니다.

## JIT 최적화 및 하드웨어 내장 함수

Preview 4는 JIT 작업을 계속합니다. 하드웨어 내장 함수 및 코드 생성 개선이 포함됩니다 — 세부 사항은 런타임 릴리스 노트에 있습니다. 이런 종류의 변경은 일반적으로 코드 변경 없이 밀도 높은 계산 루프의 처리량을 향상시킵니다.

## 프로세스 API 확장

Preview 4에서는 `System.Diagnostics.Process`의 주요 업데이트가 제공됩니다:

- `Process.RunAndCaptureTextAsync` — 프로세스 시작, stdout/stderr 캡처, 종료 대기를 데드락 위험 없이 단일 호출로 처리
- `KillOnParentExit` — 부모 프로세스와 자식 프로세스 간의 가벼운 수명 결합
- 트리머 친화적인 `SafeProcessHandle` 기반 API

데드락 없이 프로세스 출력을 캡처하기 위한 보일러플레이트를 작성해본 적이 있다면(stdout *과* stderr의 동시 비동기 읽기), `RunAndCaptureTextAsync`가 바로 필요했던 API입니다.

## Android 및 iOS용 dotnet watch

`dotnet watch`가 이제 .NET MAUI Android 및 iOS 프로젝트의 장치 선택을 지원합니다. 빌드 루프에서 장치 연결을 수동으로 관리하지 않고도 모바일에서 더 빠른 반복이 가능합니다.

## Span 기반 압축 API

새로운 span 기반 Deflate, ZLib, GZip 인코더/디코더 API가 라이브러리에 추가됩니다. 압축 데이터를 처리할 때 할당이 줄어듭니다 — 고처리량 데이터 처리를 수행하는 경우 관련이 있습니다.

## 사용해보기

[.NET 11 Preview 4 다운로드](https://dotnet.microsoft.com/download/dotnet/11.0) — 미리 보기 버전으로 프로덕션 준비가 되지 않았지만, RC 사이클 이전에 문제를 조기에 발견하기 위해 프로젝트에 적용해볼 가치가 있습니다.

원본 게시물: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
