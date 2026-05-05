---
title: "Microsoft Agent Frameworkが1.0に到達 — .NET開発者にとって本当に重要なこと"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0が安定したAPI、マルチエージェントオーケストレーション、主要AIプロバイダー向けコネクタを備えて本番環境対応になりました。.NET開発者として知っておくべきことをまとめます。"
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *この記事は自動翻訳されています。原文は[こちら]({{< ref "agent-framework-1-0-production-ready.md" >}})をご覧ください。*

Semantic KernelやAutoGenの初期からAgent Frameworkの歩みを追ってきた方にとって、今回のニュースは大きいです。Microsoft Agent Frameworkが[バージョン1.0に到達](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)しました — 本番環境対応、安定したAPI、長期サポートのコミットメント。.NETとPythonの両方で利用可能で、実際のワークロードに本当に対応できる状態です。

発表のノイズを切り抜けて、.NETでAI搭載アプリを構築している方にとって重要なポイントに集中しましょう。

## 短いまとめ

Agent Framework 1.0は、かつてSemantic KernelとAutoGenだったものを単一のオープンソースSDKに統合します。1つのエージェント抽象化。1つのオーケストレーションエンジン。複数のAIプロバイダー。エンタープライズパターン向けのSemantic Kernelと研究グレードのマルチエージェントワークフロー向けのAutoGenを行き来していた方は、もうその必要はありません。これが唯一のSDKです。

## はじめるのはほぼ不公平なほど簡単

.NETで動作するエージェントはこちら：

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

これだけです。数行でAzure Foundryに対して実行されるAIエージェントが完成します。Pythonの同等コードも同様に簡潔です。関数ツール、マルチターン会話、ストリーミングは必要に応じて追加できます — APIサーフェスは奇妙になることなくスケールアップします。

## マルチエージェントオーケストレーション — これが本題

単一エージェントはデモには十分ですが、本番シナリオには通常、調整が必要です。Agent Framework 1.0は、Microsoft ResearchとAutoGenから直接もたらされた実戦テスト済みのオーケストレーションパターンを搭載しています：

- **シーケンシャル** — エージェントが順番に処理（ライター → レビュアー → エディター）
- **コンカレント** — 複数のエージェントに並列で展開し、結果を収束
- **ハンドオフ** — 1つのエージェントがインテントに基づいて別のエージェントに委任
- **グループチャット** — 複数のエージェントが議論し、解決策に収束
- **Magentic-One** — MSRの研究グレードのマルチエージェントパターン

すべてがストリーミング、チェックポイント、ヒューマンインザループの承認、一時停止/再開をサポートしています。チェックポイントの部分は重要です — 長時間実行されるワークフローがプロセスの再起動を生き延びます。Azure Functionsで耐久性のあるワークフローを構築してきた.NET開発者にとって、これは馴染みのある感覚です。

## 最も重要な機能

知っておく価値があるものの私のリストはこちら：

**ミドルウェアフック。** ASP.NET Coreにミドルウェアパイプラインがあるのをご存知ですか？同じコンセプトですが、エージェント実行用です。すべてのステージをインターセプト — コンテンツセーフティ、ロギング、コンプライアンスポリシーを追加 — エージェントのプロンプトに触れることなく。これがエージェントをエンタープライズ対応にする方法です。

**プラガブルメモリ。** 会話履歴、永続的なキーバリューステート、ベクトルベースの検索。バックエンドを選択：Foundry Agent Service、Mem0、Redis、Neo4j、またはカスタム実装。メモリは、ステートレスなLLM呼び出しを、実際にコンテキストを覚えているエージェントに変えるものです。

**宣言的YAMLエージェント。** エージェントの指示、ツール、メモリ、オーケストレーショントポロジーをバージョン管理されたYAMLファイルで定義します。単一のAPI呼び出しでロードして実行。これは、コードを再デプロイせずにエージェントの動作をイテレーションしたいチームにとってゲームチェンジャーです。

**A2AとMCPサポート。** MCP（Model Context Protocol）により、エージェントは外部ツールを動的に発見して呼び出すことができます。A2A（Agent-to-Agentプロトコル）はクロスランタイムコラボレーションを実現します — .NETエージェントは他のフレームワークで実行されているエージェントと連携できます。A2A 1.0サポートは近日対応予定です。

## 注目すべきプレビュー機能

1.0ではいくつかの機能がプレビューとして出荷されました — 機能は動作しますがAPIは変更される可能性があります：

- **DevUI** — エージェントの実行、メッセージフロー、ツール呼び出しをリアルタイムで可視化するブラウザベースのローカルデバッガー。Application Insightsのようなものですが、エージェントの推論用です。
- **GitHub Copilot SDKとClaude Code SDK** — オーケストレーションコードから直接CopilotまたはClaudeをエージェントハーネスとして使用。同じワークフロー内の他のエージェントと一緒にコーディング対応エージェントを構成できます。
- **Agent Harness** — エージェントにシェル、ファイルシステム、メッセージングループへのアクセスを提供するカスタマイズ可能なローカルランタイム。コーディングエージェントや自動化パターンを想像してください。
- **Skills** — エージェントに構造化された機能をすぐに提供する再利用可能なドメイン機能パッケージ。

## Semantic KernelまたはAutoGenからの移行

既存のSemantic KernelまたはAutoGenコードがある場合、コードを分析してステップバイステップの移行プランを生成する専用の移行アシスタントがあります。[Semantic Kernel移行ガイド](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel)と[AutoGen移行ガイド](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen)がすべてを案内してくれます。

RCパッケージを使用していた場合、1.0へのアップグレードはバージョン番号の変更だけです。

## まとめ

Agent Framework 1.0は、エンタープライズチームが待ち望んでいた本番環境のマイルストーンです。安定したAPI、マルチプロバイダーサポート、実際に大規模に機能するオーケストレーションパターン、そしてSemantic KernelとAutoGenの両方からの移行パス。

フレームワークは[GitHubで完全にオープンソース](https://github.com/microsoft/agent-framework)で、`dotnet add package Microsoft.Agents.AI`で今日から始められます。[クイックスタートガイド](https://learn.microsoft.com/en-us/agent-framework/get-started/)と[サンプル](https://github.com/microsoft/agent-framework)をチェックして、実際に触ってみてください。

「本番環境で安全に使える」というシグナルを待っていた方へ — これがそのシグナルです。
