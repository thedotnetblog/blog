---
title: "Microsoft Agent Framework パート3：ツールからワークフローへ — ビルディングブロックがカチッとはまる"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: ".NET AIビルディングブロックシリーズのパート3では、Microsoft Agent Frameworkを取り上げます — ツールを持つ単一エージェントからメモリを持つマルチエージェントワークフローまで。本当に重要なことを解説します。"
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})からご覧いただけます。*

.NETのBuilding Blocks for AIシリーズを追っているなら、パート1が`IChatClient`（ユニバーサルモデルインターフェース）を、パート2が`Microsoft.Extensions.VectorData`（セマンティック検索とRAG）を提供したことはご存知でしょう。どちらも基礎的で、単体でも有用です。しかし、ここからすべてがつながり始めます。

パート3は[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)についてです — 正直に言うと、.NETで実現されるのを待ち望んでいたピースです。1.0は4月にリリースされました。APIは安定しています。本物のエージェントを構築する時が来ました。

## エージェントとは何か（チャットボットとの違い）

コードに入る前に、この区別を明確にしておきましょう。チャットボットはインプットを受け取り、モデルを呼び出し、アウトプットを返します。シンプルなループです。

エージェントには*自律性*があります。タスクについて推論し、どのツールを使うかを決定し、それを呼び出し、結果を評価し、次に何をすべきか決定できます — すべてのシナリオに対してステップバイステップのロジックを書く必要はありません。ツールと指示を与えれば、オーケストレーションを自分で処理します。

こう考えてみてください：`IChatClient`は会話を持つことのようなものです。エージェントはタスクリストを誰かに委任するようなものです。

## 10行で書く最初のエージェント

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

`.AsAIAgent()`拡張メソッドがブリッジです。MEAIの`.AsIChatClient()`と同じパターン — プロバイダーのSDKを安定した抽象化でラップします。Azure OpenAI、OpenAI、GitHub Models、Microsoft Foundry、またはローカルモデルで動作します。

ストリーミングも機能します：

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## エージェントにツールを与える

ここでエージェントが高度なチャットボットから脱却します。ツールはユーザーの要求に基づいてモデルが呼び出しを決定できる関数です。ルーティングロジックは不要 — モデルが自分で判断します。

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

2つのことに注目してください。まず、`AIFunctionFactory`はMEAIから来ています — 通常の`IChatClient`で使うのと同じツールファクトリーです。チャットシナリオ用にすでにツールを定義している場合、ここでも機能します。

次に、`Description`属性は非常に重要です。これがモデルがツールの機能と使用タイミングを理解する方法です。人間ではなくAIへのドキュメントとして扱ってください。

## セッション：本当に記憶する会話

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

セッションなしでは、各`RunAsync`呼び出しはステートレスです。セッションありでは、エージェントはどのジョークを指しているかを知っています。`AgentSession`はターン間で会話履歴を保持します。

本番ステートレスサービスでは、セッションはクリーンにシリアライズできます：

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... どこかに保存する ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

エージェントがサーバーレスまたは水平スケール環境で動作する場合、これは非常に重要です。

## AIContextProvider：セッションをまたいだ永続的メモリ

セッションはセッション*内*の会話履歴を保持します。しかし、セッション間でユーザーのことを知ることは？`AIContextProvider`がそれを処理します。

2つのフックがあります：
- **`ProvideAIContextAsync`** — 各インタラクションの*前*に実行され、エージェントにコンテキストを注入する
- **`StoreAIContextAsync`** — 各インタラクションの*後*に実行され、学習と永続化を可能にする

パターンはエレガントです：複数のプロバイダーを積み重ねることができます — ユーザー設定用、最近のインタラクション用、関連ドキュメントのVectorDataストアを照会するものなど。最後のものは、パート2のRAGパターンそのもので、今やすべてのエージェント呼び出しで自動的に実行されます。

## マルチエージェントワークフロー

ここでフレームワークがその名前を証明します。エグゼキューター（エージェント、関数、何でも）がエッジを介して接続するグラフベースのワークフローシステムを含みます。

ネイティブでサポートされているパターン：

- **シーケンシャル**：エージェントAの出力がエージェントBに流れる
- **コンカレント（ファンアウト/ファンイン）**：複数のエージェントに並列ディスパッチ、結果を収集
- **条件付きルーティング**：出力に基づいて異なるエージェントに作業をルーティング
- **ライター-クリティックループ**：一方のエージェントが書き、もう一方が評価し、承認までループ
- **サブワークフロー**：ワークフローを階層的に構成

ライター-クリティックの例：

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

クリーンで読みやすく、条件ベースのルーティングによりループロジックを自分で書く必要がありません。

## ヒューマン・イン・ザ・ループ

すべてが完全に自律的に実行されるべきではありません。センシティブな操作 — データベースへの書き込み、金融トランザクション、通信の送信 — には、エージェントが実行する前に人間の承認が必要です。

フレームワークには`FunctionApprovalRequestContent`と`FunctionApprovalResponseContent`を介したサポートが組み込まれています。エージェントがツール呼び出しを提案し、アプリケーションコードがユーザーに提示し、レスポンスが実行を続けるかどうかを決定します。

これがエンタープライズ環境でエージェントについて考える正しい方法です：完全な自律ではなく、*ガードレール付きの自律性*。

## 全体像

少し引いて見ると：

- **MEAI**はどのモデルへの普遍的インターフェースを提供
- **VectorData**はセマンティック検索を通じて組織の知識へのアクセスをエージェントに提供
- **Agent Framework**はすべてをオーケストレート — 内部で`IChatClient`を使用し、コンテキストプロバイダーと組み合わせ、ワークフローを通じて調整

各ピースは他のものと組み合わせられるように設計されています。[Jeremy Likness の元の投稿](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/)と[Agent Framework GitHubリポジトリ](https://github.com/microsoft/agent-framework/tree/main/dotnet)で完全なサンプルをご確認ください。

## まとめ

Microsoft Agent Framework パート3の投稿は、ビルディングブロックシリーズのループを閉じます。ツールを使い、物事を記憶し、調整する本物のエージェントを構築したい.NET開発者にとって、これが前進への道です。

安定版1.0リリースは、これを本番環境で構築できることを意味します。.NETでのエージェント開発に飛び込むのを待っていたなら、今がその時です。
