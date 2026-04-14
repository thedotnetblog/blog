---
title: "As Agent Skills no .NET ficaram realmente flexíveis"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "O Microsoft Agent Framework agora suporta três formas de criar skills — arquivos, classes e código inline — todas compostas através de um único provider. Aqui explico por que isso importa e como usar cada uma."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Se você tem construído agentes com o Microsoft Agent Framework, já conhece o processo: define skills, conecta a um provider e deixa o agente decidir qual invocar. O que há de novo é *como* você cria essas skills — e o salto em flexibilidade é significativo.

A última atualização introduz três padrões de autoria para agent skills: **baseadas em arquivos**, **baseadas em classes** e **definidas em código inline**. As três se conectam a um único `AgentSkillsProviderBuilder`, o que significa que você pode misturar e combinar sem lógica de roteamento nem código especial. Vou te mostrar cada uma e quando usar.

## Skills baseadas em arquivos: o ponto de partida

Skills baseadas em arquivos são exatamente o que parecem — um diretório no disco com um arquivo `SKILL.md`, scripts opcionais e documentos de referência. A forma mais direta de dar novas capacidades ao seu agente:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

O frontmatter do `SKILL.md` declara o nome e descrição, e a seção de instruções diz ao agente como usar os scripts e referências:

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

Depois você conecta com `SubprocessScriptRunner.RunAsync` para execução de scripts:

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

O agente descobre a skill automaticamente e invoca o script de provisioning quando precisa verificar o status das contas. Limpo e simples.

## Skills baseadas em classes: distribuir via NuGet

Aqui é onde fica interessante para times. Skills baseadas em classes derivam de `AgentClassSkill<T>` e usam atributos como `[AgentSkillResource]` e `[AgentSkillScript]` para que o framework descubra tudo por reflexão:

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

O legal é que um time pode empacotar isso como pacote NuGet. Você adiciona ao projeto, coloca no builder e funciona junto com suas skills de arquivo sem coordenação:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Ambas as skills aparecem no system prompt do agente. O agente decide qual usar baseado na conversa — sem código de roteamento.

## Skills inline: a ponte rápida

Sabe aquele momento quando outro time está construindo exatamente a skill que você precisa, mas só vai ficar pronta no próximo sprint? `AgentInlineSkill` é sua ponte:

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

Adicione ao builder assim como as outras:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Quando o pacote NuGet finalmente sair, você troca a skill inline pela versão baseada em classe. O agente não percebe a diferença.

Mas skills inline não são só para pontes. Também são a escolha certa quando você precisa gerar skills dinamicamente em runtime — pense em uma skill por unidade de negócio carregada de configuração — ou quando um script precisa capturar estado local que não pertence a um contêiner DI.

## Aprovação de scripts: humano no loop

Para nós desenvolvedores .NET construindo agentes de produção, essa é a parte que realmente desbloqueia conversas de deploy. Alguns scripts têm consequências reais — inscrever alguém em benefícios, consultar infraestrutura de produção. Ative `UseScriptApproval` e o agente pausa antes de executar qualquer script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Quando o agente quer executar um script, retorna um pedido de aprovação. Seu app coleta a decisão — aprovar ou rejeitar — e o agente continua. Em ambientes regulados, essa é a diferença entre "podemos fazer deploy disso" e "o jurídico disse não."

## Por que essa combinação importa

O verdadeiro poder não está em nenhum padrão individual — está na composição. Você pode:

- **Começar pequeno** com uma skill de arquivo, iterar nas instruções e publicar sem escrever C#
- **Distribuir skills reutilizáveis** como pacotes NuGet que outros times adicionam com uma linha
- **Cobrir lacunas** com skills inline quando precisa de algo *agora*
- **Filtrar diretórios compartilhados** com predicados para que seu agente só carregue o que deve
- **Adicionar supervisão humana** para scripts que tocam sistemas de produção

Tudo isso se compõe via `AgentSkillsProviderBuilder`. Sem roteamento especial, sem lógica condicional, sem verificações de tipo de skill.

## Para encerrar

As agent skills no .NET agora têm um modelo de autoria genuinamente flexível. Seja você um desenvolvedor solo prototipando com skills de arquivo ou um time enterprise distribuindo capacidades empacotadas via NuGet, os padrões se encaixam. E o mecanismo de aprovação de scripts o torna pronto para produção em ambientes onde você precisa daquele checkpoint humano.

Confira o [anúncio original](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), a [documentação de Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) no Microsoft Learn e os [exemplos .NET no GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) para começar.
