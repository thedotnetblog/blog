---
title: "azd update — 모든 패키지 매니저를 지배하는 하나의 명령어"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI에 설치 방법에 관계없이 작동하는 범용 업데이트 명령어가 추가되었습니다 — winget, Homebrew, Chocolatey, 설치 스크립트 모두 지원."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "azd-update-universal-upgrade-command.md" >}})를 참조하세요.*

몇 주마다 뜨는 "새로운 버전의 azd를 사용할 수 있습니다" 메시지 아시죠? `azd`를 winget으로 설치했는지, Homebrew인지, 아니면 6개월 전에 실행한 curl 스크립트인지 기억이 안 나서 그냥 무시하게 되는 그 메시지요. 드디어 해결됐습니다.

Microsoft가 [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/)를 출시했습니다 — 원래 어떤 방법으로 설치했든 상관없이 Azure Developer CLI를 최신 버전으로 업데이트하는 단 하나의 명령어입니다. Windows, macOS, Linux — 상관없습니다. 명령어 하나면 됩니다.

## 작동 방식

```bash
azd update
```

이게 전부입니다. 새로운 기능을 미리 체험하고 싶다면 일일 Insiders 빌드로 전환할 수 있습니다:

```bash
azd update --channel daily
azd update --channel stable
```

이 명령어는 현재 설치 방법을 감지하고 내부적으로 적절한 업데이트 메커니즘을 사용합니다. 더 이상 "잠깐, 이 컴퓨터에서 winget을 썼었나, choco였나?" 고민할 필요 없습니다.

## 한 가지 참고사항

`azd update`는 버전 1.23.x부터 제공됩니다. 이전 버전을 사용 중이라면 원래 설치 방법으로 마지막 수동 업데이트를 한 번만 해주면 됩니다. 그 이후로는 `azd update`가 모든 것을 처리합니다.

`azd version`으로 현재 버전을 확인하세요. 새로 설치가 필요하다면 [설치 문서](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)를 참고하세요.

## 왜 중요한가

작은 삶의 질 개선이지만, AI 에이전트와 Aspire 앱을 Azure에 배포하기 위해 매일 `azd`를 사용하는 우리에게 최신 상태를 유지한다는 것은 "그 버그는 최신 버전에서 이미 수정됐습니다"라는 순간이 줄어든다는 의미입니다. 신경 쓸 일이 하나 줄어드는 거죠.

[전체 발표](https://devblogs.microsoft.com/azure-sdk/azd-update/)와 Jon Gallant의 [상세 분석](https://blog.jongallant.com/2026/04/azd-update)에서 자세한 내용을 확인하세요.
