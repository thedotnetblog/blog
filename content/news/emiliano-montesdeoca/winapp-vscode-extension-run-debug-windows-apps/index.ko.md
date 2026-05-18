---
title: "WinApp VS Code 확장: 편집기를 벗어나지 않고 Windows 앱 실행, 디버그 및 패키징"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "WinApp VS Code 확장은 전체 Windows 앱 개발 CLI를 VS Code에 직접 제공합니다. Visual Studio 없이 WPF, WinUI, .NET, C++ 앱을 패키지 ID로 실행, 디버그, 패키징, 서명할 수 있습니다."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기]({{< ref "index.md" >}})를 클릭하세요.*

VS Code에서 Windows 앱을 개발해본 적이 있다면, 그 순간을 알 것입니다. 좋아하는 편집기에서 코드를 작성하며 흐름을 타고 있는데 — 갑자기 Windows API를 위해 패키지 ID가 필요해집니다. 또는 MSIX를 만들거나 패키지에 서명해야 합니다. 그러면 Visual Studio를 열거나, 밤 11시에 "msix packaging without visual studio"를 검색하게 됩니다.

그 마찰은 이제 사라졌습니다. [WinApp VS Code 확장](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp)이 공개 프리뷰로 출시됐습니다 — 전체 [Windows App Development CLI](https://github.com/microsoft/WinAppCli)가 VS Code에 직접 통합되었습니다. 별도 설치 없이, Visual Studio 없이.

## F5로 패키지 ID

Windows API의 문제가 있습니다 — 알림, 백그라운드 작업, 온디바이스 AI 기능, 공유 대상 — 많은 것들이 앱에 **패키지 ID**가 있어야 합니다. 없으면 해당 API들이 단순히 작동하지 않습니다.

전통적으로 패키지 ID를 얻으려면 완전한 MSIX 설치 프로그램을 빌드하거나 Visual Studio에서 실행해야 했습니다. WinApp 확장은 사용자 지정 `winapp` 디버그 타입으로 이것을 완전히 바꿉니다.

`launch.json`에 이것을 추가하세요:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

F5를 누르세요. 확장이 빌드 출력과 매니페스트를 찾아, `winapp run`을 통해 앱에 패키지 ID를 부여하고, 디버거를 연결합니다. .NET 앱은 `coreclr` (C# Dev Kit 필요), C/C++는 `cppvsdbg`, Node/Electron은 기본 제공 디버거를 사용합니다.

F5를 누를 때마다 프로젝트가 자동으로 빌드되도록 `preLaunchTask`를 구성할 수 있습니다 — Visual Studio의 빌드-앤-론치 흐름과 동일하지만 VS Code에서입니다.

## 명령 팔레트에서 모든 것을

`Ctrl+Shift+P`를 열고 `WinApp`을 입력하면 전체 툴킷을 얻을 수 있습니다:

- **Initialize Project** — Windows SDK 및/또는 Windows App SDK로 프로젝트 구성
- **Run Application** — 패키지 ID가 있는 루즈 레이아웃 패키지 앱으로 실행
- **Create MSIX Package** — 인증서 및 런타임 옵션으로 앱 패키징
- **Update Manifest Assets** — 단일 소스 이미지에서 모든 필수 앱 아이콘 자동 생성
- **Generate / Install Certificate** — 개발 인증서 관리
- **Sign Package** — MSIX 또는 실행 파일 서명
- **Run SDK Tool** — `makeappx`, `signtool`, `mt` 또는 `makepri` 직접 실행

WinApp CLI도 따로 설치할 필요가 없습니다. 확장에 번들로 포함됩니다.

## 여러 프레임워크에서 작동

.NET WPF/WinUI 전용 도구가 아닙니다. 확장은 다음과 함께 작동합니다:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

이 범위는 의도적입니다. VS Code는 웹 및 크로스플랫폼 개발자들이 사는 곳입니다. Windows 패키징이 필요한 Tauri 또는 Electron 앱을 개발하고 있다면, 이 확장이 Visual Studio를 채택하지 않고도 커버해줍니다.

## .NET 개발자에게 중요한 이유

저는 VS Code에서 많이 작업합니다 — Markdown을 작성하고, 구성을 관리하고, 소규모 프로젝트를 편집하고, 터미널을 실행하는 곳입니다. 하지만 .NET Windows 데스크톱 작업에서는 패키징 관련 작업이 필요한 순간 Visual Studio가 유일한 실제 선택지였습니다.

이 확장이 그 갭을 메웁니다. 이제 VS Code를 떠나지 않고 완전한 .NET Windows 데스크톱 개발 사이클을 가질 수 있습니다 — 편집, 빌드, 패키지 ID로 실행, 디버그, 패키징, 서명. 이는 진정한 삶의 질 향상입니다.

## 시작하기

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

또는 확장 보기(`Ctrl+Shift+X`)에서 **WinApp**을 검색하세요.

요구 사항:
- Windows 10 이상
- VS Code 1.109.0 이상
- 앱 언어에 맞는 디버거 확장

자세한 내용은 [Chiara Mooney의 전체 발표](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/)를 읽어보세요.

## 마무리

WinApp VS Code 확장은 VS Code를 사용하면서 패키징 작업을 위해 Visual Studio로 전환해야 했던 .NET Windows 데스크톱 개발자에게 환영받는 추가 기능입니다. F5로 패키지 ID, 명령 팔레트에서 MSIX 패키징, 기본 제공 인증서 관리 — 이것이 올바른 기능 조합입니다.

다음 WPF 또는 WinUI 프로젝트에서 시도해보세요. 지금까지 우회해온 마찰이 훨씬 작아졌습니다.
