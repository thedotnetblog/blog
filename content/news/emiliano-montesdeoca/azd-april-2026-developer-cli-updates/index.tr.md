---
title: "Azure Developer CLI (azd) Nisan 2026 Güncellemeleri"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd, Nisan 2026'da beş sürüm çıkardı; öne çıkan özellik Python, JavaScript, TypeScript ve .NET için çok dilli kanca desteği — ayrıca azd update genel önizlemesi, yapay zeka kotası ön kontrolleri ve daha fazlası."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd), Nisan 2026'da beş sürüm çıkardı](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14'ten 1.24.2'ye kadar); büyük tema, artık yalnızca Bash ve PowerShell'de değil Python, JavaScript, TypeScript ve .NET'te de çalışan kanculardır.

## azure.yaml'da çok dilli kancalar

Kancalar artık shell betiklerinin yanı sıra `.py`, `.js`, `.ts` veya `.cs` dosyalarına işaret edebilir. Her dil otomatik bağımlılık çözümlemesi alır:

- **Python** — `requirements.txt` veya `pyproject.toml` dosyasını tespit eder, bir virtualenv oluşturur ve çalıştırmadan önce bağımlılıkları yükler. Ortam adını `virtualEnvName` ile yapılandırın.
- **JavaScript / TypeScript** — `package.json` dosyasını tespit eder ve otomatik olarak `npm install` çalıştırır. TypeScript, derleme adımı gerektirmeden `npx tsx` aracılığıyla çalıştırılır. Paket yöneticisini `packageManager` yapılandırma bloğuyla seçin.
- **.NET** — `.cs` dosyalarını `dotnet run` ile çalıştırır. Tek dosya betikleri .NET 10+'da desteklenir. Hedef çerçeveyi `configuration/framework` bloğu aracılığıyla yapılandırın.

Bu, bu dillerden birinde zaten çalışan ekiplerin yalnızca sağlama yaşam döngüsü olaylarını bağlamak için ayrı bir Bash veya PowerShell kancası tutmasına gerek olmadığı anlamına gelir.

## azd update genel önizlemeye geçiyor

`azd update` artık tüm platformlarda genel önizlemede. Tek bir komut, azd'nin başlangıçta nasıl yüklendiğinden bağımsız olarak güncellemeyi yönetir — Homebrew, WinGet veya MSI yollarını ayrı ayrı takip etmeye gerek yok.

## AZD_NON_INTERACTIVE ile etkileşimsiz mod

`AZD_NON_INTERACTIVE=true` ayarı (veya `--non-interactive` / `--no-prompt` kullanımı) artık gerekli bir girdi otomatik olarak çözümlenemediğinde CI/CD hatlarında tutarlı, belirleyici hatalar üretir. Daha önce davranış komutlar arasında tutarsızdı.

## Yapay zeka modeli kotası ön kontrolü

`azd provision`, yapay zeka modeli kaynaklarını sağlamaya çalışmadan önce Azure Cognitive Services kotasını doğrular. Kota sınırları nedeniyle başarısız olacak dağıtımlar artık sağlamanın ortasında değil, sürecin başında hatayı gösterir.

## Copilot sorun gidermedeki "Bu hatayı düzelt"

azd'deki Copilot sorun giderme entegrasyonu, yalnızca açıklamak yerine önerilen bir düzeltmeyi doğrudan uygulama özelliği kazanır. Ajan düzeltilebilir bir sorun tespit ettiğinde, değişikliği yerinde yapabilir.

## Özel sağlama sağlayıcıları ve Key Vault gizli dizi çözücü

Uzantı yazarları artık `WithProvisioningProvider()` ile alternatif altyapı arka uçlarını kaydedebilir. Ayrıca azd, yapılandırmayı uzantılara geçirmeden önce `@Microsoft.KeyVault(...)` referanslarını otomatik olarak çözer; bu da özel sağlayıcılarda manuel gizli dizi çözümlemeye gerek kalmadığı anlamına gelir.

## Şablon ve izleme modu hariç tutmaları

İki yeni yoksayma dosyası, dosya işleme üzerinde daha hassas kontrol sağlar:
- **`.azdignore`** — Son kullanıcıların temiz bir proje iskeleti elde etmesi için yalnızca katkıda bulunanlar için olan dosyaları (belgeler, CI yapılandırmaları) şablon kopyalarından dışlar.
- **`.azdxignore`** — `azd x watch` sırasında yeniden derleme tetikleyicilerinden dizinleri dışlar; yinelemeli geliştirme sırasında gürültüyü azaltır.

## Ayrılmış ad ön kontrolü ve docker.network seçeneği

azd artık sağlama başlamadan önce tahmin edilen kaynak adlarının Azure ayrılmış sözcüklerini (`MICROSOFT`, `WINDOWS` veya `LOGIN` öneki) içereceği durumlarda uyarı verir. Yeni bir `docker.network` seçeneği, `docker build`'e `--network` iletir; bu da belirli bir Docker ağı gerektiren kurumsal proxy ortamlarında faydalıdır.

## Güvenlik düzeltmeleri

Windows MSI paketi artık kod imzalama doğrulaması içeriyor. Ayrı bir düzeltme, uzantı komutu sınırları arasında değerleri açığa çıkarabilecek bir ortam değişkeni sızıntısını kapatır.

---

Yoğun bir ay — çok dilli kanca desteği özellikle Bash'te öncelikli çalışmayan ekipler için gerçek bir sürtünme noktasını ortadan kaldırır. Beş sürümün tamamına ait değişiklik günlüğü için [tam sürüm notlarına](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) bakın.
