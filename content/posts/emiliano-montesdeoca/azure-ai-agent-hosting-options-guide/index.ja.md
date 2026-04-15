---
title: "AzureでAIエージェントをどこにホストすべき？実践的な判断ガイド"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azureには生のコンテナからフルマネージドのFoundry Hosted Agentsまで、AIエージェントをホストする6つの方法があります。.NETワークロードに最適なものを選ぶ方法を解説します。"
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *この記事は自動翻訳されています。オリジナル版は[こちら]({{< ref "azure-ai-agent-hosting-options-guide.md" >}})をご覧ください。*

今.NETでAIエージェントを構築しているなら、おそらく気づいていることがあるでしょう：Azureでホストする方法が*たくさん*あるということです。Container Apps、AKS、Functions、App Service、Foundry Agents、Foundry Hosted Agents — どれも合理的に聞こえますが、実際に選ぶ段階になると困ります。Microsoftが[AzureでのAIエージェントホスティングに関する包括的なガイド](https://devblogs.microsoft.com/all-things-azure/hostedagent/)を公開しました。これを.NET開発者の実践的な視点から整理します。

## 6つのオプション早見表

| オプション | 最適な用途 | 管理するもの |
|-----------|-----------|-------------|
| **Container Apps** | K8sの複雑さなしにコンテナを完全制御 | オブザーバビリティ、状態、ライフサイクル |
| **AKS** | エンタープライズコンプライアンス、マルチクラスター、カスタムネットワーキング | すべて（それがポイント） |
| **Azure Functions** | イベント駆動の短時間エージェントタスク | ほぼなし — 真のサーバーレス |
| **App Service** | シンプルなHTTPエージェント、予測可能なトラフィック | デプロイ、スケーリング設定 |
| **Foundry Agents** | ポータル/SDKによるコード不要エージェント | ほぼなし |
| **Foundry Hosted Agents** | マネージドインフラでカスタムフレームワークエージェント | エージェントコードのみ |

最初の4つは汎用コンピュートです — エージェントを動かす*ことはできます*が、そのために設計されたものではありません。最後の2つはエージェントネイティブで、会話、ツール呼び出し、エージェントのライフサイクルをファーストクラスの概念として理解しています。

## Foundry Hosted Agents — .NETエージェント開発者にとってのスイートスポット

注目すべきはこれです。Foundry Hosted Agentsはちょうど中間に位置しています：自分のコード（Semantic Kernel、Agent Framework、LangGraph — 何でも）を実行する柔軟性がありながら、プラットフォームがインフラ、オブザーバビリティ、会話管理を処理します。

キーピースは**Hosting Adapter**です — エージェントフレームワークをFoundryプラットフォームに接続する薄い抽象化レイヤーです。Microsoft Agent Frameworkの場合：

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

これがホスティングの全体像です。アダプターがプロトコル変換、server-sent eventsによるストリーミング、会話履歴、OpenTelemetryトレーシングを自動的に処理します。カスタムミドルウェアも手動の配管作業も不要です。

## デプロイは本当にシンプル

以前Container Appsにエージェントをデプロイしたことがありますが、状態管理やオブザーバビリティのためのグルーコードをたくさん書くことになります。Hosted Agentsと`azd`なら：

```bash
# AIエージェント拡張機能をインストール
azd ext install azure.ai.agents

# テンプレートから初期化
azd ai agent init

# ビルド、プッシュ、デプロイ — 完了
azd up
```

この1つの`azd up`がコンテナをビルドし、ACRにプッシュし、Foundryプロジェクトをプロビジョニングし、モデルエンドポイントをデプロイし、エージェントを起動します。5つのステップが1つのコマンドに凝縮されています。

## 組み込みの会話管理

本番で最も時間を節約するのはここです。独自の会話ステートストアを構築する代わりに、Hosted Agentsがネイティブに処理します：

```python
# 永続的な会話を作成
conversation = openai_client.conversations.create()

# 最初のターン
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# 2回目のターン — コンテキストが保持される
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Redisなし。Cosmos DBセッションストアなし。メッセージシリアライゼーション用のカスタムミドルウェアなし。プラットフォームがすべて処理します。

## 私の判断フレームワーク

6つすべてのオプションを検討した結果、私のクイックメンタルモデルはこうです：

1. **インフラゼロが必要？** → Foundry Agents（ポータル/SDK、コンテナなし）
2. **カスタムエージェントコードがあるがマネージドホスティングが欲しい？** → Foundry Hosted Agents
3. **イベント駆動の短期エージェントタスクが必要？** → Azure Functions
4. **K8sなしで最大限のコンテナ制御が必要？** → Container Apps
5. **厳格なコンプライアンスとマルチクラスターが必要？** → AKS
6. **予測可能なトラフィックのシンプルなHTTPエージェント？** → App Service

Semantic KernelやMicrosoft Agent Frameworkで構築しているほとんどの.NET開発者にとって、Hosted Agentsが適切なスタート地点でしょう。scale-to-zero、組み込みOpenTelemetry、会話管理、フレームワークの柔軟性が得られます — Kubernetesの管理やオブザーバビリティスタックの構築なしに。

## まとめ

AzureのエージェントホスティングランドスケープはFastに成熟しています。今日新しいAIエージェントプロジェクトを始めるなら、習慣でContainer AppsやAKSに手を伸ばす前に、Foundry Hosted Agentsを真剣に検討することをお勧めします。マネージドインフラは実際の時間を節約し、hosting adapterパターンでフレームワークの選択を維持できます。

[Microsoftの完全ガイド](https://devblogs.microsoft.com/all-things-azure/hostedagent/)と[Foundry Samplesリポジトリ](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents)で動作するサンプルを確認してください。
