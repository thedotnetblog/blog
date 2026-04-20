---
title: "azd update — Tüm Paket Yöneticileriniz İçin Tek Bir Komut"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık, onu nasıl yüklediğinizden bağımsız olarak güncelleyen evrensel bir güncelleme komutuna sahip — winget, Homebrew, Chocolatey veya kurulum betiği."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azd-update-universal-upgrade-command" >}}).*

Her birkaç haftada bir beliren "azd'nin yeni bir sürümü mevcut" mesajını biliyor musunuz? `azd`'yi winget, Homebrew veya altı ay önce çalıştırdığınız curl betiğiyle mi yüklediğinizi hatırlayamadığınız için görmezden geldiğiniz mesajı? Evet, bu sonunda düzeldi.

Microsoft, [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/)'i piyasaya sürdü — Azure Developer CLI'ı, başlangıçta nasıl yüklediğinizden bağımsız olarak en son sürüme güncelleyen tek bir komut. Windows, macOS, Linux — fark etmiyor. Tek komut.

## Nasıl çalışıyor

```bash
azd update
```

Hepsi bu. Yeni özelliklere erken erişim istiyorsanız, günlük insiders derlemesine geçebilirsiniz:

```bash
azd update --channel daily
azd update --channel stable
```

Komut, mevcut kurulum yönteminizi algılar ve arka planda uygun güncelleme mekanizmasını kullanır. Artık "bu makinede winget mi yoksa choco mu kullandım?" sorusuna gerek yok.

## Küçük bir uyarı

`azd update`, 1.23.x sürümünden itibaren gönderilmeye başlandı. Daha eski bir sürümdeyseniz, orijinal kurulum yönteminizi kullanarak son bir manuel güncelleme yapmanız gerekecek. Bundan sonra `azd update` her şeyi halleder.

Mevcut sürümünüzü `azd version` ile kontrol edin. Yeni bir kuruluma ihtiyacınız varsa, [kurulum dokümanları](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) size yol gösterir.

## Neden önemli

Bu küçük bir yaşam kalitesi iyileştirmesi, ancak Azure'a AI ajanları ve Aspire uygulamaları dağıtmak için `azd`'yi günlük kullananlar için güncel kalmak daha az "bu hata zaten son sürümde düzeltilmişti" anı demek. Düşünmek zorunda kalmamanız gereken bir şey daha.

Daha fazla bağlam için [tam duyuruyu](https://devblogs.microsoft.com/azure-sdk/azd-update/) ve Jon Gallant'ın [daha ayrıntılı incelemesini](https://blog.jongallant.com/2026/04/azd-update) okuyun.
