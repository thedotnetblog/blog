---
title: "Microsoft Agent Frameworkのバックグラウンドレスポンス：タイムアウトの不安から解放"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Frameworkが継続トークンで長時間実行AIタスクのオフロードを可能に。バックグラウンドレスポンスの仕組みと.NETエージェントにとっての重要性を解説します。"
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

o3やGPT-5.2のような推論モデルで何かを構築したことがあるなら、その痛みを知っているでしょう。エージェントが複雑なタスクについて考え始め、クライアントは待ち続け、「大丈夫」と「クラッシュした？」の間のどこかで接続がタイムアウトする。あの作業は？全て消えます。

Microsoft Agent Frameworkが[バックグラウンドレスポンス](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/)をリリースしました — 正直なところ、これは初日から存在すべきだった機能の一つです。

## ブロッキング呼び出しの問題

従来のリクエスト-レスポンスパターンでは、エージェントが終了するまでクライアントはブロックされます。簡単なタスクには問題ありません。しかし、推論モデルに深い調査、多段階分析、20ページのレポート生成を依頼する場合は？実時間で数分かかります。その間：

- HTTP接続がタイムアウトする可能性がある
- ネットワークの途切れが操作全体を壊す
- ユーザーはスピナーを見つめて何かが起きているか疑問に思う

バックグラウンドレスポンスはこれを逆転させます。

## 継続トークンの仕組み

ブロックする代わりに、エージェントタスクを起動して**継続トークン**を受け取ります。修理工場の引換券のようなものです — カウンターに立って待つ必要はなく、準備ができたら戻ってくればいいのです。

フローは単純です：

1. `AllowBackgroundResponses = true`でリクエストを送信
2. エージェントがバックグラウンド処理をサポートしていれば、継続トークンを受け取る
3. トークンが`null`を返すまでポーリング — 結果の準備完了を意味します

.NETバージョンはこちら：

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// 完了までポーリング
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

エージェントがすぐに完了する場合（簡単なタスク、バックグラウンド処理を必要としないモデル）、継続トークンは返されません。コードはそのまま動きます — 特別な処理は不要です。

## 再開付きストリーミング：本当のマジック

ポーリングはfire-and-forgetシナリオには良いですが、リアルタイムの進捗が欲しい場合は？バックグラウンドレスポンスは再開機能付きストリーミングもサポートしています。

各ストリーム更新は独自の継続トークンを持ちます。ストリーム中に接続が切れても、中断した正確な位置から再開できます：

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // ネットワーク中断をシミュレート
}

// 中断した正確な位置から再開
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

クライアントに何が起きてもサーバー側でエージェントは処理を続けます。リトライロジックやサーキットブレーカーを書くことなく、組み込みのフォールトトレランスが実現します。

## 実際にいつ使うべきか

すべてのエージェント呼び出しにバックグラウンドレスポンスが必要なわけではありません。高速な完了には無駄な複雑さを追加するだけです。しかし、ここで威力を発揮します：

- **複雑な推論タスク** — 多段階分析、深い調査、推論モデルを本気で考えさせるもの
- **長文コンテンツ生成** — 詳細レポート、複数パートのドキュメント、広範な分析
- **信頼性の低いネットワーク** — モバイルクライアント、エッジデプロイメント、不安定な企業VPN
- **非同期UXパターン** — タスクを送信し、他のことをして、結果を取りに戻る

エンタープライズアプリを構築する.NET開発者にとって、最後のポイントは特に興味深いです。ユーザーが複雑なレポートを要求するBlazorアプリを想像してください — エージェントタスクを起動し、プログレスインジケータを表示し、作業を続けてもらう。WebSocketの曲芸なし、カスタムキューインフラなし、トークンとポーリングループだけです。

## まとめ

バックグラウンドレスポンスはMicrosoft Agent Frameworkを通じて.NETとPythonの両方で今すぐ利用可能です。単純なQ&A以上のことをするエージェントを構築しているなら、ツールキットに追加する価値があります。継続トークンパターンはシンプルさを保ちながら、非常に現実的な本番環境の問題を解決します。

完全なAPIリファレンスとその他のより例については[完全なドキュメント](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/)をご覧ください。
