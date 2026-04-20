---
title: ".NET में एजेंट स्किल्स अब वास्तव में लचीले हो गए हैं"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework अब स्किल्स लिखने के तीन तरीके सपोर्ट करता है — फ़ाइलें, क्लासेज़ और इनलाइन कोड — सभी एक सिंगल प्रोवाइडर के माध्यम से कंपोज़ किए गए। जानें यह क्यों मायने रखता है और प्रत्येक का उपयोग कैसे करें।"
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

अगर आप Microsoft Agent Framework के साथ एजेंट बना रहे हैं, तो आप तरीका जानते हैं: आप स्किल्स परिभाषित करते हैं, उन्हें एक प्रोवाइडर में वायर करते हैं, और एजेंट को पता लगाने देते हैं कि कौन सा उपयोग करना है। नया यह है कि आप उन स्किल्स को *कैसे* लिखते हैं — और लचीलेपन की छलांग महत्वपूर्ण है।

लेटेस्ट अपडेट एजेंट स्किल्स के लिए तीन अलग-अलग authoring पैटर्न पेश करता है: **फ़ाइल-बेस्ड**, **क्लास-बेस्ड** और **इनलाइन कोड-डिफाइंड**। तीनों एक सिंगल `AgentSkillsProviderBuilder` में प्लग होते हैं, यानी आप बिना किसी रूटिंग लॉजिक के मिक्स और मैच कर सकते हैं।

## फ़ाइल-बेस्ड स्किल्स: शुरुआती बिंदु

फ़ाइल-बेस्ड स्किल्स बिल्कुल वैसी ही हैं जैसी लगती हैं — एक `SKILL.md` फ़ाइल, वैकल्पिक स्क्रिप्ट्स और रेफरेंस डॉक्युमेंट्स के साथ डिस्क पर एक डायरेक्टरी:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

`SKILL.md` frontmatter स्किल का नाम और विवरण बताता है, और instructions सेक्शन एजेंट को बताता है कि स्क्रिप्ट्स और रेफरेंस का उपयोग कैसे करें।

फिर आप इसे `SubprocessScriptRunner.RunAsync` के साथ वायर करते हैं:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);
```

## क्लास-बेस्ड स्किल्स: NuGet के जरिए शिप करें

यहीं से टीमों के लिए यह दिलचस्प होता है। क्लास-बेस्ड स्किल्स `AgentClassSkill<T>` से derive होती हैं और `[AgentSkillResource]` तथा `[AgentSkillScript]` जैसे attributes उपयोग करती हैं:

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

एक टीम इसे NuGet पैकेज के रूप में पैकेज कर सकती है। आप इसे अपने प्रोजेक्ट में जोड़ते हैं, बिल्डर में डालते हैं, और यह आपकी फ़ाइल-बेस्ड स्किल्स के साथ काम करता है।

## इनलाइन स्किल्स: क्विक ब्रिज

वह क्षण जब किसी अन्य टीम की स्किल बनने में समय लगे तो `AgentInlineSkill` आपका ब्रिज है:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: "1. Ask for employee ID. 2. Use calculate-balance. 3. Present results.")
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int remaining = HrDatabase.GetAnnualAllowance(employeeId, leaveType)
                      - HrDatabase.GetDaysUsed(employeeId, leaveType);
        return JsonSerializer.Serialize(new { employeeId, leaveType, remaining });
    });
```

NuGet पैकेज शिप होने पर, आप इनलाइन स्किल को क्लास-बेस्ड से बदल दें। एजेंट को फर्क नहीं पता।

## स्क्रिप्ट अप्रूवल: ह्यूमन-इन-द-लूप

प्रोडक्शन एजेंट बनाने वाले .NET डेवलपर्स के लिए, यही वह हिस्सा है जो deployment बातचीत को आगे बढ़ाता है। `UseScriptApproval` फ्लिप करें और एजेंट किसी भी स्क्रिप्ट को एग्जीक्यूट करने से पहले रुकता है:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

## समापन

.NET में एजेंट स्किल्स में अब एक वास्तव में लचीला authoring मॉडल है। चाहे आप फ़ाइल-बेस्ड स्किल्स के साथ प्रोटोटाइप बना रहे हों या NuGet के जरिए पैकेज्ड capabilities शिप कर रहे हों, सभी पैटर्न `AgentSkillsProviderBuilder` के माध्यम से कंपोज़ होते हैं।

[मूल घोषणा](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) और [GitHub samples](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills) देखें।
