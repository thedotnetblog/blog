---
title: "VS Code 1.115 — Arka Plan Terminal Bildirimleri, SSH Agent Modu ve Daha Fazlası"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115, agentlar için arka plan terminal bildirimleri, SSH uzak agent barındırma, terminale dosya yapıştırma ve oturum bazlı düzenleme takibi getiriyor. .NET geliştiricileri için önemli olan şeyler burada."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "vscode-1-115-agent-improvements" >}}).*

VS Code 1.115 az önce [yayınlandı](https://code.visualstudio.com/updates/v1_115) ve başlık özellikleri açısından hafif bir sürüm olsa da, AI kodlama asistanlarıyla her gün çalışıyorsanız agent ile ilgili iyileştirmeler gerçekten kullanışlı.

Gerçekten bilinmeye değer olanları öne çıkarayım.

## Arka plan terminalleri agentlara geri bildirim veriyor

Bu, öne çıkan özellik. Arka plan terminalleri artık komutlar tamamlandığında çıkış kodu ve terminal çıktısını da içerecek şekilde otomatik olarak agentları bilgilendiriyor. Arka plan terminallerindeki giriş istemleri de tespit edilerek kullanıcıya iletiliyor.

Bu neden önemli? Copilot'un agent modunu arka planda build komutları veya test dizileri çalıştırmak için kullandıysanız, "o bitti mi acaba?" sancısını bilirsiniz — arka plan terminalleri esasen ateş et ve unut mantığıyla çalışıyordu. Artık agent, `dotnet build` veya `dotnet test` tamamlandığında haberdar ediliyor, çıktıyı görüyor ve buna göre tepki verebiliyor. Küçük bir değişiklik, ama agent odaklı iş akışlarını önemli ölçüde daha güvenilir kılıyor.

Ayrıca, agentların kullanıcı onayıyla arka plan terminallerine komut göndermesine olanak tanıyan yeni bir `send_to_terminal` aracı var; bu da `run_in_terminal`'in zaman aşımıyla terminalleri arka plana taşıdığı ve salt okunur hale getirdiği sorunu çözüyor.

## SSH uzak agent barındırma

VS Code artık SSH üzerinden uzak makinelere bağlanmayı, CLI'yi otomatik olarak yüklemeyi ve agent ana bilgisayar modunda başlatmayı destekliyor. Bu, AI agent oturumlarınızın uzak ortamları doğrudan hedefleyebileceği anlamına geliyor — Linux sunucularda veya bulut VM'lerinde geliştirme ve test yapan .NET geliştiricileri için kullanışlı.

## Agent oturumlarında düzenleme takibi

Agent oturumları sırasında yapılan dosya düzenlemeleri artık farklar, geri alma/yeniden yapma ve durum geri yükleme ile birlikte takip ediliyor ve geri yükleniyor. Bir agent kodunuzda değişiklik yapar ve bir şeyler ters giderse, tam olarak neyin değiştiğini görebilir ve geri alabilirsiniz. Agentların kod tabanınızı değiştirmesine izin vermek için gönül rahatlığı.

## Tarayıcı sekme farkındalığı ve diğer iyileştirmeler

Birkaç yaşam kalitesi iyileştirmesi daha:

- **Tarayıcı sekme takibi** — sohbet artık bir oturum sırasında açılan tarayıcı sekmelerini takip edip bunlara bağlantı verebiliyor, böylece agentlar baktığınız web sayfalarına referans verebiliyor
- **Terminale dosya yapıştırma** — Ctrl+V, sürükle-bırak veya sağ tıklamayla terminale dosya (resimler dahil) yapıştırın
- **Minimap'te test kapsamı** — test kapsamı göstergeleri artık hızlı bir görsel özet için minimap'te gösteriliyor
- **Mac'te sıkıştırarak yakınlaştırma** — entegre tarayıcı sıkıştırarak yakınlaştırma hareketlerini destekliyor
- **Sessions'da Copilot yetkilendirmeleri** — durum çubuğu Sessions görünümünde kullanım bilgilerini gösteriyor
- **Go to File'da favicon** — açık web sayfaları hızlı seçim listesinde favicon gösteriyor

## Sonuç

VS Code 1.115 artımlı bir sürüm, ancak agent iyileştirmeleri — arka plan terminal bildirimleri, SSH agent barındırma ve düzenleme takibi — AI destekli geliştirme için fark edilir şekilde daha akıcı bir deneyim oluşturuyor. .NET projeleri için Copilot'un agent modunu kullanıyorsanız, bunlar günlük sürtünmeyi azaltan yaşam kalitesi düzeltmeleri.

Her ayrıntı için [tam sürüm notlarına](https://code.visualstudio.com/updates/v1_115) bakın.
