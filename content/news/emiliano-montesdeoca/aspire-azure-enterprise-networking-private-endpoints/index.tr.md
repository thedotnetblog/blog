---
title: "Private Endpoints, VNet'ler, NSG'ler — Aspire Artık Ağı Yönetiyor"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Aspire'ın yeni Azure kurumsal ağ desteği, VNet'leri, özel uç noktaları, NAT ağ geçitlerini, NSG'leri ve Ağ Güvenlik Çevrelerini doğrudan AppHost'ta modellemenizi sağlar — altyapı kayması olmadan."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Bu senaryoyu çok fazla gördüm. Uygulama hazır. Demo harika. Sonra güvenlik kontrol listesi ortaya çıkıyor: depolamayı genel internetten kaldırın, VNet içinde çalıştırın, iş ortağının izin listesi için giden IP'leri sağlayın, yalnızca doğru alt ağların doğru hizmetlerle iletişim kurduğunu kanıtlayın.

Bu noktada uygulama modeli ve altyapı modeli, bakımı acı verici şekillerde ayrışmaya başlıyor.

Aspire'ın yeni Azure kurumsal ağ desteği bunu doğrudan ele alıyor. Ağın şeklini AppHost'ta onu kullanan kaynakların yanında tanımlıyorsunuz.

## Yapı Taşları

Her Azure ağ kavramının ne için olduğu, özetle:

| Özellik | Ne zaman kullanılır | Neden önemli |
|---------|------------|----------------|
| Sanal Ağ | Özel adres alanına ihtiyaç duyduğunuzda | Alt ağlar, özel uç noktalar ve yönlendirme için ağ sınırı |
| Alt Ağ | VNet içinde iş yüklerini ayırmanız gerektiğinde | Sistemin her parçası kendi adres aralığını ve politika yüzeyini alır |
| Devredilmiş Alt Ağ | Bir platform hizmeti (örn. ACA) alt ağı yönetmek zorundayken | Hizmetin VNet'inizde yönetilen altyapıyı güvenli bir şekilde yerleştirmesine olanak tanır |
| NAT Ağ Geçidi | Öngörülebilir giden genel IP'lere ihtiyaç duyduğunuzda | İzin listeleri ve denetim için kararlı adres |
| Özel Uç Nokta | Bir PaaS kaynağına özel olarak erişilmesini istediğinizde | VNet'inizin içine o hizmet için özel IP yerleştirir, genel maruziyeti kaldırır |
| NSG | Alt ağ düzeyinde trafik kurallarına ihtiyaç duyduğunuzda | Alt ağ başına gelen ve giden trafik için açık izin/reddetme |

## AppHost'ta Tanımlamak

Buradaki temel değişim, ağı kullanan kaynaklarla *birlikte* modellemenizdir; zamanla uygulama modelinden uzaklaşan ayrı bir Bicep dosyasında değil.

AppHost'tan şunları yapabilirsiniz:

- `AddVirtualNetwork()` ve `AddSubnet()` ile VNet ve alt ağlar oluşturma
- Kararlı giden IP'ler için alt ağlara NAT ağ geçidi ekleme
- Depolama, Key Vault, SQL ve diğer PaaS hizmetleri için özel uç noktalar oluşturma
- Gelen ve giden güvenlik kurallarıyla NSG'ler tanımlama
- Kaynaklar arası politikalar için Ağ Güvenlik Çevrelerini yapılandırma

Sonuç olarak `azd up` çalıştırdığınızda altyapı, uygulama modelinin ihtiyaç duyduğunu söylediğiyle eşleşir. Elle bakılan şablonun söylediğiyle değil.

## Gerçek Uygulamalar için Neden Önemli

Aspire'da ağ modellendiğinde çok daha kolay hale gelen birkaç şey:

**Key Vault ve depolama için özel uç noktalar** — bu kaynaklarda `WithPrivateEndpoint()` tanımlıyorsunuz ve Aspire DNS bölgesi yapılandırmasını ve uç nokta eklemeyi hallediyor. Uygulama asla değişmiyor.

**Tutarlı giden IP'ler** — ilgili alt ağa NAT ağ geçidi ekleyin ve uygulamanızdan gelen her giden istek bilinen, kararlı bir IP üzerinden geçiyor. İş ortakları bunu izin listesine ekleyebilir. Denetçiler takip edebilir.

**Koddan NSG kuralları** — portala tıklamak veya bir Bicep parçacığını korumak yerine güvenlik kurallarınız AppHost'ta korudukları kaynakların yanında yaşar.

Bu, demoları heyecan verici yapan değil, üretim sistemlerini sürdürülebilir kılan türden bir entegrasyon.

## Sonuç

Proje yaşam döngüsünde geç ortaya çıkan ağ güvenliği, başından itibaren uygulama ile birlikte modellerseniz çözülmüş bir sorundur. Aspire'ın kurumsal ağ desteği, ayrı bir altyapı kanalına ihtiyaç duymadan bunu mümkün kılıyor.

Orijinal gönderideki tüm ayrıntılar: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
