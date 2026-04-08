---
title: "ブラックボックスに感じないリアルタイムマルチエージェントUIを構築する"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UIとMicrosoft Agent Frameworkが連携し、マルチエージェントワークフローにリアルタイムストリーミング、人間の承認、エージェントの動作の完全な可視化を備えた本格的なフロントエンドを提供します。"
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}})をご覧ください。*

マルチエージェントシステムの問題点はこうです：デモでは信じられないほど素晴らしく見えます。3つのエージェントが作業を受け渡し、問題を解決し、意思決定を行う。でも実際のユーザーの前に置いてみると...沈黙。回転するインジケーター。どのエージェントが何をしているのか、なぜシステムが停止しているのか分からない。これはプロダクトではありません — 信頼の問題です。

Microsoft Agent Frameworkチームが、MAFワークフローと[AG-UI](https://github.com/ag-ui-protocol/ag-ui)を組み合わせる[素晴らしいウォークスルー](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)を公開しました。AG-UIはServer-Sent Eventsを介してエージェント実行イベントをフロントエンドにストリーミングするオープンプロトコルです。正直に言うと、これはまさに私たちに欠けていた架け橋です。

## .NET開発者にとって重要な理由

AI搭載アプリを構築しているなら、おそらくこの壁にぶつかったことがあるでしょう。バックエンドのオーケストレーションは完璧に動作します — エージェント同士がタスクを受け渡し、ツールが実行され、意思決定が行われます。しかしフロントエンドは裏で何が起きているか全く分かりません。AG-UIは、エージェントイベント（`RUN_STARTED`、`STEP_STARTED`、`TOOL_CALL_*`、`TEXT_MESSAGE_*`など）をSSE経由でUIレイヤーに直接ストリーミングする標準プロトコルを定義することでこれを解決します。

デモは3つのエージェントを使ったカスタマーサポートワークフローです：リクエストをルーティングするトリアージエージェント、金銭関連を処理する返金エージェント、そして交換を管理する注文エージェント。各エージェントは独自のツールを持ち、ハンドオフトポロジーは明示的に定義されています — 「プロンプトから推測する」ようなことはありません。

## ハンドオフトポロジーが真の主役

私の目を引いたのは、`HandoffBuilder`でエージェント間の有向ルーティンググラフを宣言できることです：

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

各`add_handoff`は自然言語の説明付きの有向エッジを作成します。フレームワークはこのトポロジーに基づいて各エージェントのハンドオフツールを生成します。つまり、ルーティングの決定はオーケストレーション構造に基づいており、LLMの気分次第ではありません。これは本番環境の信頼性にとって非常に大きな意味があります。

## 本当に機能するHuman-in-the-loop

デモでは、実際のエージェントアプリに必要な2つの割り込みパターンを紹介しています：

**ツール承認割り込み** — エージェントが`approval_mode="always_require"`とマークされたツールを呼び出すと、ワークフローが一時停止してイベントを発行します。フロントエンドはツール名と引数を含む承認モーダルをレンダリングします。トークンを消費するリトライループはありません — クリーンな一時停止-承認-再開フローです。

**情報リクエスト割り込み** — エージェントがユーザーからより多くのコンテキスト（注文IDなど）を必要とする場合、一時停止して質問します。フロントエンドが質問を表示し、ユーザーが回答し、実行は停止した箇所からそのまま再開されます。

両方のパターンは標準のAG-UIイベントとしてストリーミングされるため、フロントエンドはエージェントごとのカスタムロジックを必要としません — SSE接続を通じて届くイベントをそのまま表示するだけです。

## 接続は驚くほど簡単

MAFとAG-UIの統合は単一の関数呼び出しで完了します：

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

`workflow_factory`はスレッドごとに新しいワークフローを作成し、各会話が分離された状態を持ちます。エンドポイントはすべてのSSE配管を自動的に処理します。すでにFastAPIを使っている（または軽量レイヤーとして追加できる）なら、ほぼゼロフリクションです。

## 私の見解

私たち.NET開発者にとって、すぐに浮かぶ質問は「C#でできるのか？」です。Agent Frameworkは.NETとPythonの両方で利用可能で、AG-UIプロトコルは言語に依存しません（ただのSSEです）。この特定のデモはPythonとFastAPIを使用していますが、パターンは直接転用できます。同じAG-UIイベントスキーマに従ったSSEエンドポイントを持つASP.NET Core最小APIを構築できるでしょう。

より大きなポイントは、マルチエージェントUIが後付けではなくファーストクラスの関心事になりつつあるということです。エージェントが人間と対話するものを構築しているなら — カスタマーサポート、承認ワークフロー、ドキュメント処理 — MAFオーケストレーションとAG-UIの透明性の組み合わせが、従うべきパターンです。

## まとめ

AG-UI + Microsoft Agent Frameworkは、バックエンドでの堅牢なマルチエージェントオーケストレーションとフロントエンドでのリアルタイム可視性という、両方の良いところを提供します。もうブラックボックスのエージェントインタラクションとはお別れです。

[完全なウォークスルー](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)と[AG-UIプロトコルリポジトリ](https://github.com/ag-ui-protocol/ag-ui)をチェックして、さらに深く掘り下げてください。
