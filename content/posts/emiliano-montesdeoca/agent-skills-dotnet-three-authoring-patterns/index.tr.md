---
title: ".NET'te Agent Skills Ciddi Anlamda Esnek Hale Geldi"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework artık skill yazmak için üç yol destekliyor — dosya tabanlı, sınıf tabanlı ve satır içi kod — hepsi tek bir provider üzerinden birleştiriliyor. Bunun neden önemli olduğu ve her birini nasıl kullanacağınız."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

Microsoft Agent Framework ile agent geliştiriyorsanız rutini bilirsiniz: skill'leri tanımlarsınız, bir provider'a bağlarsınız ve agentın hangisini çağıracağına karar vermesini beklersiniz. Yeni olan şey ise bu skill'leri *nasıl* yazdığınız — ve esneklik sıçraması önemli.

Son güncelleme, agent skill'leri için üç farklı yazım deseni sunuyor: **dosya tabanlı**, **sınıf tabanlı** ve **satır içi kod tanımlı**. Üçü de tek bir `AgentSkillsProviderBuilder`'a takılır; yani herhangi bir yönlendirme mantığı veya özel bağlantı kodu olmadan bunları karıştırıp eşleştirebilirsiniz. Her birini ve ne zaman kullanacağınızı anlatalım.

## Dosya tabanlı skill'ler: başlangıç noktası

Dosya tabanlı skill'ler tam olarak adından anlaşıldığı gibi — diskte bir `SKILL.md` dosyası, isteğe bağlı scriptler ve referans belgelerle dolu bir dizin. Agentınıza yeni yetenekler vermenin en doğrudan yolu olarak düşünün:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md` frontmatter'ı skill adını ve açıklamasını bildirir, talimatlar bölümü ise agenta scriptleri ve referansları nasıl kullanacağını söyler:

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

Ardından script yürütmesi için `SubprocessScriptRunner.RunAsync` ile bağlantı kurarsınız:

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

Agent, skill'i otomatik olarak keşfeder ve hesap durumunu kontrol etmesi gerektiğinde provisioning scriptini çağırır. Temiz ve basit.

## Sınıf tabanlı skill'ler: NuGet üzerinden yayımlayın

İşte ekipler için ilginç kısım. Sınıf tabanlı skill'ler `AgentClassSkill<T>`'dan türetilir ve `[AgentSkillResource]` ile `[AgentSkillScript]` gibi attribute'lar kullanır; framework her şeyi yansıma (reflection) yoluyla keşfeder:

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

Buradaki güzellik, bir ekibin bunu NuGet paketi olarak paketleyebilmesidir. Projenize eklersiniz, builder'a bırakırsınız ve dosya tabanlı skill'lerinizle sıfır koordinasyonla birlikte çalışır:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

Her iki skill de agentın sistem prompt'unda görünür. Agent, konuşmaya göre hangisini kullanacağına karar verir — yönlendirme kodu gerekmez.

## Satır içi skill'ler: hızlı köprü

Başka bir ekibin tam ihtiyacınız olan skill'i geliştirdiğini ama bir sprint boyunca yayımlanmayacağını bildiğiniz anı tanıyor musunuz? `AgentInlineSkill` köprünüzdür:

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

Diğerleri gibi builder'a ekleyin:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .Build();
```

NuGet paketi sonunda yayımlandığında, satır içi skill'i sınıf tabanlıyla değiştirirsiniz. Agent farkı anlamaz.

Ancak satır içi skill'ler sadece köprü için değil. Çalışma zamanında dinamik olarak skill üretmeniz gerektiğinde de doğru seçimdir — config'den yüklenen iş birimi başına bir skill gibi — veya bir scriptin DI container'ına ait olmayan yerel durumu kapatması (closure) gerektiğinde.

## Script onayı: human-in-the-loop

Üretim agentları geliştiren .NET geliştiricileri için bu, dağıtım konuşmalarını gerçekten açık eden kısım. Bazı scriptlerin gerçek sonuçları var — birini sigorta planına kaydetmek, üretim altyapısını sorgulamak. `UseScriptApproval`'ı açın ve agent herhangi bir scripti çalıştırmadan önce duraklar:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

Agent bir script çalıştırmak istediğinde, bunun yerine bir onay isteği döndürür. Uygulamanız kararı toplar — onayla veya reddet — ve agent buna göre devam eder. Düzenlenmiş ortamlarda bu, "bunu dağıtabiliriz" ile "hukuk hayır diyor" arasındaki farktır.

## Bu kombinasyonun önemi

Gerçek güç tek bir yazım deseninde değil — kompozisyondadır. Şunları yapabilirsiniz:

- **Küçük başlayın** dosya tabanlı skill ile, talimatlarda yineleyin ve C# yazmadan yayımlayın
- **Yeniden kullanılabilir skill'ler yayımlayın** NuGet paketleri olarak; diğer ekipler tek satırla ekleyebilir
- **Boşlukları kapatın** satır içi skill'lerle ihtiyacınız olan şeyi *hemen* geliştirmek için
- **Paylaşılan skill dizinlerini filtreleyin** predicate'lerle, agentınızın yalnızca gereken şeyi yüklemesi için
- **İnsan denetimi ekleyin** üretim sistemlerine dokunan scriptler için

Bunların tümü `AgentSkillsProviderBuilder` üzerinden birleşir. Özel yönlendirme, koşullu mantık, skill tür kontrolleri yok.

## Sonuç

.NET'te agent skill'leri artık gerçekten esnek bir yazım modeline sahip. İster dosya tabanlı skill'lerle prototip çizen solo bir geliştirici olun, ister NuGet aracılığıyla paketlenmiş yetenekler yayımlayan kurumsal bir ekip, desenler her duruma uyuyor. Ve script onay mekanizması, insan denetim noktasına ihtiyaç duyduğunuz ortamlar için üretime hazır hale getiriyor.

Tam rehber için [orijinal duyuruya](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/), Microsoft Learn'deki [Agent Skills belgelerine](https://learn.microsoft.com/en-us/agent-framework/agents/skills) ve uygulamalı deneyim için [GitHub'daki .NET örneklerine](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) göz atın.
