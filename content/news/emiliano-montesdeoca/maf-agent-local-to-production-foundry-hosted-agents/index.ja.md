---
title: "あなたのローカル MAF エージェントが本番環境の家を手に入れました"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents は Microsoft Agent Framework エージェントにアイデンティティ、スケーリング、セッション永続性、追加設定不要の可観測性を提供します。実際にどのように見えるかをご紹介します。"
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

エージェントをローカルで動作させることは楽しい部分です。難しい部分はその後のすべてです：正気を保ちながらデプロイし、セッションを管理し、アイデンティティを設定し、可観測性を配線する。通常、これは多くのカスタムインフラの「接着剤」を意味します。

Foundry Hosted Agents は、Microsoft Agent Framework (MAF) ユーザーにとってそのような接着剤の大部分を取り除いてくれました。

## Foundry Hosted Agents が実際に何をするか

MAF エージェントを Foundry Hosted Agents にデプロイすると、プラットフォームは驚くほど長いリストのことを処理してくれます。それを自分で構築する必要がなくなります：

- **ゼロへのスケール** — アイドル時にコストがかからず、自動的に起動します
- **セッションごとの VM 分離サンドボックス** — 各ユーザーセッションがスケールダウンイベントを乗り越えるファイルシステム永続性を持つ独自のサンドボックスを取得します
- **組み込み Entra ID** — 各エージェントが Foundry モデル、Toolbox、Azure サービスをシークレットをイメージに焼き付けずに呼び出せる独自のアイデンティティを取得します
- **バージョン管理されたデプロイメント** — 各デプロイメントが不変のスナップショットで、blue/green とカナリアロールアウトサポートがあります
- **設定不要の可観測性** — `APPLICATIONINSIGHTS_CONNECTION_STRING` が実行時に注入されるため、MAF の OpenTelemetry トレースが App Insights に自動的に流れます

最後のものは本当に便利です。追加の配線なし、追加の設定なし。トレースがただ表示されます。

## コードの違いは最小限

この統合で最も気に入っているのはこれです。エージェントを書き直す必要はありません。ただラップするだけです：

**.NET の場合：**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Python の場合：**

```python
server = ResponsesHostServer(agent)
server.run()
```

それだけです。ローカルでテストしたのと同じロジックが本番環境で実行されます。プラットフォームはセッション管理、アイデンティティ、スケーリングインフラでそれをラップします。

## 2 つのプロトコル、1 つのエージェント

Hosted Agents は 2 つのエンドポイントスタイルをサポートします：

- **Responses** (`/responses`) — OpenAI 互換、会話履歴とストリーミングを管理します。チャット形式のエージェントの良いデフォルト。
- **Invocations** (`/invocations`) — リクエスト/レスポンススキーマを定義します。非会話的なワークフローに適しています。

会話のように見えるものを構築している場合は、Responses から始めてください。構造化された入力を受け取り、構造化された出力を返す API 形式のエージェントを構築している場合は、Invocations が柔軟性を提供します。

## `azd` を使ったデプロイフロー

MAF エージェントで `azd up` を実行すると：

1. オプションで Foundry プロジェクトを作成してモデルをデプロイ
2. コードをパッケージ化して Azure Container Registry にイメージをプッシュ
3. ACR イメージからコンピューティングをプロビジョニング
4. エージェントに専用の Entra ID を割り当て
5. 安定したエンドポイントを公開 (`https://{project_endpoint}/agents/{agent_name}`)
6. それ以降はすべてを処理

セッションは最大 30 日間持続します。アイドル状態のコンピューティングは 15 分後にデプロビジョニングされ、次のリクエスト時に透過的に復元されます。エージェントの観点からは、何も変わっていません。

## まとめ

「ローカルで動作している」から「本番で実行されている」までの距離は、AI エージェントにとって歴史的に長くて辛いものでした。Foundry Hosted Agents + MAF はそのギャップを大幅に縮めます。Agent Framework で構築されたローカルエージェントがすでにある場合は、今日試す価値があります。

チームは GA が近いと言っています — これは現在プレビュー中です。始めるには [MAF Hosted Agent 統合ドキュメント](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) と [.NET サンプル](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) を確認してください。

元の記事: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
