---
title: "Kodlama Aracıları için Misyon Kontrol: VS Code'da Birleşik Bir Deneyim"
description: "VS Code, yerel, bulut, CLI ve üçüncü taraf kodlama aracılarını Agent Sessions'a getirerek geliştiricilerin otonom çalışmayı izlemelerine, kesintiye uğratmalarına ve koordine etmelerine olanak tanır."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> **Not:** Bu sayfa {{< ref "index.md" >}} sayfasının otomatik tercümesidir.

# Kodlama Aracıları için Misyon Kontrol: VS Code'da Birleşik Bir Deneyim

Tek bir kodlama asistanı anlamak kolaydır. Farklı yerlerde çalışan birden fazla ajan anlamak değildir.

Bir ajan VS Code'da yerel olarak çalışır. Başka bir ajan bulut ortamında bir GitHub konusu üzerinde çalışır. Bir CLI ajanı terminalde yaşar. Üçüncü taraf bir kodlama ajanı farklı bir oturum modeline ve farklı sınırlara sahip olabilir. Paylaşılan bir görünüm olmadan, geliştiriciler işi denetlemekten daha fazla zaman harcayarak çalışmayı izlemeye harcıyor.

VS Code'un birleşik ajan deneyimi, Agent Sessions ile bu koordinasyon sorununu çözer: ajanları başlatmak, durumlarını görmek, konuşmalarını açmak ve plan değiştiğinde müdahale etmek için bir yer.

Bu, başka bir ajan eklemekten daha çok, birden fazla ajanı yönetilebilir hale getirme hakkındadır.

## Farklı İş Türleri için Bir Görünüm

Kaynak makale dört farklı katılımcıyı açıklar: yerel GitHub Copilot, buluttaki Copilot Kodlama Ajanı, GitHub Copilot CLI ve uygun Copilot abone kullanıcıları için OpenAI Codex.

Farklı güçlü yönleri vardır:

- Yerel bir ajan mevcut çalışma alanını inceleyebilir ve hızlı değişiklikler yapabilir.
- Bir bulut kodlama ajanı bir konuda asynchron olarak çalışabilir ve bir pull request açabilir.
- Bir CLI ajanı, terminalin ağır kullanıldığı iş akışlarına ve operasyonel komutlara uyar.
- Başka bir sağlayıcı farklı bir model veya akıl yürütme stili sunabilir.

Agent Sessions bu görevlere ortak bir ev verir. Neyin çalıştığını, ne yaptığını ve konuşmayı nerede devam ettirebileceğinizi görebilirsiniz.

Bu görünürlük önemlidir çünkü otonom çalışma koordinasyon gerektirmeyi ortadan kaldırmaz. Koordinasyonu birinci sınıf bir mühendislik görevi haline getirir.

## Kesintiler İş Akışının Bir Parçasıdır

Kaynak basit bir gözlem yapar: "Bir istem gönder ve önemli bir şeyi unuttuğunuzu fark etmek yaygındır." Daha önce seçim genellikle bekleme veya iptal etmek idi. Chat editörleriyle, etkin bir oturumu açabilir ve ajan çalışırken bilgi ekleyebilirsiniz.

Bu gerçek işbirliğine daha yakındır. Gereksinimler değişir. Bir test bir varsayımı ortaya çıkarır. Bir gözden geçiren bir API'nin geriye dönük uyumlu kalması gerektiğini fark eder. Yararlı olan ajan, asla düzeltme gerektirmeyen değildir; tüm görevi kaybetmeden düzeltmeyi içerebilen olandır.

.NET çalışması için, bir kesinti basit olabilir:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

Talimat kısadır çünkü depo zaten daha büyük bağlamı taşır. Oturum, yönü düzeltmek için yerdir, tüm sistemi yeniden belirtmek için değildir.

## Özel Ajanlar Takım Alışkanlıklarını Rollere Dönüştürür

VS Code ayrıca Plan gibi özel ajanlar tanıtır. Hemen uygulamak yerine, bir planlama ajanı uygulama spesifikasyonu üretmeden önce kapsam, bileşenler, kütüphaneler ve kısıtlamalar hakkında sorular sorar.

Bu desen yerleşik bir ajandan ötesinde kullanışlıdır. Bir takım odaklanmış rolleri tanımlayabilir:

- **Araştırma** kanıt toplar ve kısa bir karar kaydı yazar.
- **İnceleme** bir değişikliği depo kurallarına karşı kontrol eder.
- **Test** eksik durumları tanımlar ve bir test planı önerir.
- **Mimari** dosyaları değiştirmeden seçenekleri karşılaştırır.

Küçük özel bir ajan tanımı şöyle görünebilir:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

Yararlı olan kısım YAML değildir. Sorumlulukların açık ayrımıdır. Bir planlama ajanı sessizce üretim kodunu düzenlememelidir. Bir inceleme ajanı değerlendirdiği tasarımı yeniden yazmamalıdır.

## Alt Ajanlar Bağlam Çarpışmalarını Azaltır

Uzun konuşmalar ilişkisiz bağlamı biriktirir. Alt ajanlar sınırlanmış bir araştırma görevi için izole bir çalışma alanı sağlar, ardından sonucu ana oturuma döndürür.

Bu, şu sorular için iyi bir uyumudur:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

Ana ajan uygulama üzerine odaklanmış kalırken araştırma ajanı daha dar bir soruyu işler. Aynı ilke takımlar için de geçerlidir: açık delegasyon, overlapping otoritesiyle birden fazla ajan başlatmaktan daha iyi sonuçlar üretir.

## Uyarı: Daha Fazla Ajan Daha Fazla Koordinasyon Anlamına Gelir

Agent Sessions aktiviteyi gösterebilir, ancak çelişkili mülkiyeti çözemez. Aynı alanı düzenleyen iki ajan yine bir merge sorunu oluşturabilir. Bir bulut ajanı ve yerel bir ajan uyumsuz varsayımlar yapabilir. Özel bir ajan başka bir ajanın görmezden geldiği bir tavsiye üretebilir.

Sınırlar belirleyin:

1. Belirli bir dal için bir ajan uygulamaya sahiptir.
2. Araştırma ajanları yapıları döndürür, takip edilmeyen düzenlemeleri değil.
3. Pull istekleri inceleme sınırı kalır.
4. Ajan adları ve istemi ne değiştirebileceklerini belirtir.
5. Oturum çıktısı önemli bir kararı açıkladığında saklanır.

## Benim Görüşüm

Çoklu ajan geleceği sohbet pencereleri sırası değildir. Bu, rolleri, teslim alma noktaları ve hesap verebilirliği olan küçük bir takımdır.

Agent Sessions değerlidir çünkü bu gerçeği kabul eder. Geliştiricilere editör, terminal ve bulut arasında zaten olan işler için bir kontrol yüzeyi verir. Bir sonraki verimlilik kazancı daha fazla ajanın olmasından daha az ve sınırlarını okunaklı hale getirmekten gelecektir.

Bir .NET takımı için, bir planlama ajanı ve bir uygulama ajanıyla başlardım. Planlama çıktısını sorun veya pull isteği spesifikasyonu olarak kullan, ardından uygulama ajanının bu sınır içinde çalışmasına izin ver. Daha fazla rol eklemeden önce yeniden çalışmayı ölç.

En iyi misyon kontrol, yine de sahipliği açık hale getiren olandır.
