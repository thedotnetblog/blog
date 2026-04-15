---
title: ".NET 2026年4月服务更新 — 你今天就该应用的安全补丁"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "2026年4月的服务更新修补了 .NET 10、.NET 9、.NET 8 和 .NET Framework 中的6个CVE — 其中包括两个远程代码执行漏洞。"
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}})。*

.NET 和 .NET Framework 的 [2026年4月服务更新](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) 已发布，这次包含了你需要尽快应用的安全修复。共修补了六个CVE，其中包括两个远程代码执行（RCE）漏洞。

## 修补内容

快速总结如下：

| CVE | 类型 | 影响范围 |
|-----|------|----------|
| CVE-2026-26171 | 安全功能绕过 | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **远程代码执行** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **远程代码执行** | .NET 10, 9, 8 |
| CVE-2026-32203 | 拒绝服务 | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | 拒绝服务 | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | 拒绝服务 | .NET Framework 2.0–4.8.1 |

两个RCE CVE（CVE-2026-32178 和 CVE-2026-33116）影响范围最广，应当优先处理。

## 更新版本

- **.NET 10**：10.0.6
- **.NET 9**：9.0.15
- **.NET 8**：8.0.26

均可通过常规渠道获取 — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0)、MCR上的容器镜像以及Linux包管理器。

## 应该怎么做

将你的项目和CI/CD管道更新到最新的补丁版本。如果你在运行容器，拉取最新的镜像。如果你在使用 .NET Framework，请查看 [.NET Framework 发行说明](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) 获取对应的补丁。

对于在生产环境运行 .NET 10 的用户（这是当前版本），10.0.6 是必须更新的。.NET 9.0.15 和 .NET 8.0.26 也是如此，如果你在使用这些LTS版本的话。两个RCE漏洞可不是你能拖延的事情。
