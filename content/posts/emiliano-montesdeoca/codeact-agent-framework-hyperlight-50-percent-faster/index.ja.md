---
title: "Agent FrameworkのCodeAct：エージェントのレイテンシを半分にする方法"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeActは複数ステップのツールチェーンを単一のサンドボックス化されたコードブロックに圧縮します。レイテンシ52%削減、トークン使用量64%削減を実現します。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

エージェントプロジェクトの開発中、トレースを見て「なぜこんなに時間がかかるんだろう？」と思う瞬間があります。モデルは問題ない。ツールも動いている。でも、1回で計算できる結果を得るのに7回のラウンドトリップが発生している。

これがまさにCodeActが解決する問題です。[Agent FrameworkチームはHyperlightパッケージでのアルファサポートをリリース](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)しました。

## CodeActとは？

[CodeActパターン](https://arxiv.org/abs/2402.01030)はエレガントにシンプルです。モデルにツールリストを渡して1つずつ呼び出させる代わりに、単一の`execute_code`ツールを与え、*計画全体*を短いPythonプログラムとして表現させます。エージェントはコードを1回書き、サンドボックスがそれを実行し、1つの統合された結果を得ます。

| 方式 | 時間 | トークン |
|--------|------|--------|
| 従来型 | 27.81秒 | 6,890 |
| CodeAct | 13.23秒 | 2,489 |
| **改善** | **52.4%** | **63.9%** |

## セキュリティ：Hyperlightマイクロ-VM

`agent-framework-hyperlight`パッケージは[Hyperlight](https://github.com/hyperlight-dev/hyperlight)のマイクロ-VMを使用します。各`execute_code`呼び出しは独自の新しいマイクロ-VMを取得します。起動はミリ秒単位で計測されます。分離はほぼコストゼロです。

ツールはホストで実行し続けます。モデルが生成した*グルーコード*はサンドボックスで実行されます。これが正しい分離です。

## 最小セットアップ

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## いつCodeActを使うか（使わないか）

**CodeActを使う場合：**
- タスクが多くの小さなツール呼び出しを連鎖させる（ルックアップ、結合、計算）
- レイテンシとトークンコストが重要
- モデル生成コードに強力な分離が必要

**従来のtool-callingを使う場合：**
- エージェントがターンごとに1〜2回しかツールを呼び出さない
- 各呼び出しに個別の承認が必要な副作用がある
- ツールの説明が乏しいか曖昧

## 今すぐ試す

```bash
pip install agent-framework-hyperlight --pre
```

[Agent Frameworkブログの完全な投稿](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)でより詳しい解説をご覧ください。
