---
title: "Agent Harness、Hosted Agents、CodeAct: 私が注目する Agent Framework の更新はこれだ"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Build 2026 の Agent Framework 発表は盛りだくさんですが、特に重要なのは harness モデル、Foundry の hosted agents、そしてオーケストレーションのオーバーヘッドを減らす CodeAct です。"
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Build における Agent Framework の大きな発表には多くの内容が含まれていますが、私には最初に次の3つが特に目に留まりました。

- **harness が、より一級の runtime の話になってきていること**
- **Foundry の hosted agents が production への道筋を示していること**
- **CodeAct が複数ステップの orchestration オーバーヘッドを減らしていること**

私ならここに注目します。

## harness が本当の重心になりつつある

元の投稿では、harness をモデルの推論と実際の実行が出会う層として説明しています。

その説明はまさにその通りだと思いますし、だからこそこの部分は個々の機能項目の多くよりも重要だと感じます。

エージェントに次のものが必要になった瞬間に、

- ファイルアクセス
- シェル実行
- 計画モード
- ToDo
- セッションメモリ
- 承認ワークフロー

もう prompt と model だけの話ではありません。

runtime の振る舞いを話しているのです。

フレームワークが本当に役立つか、それともおもちゃのままで終わるかは、まさにそこで決まります。

そして Microsoft Agent Framework は明らかに、その層をより有用なものにしようとしています。

## hosted agents は、ローカルから production への話を現実のものにする場所

この hosted agents の部分も、発表の中で戦略的にかなり重要だと思います。

元の投稿でも、これがその agent に production の居場所を与える最も簡単な方法だと明言されています。

多くの agent framework は、運用デプロイよりもローカル実験のほうがまだずっと強いからこそ、この言い回しは重要です。

もし Foundry hosted agents が、ローカル開発から次の段階へ移ることを:

- スケーリング
- 可観測性
- マネージド ID
- セッション処理
- バージョニング

まで含めて大きく簡単にしてくれるなら、今の agent エコシステムにある最大級のギャップのひとつが埋まります。

それは大きな改善です。

## CodeAct は、この更新で最も面白い技術的アイデアです

もし私がこの投稿で最も興味深い技術概念を1つ選ぶなら、CodeAct を選ぶと思います。

それが解こうとしている問題はとても現実的です。多段の agent ワークフローは、オーケストレーションのループ自体がモデルの往復回数を使いすぎるために高くつきます。

なので、元の投稿に次のような結果が出てくると:

- 52.4% faster
- 63.9% fewer tokens

私はすぐに反応します。

もちろん、これは代表的なワークロードに基づく benchmark の数字であって、普遍的な法則ではありません。でも、より大きな考え方はそれでも十分に魅力的です。

もしモデルが tool-calling の連鎖をより効率的な実行形に圧縮できるなら、agent system の経済性はかなり変わり得ます。

## この更新から開発者が本当に受け取るべきもの

大事なのは、どれだけ機能が追加されたかではありません。

大事なのは、framework が実際のアプリケーションに最も必要な場所で強くなっていることです。

- runtime shell
- deployment path
- execution efficiency
- built-in operational patterns

こうした成熟のシグナルは、もう1枚の表面的な AI 機能一覧よりずっと重要です。

## 私の見方

この更新が重要なのは、単に表面積を増やしているだけではないからです。

実際のアプリケーションが必要とする領域、特にローカル実験から実際に動かして保守できるシステムへ移したいチームにとって重要な領域で、agents を取り巻く runtime と deployment の話を強化しています。

そこが framework の説得力が増すところです。

このリリースを追うなら、harness、hosted agents、CodeAct は間違いなく最も注目する部分です。

原文: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
