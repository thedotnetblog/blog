---
title: "Windows App Dev CLI v0.3: 터미널에서 F5 디버그와 에이전트를 위한 UI 자동화"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3는 터미널에서 디버그 실행을 위한 winapp run, UI 자동화를 위한 winapp ui, 그리고 패키지 앱에서 dotnet run을 동작하게 하는 NuGet 패키지를 제공합니다."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*이 게시물은 자동으로 번역되었습니다. 원본을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

Visual Studio의 F5 경험은 훌륭합니다. 하지만 CI 파이프라인, 자동화 워크플로우, 또는 AI 에이전트가 테스트를 수행할 때 패키지된 Windows 앱을 시작하고 디버그하기 위해 VS를 열어야 한다면 너무 번거롭습니다.

Windows App Development CLI v0.3이 [출시](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)되었으며, 두 가지 핵심 기능으로 이를 직접 해결합니다: `winapp run`과 `winapp ui`.

## winapp run: 어디서나 F5

`winapp run`은 언패키지된 앱 폴더와 매니페스트를 받아, VS가 디버그 시작 시 수행하는 모든 작업을 실행합니다: 루스 패키지 등록, 앱 시작, 재배포 간 `LocalState` 보존.

```bash
# 앱을 빌드한 다음 패키지 앱으로 실행
winapp run ./bin/Debug
```

WinUI, WPF, WinForms, Console, Avalonia 등에서 동작합니다. 모드는 개발자와 자동화 워크플로우 모두를 위해 설계되었습니다:

- **`--detach`**: 시작 후 즉시 터미널에 제어권을 반환합니다. CI/자동화에 적합합니다.
- **`--unregister-on-exit`**: 앱 종료 시 등록된 패키지를 정리합니다.
- **`--debug-output`**: `OutputDebugString` 메시지와 예외를 실시간으로 캡처합니다.

## 새로운 NuGet 패키지: 패키지 앱을 위한 dotnet run

.NET 개발자를 위한 새로운 NuGet 패키지가 있습니다: `Microsoft.Windows.SDK.BuildTools.WinApp`. 설치 후 `dotnet run`이 전체 이너 루프를 처리합니다: 빌드, 루스 레이아웃 패키지 준비, Windows 등록 및 시작 — 모두 한 단계로.

```bash
winapp init
# 또는
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: 커맨드 라인에서 UI 자동화

이것이 에이전트 시나리오를 여는 기능입니다. `winapp ui`는 터미널에서 실행 중인 모든 Windows 앱(WPF, WinForms, Win32, Electron, WinUI3)에 대한 완전한 UI 자동화 액세스를 제공합니다.

가능한 작업:

- 모든 최상위 창 나열
- 창의 전체 UI 자동화 트리 탐색
- 이름, 유형 또는 자동화 ID로 요소 검색
- 클릭, 호출 및 값 설정
- 스크린샷 캡처
- 요소 나타날 때까지 대기 — 테스트 동기화에 이상적

`winapp ui`와 `winapp run`을 결합하면 터미널에서 완전한 빌드 → 시작 → 검증 워크플로우가 가능합니다. 에이전트가 앱을 실행하고, UI 상태를 검사하고, 프로그래밍 방식으로 상호작용하여 결과를 검증할 수 있습니다.

## 기타 새로운 기능

- **`winapp unregister`**: 완료 후 사이드로드된 패키지를 제거합니다.
- **`winapp manifest add-alias`**: 터미널에서 이름으로 앱을 시작하는 별칭을 추가합니다.
- **탭 자동완성**: 단일 명령으로 PowerShell 완성을 구성합니다.

## 설치 방법

```bash
winget install Microsoft.WinAppCli
# 또는
npm install -g @microsoft/winappcli
```

CLI는 공개 미리 보기 중입니다. 전체 문서는 [GitHub 저장소](https://github.com/microsoft/WinAppCli)를, 모든 세부 정보는 [원본 발표](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)를 참조하세요.
