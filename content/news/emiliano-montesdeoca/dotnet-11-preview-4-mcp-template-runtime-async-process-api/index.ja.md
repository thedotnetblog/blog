---
title: ".NET 11 Preview 4: MCPサーバー テンプレート、Runtime-Async ライブラリ、プロセス API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 がリリースされました。注目点: SDK の MCP サーバー テンプレート、runtime-async でコンパイルされたランタイム ライブラリ、モバイル向け dotnet watch、プロセス API の大幅な拡張。"
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 が利用可能になりました。.NET の主要プレビューの各リリースでは、ランタイム、SDK、ライブラリ、ASP.NET Core、MAUI、C#、Entity Framework にわたる長いリストの変更が追加されます。完全なリストを繰り返す代わりに、私が注目した点を紹介します。

## .NET SDK に MCP サーバー テンプレートが追加

最も興味深い点: MCP サーバー プロジェクト テンプレートが SDK に含まれるようになりました。つまり、`dotnet new mcp-server`（またはコマンドの最終名）がそのまま動作します。.NET で MCP ツールを構築している方にとって、初期設定の手間が大幅に減ります。プラットフォームの toolchain への MCP 統合は、エコシステムの進む方向を示しています。

## Runtime-Async でコンパイルされたランタイム ライブラリ

ランタイム自体が標準ライブラリを runtime-async 機能を使ってコンパイルするようになりました。これはパフォーマンスに影響する内部変更です — ランタイムの async 状態マシンがより効率的になります。ここでの重要性は、目に見える API の変更にあるのではなく、runtime-async が BCL 自体に使用できるほど成熟しているという点であり、機能の準備状況について意味のあるシグナルです。

## JIT 最適化とハードウェア イントリンシック

Preview 4 では JIT の改善が継続されています。ハードウェア イントリンシックとコード生成の改善が含まれています — 詳細はランタイムのリリース ノートをご確認ください。このような変更は通常、コードを変更せずに計算量の多いループのスループットを改善します。

## プロセス API の大幅な拡張

Preview 4 では `System.Diagnostics.Process` に大きな更新が加えられます:

- `Process.RunAndCaptureTextAsync` — プロセスを開始し、stdout/stderr をキャプチャし、終了を待機。デッドロックのリスクなしに 1 つの呼び出しで完結
- `KillOnParentExit` — 親プロセスと子プロセス間の軽量なライフタイム結合
- トリマーフレンドリーな `SafeProcessHandle` ベースの API

デッドロックを起こさずにプロセス出力をキャプチャするためのボイラープレートを書いたことがある方（stdout *と* stderr の非同期読み取りを同時に行う）、`RunAndCaptureTextAsync` はまさに求めていた API です。

## Android と iOS 向けの dotnet watch

`dotnet watch` が .NET MAUI の Android および iOS プロジェクトのデバイス選択をサポートするようになりました。ビルド ループでデバイス接続を手動で管理せずに、モバイルでより速い反復が可能になります。

## Span ベースの圧縮 API

新しい span ベースの Deflate、ZLib、GZip エンコーダー/デコーダー API がライブラリに追加されます。圧縮データを扱う際のアロケーションが削減されます — 高スループットのデータ処理を行っている場合に関係します。

## 試してみる

[.NET 11 Preview 4 をダウンロード](https://dotnet.microsoft.com/download/dotnet/11.0) — プレビュー版であり、本番環境向けではありませんが、RC サイクル前に問題を早期発見するためプロジェクトで試してみる価値があります。

元の投稿: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
