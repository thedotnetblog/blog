---
title: ".NET의 Agent Skills가 정말 유연해졌다"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework가 이제 스킬을 만드는 세 가지 방법을 지원합니다 — 파일, 클래스, 인라인 코드 — 모두 단일 provider를 통해 조합 가능합니다. 왜 중요한지, 각각 어떻게 사용하는지 설명합니다."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}})에서 확인하세요.*

Microsoft Agent Framework로 에이전트를 구축해왔다면 흐름은 알고 있을 겁니다: 스킬을 정의하고, provider에 연결하고, 에이전트가 어떤 것을 호출할지 결정하게 합니다. 새로운 것은 스킬을 *만드는 방법*이고, 유연성의 향상이 상당합니다.

최신 업데이트는 에이전트 스킬에 대한 세 가지 작성 패턴을 도입합니다: **파일 기반**, **클래스 기반**, **인라인 코드 정의**. 세 가지 모두 단일 `AgentSkillsProviderBuilder`에 연결되므로 라우팅 로직이나 특별한 접착 코드 없이 자유롭게 조합할 수 있습니다. 각 패턴과 언제 사용해야 하는지 설명하겠습니다.

## 파일 기반 스킬: 시작점

파일 기반 스킬은 말 그대로입니다 — `SKILL.md` 파일, 선택적 스크립트, 참조 문서가 있는 디스크의 디렉토리입니다. 에이전트에 새로운 기능을 부여하는 가장 직접적인 방법입니다:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md`의 프론트매터에서 스킬 이름과 설명을 선언하고, 지시 섹션에서 에이전트에게 스크립트와 참조를 어떻게 사용하는지 알려줍니다:

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

그런 다음 `SubprocessScriptRunner.RunAsync`로 스크립트 실행을 연결합니다:

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

에이전트는 자동으로 스킬을 발견하고 계정 상태를 확인해야 할 때 프로비저닝 스크립트를 호출합니다. 깔끔하고 간단합니다.

## 클래스 기반 스킬: NuGet으로 배포

여기서 팀에게 흥미로워집니다. 클래스 기반 스킬은 `AgentClassSkill<T>`에서 파생하며 `[AgentSkillResource]`와 `[AgentSkillScript]` 같은 속성을 사용하여 프레임워크가 리플렉션을 통해 모든 것을 발견합니다:

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

멋진 점은 팀이 이것을 NuGet 패키지로 패키징할 수 있다는 것입니다. 프로젝트에 추가하고, 빌더에 넣으면 파일 기반 스킬과 함께 조율 없이 동작합니다:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

두 스킬 모두 에이전트의 시스템 프롬프트에 나타납니다. 에이전트가 대화에 따라 어떤 것을 사용할지 결정합니다 — 라우팅 코드가 필요 없습니다.

## 인라인 스킬: 빠른 브릿지

다른 팀이 정확히 필요한 스킬을 만들고 있는데 다음 스프린트까지 완성되지 않는 그 순간 아시죠? `AgentInlineSkill`이 당신의 브릿지입니다:

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

다른 것들처럼 빌더에 추가합니다:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

NuGet 패키지가 최종 출시되면 인라인 스킬을 클래스 기반 버전으로 교체하면 됩니다. 에이전트는 차이를 모릅니다.

하지만 인라인 스킬은 브릿지만을 위한 것이 아닙니다. 런타임에 동적으로 스킬을 생성해야 할 때 — 구성에서 로드되는 비즈니스 유닛별 스킬을 생각해보세요 — 또는 스크립트가 DI 컨테이너에 속하지 않는 로컬 상태를 캡처해야 할 때도 올바른 선택입니다.

## 스크립트 승인: 휴먼 인 더 루프

프로덕션 에이전트를 구축하는 .NET 개발자로서 이 부분이 배포 논의를 정말로 열어줍니다. 일부 스크립트에는 실제 결과가 있습니다 — 누군가를 복리후생에 등록하거나 프로덕션 인프라를 조회하는 것. `UseScriptApproval`을 활성화하면 에이전트가 스크립트 실행 전에 일시 중지합니다:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

에이전트가 스크립트를 실행하려 할 때, 대신 승인 요청을 반환합니다. 앱이 결정을 수집하고 — 승인 또는 거부 — 에이전트가 그에 따라 계속합니다. 규제 환경에서는 "이것을 배포할 수 있다"와 "법무팀이 안 된다고 했다" 사이의 차이입니다.

## 왜 이 조합이 중요한가

진정한 힘은 개별 패턴이 아니라 구성에 있습니다. 다음이 가능합니다:

- 파일 기반 스킬로 **작게 시작**하고, 지시를 반복하고, C#을 작성하지 않고도 게시
- 다른 팀이 한 줄로 추가할 수 있는 NuGet 패키지로 **재사용 가능한 스킬을 배포**
- *지금* 필요한 것이 있을 때 인라인 스킬로 **격차를 메움**
- 에이전트가 로드해야 할 것만 로드하도록 프레디케이트로 **공유 디렉토리를 필터링**
- 프로덕션 시스템을 건드리는 스크립트에 **인간 감독을 추가**

이 모든 것이 `AgentSkillsProviderBuilder`를 통해 구성됩니다. 특별한 라우팅 없이, 조건 로직 없이, 스킬 타입 체크 없이.

## 마무리

.NET의 에이전트 스킬은 이제 진정으로 유연한 작성 모델을 갖추었습니다. 파일 기반 스킬로 프로토타이핑하는 솔로 개발자이든 NuGet을 통해 패키지된 기능을 배포하는 엔터프라이즈 팀이든 패턴이 맞습니다. 그리고 스크립트 승인 메커니즘이 인간 체크포인트가 필요한 환경에서 프로덕션 준비를 가능하게 합니다.

[원본 발표](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), Microsoft Learn의 [Agent Skills 문서](https://learn.microsoft.com/en-us/agent-framework/agents/skills), GitHub의 [.NET 샘플](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills)을 확인하고 시작하세요.
