---
title: "NuGet package pruning в .NET 10 — это такое улучшение, которое ощущается везде"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Новое NuGet package pruning в .NET 10 уменьшает число ложноположительных отчётов о уязвимостях, упрощает restore graph и повышает производительность restore. Это одно из тех изменений платформы, которые тихо делают повседневную работу лучше."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

*Эта статья была автоматически переведена. Оригинал доступен [здесь]({{< ref "index.md" >}}).*

Некоторые улучшения платформы интересны потому, что открывают новые сценарии.

Другие интересны потому, что делают существующие workflows менее шумными, менее хрупкими и менее раздражающими.

**NuGet package pruning в .NET 10** явно относится ко второй категории, и я говорю это как комплимент.

## Почему это важно

Если вы когда-либо сталкивались с шумом от transitive vulnerability reports, слишком большими restore graphs или пакетами, которые технически присутствуют, но на самом деле не важны для runtime, который использует ваше приложение, это изменение решает реальную pain point.

Pruning помогает, удаляя из effective dependency graph пакеты, предоставляемые платформой, когда runtime уже предоставляет их сам.

Это означает:

- меньше ложноположительных отчётов о уязвимостях
- более чистые transitive dependency graphs
- меньший restore overhead
- более actionable audit results

## Моё мнение

Именно такие улучшения .NET мне нравятся.

Они делают defaults лучше, уменьшают mental overhead и улучшают как качество security signal, так и поведение tooling в повседневной работе.

Это победа, даже если она никогда не попадёт на keynote slide.

Оригинал: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
