---
title: "Visual Studio の中で pull request をレビューできるのは、まさに私が好きな摩擦軽減です"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "Visual Studio は今や IDE を離れずに pull request を最初から最後までレビューできます。これは段階的に見えるかもしれませんが、Visual Studio に一日中いるチームにとっては、不要なコンテキスト切り替えをかなり減らします。"
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *この記事は自動翻訳されています。原文は[こちら]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}})をご覧ください。*

ブラウザは、コードレビューのワークフローからあまりにも長く、あまりにも多くを奪ってきました。

だからこそ、Visual Studio が **IDE の中で最初から最後まで pull request をレビューする** 方向へさらに進んでいるのを見るのは、とても嬉しいです。

これは大きな見出しを作るタイプの機能ではないかもしれませんが、日々の開発を確実に良くしてくれます。

## 主な価値は単純です。コンテキスト切り替えが減ること

レビューのループが IDE とブラウザの両方にまたがっていると、摩擦が積み重なります。

- 別の場所で PR を開く
- あるツールで変更を確認する
- より深く調べるために solution に戻る
- コメントや承認のためにまた切り替える

それは致命的ではありません。ただ非効率なだけです。

Visual Studio が、同じ作業環境から PR を開き、確認し、コメントし、承認し、マージできるなら、それは本当の生産性向上です。

## "checkout せずにレビュー" は特にいい機能です

私が特に気に入っているのは、PR ブランチを checkout せずにレビューできる点です。

小さく聞こえるかもしれませんが、次のような場面にぴったりです。

- 素早いレビュー
- 割り込みベースのフィードバック依頼
- 現在のブランチとローカル状態をそのまま保つこと

これはまさに、優れたコードレビュー ツールに必要な柔軟性です。

## 私見

これは革命的な機能ではありません。

もっと良いものです。実用的な機能です。

Visual Studio で一日の大半を過ごすチームにとって、PR レビューのサポートが強化されることは、ワークフローの中断を減らし、確認から行動までをより滑らかにします。

それは十分に価値のある改善だと思います。

原文: [Visual Studio を離れずに pull request をレビューする](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)