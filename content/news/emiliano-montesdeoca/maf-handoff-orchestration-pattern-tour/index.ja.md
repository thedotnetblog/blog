---
title: "ハンドオフパターン：1つのエージェントでは不十分な時"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Microsoft Agent FrameworkのHandoffオーケストレーションパターンにより、エージェントは会話コンテキストを失ったりトポロジルールを破ったりすることなく、次のターンを誰が処理するかを決定できます。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

どのマルチエージェントシステムも、いつかはシンプルなルーターを超えます。最初のサインは、専門エージェントがフォローアップの質問をする必要があるとき、またはターンの途中で別のエージェントが続けるべきだと気付くときです。固定パイプラインはそこで失敗します。ワンショットルーターもそこで失敗します。

それこそがMicrosoft Agent FrameworkのHandoffオーケストレーションパターンが対処するために設計された問題です。

## Handoffの仕組み

開発者がグラフを宣言します：エージェントはこれで、エージェント間のエッジはこれです。フレームワークが残りを行います — 各出力エッジにハンドオフツールを合成して各エージェントに注入します。エージェントが制御を渡すと決めたらツールを呼び出します。フレームワークがトポロジを強制します。

これをエージェントが互いを呼び出すことと異なるものにする3つのこと：

1. **1つの共有トランスクリプト** — 受信エージェントは完全な会話履歴を見ます。ゼロから始まることはありません。
2. **トポロジの強制** — エージェントは宣言されたターゲットにのみハンドオフできます。ルーティングのバグは作成時に検出され、プロダクションでは検出されません。
3. **自然な終了** — アクティブエージェントがハンドオフツールを呼び出さずにターンを終えると、ワークフローはユーザーに譲ります。ポーリングなし、明示的な終了条件なし。

## 最小限の例

.NETでhandoffワークフローを構築するとこのようになります：

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triageはどちらの専門家にも送れます。両方の専門家がtriageに戻せます。グラフは非巡回対応ですが、必要なとき("もっと情報が必要" → 調査に戻る)にバックエッジをサポートします。

## Handoffを使う時（と使わない時）

Handoffが適している場面：

- **所有権が会話の途中で変わりうる** — エージェントが自分が間違った専門家だと気付く場合
- **バックエッジが重要** — 再起動なしに前のステップを再訪する必要がある場合
- **ルーティング決定が曖昧** — ハンドオフするかどうかの決定が文脈的で、型付きの述語よりモデルが判断した方が良い場合

*適していない*場面：

- パイプラインが固定で順次的 — その場合は`Sequential`ワークフローを使用
- 各ステップが独立 — 1つしか必要としていないのに全員がトランスクリプトを共有するのは雑音
- 厳格な処理保証が必要 — モデル駆動ルーティングの非決定論は望むものではない

## バックエッジとHuman-in-the-Loop

Handoffが可能にする最も興味深い形の一つは、本物のバックエッジです。エージェントは「情報が不十分」と判断して研究ステップに戻るルーティングをすることができます — ハードコードされたループではなく、モデルがそれが正しい判断だと決めるからです。

Human-in-the-loopのインタラクションも自然に構成されます。専門家がユーザー入力を必要とするとき、ワークフローはデフォルトのターンループを通じてユーザーに戻し、応答を収集し、完全なコンテキストで再開します。エージェントは会話を失いません。

## まとめ

Handoffは内面化すると多くを可能にするシンプルに見えるパターンの一つです：分散ルーティング、共有コンテキスト、強制されたトポロジ、自然な終了。エージェントが「実際は他の誰かがこれを処理すべきだ」と言い始めたときの次のステップです。

元の投稿で完全なウォークスルーを読む: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
