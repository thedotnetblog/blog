---
title: "Handoff Deseni: Tek Bir Ajan Yetmediğinde"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework'ün Handoff orkestrasyonu deseni, ajanların konuşma bağlamını kaybetmeden veya topoloji kurallarını çiğnemeden bir sonraki turu kimin yöneteceğine karar vermesini sağlar."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

Bir noktada, her çok ajanlı sistem basit bir yönlendiricinin ötesine geçer. İlk işaret genellikle bir uzman ajanın takip sorusu sorması gerektiğinde veya bir turun ortasında başka bir ajanın devam etmesi gerektiğini fark ettiğinde gelir. Sabit pipeline orada başarısız olur. Tek geçişli yönlendirici orada başarısız olur.

Microsoft Agent Framework'teki Handoff orkestrasyonu deseni tam olarak bu sorunu çözmek için tasarlanmıştır.

## Handoff Nasıl Çalışır

Geliştirici bir grafik bildirir: bunlar ajanlar, bunlar aralarındaki kenarlar. Framework gerisini halleder — her giden kenar için bir handoff aracı sentezler ve her ajana enjekte eder. Bir ajan kontrolü devretmeye karar verdiğinde, aracı çağırır. Framework topolojiyi uygular.

Bu onu ajanların birbirini çağırmasından farklı kılan üç şey:

1. **Paylaşılan bir transkript** — alıcı ajan tam konuşma geçmişini görür. Sıfırdan başlamadan.
2. **Topoloji zorlaması** — bir ajan yalnızca bildirilen hedeflere handoff yapabilir. Yönlendirme hataları üretimde değil, geliştirme aşamasında yakalanır.
3. **Doğal sonlanma** — aktif ajan bir handoff aracı çağırmadan turunu bitirdiğinde, iş akışı kullanıcıya bırakır. Yoklama yok, açık çıkış koşulu yok.

## Minimal Bir Örnek

.NET'te bir handoff iş akışı oluşturmak şöyle görünür:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage her iki uzmana da gönderebilir. Her iki uzman da triage'a geri gönderebilir. Grafik döngüsüz uyumludur ancak gerektiğinde ("daha fazla bilgiye ihtiyacım var" → araştırmaya geri) geri kenarları destekler.

## Handoff'u Ne Zaman Kullanmalı (ve Ne Zaman Kullanmamalı)

Handoff şu durumlarda iyi bir seçimdir:

- **Sahiplik konuşmanın ortasında değişebilir** — bir ajan yanlış uzman olduğunu fark edebilir
- **Geri kenarlar önemlidir** — yeniden başlatmadan önceki bir adıma dönmeniz gerekebilir
- **Yönlendirme kararları nüanslıdır** — handoff kararı bağlamsal ve tiplenmiş tahminlerden ziyade model tarafından daha iyi alınır

Şu durumlarda *doğru* seçim değildir:

- Pipeline'ınız sabit ve sıralı — bunun için `Sequential` iş akışını kullanın
- Her adım bağımsız — yalnızca birinin ihtiyaç duyduğu bir transkripti paylaşan ajanlar sadece gürültüdür
- Katı işleme garantilerine ihtiyacınız var — model odaklı yönlendirmenin belirsizliği istediğiniz şey değildir

## Geri Kenarlar ve Human-in-the-Loop

Handoff'un mümkün kıldığı en ilginç formlardan biri gerçek geri kenarlardır. Bir ajan "yeterli bilgim yok" kararını verebilir ve sabit kodlu bir döngüyle değil, modelin doğru karar olduğuna karar verdiği için bir araştırma adımına yeniden yönlendirebilir.

Human-in-the-loop etkileşimleri de doğal olarak oluşur. Bir uzman kullanıcı girdisine ihtiyaç duyduğunda, iş akışı varsayılan tur döngüsü aracılığıyla kullanıcıya bırakır, yanıtı toplar ve tam bağlamla devam eder. Ajan konuşmayı hiç kaybetmedi.

## Sonuç

Handoff, içselleştirildikten sonra çok şeyi mümkün kılan basit görünen desenlerden biridir: merkezsizleştirilmiş yönlendirme, paylaşılan bağlam, zorlanan topoloji, doğal sonlanma. Ajanlarınız "aslında bunu başkasının halletmesi gerekiyor" demeye başladığında doğru sonraki adımdır.

Orijinal gönderide tam rehberi okuyun: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
