---
title: "Microsoft Foundry 2026年4月: Foundry Local GA、GPT-5.5、HyperlightによるCodeAct"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "4月のFoundryまとめは盛りだくさん：Foundry LocalがGAに、GPT-5.5が登場、Agent FrameworkがOpenTelemetryトレーシングを取得、CodeActがHyperlight マイクロVMでPythonを実行、エージェント監視ダッシュボードが登場。"
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Microsoft Foundryにとって忙しい月でした。最も重要なアナウンスをご紹介します。

## Foundry Localが一般提供開始

Foundry Local — MicrosoftのクロスプラットフォームのローカルAIランタイム — がWindows、macOS（Apple Silicon）、Linux x64でプレビューからGAになりました。開発者向けSDKを備えた、本番環境対応のローカルモデル推論です。バージョン1.1では文字起こし、embeddings、Responses APIのサポートが追加されています。

## GPT-5.5

GPT-5ファミリーの最新モデルがFoundryで利用可能になりました。Tier 5およびTier 6サブスクリプションのデフォルトクォータ。以前のGPT-5バリアントで作業していた場合、ユースケースに合わせて評価する価値があります。

## FoundryでのAgent Frameworkトレーシング

今月、2つのトレーシング機能がプレビューとして提供されます：

**Microsoft Agent Frameworkトレーシング** — MAFエージェントがFoundryにOpenTelemetryトレースを送信できるようになりました。エージェントの動作をデバッグし、多段階実行をトレースし、ツール呼び出し全体の遅延とエラーを表面化させます。これは実際のギャップを埋めます：何を返したかだけでなく、*エージェントが本番で実際に何をしたか*を知ること。

**ホステッドエージェントトレーシング** — ホステッドエージェントのセッション、ツール呼び出し、実行ステップもFoundryトレースに表示されます。同じオブザーバビリティストーリーがホステッドティアにも拡張されます。

## HyperlightによるCodeAct（Alpha）

これは技術的に最も興味深い追加機能です：Agent Frameworkが[Hyperlight](https://github.com/hyperlight-dev/hyperlight)マイクロ仮想マシン内でPythonコードを実行できるようになりました。

CodeActはエージェントがツールとしてPythonコードを生成して実行するパターンです。明らかな懸念はセキュリティ — モデルが生成したコードを実行しています。HyperlightのマイクロVMはネイティブに近い起動時間でプロセスレベルの隔離を提供し、フルコンテナやVMのオーバーヘッドなしでサンドボックスコード実行を実用的にします。

コード実行が必要なエージェントワークフローにとって、これはホストプロセスでコードを実行するよりも大幅なセキュリティ改善です。

## エージェント監視ダッシュボード（プレビュー）

トークン使用量、遅延、実行成功率、エバリュエータースコアを1つのビューに組み合わせた統合オペレーションダッシュボード。通常のオブザーバビリティダッシュボードとの違い：オペレーションメトリクスとともに評価結果が含まれているため、「エージェントが遅くなっている」と「エバリュエータースコアが下がった」を相関させたり、関係ないことを確認したりできます。

## 継続的評価カスタムエバリュエーター（プレビュー）

独自のコードベースまたはプロンプトベースのエバリュエーターを継続的評価パイプラインに持ち込めるようになりました。以前は、継続的評価は組み込みエバリュエーターに限定されていました。カスタムエバリュエーターを使用すると、本番監視ループでチーム固有の品質基準を適用できます。

## コントロールプレーンのエージェントインベントリ

FoundryコントロールプレーンのOperate ビューで、サブスクリプション全体のすべてのサポートされているエージェントが表示されるようになりました：Foundryエージェント、Azure SRE Agent、Logic Appsエージェントループ、および登録済みカスタムエージェント。何がどこにデプロイされているかを把握するための1つのビュー。

元の投稿：[What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
