---
title: "エージェントを作るのは簡単な部分 — 安全に実行するのが難しい部分"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework と Agent Governance Toolkit が連携して、ランタイムポリシーを適用し、ツール呼び出しを管理し、Merkle チェーンの監査ログを提供します — エージェントのプロンプトを変更せずに。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

AI エージェント開発には「デモ後悔」と呼び始めたパターンがあります。エージェントはデモでは完璧に動作します。そして誰かが聞きます: 間違ったツールを呼び出したら何が起こる? アクセスすべきでないデータにアクセスしたら? 誰が監査した?

Microsoft Agent Framework はビルドとオーケストレーションをサポートします。Agent Governance Toolkit（AGT）はその後の部分をカバーします — ガバナンス、ポリシー適用、ランタイムでの監査可能性。

## 各プロジェクトが実際に行うこと

**Microsoft Agent Framework (MAF)** はプログラミングモデルを提供します: マルチエージェントワークフロー、A2A プロトコル相互運用性、ミドルウェアフック、メモリ、Foundry Agent Service によるマネージドホスティング。モデル入出力レベルでコンテンツセーフティを処理します。

**Agent Governance Toolkit (AGT)** は同じミドルウェアパイプラインに接続して *アクション* を管理します。すべてのツール呼び出し、リソースアクセス、エージェント間メッセージは実行前にポリシーに対して評価されます。サブミリ秒のオーバーヘッド。サイドカーなし、プロキシなし、変更されたプロンプトなし。

```
エージェントアクション --> ポリシーチェック --> 許可 / 拒否 --> 監査ログ    (< 0.1 ms)
```

異なるレイヤー、完全なカバレッジ、1つのパイプライン。

## 接続はミドルウェアを追加するだけ

Python では、AGT はログやコンテンツフィルターに使うのと同じ `middleware` パラメーターに追加されます:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

.NET では `.Use()` を通じて同じパターン:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

同じエージェント、同じオーケストレーション、同じツール。AGT はエージェントのロジックを変更せずにガバナンス機能を追加します。

## 何を得るか

- **GovernancePolicyMiddleware** — 宣言的ポリシールールに対してすべてのアクションを評価
- **CapabilityGuardMiddleware** — エージェントが呼び出しを許可されているツールのホワイトリスト（上記の `approve_small_loan` ツールは意図的に許可リストに含まれていない）
- **RogueDetectionMiddleware** — ランタイムで異常な動作パターンを検出
- **AuditTrailMiddleware** — すべてのアクションを暗号学的に改ざん耐性にするための Merkle チェーン監査ログ

最後のものはコンプライアンスに重要です。Merkle チェーンは、誰かがログを変更すると、チェーンが壊れることを意味します。監査が証拠です。

## 5つの業界シナリオ

AGT リポジトリには5つの完全なエンドツーエンドシナリオが含まれています: 金融サービス（ローン担当者）、医療（患者データ）、法律（契約審査）、政府（市民サービス）、製造（品質管理）。それぞれが実際の MAF エージェントと実際の AGT ガバナンスミドルウェアを組み合わせています。

おもちゃのデモではありません。実際に本番でガバナンスが必要なシナリオです。

## まとめ

実際のデータに触れる、結果を伴う決定を下す、または本番で監視なしで動作するエージェントを構築している場合 — ガバナンスは任意ではありません。MAF + AGT の組み合わせが完全なスタックを提供します: Agent Framework でビルドし、AGT で管理します。

両プロジェクトはオープンソースです。元の記事には完全なコードサンプルへのリンクがあります。

元の投稿: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
