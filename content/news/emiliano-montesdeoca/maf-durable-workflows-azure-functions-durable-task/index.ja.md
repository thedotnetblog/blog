---
title: "Microsoft Agent Frameworkにおける永続的ワークフロー：In-MemoryからAzure Functionsへ"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAFのワークフロープログラミングモデルがDurable Taskによる永続的実行をサポートするようになりました。プロセス再起動を乗り越えAzure Functions上でスケールする、組み合わせ可能なエージェントワークフローの構築方法を紹介します。"
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

初期のAIエージェントワークフローの問題点のひとつ：脆弱性です。単一プロセスに縛られた長時間実行のマルチステップワークフローは、プロセス再起動 = 状態喪失を意味します。シンプルなデモには問題ありませんが、本番ワークロードには向きません。

Microsoft Agent FrameworkのワークフロープログラミングモデルがAzure Functionsホスティングでのdurable task フレームワークによる**永続的実行**をサポートするようになりました。プログラミングモデルの仕組みと、永続性の重要性について説明します。

## 基本的な構成要素

**Executor**は作業の基本単位です。各Executorは型付きで、特定の入力を受け取り、特定の出力を生成します：

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // 注文を検索して返す
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflow**はFluentビルダーを使ってExecutorを有向グラフに接続します。フレームワークが実行、ステップ間のデータフロー、エラー伝播を処理します。

モデル化できるもの：
- 順次チェーン（ステップA → ステップB → ステップC）
- 並列Fan-out/Fan-in（エージェントA、B、Cを並列実行して結果を集約）
- 条件分岐
- ヒューマン・イン・ザ・ループ承認（ワークフローを一時停止して外部シグナルを待機）

## ローカル開発用In-Memoryランナー

開始は素早くできます：

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

コアパッケージには軽量なインプロセスランナーが含まれています。外部依存関係なし、データベースなし、Azureリソースなし。ローカル開発とユニットテストに最適です。

## Durable Taskで永続性を追加

ワークフローがプロセス再起動を乗り越える必要がある場合 — 長時間実行だから、ヒューマン・イン・ザ・ループステップがあるから、多くの並列エージェント呼び出しに分散するから — In-Memoryランナーでは不十分です。

MAFのDurable Task統合はワークフロー状態をAzure Storageに保存します。プロセスが再起動しても、ワークフローは中断した場所から再開されます。プログラミングモデルは変わりません。ランナーを入れ替えるだけです。

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

同じExecutor、同じワークフローグラフ — 永続的な状態に支えられています。

## Azure Functionsホスティング

3番目の層はAzure Functionsホスティングです。ワークフローはFunctionアプリになります：HTTPエンドポイントでワークフローをトリガーし、永続的ランタイムがスケーリング、状態、信頼性を管理します。

これにより、並列呼び出し、条件分岐、ヒューマン承認を持つマルチエージェントワークフローが、カスタム状態管理なしでサーバーレスFunctions環境でスケールできます。

## なぜこれが重要か

この組み合わせは本番AIシステムにとって重要です：

- **並列エージェント呼び出し** — ブロックなしで複数の専門エージェントに同時に分散し、全員が完了したら結果を集約
- **長時間実行プロセス** — ヒューマン承認や外部イベントを含むワークフローが時間や日をまたいで一時停止・再開できる
- **スケーリング** — Azure Functionsが実行を水平スケール；Durable Taskフレームワークが並列状態の調整を管理

シンプルなローカルデモを超えたMAFワークフローを構築するなら、これが本番品質の実行への道筋です。

元の投稿：[Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
