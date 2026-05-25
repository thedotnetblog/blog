---
title: ".NET 10 の NuGet パッケージ pruning は、あらゆる場面で効果を感じる改善だ"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: ".NET 10 の新しい NuGet パッケージ pruning は、誤検知の脆弱性レポートを減らし、restore グラフを簡潔にし、restore のパフォーマンスを改善する。これは、日々の作業を静かに良くしてくれるタイプのプラットフォーム変更だ。"
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *この記事は自動翻訳です。原文は[こちら]({{< ref "index.md" >}})。*

プラットフォームの改善には、新しいシナリオを開くからワクワクするものがあります。

一方で、既存のワークフローをより静かに、より壊れにくく、より煩わしさの少ないものにしてくれるからワクワクする改善もあります。

**.NET 10 の NuGet パッケージ pruning** は、明らかに後者です。しかも、それは褒め言葉です。

## なぜ重要なのか

トランジティブな脆弱性のノイズ、不要に大きい restore グラフ、あるいは技術的には存在しているもののアプリが使うランタイムには実際には関係ないパッケージに悩まされたことがあるなら、この変更はまさに現実の痛点に触れています。

pruning は、ランタイムがすでに提供している platform-provided packages を有効な依存関係グラフから取り除くことで役立ちます。

それによって得られるものは次のとおりです。

- 誤検知の脆弱性レポートの削減
- よりきれいなトランジティブ依存関係グラフ
- restore オーバーヘッドの低減
- より実行可能な audit 結果

## 私の見解

これは、まさに私が好きな .NET の改善です。

既定値をより良くし、頭の中の負担を減らし、セキュリティシグナルの品質と日々の tooling の振る舞いの両方を改善してくれます。

keynote のスライドにならなくても、それは十分に勝利です。

Original post: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
