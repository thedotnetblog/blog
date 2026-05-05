---
title: "Azure MCP Araçları Artık Visual Studio 2022'ye Entegre — Uzantı Gerekmiyor"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP araçları, Visual Studio 2022'de Azure geliştirme iş yükünün bir parçası olarak geliyor. 230'dan fazla araç, 45 Azure servisi, yüklenecek sıfır uzantı."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

Azure MCP araçlarını ayrı uzantı üzerinden Visual Studio'da kullandıysanız, süreci biliyorsunuzdur — VSIX'i kurun, yeniden başlatın, bir şeylerin bozulmamasını umun, sürüm uyumsuzluklarıyla uğraşın. O sürtünme artık tarihe karışıyor.

Yun Jung Choi [duyurdu](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/): Azure MCP araçları artık Visual Studio 2022'de Azure geliştirme iş yükünün doğrudan bir parçası olarak geliyor. Uzantı yok. VSIX yok. Yeniden başlatma dansı yok.

## Bu aslında ne anlama geliyor

Visual Studio 2022 sürüm 17.14.30 itibarıyla Azure MCP Server, Azure geliştirme iş yüküyle birlikte geliyor. Bu iş yükünü zaten yüklediyseniz, tek yapmanız gereken GitHub Copilot Chat'te etkinleştirip kullanmaya başlamak.

45 Azure servisi genelinde 230'dan fazla araç — doğrudan sohbet penceresinden erişilebilir. Depolama hesaplarınızı listeleyin, ASP.NET Core uygulaması dağıtın, App Service sorunlarını tanılayın, Log Analytics'i sorgulayın — tek bir tarayıcı sekmesi açmadan.

## Bu neden göründüğünden daha önemli

Geliştirici araçlarındaki şu gerçeği biliyoruz: her ekstra adım sürtünmedir, sürtünme ise benimsemeyi öldürür. MCP'nin ayrı bir uzantı olması; sürüm uyumsuzlukları, kurulum hataları ve güncel tutulması gereken bir şey daha demekti. İş yüküne entegre etmek şu anlama geliyor:

- Visual Studio Installer üzerinden **tek güncelleme yolu**
- Uzantı ile IDE arasında **sürüm kayması yok**
- **Her zaman güncel** — MCP Server, düzenli VS sürümleriyle birlikte güncelleniyor

Azure üzerinde standartlaştıran ekipler için bu büyük bir avantaj. İş yükünü bir kez kuruyorsunuz, araçları etkinleştiriyorsunuz ve her oturumda hazır oluyorlar.

## Bununla neler yapabilirsiniz

Araçlar Copilot Chat üzerinden tüm geliştirme yaşam döngüsünü kapsıyor:

- **Öğrenin** — Azure servisleri, en iyi pratikler, mimari kalıplar hakkında sorular sorun
- **Tasarlayın ve geliştirin** — servis önerileri alın, uygulama kodunu yapılandırın
- **Dağıtın** — kaynakları sağlayın ve doğrudan IDE'den dağıtın
- **Sorun giderin** — günlükleri sorgulayın, kaynak sağlığını kontrol edin, üretim sorunlarını tanılayın

Hızlı bir örnek — Copilot Chat'e şunu yazın:

```
List my storage accounts in my current subscription.
```

Copilot, arka planda Azure MCP araçlarını çağırır, aboneliklerinizi sorgular ve isimler, konumlar ve SKU'larla birlikte biçimlendirilmiş bir liste döndürür. Portal gerekmez.

## Nasıl etkinleştirilir

1. Visual Studio 2022 **17.14.30** veya üzerine güncelleyin
2. **Azure development** iş yükünün yüklendiğinden emin olun
3. GitHub Copilot Chat'i açın
4. **Select tools** düğmesine tıklayın (iki İngiliz anahtarı simgesi)
5. **Azure MCP Server**'ı etkinleştirin

Hepsi bu. Oturumlar arasında etkin kalır.

## Bir not

Araçlar varsayılan olarak devre dışıdır — katılımınız gerekiyor. VS 2026'ya özgü araçlar VS 2022'de mevcut değil. Araç kullanılabilirliği de portaldaki gibi Azure abonelik izinlerinize bağlı.

## Büyük resim

Bu, net bir trendin parçası: MCP, bulut araçlarını geliştirici IDE'lerinde sunmanın standart yolu haline geliyor. [Azure MCP Server 2.0 kararlı sürümünü](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) ve VS Code ile diğer editörlerdeki MCP entegrasyonlarını zaten gördük. Visual Studio'nun iş yükü sistemine entegre olması doğal bir ilerleme.

Visual Studio'da yaşayan .NET geliştiricileri olarak bu, Azure portalına bağlam değiştirmek için bir neden daha ortadan kalkıyor. Ve dürüst olmak gerekirse, ne kadar az sekme değiştirirsek o kadar iyi.
