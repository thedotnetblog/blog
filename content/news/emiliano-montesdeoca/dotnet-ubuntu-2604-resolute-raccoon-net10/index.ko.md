---
title: ".NET 10이 Ubuntu 26.04 LTS에 탑재됐다 — 새로운 것들"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon)가 .NET 10을 일급 도구체인으로 탑재했습니다. Native AOT, Chiseled 컨테이너, Linux 7.0."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*이 게시물은 자동 번역되었습니다. 원문을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

Ubuntu LTS의 날입니다. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon)이 오늘 출시됐으며, 모든 Ubuntu LTS처럼 최신 .NET LTS — 이번에는 [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) — 을 탑재합니다.

## .NET 10을 두 명령으로 설치

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET은 [Ubuntu에서 공식 지원하는 도구체인](https://ubuntu.com/toolchains) 중 하나입니다.

## 컨테이너: `-noble`을 `-resolute`로 업데이트

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

## Native AOT: 3ms 시작, 1.4MB 바이너리

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# 1.4MB 네이티브 바이너리, 3ms 시작
```

콜드 스타트 시간이 중요한 클라우드 네이티브 워크로드 — Functions, 컨테이너, 서버리스 — 에서 진정한 게임 체인저입니다.

## .NET 8 또는 9가 필요한가요?

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[전체 게시물](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/)에서 cgroup v2, 포스트-퀀텀 암호화, Linux 7.0에 대한 자세한 내용을 확인하세요.
