---
title: "Microsoft Foundry 2026年3月 — GPT-5.4、Agent Service GA、そしてすべてを変えるSDKリフレッシュ"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsoft Foundryの2026年3月アップデートは大規模：Agent ServiceがGAに到達、GPT-5.4が信頼性の高い推論を実現、azure-ai-projects SDKが全言語で安定版に、そしてFireworks AIがオープンモデルをAzureに提供。"
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}})をご覧ください。*

毎月の「Microsoft Foundryの新着情報」記事は、通常インクリメンタルな改善と時折のヘッドライン機能の組み合わせです。[2026年3月版](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)はどうでしょう？基本的にすべてがヘッドライン機能です。Foundry Agent ServiceがGAに、GPT-5.4が本番環境向けにリリース、SDKがメジャーな安定版リリースを受け、Fireworks AIがオープンモデル推論をAzureに提供します。.NET開発者にとって何が重要かを詳しく見ていきましょう。

## Foundry Agent Serviceが本番環境対応に

これが最大のニュースです。次世代エージェントランタイムが一般提供開始されました — OpenAI Responses APIの上に構築され、OpenAIエージェントとワイヤー互換性があり、複数のプロバイダーのモデルに対応しています。今日Responses APIで構築している方は、Foundryに移行することでエンタープライズセキュリティ、プライベートネットワーキング、Entra RBAC、完全なトレーシング、そして既存のエージェントロジック上での評価が追加されます。

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

主な追加機能：エンドツーエンドのプライベートネットワーキング、MCP認証の拡張（OAuthパススルーを含む）、音声対音声エージェント向けVoice Liveプレビュー、6つの新リージョンでのホスティングエージェント。

## GPT-5.4 — 純粋な知性より信頼性

GPT-5.4はより賢くなることが目的ではありません。より信頼性が高くなることが目的です。長い対話での強力な推論、より良い指示への忠実度、ワークフロー中の障害の減少、そして統合されたコンピュータ使用機能。本番環境のエージェントにとって、その信頼性はベンチマークスコアよりもはるかに重要です。

| モデル | 価格（100万トークンあたり） | 最適な用途 |
|--------|--------------------------|-----------|
| GPT-5.4 (≤272K) | $2.50 / $15 出力 | 本番エージェント、コーディング、ドキュメントワークフロー |
| GPT-5.4 Pro | $30 / $180 出力 | 深い分析、科学的推論 |
| GPT-5.4 Mini | コスト効率的 | 分類、抽出、軽量なツール呼び出し |

賢い戦略はルーティングです：GPT-5.4 Miniが高ボリューム・低レイテンシーの作業を処理し、GPT-5.4が推論の重いリクエストを担当します。

## SDKがついに安定版に

`azure-ai-projects` SDKが全言語で安定版をリリースしました — Python 2.0.0、JS/TS 2.0.0、Java 2.0.0、そして.NET 2.0.0（4月1日）。`azure-ai-agents`の依存関係はなくなり、すべてが`AIProjectClient`の下に統合されました。`pip install azure-ai-projects`でインストールでき、パッケージは`openai`と`azure-identity`を直接の依存関係としてバンドルしています。

.NET開発者にとって、これはFoundry全体の機能に対する単一のNuGetパッケージを意味します。別々のエージェントSDKを使い分ける必要はもうありません。

## Fireworks AIがオープンモデルをAzureに提供

おそらくアーキテクチャ的に最も興味深い追加：Fireworks AIが毎日13兆以上のトークンを~180Kリクエスト/秒で処理し、Foundryを通じて利用可能になりました。DeepSeek V3.2、gpt-oss-120b、Kimi K2.5、MiniMax M2.5がローンチ時に利用可能です。

本当の注目点は**bring-your-own-weights** — サービングスタックを変更せずに、どこからでも量子化またはファインチューニングされた重みをアップロードできます。サーバーレスのペイパートークンまたはプロビジョニングされたスループットでデプロイ可能です。

## その他のハイライト

- **Phi-4 Reasoning Vision 15B** — チャート、ダイアグラム、ドキュメントレイアウト向けのマルチモーダル推論
- **Evaluations GA** — Azure Monitorに連携した継続的な本番モニタリング付きのすぐに使えるエバリュエーター
- **Priority Processing**（プレビュー）— レイテンシーに敏感なワークロード向けの専用コンピュートレーン
- **Voice Live** — Foundryエージェントに直接接続する音声対音声ランタイム
- **Tracing GA** — ソートとフィルター付きのエンドツーエンドエージェントトレース検査
- **PromptFlowの非推奨化** — 2027年1月までにMicrosoft Framework Workflowsへの移行

## まとめ

2026年3月はFoundryにとって転換点です。Agent Service GA、全言語での安定SDK、信頼性の高い本番エージェント向けGPT-5.4、そしてFireworks AIによるオープンモデル推論 — プラットフォームは本格的なワークロードに対応する準備が整っています。

[完全なまとめ](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)を読んで、[最初のエージェントを構築](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code)して始めましょう。
