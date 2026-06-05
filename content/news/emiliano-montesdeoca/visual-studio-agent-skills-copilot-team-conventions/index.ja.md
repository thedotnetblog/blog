---
title: "Visual StudioのAgent Skills：チームの実際の作業方法をCopilotに教える"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual StudioはAgent Skillsをサポートするようになりました。これはCopilotにチーム固有のワークフロー、コーディング標準、規約を教える再利用可能な指示セットです。一度定義すれば、自動的に適用されます。"
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

AIコーディングアシスタントに関する持続的な不満の一つ：一般的なプログラミングはよく知っているが、*あなたの*チーム固有の規約、内部API、好みのパターンは知らない。毎セッション、コンテキストを再説明することになる。Visual StudioのAgent Skillsはこの問題を解決するために設計されています。

## Agent Skillsとは

`SKILL.md`ファイルで定義された再利用可能な指示セット。Copilotエージェントに特定のタスクの処理方法を教えます。「ビルドパイプラインの実行方法」、「サービス層のボイラープレートの生成方法」、「コードレビューチェックリスト」などのスキルを定義します。エージェントは関連する場合に自動的にスキルを適用します。

これは新しい概念ではありません（`.github/copilot-instructions.md`はしばらく前から存在します）が、Visual Studioの統合によって、発見UIを持つファーストクラスオブジェクトになります。

## Visual StudioでのSkillの作成

統合されたUIフロー：Copilot Chatのツールアイコンをクリックし、スキルパネルを開き、`+`をクリック。グローバル（個人）またはソリューションレベルのスコープを選択し、名前を選択すると、Visual Studioがテンプレートを生成します。CopilotエージェントモードでテンプレートをFillするサポートを受けられます — エージェントを使ってエージェント用のスキルを書くことができます。

現在Insidersチャンネルで利用可能、まもなくReleaseに来る予定。

スキルを手動で作成することもできます：

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## 検出場所

スキルは標準パスから自動検出されます：

**ソリューションレベル（リポジトリ経由で共有）：** `.github/skills/`、`.claude/skills/`、`.agents/skills/`

**グローバル/個人（ユーザープロファイル、どこでも利用可能）：** `~/.copilot/skills/`、`~/.agents/skills/`

マルチロケーションサポートにより、同じ規約がGitHub Copilot、Claude Code、その他のエージェントフレームワークで機能します — スキルを一度定義すれば、どこでも使えます。

## フォーマット

スキルは[agentskills.io/specification](https://agentskills.io/specification)フォーマットに従います — 人間が読めて機械が解析できるMarkdownベースの仕様。`SKILL.md`と並べてスクリプト、テンプレート、例を含めることができます。

## 実践的な価値

本当の力は個々の機能にあるのではなく — チーム共有スキル（`.github/skills/`経由）と個人スキル（`~/.agents/skills/`経由）の組み合わせにあります。チームスキルは組織がどのように物事を行うかを符号化します。個人スキルはあなたが具体的にどのように作業するかを符号化します。エージェントは両方のコンテキストを自動的に取得します。

すでにCopilotを積極的に使用している組織にとって、これは一般的なアドバイスを与えるのではなく、ツールがコードベースの具体的な規約を実際に把握するための重要なステップです。

元の投稿: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
