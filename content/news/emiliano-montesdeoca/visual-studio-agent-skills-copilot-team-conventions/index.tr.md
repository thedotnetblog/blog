---
title: "Visual Studio'da Agent Skills: Copilot'a Ekibinizin Gerçekte Nasıl Çalıştığını Öğretin"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio artık Agent Skills'i destekliyor — Copilot'a ekibinizin özel iş akışlarını, kodlama standartlarını ve kuralları öğreten yeniden kullanılabilir talimat setleri. Bir kez tanımlayın, otomatik olarak uygulayın."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

AI kodlama asistanlarıyla ilgili kalıcı bir hayal kırıklığı: Genel programlamayı iyi biliyorlar ama *ekibinizin* özel kurallarını, dahili API'lerinizi veya tercih ettiğiniz kalıpları bilmiyorlar. Her oturumda bağlamı yeniden açıklıyorsunuz. Visual Studio'daki Agent Skills bunu çözmek için tasarlanmıştır.

## Agent Skills Nedir

`SKILL.md` dosyalarında tanımlanan yeniden kullanılabilir talimat setleri — Copilot ajanlarına belirli görevleri nasıl ele alacaklarını öğretir. "Build pipeline'ımızı nasıl çalıştırırız", "Servis katmanımız için nasıl boilerplate üretiriz" veya "Kod inceleme kontrol listemiz" için bir skill tanımlayın. Ajan, skill'i ilgili olduğunda otomatik olarak uygular.

Bu yeni bir kavram değil (`.github/copilot-instructions.md` bir süredir var), ancak Visual Studio entegrasyonu onları bir keşif UI'ı ile birinci sınıf nesneler haline getiriyor.

## Visual Studio'da Skills Oluşturma

Entegre UI akışı: Copilot Chat'te araçlar simgesine tıklayın, skills panelini açın, `+`'ya tıklayın. Küresel (kişisel) veya çözüm düzeyi kapsamı seçiyor, bir isim seçiyor ve Visual Studio bir şablon oluşturuyor. Copilot Ajan modu daha sonra şablonu doldurmaya yardımcı olabilir — ajan için skill'i yazmak için ajanı kullanın.

Şu anda Insiders kanalında, yakında Release'de.

Skills'i manuel olarak da oluşturabilirsiniz:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Keşif Konumları

Skills standart yollardan otomatik olarak keşfedilir:

**Çözüm düzeyinde (repo aracılığıyla paylaşılan):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Küresel/kişisel (kullanıcı profiliniz, her yerde kullanılabilir):** `~/.copilot/skills/`, `~/.agents/skills/`

Çok konumlu destek, aynı kuralın GitHub Copilot, Claude Code ve diğer ajan çerçeveleriyle çalıştığı anlamına gelir — skills'lerinizi bir kez tanımlayın, her yerde kullanın.

## Format

Skills, [agentskills.io/specification](https://agentskills.io/specification) formatını izler — hem insan tarafından okunabilir hem de makine tarafından ayrıştırılabilir Markdown tabanlı bir özellik. `SKILL.md`'nin yanına betikler, şablonlar ve örnekler ekleyebilirsiniz.

## Pratik Değer

Gerçek güç bireysel özelliklerde değil — ekip paylaşımlı skills (`.github/skills/` aracılığıyla) ve kişisel skills (`~/.agents/skills/` aracılığıyla) kombinasyonunda. Ekip skills'leri, organizasyonunuzun işleri nasıl yaptığını kodlar. Kişisel skills'ler, sizin özellikle nasıl çalıştığınızı kodlar. Ajan her iki bağlamı da otomatik olarak alır.

Copilot'u zaten yoğun kullanan organizasyonlar için bu, aracın genel tavsiyeler vermek yerine kod tabanınızın özel kurallarının gerçekten farkında olmasını sağlama yolunda anlamlı bir adım.

Orijinal gönderi: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
