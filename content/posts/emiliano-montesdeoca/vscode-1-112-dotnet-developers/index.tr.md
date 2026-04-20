---
title: ".NET Geliştiricilerinin VS Code 1.112'de Gerçekten Önemsemesi Gerekenler"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 yayınlandı ve agent yükseltmeleri, entegre bir tarayıcı hata ayıklayıcı, MCP korumalı alan ve monorepo desteğiyle dolu. .NET ile geliştirme yapıyorsanız gerçekten önemli olan şeyler burada."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "vscode-1-112-dotnet-developers" >}}).*

VS Code 1.112 yayınlandı ve dürüstçe söylemek gerekirse? .NET dünyasında gününüzü geçiriyorsanız bu sürüm farklı bir his veriyor. [Resmi sürüm notlarında](https://code.visualstudio.com/updates/v1_112) pek çok şey var, ama sizi biraz kaydırmadan kurtarayım ve gerçekten bizim için önemli olanlara odaklanayım.

## Copilot CLI çok daha kullanışlı hale geldi

Bu sürümün büyük teması **agent özerkliği** — Copilot'a her adımı siz denetlemeden işini yapması için daha fazla alan tanıma.

### Mesaj yönlendirme ve sıralama

Copilot CLI bir görevin ortasındayken bir şeyi söylemeyi unuttuğunuzu fark ettiğiniz o anı bilirsiniz. Önce beklemeniz gerekiyordu. Artık bir istek hâlâ çalışırken mesaj gönderebilirsiniz — ya mevcut yanıtı yönlendirmek ya da takip talimatlarını sıraya almak için.

Bu, Copilot'un bir proje kurduğunu izlerken "ah, buna MassTransit de eklemeliyim" dediğiniz uzun `dotnet` iskele görevleri için çok önemli.

### İzin seviyeleri

En çok heyecanlandığım bu. Copilot CLI oturumları artık üç izin seviyesini destekliyor:

- **Default Permissions** — araçların çalışmadan önce onay istediği olağan akış
- **Bypass Approvals** — her şeyi otomatik onaylar ve hatalarda yeniden dener
- **Autopilot** — tamamen özerk: araçları onaylar, kendi sorularını yanıtlar ve görev tamamlanana kadar devam eder

Entity Framework ile migrasyonlar, Docker kurulumu ve yeni bir ASP.NET Core API'si oluşturuyorsanız — Autopilot modu demek istediğinizi tanımlayıp kahve almaya gidebilirsiniz demek. Gerisini halledecek.

Autopilot'u `chat.autopilot.enabled` ayarıyla etkinleştirebilirsiniz.

### Devretmeden önce değişiklikleri önizleyin

Copilot CLI'a bir görev devrettiğinizde bir worktree oluşturur. Daha önce, teslim edilmemiş değişiklikleriniz varsa nelerin etkileneceğini görmek için Source Control'ü kontrol etmeniz gerekiyordu. Artık Chat görünümü, kopyalamak, taşımak veya yoksaymak isteyip istemediğinize karar vermeden önce bekleyen değişiklikleri doğrudan orada gösteriyor.

Küçük bir şey, ama "dur, ne hazırlamıştım?" anından kurtarıyor.

## VS Code'dan çıkmadan web uygulamalarını hata ayıklayın

Entegre tarayıcı artık **tam hata ayıklamayı** destekliyor. Kesme noktaları koyabilir, kod üzerinde adım adım ilerleyebilir ve değişkenleri inceleyebilirsiniz — hepsi VS Code içinde. Artık Edge DevTools'a geçiş yok.

Yeni bir `editor-browser` hata ayıklama türü var ve mevcut `msedge` veya `chrome` başlatma yapılandırmalarınız varsa, geçiş `launch.json`'daki `type` alanını değiştirmek kadar basit:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Blazor geliştiricileri için bu oyun değiştirici. Terminalde zaten `dotnet watch` çalıştırıyorsunuz — artık hata ayıklamanız da aynı pencerede kalıyor.

Tarayıcı aynı zamanda bağımsız yakınlaştırma seviyeleri (sonunda!), düzgün sağ tıklama bağlam menüleri aldı ve yakınlaştırma web sitesi başına hatırlanıyor.

## MCP sunucu korumalı alanı

Bu, düşündüğünüzden daha önemli. MCP sunucuları kullanıyorsanız — belki Azure kaynaklarınız veya veritabanı sorguları için özel bir tane kurduysanız — bunlar VS Code sürecinizle aynı izinlerle çalışıyordu. Yani dosya sisteminize, ağınıza, her şeye tam erişim.

Artık onları korumalı alana alabilirsiniz. `mcp.json` dosyanızda:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Korumalı alandaki bir sunucu sahip olmadığı bir şeye erişim gerektirdiğinde, VS Code izin vermeniz için sizi uyarıyor. "Kimse garip bir şey yapmasın" yaklaşımından çok daha iyi.

> **Not:** Korumalı alan şimdilik macOS ve Linux'ta kullanılabilir. Windows desteği geliyor — WSL gibi uzak senaryolar çalışıyor.

## Monorepo özelleştirme keşfi

Bir monorepo'da çalışıyorsanız (ve dürüstçe söylemek gerekirse, pek çok kurumsal .NET çözümü buna dönüşüyor), bu gerçek bir sorun noktasını çözüyor.

Daha önce, reponuzun bir alt klasörünü açtığınızda VS Code, depo kökünüzdeki `copilot-instructions.md`, `AGENTS.md` veya özel becerileri bulamıyordu. Artık `chat.useCustomizationsInParentRepositories` ayarıyla `.git` köküne kadar yukarı çıkıp her şeyi buluyor.

Bu, ekibinizin tüm monorepo projelerine herkesin kök klasörü açmasına gerek kalmadan agent talimatlarını, prompt dosyalarını ve özel araçları paylaşabilmesi anlamına geliyor.

## Agent hata ayıklama için /troubleshoot

Özel talimatlar veya beceriler ayarlayıp neden alınmadığını hiç merak ettiniz mi? Yeni `/troubleshoot` becerisi agent hata ayıklama günlüklerini okuyup ne olduğunu söylüyor — hangi araçların kullanıldığı veya atlandığı, neden talimatların yüklenmediği ve yavaş yanıtlara neyin yol açtığı.

Bunu şununla etkinleştirin:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Ardından sohbette `/troubleshoot neden özel beceri yüklenmiyor?` yazın.

Bu hata ayıklama günlüklerini artık dışa ve içe aktarabilirsiniz; bir şey beklendiği gibi çalışmadığında ekibinizle paylaşmak için harika.

## Resim ve ikili dosya desteği

Agentlar artık diskten resim dosyalarını ve ikili dosyaları doğrudan okuyabiliyor. İkili dosyalar hexdump formatında sunuluyor ve resim çıktıları (entegre tarayıcıdan alınan ekran görüntüleri gibi) bir carousel görünümünde gösteriliyor.

.NET geliştiricileri için düşünün: bir UI hatasının ekran görüntüsünü sohbete yapıştırın ve agent neyin yanlış olduğunu anlasın, ya da Blazor bileşeni render çıktısını analiz ettirin.

## Otomatik sembol referansları

Küçük bir yaşam kalitesi iyileştirmesi: bir sembol adını (bir sınıf, metot vb.) kopyalayıp sohbete yapıştırdığınızda VS Code artık otomatik olarak `#sym:İsim` referansına dönüştürüyor. Bu, agent'a manuel olarak eklemek zorunda kalmadan bu sembol hakkında tam bağlam sağlıyor.

Bunun yerine düz metin istiyorsanız `Ctrl+Shift+V` kullanın.

## Eklentiler artık etkinleştirilebilir/devre dışı bırakılabilir

Daha önce bir MCP sunucusunu veya eklentiyi devre dışı bırakmak kaldırmak anlamına geliyordu. Artık hem genel hem de çalışma alanı başına açıp kapatabilirsiniz. Extensions görünümünde veya Customizations görünümünde sağ tıklayın ve işiniz bitti.

npm ve pypi'den eklentiler artık otomatik güncellenebilir; ancak güncellemeler makinenizde yeni kod çalıştırmak anlamına geldiğinden önce onay isteyecekler.

## Sonuç

VS Code 1.112, agent deneyimini açıkça ileriye taşıyor — daha fazla özerklik, daha iyi hata ayıklama, daha sıkı güvenlik. .NET geliştiricileri için entegre tarayıcı hata ayıklama ve Copilot CLI iyileştirmeleri öne çıkan özellikler.

Bir .NET projesi için tam Copilot CLI oturumu Autopilot modunda henüz denemediyseniz bu sürüm başlamak için iyi bir zaman. Sadece izinlerinizi ayarlamayı ve bırakıp gidermeyi unutmayın.

[VS Code 1.112'yi indirin](https://code.visualstudio.com/updates/v1_112) veya **Help > Check for Updates** aracılığıyla VS Code içinden güncelleyin.
