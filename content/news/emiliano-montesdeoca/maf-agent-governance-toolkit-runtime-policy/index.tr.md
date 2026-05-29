---
title: "Ajan Oluşturmak Kolay Kısım — Onları Güvenle Çalıştırmak Zor Kısım"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework ve Agent Governance Toolkit, çalışma zamanı politikalarını uygulamak, araç çağrılarını yönetmek ve Merkle zincirli denetim günlükleri sağlamak için bir araya geliyor — ajan istemlerini değiştirmeden."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

AI ajan geliştirmede "demo pişmanlığı" diye adlandırmaya başladığım bir desen var. Ajan demo'larda harika çalışıyor. Ardından biri soruyor: yanlış aracı çağırırsa ne olur? Erişmemesi gereken verilere erişirse? Kim denetledi bunu?

Microsoft Agent Framework sizi oluşturma ve düzenleme konusunda destekler. Agent Governance Toolkit (AGT) sonrasını kapsar — yönetim, politika uygulaması ve çalışma zamanında denetlenebilirlik.

## Her Projenin Gerçekte Ne Yaptığı

**Microsoft Agent Framework (MAF)** size programlama modelini sunar: çok ajanlı iş akışları, A2A protokol birlikte çalışabilirliği, ara yazılım kancaları, bellek ve Foundry Agent Service aracılığıyla yönetilen barındırma. Model giriş/çıkış düzeyinde içerik güvenliğini yönetir.

**Agent Governance Toolkit (AGT)** aynı ara yazılım pipeline'ına bağlanarak *eylemleri* yönetir. Her araç çağrısı, kaynak erişimi ve ajanlar arası mesaj, yürütmeden önce politikaya göre değerlendirilir. Milisaniye altı ek yük. Sidecar yok, proxy yok, değiştirilmiş istem yok.

```
Ajan Eylemi --> Politika Kontrolü --> İzin Ver / Reddet --> Denetim Günlüğü    (< 0.1 ms)
```

Farklı katmanlar, tam kapsam, tek pipeline.

## Bağlanmak Sadece Ara Yazılım Eklemek

Python'da AGT, loglama veya içerik filtreleri için kullandığınız aynı `middleware` parametresine eklenir:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

.NET'te `.Use()` aracılığıyla aynı desen:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Aynı ajan, aynı düzenleme, aynı araçlar. AGT, ajan mantığına dokunmadan yönetim yetenekleri ekler.

## Ne Elde Edersiniz

- **GovernancePolicyMiddleware** — her eylemi bildirimsel politika kurallarına göre değerlendirir
- **CapabilityGuardMiddleware** — bir ajanın çağırmasına izin verilen araçların izin listesi (yukarıdaki `approve_small_loan` aracı izin listesinde bilinçli olarak yok)
- **RogueDetectionMiddleware** — çalışma zamanında anormal davranış kalıplarını tespit eder
- **AuditTrailMiddleware** — her eylemin kriptografik olarak kurcalamaya karşı korumalı olması için Merkle zincirli denetim günlüğü

Sonuncusu uyumluluk için önemlidir. Merkle zinciri, birisi günlüğü değiştirirse zincirin kırılacağı anlamına gelir. Denetim kanıttır.

## Beş Sektör Senaryosu

AGT deposu beş tam uçtan uca senaryo içerir: finansal hizmetler (kredi memuru), sağlık hizmetleri (hasta verileri), hukuki (sözleşme incelemesi), hükümet (vatandaş hizmetleri) ve üretim (kalite kontrol). Her biri gerçek MAF ajanlarını gerçek AGT yönetim ara yazılımıyla eşleştirir.

Bunlar oyuncak demo'lar değil. Gerçekte üretimde yönetime ihtiyaç duyacağınız senaryolar bunlar.

## Sonuç

Gerçek verilere dokunan, sonuçları olan kararlar alan veya üretimde gözetimsiz çalışan ajanlar oluşturuyorsanız — yönetim isteğe bağlı değildir. MAF + AGT kombinasyonu size tam yığını sağlar: Agent Framework ile oluşturun, AGT ile yönetin.

Her iki proje de açık kaynaklıdır. Orijinal makale tam kod örneklerine bağlantılar içerir.

Orijinal gönderi: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
