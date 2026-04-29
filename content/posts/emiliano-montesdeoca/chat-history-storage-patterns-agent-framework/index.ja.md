---
title: "あなたのエージェントはどこで物事を覚えているか？チャット履歴ストレージの実践ガイド"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "サービス管理かクライアント管理か？線形か分岐型か？AIエージェントが実際に何ができるかを決める重要なアーキテクチャ上の決定。C#とPythonのコード例付き。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

AIエージェントを構築する際、ほとんどのエネルギーをモデル、ツール、プロンプトに費やします。*会話履歴がどこに保存されるか*という問題は実装の詳細に見えますが、実は最も重要なアーキテクチャ上の決定の一つです。

これにより、ユーザーが会話を分岐させたり、回答を元に戻したり、再起動後にセッションを再開したりできるかどうか、そしてデータがインフラから出るかどうかが決まります。[Agent FrameworkチームはLデープな分析を公開しました](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/)。

## 2つの基本パターン

**サービス管理型**: AIサービスが会話状態を保存します。アプリは参照（スレッドID、レスポンスID）を保持し、サービスは各リクエストに関連する履歴を自動的に含めます。

**クライアント管理型**: アプリが完全な履歴を管理し、各リクエストに関連メッセージを送信します。サービスはステートレスです。すべてを制御できます。

## Agent Frameworkによる抽象化

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("私の名前はAliceです。", session);
var second = await agent.RunAsync("私の名前は何ですか？", session);
```

```python
session = agent.create_session()
first = await agent.run("私の名前はAliceです。", session=session)
second = await agent.run("私の名前は何ですか？", session=session)
```

セッションが基礎的な違いを処理します。プロバイダーを切り替えてもアプリケーションコードは変わりません。

## プロバイダー早見表

| プロバイダー | ストレージ | モデル | 圧縮 |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | クライアント | N/A | 開発者 |
| Foundry Agent Service | サービス | 線形 | サービス |
| Responses API（デフォルト） | サービス | 分岐型 | サービス |
| Anthropic Claude, Ollama | クライアント | N/A | 開発者 |

## 選び方

1. **会話の分岐や「やり直し」が必要？** → サービス管理型のResponses API
2. **データ主権が必要？** → データベースバックドプロバイダーのクライアント管理型
3. **シンプルなチャットボット？** → サービス管理型の線形で十分

[完全な記事](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/)で意思決定ツリー全体を確認してください。
