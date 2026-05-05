---
title: ".NETのAgent Skillsが本気で柔軟になった"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Frameworkがスキルの作成方法を3つサポート — ファイル、クラス、インラインコード — すべて単一のプロバイダーで構成可能に。なぜこれが重要なのか、それぞれの使い方を解説します。"
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *この記事は自動翻訳されました。原文は[こちら]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}})をご覧ください。*

Microsoft Agent Frameworkでエージェントを構築しているなら、流れは分かっているはずです：スキルを定義し、プロバイダーに接続し、エージェントにどれを呼び出すか判断させる。新しいのはスキルの*作り方*であり、柔軟性の向上は大きなものです。

最新のアップデートでは、エージェントスキルの3つのオーサリングパターンが導入されました：**ファイルベース**、**クラスベース**、**インラインコード定義**。3つすべてが単一の `AgentSkillsProviderBuilder` に接続されるため、ルーティングロジックや特別なグルーコードなしで自由に組み合わせることができます。それぞれのパターンと、いつ使うべきかを説明します。

## ファイルベースのスキル：出発点

ファイルベースのスキルはそのままの意味です — `SKILL.md`ファイル、オプションのスクリプト、参照ドキュメントを含むディスク上のディレクトリです。エージェントに新しい能力を与える最もシンプルな方法です：

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md`のフロントマターでスキル名と説明を宣言し、指示セクションでスクリプトと参照の使い方をエージェントに伝えます：

```markdown
---
name: onboarding-guide
description: >-
  Walk new hires through their first-week setup checklist.
---

## Instructions

1. Ask for the employee's name and start date.
2. Run `scripts/check-provisioning.py` to verify accounts.
3. Walk through `references/onboarding-checklist.md`.
4. Follow up on incomplete items.
```

そして `SubprocessScriptRunner.RunAsync` でスクリプト実行を接続します：

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);

AIAgent agent = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential())
    .GetResponsesClient()
    .AsAIAgent(new ChatClientAgentOptions
    {
        Name = "HRAgent",
        ChatOptions = new() { Instructions = "You are a helpful HR assistant." },
        AIContextProviders = [skillsProvider],
    },
    model: deploymentName);
```

エージェントは自動的にスキルを発見し、アカウントステータスを確認する必要があるときにプロビジョニングスクリプトを呼び出します。クリーンでシンプルです。

## クラスベースのスキル：NuGetで配布

ここからがチームにとって面白いところです。クラスベースのスキルは `AgentClassSkill<T>` から派生し、`[AgentSkillResource]` や `[AgentSkillScript]` などの属性を使用して、フレームワークがリフレクションですべてを発見します：

```csharp
public sealed class BenefitsEnrollmentSkill : AgentClassSkill<BenefitsEnrollmentSkill>
{
    public override AgentSkillFrontmatter Frontmatter { get; } = new(
        "benefits-enrollment",
        "Enroll an employee in health, dental, or vision plans.");

    protected override string Instructions => """
        1. Read the available-plans resource.
        2. Confirm the plan the employee wants.
        3. Use the enroll script to complete enrollment.
        """;

    [AgentSkillResource("available-plans")]
    [Description("Plan options with monthly pricing.")]
    public string AvailablePlans => """
        ## Available Plans (2026)
        - Health: Basic HMO ($0/month), Premium PPO ($45/month)
        - Dental: Standard ($12/month), Enhanced ($25/month)
        - Vision: Basic ($8/month)
        """;

    [AgentSkillScript("enroll")]
    [Description("Enrolls employee in the specified benefit plan.")]
    private static string Enroll(string employeeId, string planCode)
    {
        bool success = HrClient.EnrollInPlan(employeeId, planCode);
        return JsonSerializer.Serialize(new { success, employeeId, planCode });
    }
}
```

素晴らしいのは、チームがこれをNuGetパッケージとしてパッケージ化できることです。プロジェクトに追加し、ビルダーに入れるだけで、ファイルベースのスキルと一緒に調整なしで動作します：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

両方のスキルがエージェントのシステムプロンプトに表示されます。エージェントは会話に基づいてどちらを使うか判断します — ルーティングコードは不要です。

## インラインスキル：素早いブリッジ

別のチームがまさに必要なスキルを構築しているけど、次のスプリントまで完成しない、あの瞬間を知っていますか？`AgentInlineSkill` があなたのブリッジです：

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: """
        1. Ask for the employee ID if not provided.
        2. Use calculate-balance to get the remaining balance.
        3. Present used and remaining days clearly.
        """)
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int totalDays = HrDatabase.GetAnnualAllowance(employeeId, leaveType);
        int daysUsed = HrDatabase.GetDaysUsed(employeeId, leaveType);
        int remaining = totalDays - daysUsed;
        return JsonSerializer.Serialize(new { employeeId, leaveType, totalDays, daysUsed, remaining });
    });
```

他のスキルと同じようにビルダーに追加します：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

NuGetパッケージが最終的にリリースされたら、インラインスキルをクラスベースのバージョンに交換するだけです。エージェントは違いに気づきません。

ただし、インラインスキルはブリッジだけのものではありません。ランタイムで動的にスキルを生成する必要がある場合 — 設定からロードされるビジネスユニットごとのスキルを考えてみてください — やスクリプトがDIコンテナに属さないローカルステートをキャプチャする必要がある場合にも適切な選択です。

## スクリプト承認：ヒューマンインザループ

本番エージェントを構築する.NET開発者にとって、これがデプロイメントの議論を本当に前進させる部分です。一部のスクリプトには実際の影響があります — 誰かを福利厚生に登録する、本番インフラを照会する。`UseScriptApproval` を有効にすると、エージェントはスクリプト実行前に一時停止します：

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

エージェントがスクリプトを実行したいとき、代わりに承認リクエストを返します。アプリが判断を収集し — 承認または拒否 — エージェントはそれに応じて続行します。規制環境では、これが「デプロイできる」と「法務がノーと言っている」の違いです。

## なぜこの組み合わせが重要なのか

本当の力は個々のパターンにあるのではなく、構成にあります。以下が可能になります：

- ファイルベースのスキルで**小さく始めて**、指示を反復し、C#を書かずに公開する
- 他のチームが1行で追加できるNuGetパッケージとして**再利用可能なスキルを配布**する
- 何か*今すぐ*必要なときにインラインスキルで**ギャップを埋める**
- エージェントが必要なものだけをロードするようにプレディケートで**共有ディレクトリをフィルタリング**する
- 本番システムに触れるスクリプトに**人間の監視を追加**する

これらすべてが `AgentSkillsProviderBuilder` を通じて構成されます。特別なルーティングなし、条件ロジックなし、スキルタイプチェックなし。

## まとめ

.NETのエージェントスキルは、真に柔軟なオーサリングモデルを手に入れました。ファイルベースのスキルでプロトタイピングするソロ開発者であろうと、NuGet経由でパッケージ化された機能を配布するエンタープライズチームであろうと、パターンは適合します。そしてスクリプト承認メカニズムにより、人間のチェックポイントが必要な環境でも本番対応できます。

[オリジナルの発表](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/)、Microsoft Learnの[Agent Skillsドキュメント](https://learn.microsoft.com/en-us/agent-framework/agents/skills)、GitHubの[.NETサンプル](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills)をチェックして始めましょう。
