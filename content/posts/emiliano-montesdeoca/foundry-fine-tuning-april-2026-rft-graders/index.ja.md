---
title: "FoundryのRFTがより安く、よりスマートに — 変更点まとめ"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundryが今月3つのRFTアップデートをリリース：o4-miniのグローバルトレーニング、新しいGPT-4.1モデルグレーダー、そしてデバッグ時間を大幅に節約できるベストプラクティスガイド。"
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *この記事は自動翻訳されています。原文は[こちら]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}})をご覧ください。*

ファインチューニングされたモデルに依存する.NETアプリを開発しているなら、今月のFoundryアップデートは注目に値します。Reinforcement Fine-Tuningがより利用しやすく、大幅に安くなりました。

詳細は[公式発表](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/)にありますが、ここでは実用的なポイントをまとめます。

## o4-miniのグローバルトレーニング

o4-miniは推論重視のワークロードやエージェント型ワークロードに最適なモデルです。大きなニュース：13以上のAzureリージョンからファインチューニングジョブを起動でき、Standardトレーニングと比較してトークンあたりのトレーニングコストが低くなりました。同じインフラ、同じ品質、より広い対応範囲。

チームが複数の地域に分散している場合、これは重要です。トレーニングのために少数のリージョンに縛られることはもうありません。

グローバルトレーニングジョブを開始するREST APIコールはこちらです：

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

この`trainingType: globalstandard`フラグが重要な違いです。

## 新しいモデルグレーダー：GPT-4.1ファミリー

グレーダーはモデルが最適化する報酬シグナルを定義します。これまで、モデルベースのグレーダーは限られたモデルセットに制約されていました。今回、GPT-4.1、GPT-4.1-mini、GPT-4.1-nanoの3つの新しいオプションが追加されました。

決定的グレーダーの代わりにモデルグレーダーを使うべきなのはどんな時でしょうか？タスクの出力がオープンエンドの場合、複数の次元で部分的なスコアリングが必要な場合、またはツール呼び出しの正確さがセマンティックコンテキストに依存するエージェント型ワークフローを構築している場合です。

ポイントは、ティアリング戦略が実用的であること：

- **GPT-4.1-nano** 初期のイテレーション用。低コスト、高速なフィードバックループ。
- **GPT-4.1-mini** 評価ルーブリックが安定し、より高い精度が必要になったら。
- **GPT-4.1** 本番環境の評価や、すべてのスコアリング判断が重要な複雑なルーブリック用。

単一のRFTジョブでグレーダータイプを混在させることもできます。「正解」の次元にはstring-matchを使い、推論品質の評価にはモデルグレーダーを使う。この柔軟性が、実際のワークロードで本当に役立つ理由です。

## RFTデータフォーマットの落とし穴

ここでつまずく人が多いです。RFTのデータフォーマットはSFTとは異なります。各行の最後のメッセージはUserまたはDeveloperロールでなければなりません — Assistantではありません。期待される回答は、グレーダーが直接参照する`reference_answer`のようなトップレベルのキーに入れます。

これまでSupervised Fine-Tuningを行っていてRFTに切り替えたい場合は、トレーニングデータを再構築する必要があります。このステップを飛ばすと、ジョブがサイレントに失敗します。

## .NET開発者にとってなぜ重要か

Azure OpenAI SDKを通じて.NETアプリからファインチューニングされたモデルを呼び出している場合、トレーニングコストの低下はより積極的にイテレーションできることを意味します。モデルグレーダーのオプションにより、完全一致シナリオだけでなく、ニュアンスのあるタスクに対してファインチューニングが可能になります。そして[GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md)のベストプラクティスガイドは、実際のデバッグ時間を節約してくれます。

小さく始めましょう。10から100サンプル。シンプルなグレーダー。ループを検証。そしてスケール。
