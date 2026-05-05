---
title: "VS Code 1.117: Agentlar Artık Kendi Git Dallarını Alıyor ve Ben Bunun İçin Buradayım"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117, agent oturumları için worktree izolasyonu, kalıcı Autopilot modu ve alt-agent desteği sunuyor. Ajanlı kodlama iş akışı çok daha gerçek hale geldi."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

"AI asistanı" ile "AI takım üyesi" arasındaki çizgi giderek inceliyor. VS Code 1.117 az önce yayınlandı ve [tam sürüm notları](https://code.visualstudio.com/updates/v1_117) çok şey içeriyor, ancak buradaki hikaye açık: agentlar geliştirme iş akışınızda birinci sınıf vatandaş haline geliyor.

İşte gerçekten önemli olan şeyler.

## Autopilot modu artık tercihinizi hatırlıyor

Daha önce her yeni oturum başlattığınızda Autopilot'u yeniden etkinleştirmeniz gerekiyordu. Can sıkıcıydı. Artık izin modunuz oturumlar arasında korunuyor ve varsayılanı yapılandırabiliyorsunuz.

Agent Host üç oturum yapılandırmasını destekliyor:

- **Default** — araçlar çalışmadan önce onay istiyor
- **Bypass** — her şeyi otomatik onaylıyor
- **Autopilot** — tamamen özerk, kendi sorularını yanıtlıyor ve devam ediyor

Migrasyonlar, Docker ve CI ile yeni bir .NET projesi kuruyorsanız — Autopilot'u bir kez ayarlayın ve unutun. O tercih kalıcı.

## Agent oturumları için worktree ve git izolasyonu

Bu en büyük özellik. Agent oturumları artık tam worktree ve git izolasyonunu destekliyor. Bu, bir agent bir görev üzerinde çalışırken kendi dalını ve çalışma dizinini aldığı anlamına geliyor. Ana dalınız dokunulmadan kalıyor.

Daha da iyisi — Copilot CLI bu worktree oturumları için anlamlı dal adları üretiyor. Artık `agent-session-abc123` yok. Agentin ne yaptığını gerçekten açıklayan bir şey alıyorsunuz.

Birden fazla özellik dalı üzerinde çalışan veya uzun bir iskele görevi çalışırken hata düzelten .NET geliştiricileri için bu oyun değiştirici. Bir worktree'de API controller'larınızı oluşturan bir agent varken siz başka bir worktree'de servis katmanı sorununu ayıklıyor olabilirsiniz. Çakışma yok. Stash yok. Karmaşa yok.

## Alt-agentlar ve agent ekipleri

Agent Host Protocol artık alt-agentları destekliyor. Bir agent, bir görevin parçalarını yönetmek için başka agentlar çalıştırabilir. Görevlendirme gibi düşünün — ana agent koordine eder, uzman agentlar parçaları yönetir.

Bu erken aşamada, ancak .NET iş akışları için potansiyel açık. EF Core migrasyonlarınızı yöneten bir agent varken diğeri entegrasyon testlerinizi kuruyor, bunu hayal edin. Tam olarak oraya henüz ulaşmadık, ancak protokol desteğinin şimdi gelmesi tooling'in hızla takip edeceği anlamına geliyor.

## Agentlar girdi gönderdiğinde terminal çıktısı otomatik dahil ediliyor

Küçük ama anlamlı. Bir agent terminale girdi gönderdiğinde, terminal çıktısı artık otomatik olarak bağlama dahil ediliyor. Daha önce, agent ne olduğunu görmek için ekstra bir tur atmak zorundaydı.

Bir agentin `dotnet build` çalıştırdığını, başarısız olduğunu ve ardından hatayı görmek için başka bir gidiş-dönüş yaptığını izlediyseniz — bu sürtünme gitti. Çıktıyı hemen görüyor ve tepki veriyor.

## macOS'ta Agents uygulaması kendi kendini güncelliyor

macOS'taki bağımsız Agents uygulaması artık kendi kendini güncelliyor. Artık yeni sürümleri manuel olarak indirmeye gerek yok. Güncel kalıyor.

## Bilmeye değer küçük şeyler

- **package.json hover'ları** artık hem yüklü sürümü hem de mevcut en son sürümü gösteriyor. .NET projelerinizin yanında npm tooling yönetiyorsanız kullanışlı.
- **JSDoc** yorumlarındaki **resimler** hover ve tamamlamalarda doğru şekilde render ediliyor.
- **Copilot CLI oturumları** artık VS Code tarafından mı yoksa harici olarak mı oluşturulduklarını gösteriyor — terminaller arasında atlıyorsanız kullanışlı.
- **Copilot CLI, Claude Code ve Gemini CLI** kabuk türleri olarak tanınıyor. Editör ne çalıştırdığınızı biliyor.

## Sonuç

VS Code 1.117 gösterişli bir özellik yığını değil. Altyapı. Worktree izolasyonu, kalıcı izinler, alt-agent protokolleri — bunlar, agentların kodunuza basmadan gerçek, paralel görevleri üstlendiği bir iş akışının yapı taşları.

.NET ile geliştirme yapıyorsanız ve henüz ajanlı iş akışına girmediyseniz, dürüstçe söylemek gerekirse, başlamak için şimdi tam zamanı.
