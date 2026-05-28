---
title: "Foundry Local 1.1: 실시간 전사, Embeddings, Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1은 라이브 마이크 전사, 텍스트 embeddings, Responses API 지원을 추가합니다 — 클라우드 의존성 없이, 네트워크 지연 없이, 토큰 비용 없이 모두 로컬에서 실행됩니다."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0은 개념을 증명했습니다: 개발자 친화적인 SDK로 Windows, macOS(Apple Silicon), Linux x64에서 AI 모델을 로컬로 실행할 수 있다는 것. 버전 1.1은 많은 실제 프로덕션 사용 사례를 다루는 세 가지 기능을 추가합니다.

## 라이브 오디오 전사

가장 중요한 새 기능: 마이크에서 직접 실시간 음성-텍스트 스트리밍. 자막, 음성 UI, 회의 전사, 접근성 도구 — 클라우드 의존성 없이 모두 로컬에서 실행됩니다.

API는 세션 기반이며 결과가 도착할 때 스트리밍하고, 중간 텍스트와 최종 텍스트를 구분하는 `is_final` 마커를 사용합니다. JavaScript, C#, Python, Rust의 모든 언어 바인딩에서 사용 가능합니다.

카탈로그에서 스트리밍 음성 모델을 로드하고, 오디오 설정(샘플 레이트, 채널, 언어)으로 세션을 생성하고, 시작하고, 원시 PCM 오디오 청크를 푸시하고, 결과의 비동기 스트림을 소비합니다. 게시물에는 Python과 C#의 전체 예제가 있습니다.

## 텍스트 Embeddings

시맨틱 검색, RAG 파이프라인, 클러스터링, 유사성 매칭 — 이 모든 것에는 embeddings가 필요합니다. Foundry Local 1.1은 embedding 모델 지원을 추가하여 클라우드 엔드포인트에 데이터를 보내지 않고 같은 SDK에서 로컬로 벡터를 생성할 수 있습니다.

데이터 거주지가 중요하거나 민감한 콘텐츠를 처리하는 애플리케이션의 경우, 로컬 embedding 생성은 중요한 기능입니다.

## Responses API

Foundry Local은 이제 [Responses API](https://platform.openai.com/docs/api-reference/responses) — 에이전틱 상호작용을 위해 설계된 구조화된 인터페이스 — 를 지원합니다. 이것은 다음을 추가합니다:

- **도구 호출** — 로컬에서 실행되는 모델이 정의한 도구를 호출하도록 허용합니다
- **멀티모달 비전-언어 입력** — 비전 지원 모델에 이미지 + 텍스트를 전달합니다
- 표준 API 형태와 호환되므로 OpenAI의 Responses API를 대상으로 하는 기존 에이전트가 로컬 모델에 대해 작동합니다

## 패키지 크기 개선

두 가지 변경으로 JavaScript 패키지 크기가 줄어듭니다:
- `koffi` FFI 레이어가 사용자 정의 Node-API C 애드온으로 교체되었습니다
- WebGPU 실행 공급자가 별도의 플러그인으로 제공되므로 GPU 가속이 필요 없는 애플리케이션은 크기 비용을 지불하지 않아도 됩니다

C# SDK는 이제 광범위한 .NET 호환성을 위해 더 낮은 프레임워크 버전을 대상으로 합니다.

## 왜 중요한가

세 가지 기능 — 전사, embeddings, 도구 호출 — 은 많은 AI 애플리케이션의 핵심 구성 요소를 다룹니다. 로컬에서 실행하면 다음을 의미합니다:
- 인터넷 불필요
- 토큰 비용 없음
- 머신을 떠나는 데이터 없음
- 네트워크 상태에 관계없이 일관된 지연

Foundry Local은 엣지 시나리오, 프라이버시에 민감한 워크로드, 오프라인 애플리케이션, 또는 개발 중 클라우드 의존성을 피하고 싶은 모든 경우에 적합합니다.

원본 게시물: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
