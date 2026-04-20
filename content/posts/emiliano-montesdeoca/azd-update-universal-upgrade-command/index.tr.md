---
title: "azd update — Tüm Paket Yöneticilerinizi Yönetmek İçin Tek Komut"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI artık nasıl kurduğunuzdan bağımsız olarak çalışan evrensel bir güncelleme komutuna sahip — winget, Homebrew, Chocolatey veya kurulum betiği."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azd-update-universal-upgrade-command" >}}).*

Her birkaç haftada bir açılan "azd'nin yeni bir sürümü mevcut" mesajını biliyor musunuz? `azd`'yi winget, Homebrew veya altı ay önce çalıştırdığınız curl betiğiyle mi kurduğunuzu hatırlayamadığınız için kapatıp geçtiğiniz şeyi? Bu sonunda düzeltildi.

Microsoft [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/)'i yayımladı — Azure Developer CLI'yi, başlangıçta nasıl kurduğunuzdan bağımsız olarak en son sürüme güncelleyen tek bir komut.

## Nasıl çalışır

```bash
azd update
```

Hepsi bu. Yeni özellikler için erken erişim istiyorsanız:

```bash
azd update --channel daily
azd update --channel stable
```

Komut, mevcut kurulum yönteminizi algılar ve perde arkasında uygun güncelleme mekanizmasını kullanır.

## Küçük not

`azd update` 1.23.x sürümünden itibaren geliyor. Daha eski bir sürümdeyseniz, orijinal kurulum yönteminizi kullanarak bir son manuel güncelleme yapmanız gerekecek. Ondan sonra `azd update` her şeyi halleder.

## Neden önemli

Bu küçük bir yaşam kalitesi iyileştirmesidir, ancak AI agentları ve Aspire uygulamalarını Azure'a dağıtmak için günlük `azd` kullananlar için güncel kalmak önemlidir.

[Tam duyuruyu](https://devblogs.microsoft.com/azure-sdk/azd-update/) okuyun.
