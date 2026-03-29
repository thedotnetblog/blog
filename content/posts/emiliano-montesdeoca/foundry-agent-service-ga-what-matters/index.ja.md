---
title: "Foundry Agent ServiceがGA：.NETエージェント開発者にとって本当に重要なこと"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "MicrosoftのFoundry Agent ServiceがプライベートネットワーキングVoice Live、本番評価、オープンなマルチモデルランタイムでGAに到達。知っておくべきことはこちら。"
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

正直に言いましょう — AIエージェントのプロトタイプを作るのは簡単な部分です。難しいのはその後のすべて：適切なネットワーク分離で本番に乗せること、実際に意味のある評価を実行すること、コンプライアンス要件に対応すること、そして午前2時にものを壊さないこと。

[Foundry Agent ServiceがGAになりました](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)。そしてこのリリースは「その後のすべて」のギャップにレーザーのように集中しています。

## Responses APIの上に構築

見出し：次世代のFoundry Agent ServiceはOpenAI Responses APIの上に構築されています。すでにそのワイヤープロトコルで開発しているなら、Foundryへの移行は最小限のコード変更で済みます。得られるもの：エンタープライズセキュリティ、プライベートネットワーキング、Entra RBAC、完全なトレーシング、評価 — 既存のエージェントロジックの上に。

アーキテクチャは意図的にオープンです。一つのモデルプロバイダーや一つのオーケストレーションフレームワークに縛られません。プランニングにDeepSeek、生成にOpenAI、オーケストレーションにLangGraph — ランタイムが一貫性レイヤーを処理します。

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> `azure-ai-agents`パッケージから来ている場合、エージェントは`azure-ai-projects`の`AIProjectClient`でファーストクラスの操作になりました。スタンドアロンの依存関係を削除し、`get_openai_client()`でレスポンスを駆動してください。

## プライベートネットワーキング：エンタープライズのブロッカー除去

これはエンタープライズ採用のブロックを解除する機能です。FoundryはBYO VNetで完全なエンドツーエンドのプライベートネットワーキングをサポートするようになりました：

- **パブリックエグレスなし** — エージェントのトラフィックはパブリックインターネットに触れない
- **コンテナ/サブネットインジェクション** — ローカル通信のためにネットワークに注入
- **ツール接続性も含む** — MCPサーバー、Azure AI Search、Fabricデータエージェントすべてがプライベートパスで動作

最後のポイントが重要です。プライベートのままなのは推論呼び出しだけではありません — すべてのツール呼び出しと検索コールもネットワーク境界内にとどまります。外部ルーティングを禁止するデータ分類ポリシーの下で運用しているチームにとって、これが欠けていたものです。

## MCP認証を正しく

MCPサーバー接続は認証パターンの全スペクトルをサポートするようになりました：

| 認証方法 | 使用タイミング |
|----------|---------------|
| キーベース | 組織全体の内部ツール向けシンプルな共有アクセス |
| Entra Agent Identity | サービス間；エージェントがそれ自体として認証 |
| Entra Managed Identity | プロジェクト単位の分離；クレデンシャル管理不要 |
| OAuth Identity Passthrough | ユーザー委任アクセス；エージェントがユーザーに代わって行動 |

OAuth Identity Passthroughが興味深い。ユーザーがエージェントに個人データへのアクセスを許可する必要がある場合 — OneDrive、Salesforce org、ユーザースコープのSaaS API — エージェントは標準のOAuthフローでユーザーに代わって行動します。全員のふりをする共有システムIDはありません。

## Voice Live：配管なしの音声対音声

エージェントに音声を追加するには、STT、LLM、TTSを組み合わせる必要がありました — 3つのサービス、3つのレイテンシホップ、3つの課金サーフェス、すべて手動で同期。**Voice Live**はこれを単一のマネージドAPIに凝縮します：

- セマンティック音声アクティビティとターンエンド検出（沈黙だけでなく意味を理解）
- サーバーサイドのノイズ抑制とエコーキャンセル
- 割り込みサポート（ユーザーが応答中に割り込める）

音声インタラクションはテキストと同じエージェントランタイムを通過します。同じ評価者、同じトレース、同じコスト可視性。カスタマーサポート、フィールドサービス、アクセシビリティシナリオで、以前はカスタムオーディオパイプラインが必要だったものを置き換えます。

## 評価：チェックボックスから継続的モニタリングへ

ここでFoundryが本番品質について本気になります。評価システムには3つのレイヤーがあります：

1. **組み込み評価者** — 一貫性、関連性、根拠性、検索品質、安全性。データセットまたはライブトラフィックに接続してスコアを取得。

2. **カスタム評価者** — 独自のビジネスロジック、トーン標準、ドメイン固有のコンプライアンスルールをエンコード。

3. **継続的評価** — Foundryがライブ本番トラフィックをサンプリングし、評価者スイートを実行し、ダッシュボードに結果を表示。根拠性が低下したりセキュリティ閾値を超えた場合のAzure Monitorアラートを設定。

すべてがAzure Monitor Application Insightsに公開されます。エージェント品質、インフラ健全性、コスト、アプリテレメトリ — すべて一か所に。

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## ホステッドエージェント向け6つの新リージョン

ホステッドエージェントがEast US、North Central US、Sweden Central、Southeast Asia、Japan Eastなどで利用可能になりました。これはデータレジデンシー要件と、エージェントがデータソースの近くで実行される場合のレイテンシ圧縮に重要です。

## .NET開発者にとってなぜ重要か

GAアナウンスのコードサンプルはPythonファーストですが、基盤となるインフラストラクチャは言語に依存しません — そして`azure-ai-projects`の.NET SDKも同じパターンに従います。Responses API、評価フレームワーク、プライベートネットワーキング、MCP認証 — これらすべてが.NETから利用可能です。

AIエージェントが「かっこいいデモ」から「実際に仕事で出荷できる」に変わるのを待っていたなら、このGAリリースがそのシグナルです。プライベートネットワーキング、適切な認証、継続的評価、本番モニタリングが欠けていたピースです。

## まとめ

Foundry Agent Serviceは今すぐ利用可能です。SDKをインストールし、[ポータル](https://ai.azure.com)を開いて構築を始めましょう。[クイックスタートガイド](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)で数分でゼロから動くエージェントに到達できます。

すべてのコードサンプルを含む完全な技術的ディープダイブは[GAアナウンスメント](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)をご覧ください。
