---
title: ".NET 10 中的 NuGet package pruning 是那种你会在各处都感受到的改进"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 中新的 NuGet package pruning 可以减少误报的漏洞报告，简化 restore graph，并提升 restore 性能。它是那种会悄悄让日常工作更好的平台变化。"
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *本文已自动翻译。原文请[点击这里]({{< ref "index.md" >}})。*

有些平台改进之所以令人兴奋，是因为它们打开了新的场景。

而另一些改进之所以令人兴奋，是因为它们让现有 workflow 更少噪音、更不脆弱，也更不烦人。

**.NET 10 中的 NuGet package pruning** 明显属于第二类，而且我这是在夸它。

## 为什么这很重要

如果你曾经处理过 transitive vulnerability noise、过大的 restore graph，或者那些技术上存在但对你的应用所用 runtime 并不真正相关的 package，那么这个变化正好击中了真实的痛点。

Pruning 会在 runtime 已经提供平台包时，把这些 platform-provided packages 从有效 dependency graph 中移除。

这意味着：

- 更少的误报漏洞报告
- 更干净的 transitive dependency graphs
- 更少的 restore overhead
- 更可操作的 audit 结果

## 我的看法

这正是我喜欢的那种 .NET 改进。

它让默认值更好，减少 mental overhead，并同时改善 security signal quality 和日常 tooling 行为。

这就是一种胜利，即使它从来不会出现在 keynote slide 上。

原文： [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
