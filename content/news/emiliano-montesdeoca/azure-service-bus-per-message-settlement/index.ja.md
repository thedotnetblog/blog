---
title: "Azure Service Bus におけるオールオアナッシング・バッチ処理の解消"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions が Service Bus トリガーのメッセージ単位のセトルメントをサポートし、バッチ内の各メッセージを独立して完了・破棄・デッドレター・遅延処理できるようになりました。"
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[Azure Functions における Azure Service Bus のメッセージ単位のセトルメント](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/)は、オールオアナッシング・バッチ失敗問題を解消します：50件のバッチで1件が失敗すると、50件すべてがキューに戻されていた問題です。

## バッチ問題

旧モデルでは、Azure Functions はバッチモードでメッセージを処理し、結果は二択でした：バッチ全体が成功するか、バッチ全体が失敗するかです。不正な形式のメッセージが1件あるだけで、49件の正常なメッセージがすべてキューに戻され、再処理され、べき等性が再確認されていました — コンピューティングリソースを無駄にし、コストを増大させ、脱出困難なリトライループを生み出していました。

## 4種類のメッセージ単位セトルメントアクション

メッセージ単位のセトルメントでは、各メッセージに対して4つの独立したアクションが可能です：

- **完了 (Complete)** — メッセージをキューから削除する（処理成功）
- **破棄 (Abandon)** — リトライのために返却する。アプリプロパティの変更も可能（一時的エラーに有用）
- **デッドレター (Dead-letter)** — デッドレターキューに移動する（毒メッセージ、回復不可能）
- **遅延 (Defer)** — 保持するが、シーケンス番号でのみ取得可能にする

50件のバッチで、47件を完了し、2件を一時的エラーで破棄し、1件の不正メッセージをデッドレターに送る — すべて1回の関数呼び出しで実現できます。

## コード例

**.NET (C#):**
```csharp
[Function("ProcessOrderBatch")]
public async Task Run(
    [ServiceBusTrigger("orders-queue", IsBatched = true)] ServiceBusReceivedMessage[] messages,
    ServiceBusMessageActions messageActions)
{
    foreach (var message in messages)
    {
        try {
            await messageActions.CompleteMessageAsync(message);
        } catch {
            await messageActions.DeadLetterMessageAsync(message);
        }
    }
}
```

**Node.js/TypeScript:**
```typescript
import '@azure/functions-extensions-servicebus';
export async function processOrderBatch(sbContext, context) {
    const { messages, actions } = sbContext;
    for (const message of messages) {
        try {
            await processOrder(messageBodyAsJson(message));
            await actions.complete(message);
        } catch {
            await actions.deadletter(message);
        }
    }
}
app.serviceBusQueue('processOrderBatch', {
    sdkBinding: true,
    autoCompleteMessages: false,
    cardinality: 'many',
    handler: processOrderBatch
});
```

**Python V2:**
```python
@app.service_bus_queue_trigger(auto_complete_messages=False, cardinality="many")
def process_order_batch(messages, message_actions):
    for message in messages:
        try:
            process_order(json.loads(message.body))
            message_actions.complete(message)
        except:
            message_actions.deadletter(message)
```

## 追加インフラなしのエクスポネンシャルバックオフ

`abandon` と変更されたアプリプロパティを組み合わせることで、追加のキューや Durable Functions なしに、キュー上で直接エクスポネンシャルバックオフを実現できます。メッセージのアプリケーションプロパティにリトライカウントを保存し、再配信時に読み取り、遅延を計算します。このパターンはかつて大規模なオーケストレーションが必要でしたが、今やリトライハンドラーの数行で済みます。

## バッチ効率の向上

旧プリバッチモデルでは各メッセージが個別の関数呼び出しとして送信されていました：50件のメッセージは50回の接続、50回のコールドスタート、50回のティアダウンを意味しました。新しいモデルでは50件すべてを1回の呼び出しで処理し、メッセージ単位のセトルメントによりエラーが発生してもその効率を失いません。

完全な記事は [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) でご覧ください。
