---
title: "Las Agent Skills en .NET se volvieron muy flexibles"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "El Microsoft Agent Framework ahora soporta tres formas de crear skills — archivos, clases y código inline — todas compuestas a través de un único provider. Aquí te cuento por qué importa y cómo usar cada una."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Este artículo fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "agent-skills-dotnet-three-authoring-patterns.md" >}}).*

Si has estado construyendo agentes con el Microsoft Agent Framework, ya conoces la dinámica: defines skills, las conectas a un provider y dejas que el agente decida cuál invocar. Lo nuevo es *cómo* creas esas skills — y el salto en flexibilidad es importante.

La última actualización introduce tres patrones de autoría para agent skills: **basadas en archivos**, **basadas en clases** y **definidas en código inline**. Las tres se conectan a un único `AgentSkillsProviderBuilder`, lo que significa que puedes mezclar y combinar sin lógica de enrutamiento ni código especial. Te explico cada una y cuándo usarla.

## Skills basadas en archivos: el punto de partida

Las skills basadas en archivos son exactamente lo que suenan — un directorio en disco con un archivo `SKILL.md`, scripts opcionales y documentos de referencia. Es la forma más directa de darle nuevas capacidades a tu agente:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

El frontmatter del `SKILL.md` declara el nombre y descripción, y la sección de instrucciones le dice al agente cómo usar los scripts y referencias:

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

Luego lo conectas con `SubprocessScriptRunner.RunAsync` para la ejecución de scripts:

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

El agente descubre la skill automáticamente e invoca el script de provisión cuando necesita verificar el estado de las cuentas. Limpio y simple.

## Skills basadas en clases: distribuir vía NuGet

Aquí es donde se pone interesante para los equipos. Las skills basadas en clases derivan de `AgentClassSkill<T>` y usan atributos como `[AgentSkillResource]` y `[AgentSkillScript]` para que el framework descubra todo por reflexión:

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

Lo mejor es que un equipo puede empaquetar esto como un paquete NuGet. Lo agregas a tu proyecto, lo metes en el builder y funciona junto a tus skills basadas en archivos sin coordinación:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Ambas skills aparecen en el system prompt del agente. El agente decide cuál usar según la conversación — sin código de enrutamiento.

## Skills inline: el puente rápido

¿Conoces ese momento cuando otro equipo está construyendo exactamente la skill que necesitas, pero no la tendrán lista hasta el próximo sprint? `AgentInlineSkill` es tu puente:

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

Agrégala al builder igual que las demás:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Cuando el paquete NuGet finalmente salga, intercambias la skill inline por la basada en clases. El agente no nota la diferencia.

Pero las skills inline no son solo para puentes. También son la opción correcta cuando necesitas generar skills dinámicamente en runtime — piensa en una skill por unidad de negocio cargada desde configuración — o cuando un script necesita capturar estado local que no pertenece a un contenedor DI.

## Aprobación de scripts: humano en el bucle

Para los que construimos agentes de producción en .NET, esta es la parte que realmente desbloquea las conversaciones de despliegue. Algunos scripts tienen consecuencias reales — inscribir a alguien en beneficios, consultar infraestructura de producción. Activa `UseScriptApproval` y el agente se pausa antes de ejecutar cualquier script:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Cuando el agente quiere ejecutar un script, devuelve una solicitud de aprobación. Tu app recoge la decisión — aprobar o rechazar — y el agente continúa. En entornos regulados, esta es la diferencia entre "podemos desplegar esto" y "legal dice que no."

## Por qué esta combinación importa

El verdadero poder no está en ningún patrón individual — está en la composición. Puedes:

- **Empezar pequeño** con una skill basada en archivos, iterar en las instrucciones y publicarla sin escribir C#
- **Distribuir skills reutilizables** como paquetes NuGet que otros equipos pueden agregar con una línea
- **Cubrir huecos** con skills inline cuando necesitas algo *ya*
- **Filtrar directorios compartidos** con predicados para que tu agente solo cargue lo que debe
- **Agregar supervisión humana** para scripts que tocan sistemas de producción

Todo esto se compone a través de `AgentSkillsProviderBuilder`. Sin enrutamiento especial, sin lógica condicional, sin verificaciones de tipo de skill.

## Para cerrar

Las agent skills en .NET ahora tienen un modelo de autoría genuinamente flexible. Ya sea que seas un desarrollador solo prototipando con skills basadas en archivos o un equipo enterprise distribuyendo capacidades empaquetadas vía NuGet, los patrones encajan. Y el mecanismo de aprobación de scripts lo hace listo para producción en entornos donde necesitas ese checkpoint humano.

Echa un vistazo al [anuncio original](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), la [documentación de Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills) en Microsoft Learn y los [ejemplos en .NET en GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) para ponerte manos a la obra.
