---
title: "KubeCon Europe 2026: .NET Geliştiricilerinin Gerçekten Önemsemesi Gerekenler"
date: 2026-03-29
author: "Emiliano Montesdeoca"
description: "Microsoft, KubeCon Europe 2026'da bir dizi Kubernetes duyurusu yaptı. İşte filtrelenmiş sürüm — yalnızca .NET uygulamaları gönderiyorsanız önemli olan AKS ve cloud-native güncellemeleri."
tags:
  - kubernetes
  - aks
  - azure
  - dotnet
  - cloud-native
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "kubecon-2026-aks-updates-dotnet-developers" >}}).*

Microsoft yeni [KubeCon Europe 2026 özetini](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/) yayımladı.

## Service mesh vergisi olmadan mTLS

[Azure Kubernetes Application Network](https://aka.ms/aks/application-network), tam sidecar ağırlıklı bir mesh dağıtmadan karşılıklı TLS, uygulama farkında yetkilendirme ve trafik telemetrisi sağlar. ASP.NET Core API'leriniz arka plan işçileriyle konuşurken — tümü ağ düzeyinde şifrelenmiş, sıfır uygulama kodu değişikliği.

## GPU gözlemlenebilirliği

[AKS artık GPU metriklerini yerel olarak](https://aka.ms/aks/managed-gpu-metrics) yönetilen Prometheus ve Grafana'ya gösteriyor. Özel dışa aktarıcılar yok.

## Küme arası ağ

Azure Kubernetes Fleet Manager artık [küme arası ağ](https://aka.ms/kubernetes-fleet/networking/cross-cluster) sunuyor — unified connectivity, global service registry.

## Daha güvenli yükseltmeler

**Mavi-yeşil agent pool yükseltmeleri** paralel node pool oluşturur. **Agent pool geri alma** önceki sürüme dönmenizi sağlar.

## Nereden başlamalı

1. **Önce gözlemlenebilirlik** — GPU metriklerini ve ağ akış günlüklerini etkinleştirin
2. **Mavi-yeşil yükseltmeleri deneyin** — geri alma iş akışını test edin
3. **Kimlik farkındalıklı ağı pilot edin** — bir servis yolu için mTLS etkinleştirin
