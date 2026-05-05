---
title: "Azure MCP 도구가 Visual Studio 2022에 기본 탑재 — 확장 프로그램 설치 불필요"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP 도구가 Visual Studio 2022의 Azure 개발 워크로드의 일부로 제공됩니다. 230개 이상의 도구, 45개 Azure 서비스, 설치할 확장 프로그램 제로."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *이 글은 자동 번역되었습니다. 원문을 보시려면 [여기를 클릭]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}})하세요.*

Visual Studio에서 별도 확장 프로그램을 통해 Azure MCP 도구를 사용해 왔다면, 그 과정을 잘 아실 겁니다 — VSIX 설치, 재시작, 문제가 안 생기길 바라기, 버전 불일치 관리. 그 번거로움이 사라졌습니다.

Yun Jung Choi가 [발표](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/)한 바와 같이, Azure MCP 도구가 이제 Visual Studio 2022의 Azure 개발 워크로드의 일부로 직접 제공됩니다. 확장 프로그램 없음. VSIX 없음. 재시작 댄스 없음.

## 이것이 실제로 의미하는 것

Visual Studio 2022 버전 17.14.30부터 Azure MCP Server가 Azure 개발 워크로드에 번들로 포함됩니다. 이미 해당 워크로드가 설치되어 있다면, GitHub Copilot Chat에서 활성화하기만 하면 됩니다.

45개 Azure 서비스에 걸친 230개 이상의 도구 — 채팅 창에서 직접 접근할 수 있습니다. 스토리지 계정 목록 조회, ASP.NET Core 앱 배포, App Service 문제 진단, Log Analytics 쿼리 — 브라우저 탭을 열 필요 없이 모두 가능합니다.

## 왜 이것이 들리는 것보다 더 중요한가

개발자 도구에 대해 이런 말이 있습니다: 추가 단계 하나하나가 마찰이고, 마찰은 도입을 망칩니다. MCP가 별도 확장 프로그램이었을 때는 버전 불일치, 설치 실패, 그리고 업데이트해야 할 것이 하나 더 생긴다는 것을 의미했습니다. 워크로드에 내장된다는 것은:

- **단일 업데이트 경로** — Visual Studio Installer를 통해
- **버전 차이 없음** — 확장 프로그램과 IDE 간에
- **항상 최신** — MCP Server가 정기 VS 릴리스와 함께 업데이트

Azure를 표준으로 사용하는 팀에게 이것은 큰 의미가 있습니다. 워크로드를 한 번 설치하고, 도구를 활성화하면, 매 세션마다 사용할 수 있습니다.

## 이것으로 무엇을 할 수 있는가

도구들은 Copilot Chat를 통해 전체 개발 라이프사이클을 지원합니다:

- **학습** — Azure 서비스, 모범 사례, 아키텍처 패턴에 대해 질문
- **설계 및 개발** — 서비스 추천 받기, 앱 코드 구성
- **배포** — 리소스 프로비저닝 및 IDE에서 직접 배포
- **문제 해결** — 로그 쿼리, 리소스 상태 확인, 프로덕션 문제 진단

간단한 예시 — Copilot Chat에 다음을 입력해 보세요:

```
List my storage accounts in my current subscription.
```

Copilot이 뒤에서 Azure MCP 도구를 호출하고, 구독을 조회하여, 이름, 위치, SKU가 포함된 정리된 목록을 반환합니다. 포털이 필요 없습니다.

## 활성화 방법

1. Visual Studio 2022 **17.14.30** 이상으로 업데이트
2. **Azure development** 워크로드가 설치되어 있는지 확인
3. GitHub Copilot Chat 열기
4. **Select tools** 버튼(렌치 아이콘) 클릭
5. **Azure MCP Server** 활성화

끝입니다. 세션 간에 활성화 상태가 유지됩니다.

## 한 가지 주의사항

도구는 기본적으로 비활성화되어 있습니다 — 직접 활성화해야 합니다. 그리고 VS 2026 전용 도구는 VS 2022에서 사용할 수 없습니다. 도구 사용 가능 여부는 Azure 구독 권한에 따라 달라지며, 포털과 동일합니다.

## 더 큰 그림

이것은 분명한 트렌드의 일부입니다: MCP는 개발자 IDE에서 클라우드 도구를 제공하는 표준이 되어가고 있습니다. 이미 [Azure MCP Server 2.0 안정 버전 출시](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)와 VS Code 및 기타 에디터에서의 MCP 통합을 봐왔습니다. Visual Studio의 워크로드 시스템에 내장하는 것은 자연스러운 발전입니다.

Visual Studio에서 살다시피 하는 .NET 개발자에게, Azure 포털로 컨텍스트 전환해야 할 이유가 하나 더 사라진 셈입니다. 솔직히, 탭 전환은 적을수록 좋으니까요.
