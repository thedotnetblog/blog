---
title: "KubeCon Avrupa 2026: .NET Geliştiricilerinin Gerçekten Önemsemesi Gerekenler"
date: 2026-03-29
author: "Emiliano Montesdeoca"
description: "Microsoft, KubeCon Avrupa 2026'da bir dizi Kubernetes duyurusu yaptı. İşte filtrelenmiş versiyonu — .NET uygulamaları gönderiyorsanız önemli olan yalnızca AKS ve cloud-native güncellemeleri."
tags:
  - kubernetes
  - aks
  - azure
  - dotnet
  - cloud-native
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "kubecon-2026-aks-updates-dotnet-developers" >}}).*

Büyük bir duyuru yazısı yayımlandığında ve "harika, ama bu benim için ne değiştiriyor ki" diye düşünerek kaydırma yaptığınız o hissi bilirsiniz, değil mi? Ben her KubeCon sezonunda böyle hissediyorum.

Microsoft, [KubeCon Avrupa 2026 tam özetini](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/) yayımladı — bizzat Brendan Burns tarafından yazıldı — ve dürüst olmak gerekirse? Burada gerçek bir içerik var. Yalnızca özellik onay kutuları değil, üretimdeki çalışma biçiminizi değiştiren türden operasyonel iyileştirmeler.

.NET geliştiricileri olarak bizim için gerçekten önemli olanları ele alayım.

## Service Mesh Yükü Olmadan mTLS

Service mesh'ler hakkında şunu söylemek gerekir: herkes güvenlik garantilerini istiyor, kimse operasyonel yükü istemiyor. AKS nihayet bu boşluğu kapatıyor.

[Azure Kubernetes Application Network](https://aka.ms/aks/application-network), ağır sidecar'lı bir mesh dağıtmadan karşılıklı TLS, uygulama farkında yetkilendirme ve trafik telemetrisi sunuyor. [Advanced Container Networking Services'deki Cilium mTLS](https://aka.ms/acns/cilium-mtls) ile birleşince, kimlik yönetimi için X.509 sertifikaları ve SPIRE kullanan şifreli pod-to-pod iletişimi elde ediyorsunuz.

Pratikte ne anlama geliyor: arka plan worker'larıyla konuşan ASP.NET Core API'leriniz, birbirini çağıran gRPC servisleriniz — sıfır uygulama kodu değişikliğiyle ağ düzeyinde şifreli ve kimlik doğrulamalı. Bu büyük bir şey.

`ingress-nginx`'ten geçiş yapan ekipler için tam Kubernetes Gateway API desteğiyle [Application Routing with Meshless Istio](https://aka.ms/aks/app-routing/gateway-api) da mevcut. Sidecar yok. Standart tabanlı. Ve kademeli geçiş için `ingress2gateway` araçlarını gönderdiler.

## Sonradan Düşünülmemiş GPU Gözlemlenebilirliği

.NET servislerinizin yanında AI çıkarımı çalıştırıyorsanız (ve dürüst olalım, kim başlamıyor?), GPU izleme kör noktasına çarpmış olabilirsiniz. Harika CPU/bellek dashboard'larınız olur ve ardından... manuel exporter bağlantıları olmadan GPU'lar için hiçbir şey.

[AKS artık GPU metriklerini](https://aka.ms/aks/managed-gpu-metrics) yönetilen Prometheus ve Grafana'ya yerel olarak sunuyor. Aynı yığın, aynı dashboard'lar, aynı uyarı pipeline'ı. Özel exporter yok, üçüncü taraf ajan yok.

Ağ tarafında, [tek tıklamalı Azure Monitor deneyimiyle](https://learn.microsoft.com/en-us/azure/aks/container-network-observability-logs) HTTP, gRPC ve Kafka trafiği için akış başına görünürlük eklediler. IP'ler, portlar, iş yükleri, akış yönü, politika kararları — hepsi yerleşik dashboard'larda.

Ve beni iki kez baktıran şu oldu: [agentic container networking](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview) kümenizin ağ durumu hakkında doğal dil soruları sorabileceğiniz bir web UI ekliyor. "Pod X neden servis Y'ye ulaşamıyor?" → canlı telemetriden salt okunur tanılamalar. Gece 2'de gerçekten kullanışlı.

## PhD Gerektirmeyen Kümeler Arası Ağ

Multi-cluster Kubernetes, tarihsel olarak "kendi ağ yapıştırıcınızı getirin" deneyimiydi. Azure Kubernetes Fleet Manager artık yönetilen Cilium cluster mesh üzerinden [kümeler arası ağ](https://aka.ms/kubernetes-fleet/networking/cross-cluster) sunuyor:

- AKS kümeleri arasında birleşik bağlantı
- Kümeler arası keşif için global servis kaydı
- Merkezi olarak yönetilen, küme başına tekrarlanmayan konfigürasyon

Dayanıklılık veya uyumluluk için bölgeler arasında .NET mikro servisler çalıştırıyorsanız, bu çok sayıda kırılgan özel yapıştırıcının yerini alıyor. West Europe'daki A Servisi, tutarlı yönlendirme ve güvenlik politikalarıyla mesh üzerinden East US'deki B Servisini keşfedebilir ve çağırabilir.

## Cesaret Gerektirmeyen Yükseltmeler

Dürüst olalım — üretimdeki Kubernetes yükseltmeleri streslidir. "Yükselt ve umut et" pek çok ekip için fiili strateji olmuştur ve kümelerin sürümlerin gerisinde kalmasının ana nedenidir.

İki yeni özellik bunu değiştiriyor:

**Mavi-yeşil agent pool yükseltmeleri** yeni konfigürasyonla paralel bir node pool oluşturur. Davranışı doğrulayın, trafiği kademeli olarak kaydırın ve temiz bir geri alma yolu tutun. Üretim node'larında artık yerinde mutasyon yok.

**Agent pool rollback**, bir yükseltme ters gittiğinde kümeyi yeniden oluşturmadan bir node pool'u önceki Kubernetes sürümüne ve node imajına döndürmenizi sağlar.

Birlikte ele alındığında, bunlar nihayet operatörlere yükseltme yaşam döngüsü üzerinde gerçek kontrol veriyor. .NET ekipleri için bu önemlidir çünkü platform hızı, yeni runtime'ları, güvenlik yamalarını ve ağ özelliklerini ne kadar hızlı benimseyebileceğinizi doğrudan belirler.

## AI İş Yükleri Birinci Sınıf Kubernetes Vatandaşı Oluyor

Upstream açık kaynak çalışması da eşit derecede önemli. Dynamic Resource Allocation (DRA) Kubernetes 1.36'da GA'ya geçti, GPU planlamasını bir geçici çözüm yerine gerçek anlamda birinci sınıf bir özellik haline getirdi.

İzlemeye değer birkaç proje:

| Proje | Ne Yapıyor |
|-------|-----------|
| [AI Runway](https://github.com/kaito-project/kubeairunway) | Çıkarım için ortak Kubernetes API'si — K8s bilmeden model dağıtın, HuggingFace keşfi ve maliyet tahminleriyle |
| [HolmesGPT](https://www.cncf.io/blog/2026/01/07/holmesgpt-agentic-troubleshooting-built-for-the-cloud-native-era/) | Cloud-native için agentic sorun giderme — artık CNCF Sandbox projesi |
| [Dalec](https://github.com/project-dalec/dalec) | SBOM üretimiyle bildirimsel container imaj oluşturma — derleme aşamasında daha az CVE |

Yön açık: .NET API'niz, Semantic Kernel orkestrasyon katmanınız ve çıkarım iş yüklerinizin hepsi tek tutarlı bir platform modelinde çalışmalı. Oraya doğru ilerliyoruz.

## Bu Hafta Nereden Başlardım

Bu değişiklikleri ekibiniz için değerlendiriyorsanız, işte dürüst öncelik listem:

1. **Önce gözlemlenebilirlik** — üretim dışı bir kümede GPU metriklerini ve ağ akış günlüklerini etkinleştirin. Neyi kaçırdığınızı görün.
2. **Mavi-yeşil yükseltmeleri deneyin** — bir sonraki üretim kümesi yükseltmenizden önce rollback iş akışını test edin. Sürece güven inşa edin.
3. **Kimlik farkında ağı pilot edin** — bir dahili servis yolu seçin ve Cilium ile mTLS'i etkinleştirin. Yükü ölçün (spoiler: minimumdur).
4. **Fleet Manager'ı değerlendirin** — ikiden fazla küme çalıştırıyorsanız, kümeler arası ağ azaltılan özel yapıştırıcıyla kendini amorti eder.

Küçük deneyler, hızlı geri bildirim. Her zaman doğru hamle budur.

## Son Söz

KubeCon duyuruları bunaltıcı olabiliyor, ancak bu grup gerçekten AKS'teki .NET ekipleri için iğneyi hareket ettiriyor. Mesh yükü olmadan daha iyi ağ güvenliği, gerçek GPU gözlemlenebilirliği, daha güvenli yükseltmeler ve daha güçlü AI altyapısı temelleri.

Halihazırda AKS'teyseniz, bu operasyonel temelinizi sıkılaştırmak için harika bir an. .NET iş yüklerini Kubernetes'e taşımayı planlıyorsanız — platform önemli ölçüde daha üretim hazır hale geldi.
