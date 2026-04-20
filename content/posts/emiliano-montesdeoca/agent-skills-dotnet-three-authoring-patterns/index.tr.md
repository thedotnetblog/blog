---
title: ".NET'te Agent Skills Artık Gerçekten Esnek"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework artık üç şekilde yetenek yazmayı destekliyor — dosyalar, sınıflar ve satır içi kod — hepsi tek bir sağlayıcı aracılığıyla birleştirilmiş. İşte bu neden önemli ve her birini nasıl kullanacaksınız."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

Microsoft Agent Framework ile ajan oluşturuyorsanız, süreci biliyorsunuzdur: yetenekleri tanımlarsınız, bir sağlayıcıya bağlarsınız ve ajanın hangisini çağıracağını belirlemesine izin verirsiniz. Yeni olan, bu yetenekleri *nasıl* yazdığınız — ve esneklik sıçraması önemli.

Son güncelleme, ajan yetenekleri için üç farklı yazma deseni sunuyor: **dosya tabanlı**, **sınıf tabanlı** ve **satır içi kod tanımlı**. Üçü de tek bir `AgentSkillsProviderBuilder`'a bağlanıyor, yani yönlendirme mantığı olmadan karıştırıp eşleştirebilirsiniz.

## Dosya tabanlı yetenekler: başlangıç noktası

Dosya tabanlı yetenekler tam olarak göründüğü gibi — bir `SKILL.md` dosyası, isteğe bağlı betikler ve referans belgelerle diskte bir dizin:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md` ön maddesi yetenek adını ve açıklamasını bildirir, talimatlar bölümü ise ajana betikleri ve referansları nasıl kullanacağını söyler.

`SubprocessScriptRunner.RunAsync` ile bağlarsınız:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);
```

## Sınıf tabanlı yetenekler: NuGet ile gönder

Burada takımlar için işler ilginçleşiyor. Sınıf tabanlı yetenekler `AgentClassSkill<T>`'den türetilir ve `[AgentSkillResource]` ve `[AgentSkillScript]` gibi nitelikleri kullanır:

```csharp
public sealed class BenefitsEnrollmentSkill : AgentClassSkill<BenefitsEnrollmentSkill>
{
    public override AgentSkillFrontmatter Frontmatter { get; } = new(
        "benefits-enrollment",
        "Enroll an employee in health, dental, or vision plans.");

    [AgentSkillScript("enroll")]
    private static string Enroll(string employeeId, string planCode)
    {
        bool success = HrClient.EnrollInPlan(employeeId, planCode);
        return JsonSerializer.Serialize(new { success, employeeId, planCode });
    }
}
```

Bir takım bunu NuGet paketi olarak paketleyebilir. Projenize eklersiniz, oluşturucuya bırakırsınız ve dosya tabanlı yeteneklerinizle birlikte çalışır.

## Satır içi yetenekler: hızlı köprü

Başka bir takımın tam ihtiyaç duyduğunuz yeteneği oluşturduğu ama bir sprint için gelmeyeceği an? `AgentInlineSkill` köprünüzdür:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: "1. Çalışan ID'sini iste. 2. calculate-balance kullan. 3. Sonuçları sun.")
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int remaining = HrDatabase.GetAnnualAllowance(employeeId, leaveType)
                      - HrDatabase.GetDaysUsed(employeeId, leaveType);
        return JsonSerializer.Serialize(new { employeeId, leaveType, remaining });
    });
```

NuGet paketi geldiğinde, satır içi yeteneği sınıf tabanlıyla değiştirirsiniz. Ajan farkı anlamaz.

## Betik onayı: human-in-the-loop

Üretim ajanları oluşturan .NET geliştiricileri için bu, dağıtım konuşmalarının önünü açan kısım. `UseScriptApproval`'ı açın ve ajan herhangi bir betiği çalıştırmadan önce duraklar:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

## Sonuç

.NET'te agent skills artık gerçekten esnek bir yazma modeline sahip. Dosya tabanlı yeteneklerle prototip oluşturuyor veya NuGet aracılığıyla paketlenmiş yetenekler gönderiyorsanız da, tüm desenler `AgentSkillsProviderBuilder` aracılığıyla birleşir.

[Orijinal duyuruya](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) ve [GitHub örneklerine](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) göz atın.
