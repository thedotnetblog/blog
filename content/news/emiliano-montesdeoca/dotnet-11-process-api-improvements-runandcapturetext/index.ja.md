---
title: ".NET 11がついにプロセスAPIを修正"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process が年来最大のアップデートを受けます。RunAndCaptureTextAsync、KillOnParentExit、SafeProcessHandle API、標準ハンドルのリダイレクトを完全制御 — デッドロックの定型コードはもう不要。"
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

プロセスを起動して出力をキャプチャする必要があった .NET 開発者は誰もが、同じ危険な定型コードの何らかのバリエーションを書いてきました：stdout の非同期読み取り、stderr の非同期読み取り、`WaitForExitAsync`、両方のストリームをドレインするのを忘れるとデッドロックが発生する。これは長年知られている落とし穴です。

.NET 11 がついにこれを適切に修正します。

## RunAndCaptureTextAsync

主要な追加：プロセスを起動し、stdout と stderr をキャプチャし、デッドロックなしに終了を待機する単一の静的メソッド。

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

1回の呼び出し。手動ストリームドレインなし。注意深く配置した `WaitForExit` なし。何かを実行してその出力を得るだけなら、これが求めていた API です。

出力をキャプチャせずに終了を待ちたい場合のために `Process.RunAsync` もあります。

## KillOnParentExit

起動されたプロセスでよくある問題：親プロセスがクラッシュまたは終了された場合、子プロセスはオーファンとして実行し続けます。`KillOnParentExit` を使用すると、プロセス起動時に親プロセスが終了したときに子プロセスも終了することをあらかじめ宣言できます。

この機能はプラットフォーム固有の方法（Windows ではジョブオブジェクト、Linux では prctl）で存在していましたが、.NET から使用するには p/invoke またはサードパーティライブラリが必要でした。今では `ProcessStartInfo` のファーストクラスのプロパティになりました。

## SafeProcessHandle ベースの API

新しい軽量 API サーフェスは、完全な `Process` クラスではなく `SafeProcessHandle` を中心に構築されています。完全な `Process` クラスは多くの状態を抱えており、トリムが困難です — `SafeProcessHandle` パスは出力サイズを最小化する必要があるアプリケーション（WASM、ネイティブ AOT）にとってよりトリマーフレンドリーです。

## ハンドル継承の完全制御

このアップデートでは、子プロセスが継承するハンドルと標準ハンドルのリダイレクト方法に対するきめ細かい制御も追加されます。以前は stdin/stdout/stderr をリダイレクトできましたが、OS レベルでどのハンドルを継承するかを正確に指定することはできませんでした。新しい API はそのコントロールを公開します。

## なぜ重要か

`Process` クラスはツール、ビルドシステム、テストランナー、および他の実行ファイルを呼び出すあらゆるアプリケーションで使用されています。古い API サーフェスは .NET Framework 時代のものであり、時代遅れになっていました。これは破壊的変更ではありません — 古い API は引き続き動作します — しかし新しいコードは新しいサーフェスを優先すべきです。

トリムされたアプリケーションや AOT コンパイルシナリオでは、`SafeProcessHandle` パスが特に歓迎されます。古い `Process` クラスはトリムを複雑にするリフレクション重いコードを多く持ち込んでいました。

元の記事: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
