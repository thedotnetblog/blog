---
title: "Azure DevOps Server Nisan 2026 Yaması — PR Tamamlama Düzeltmesi ve Güvenlik Güncellemeleri"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server, PR tamamlama hatalarına yönelik düzeltme, geliştirilmiş oturum kapatma doğrulaması ve GitHub Enterprise Server PAT bağlantılarını geri kazanımla birlikte Patch 3 alıyor."
tags:
  - azure-devops
  - devops
  - patches
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-devops-server-april-2026-patch" >}}).*

Kendi sunucusunda Azure DevOps Server çalıştıran ekiplere hızlı bir not: Microsoft, üç hedefli düzeltmeyle [Nisan 2026 için Patch 3'ü](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) yayımladı.

## Neler düzeltildi

- **Pull request tamamlama hataları** — iş öğesi otomatik tamamlama sırasında bir null reference istisnası PR birleştirmelerinin başarısız olmasına neden olabiliyordu
- **Oturum kapatma yönlendirme doğrulaması** — potansiyel kötü amaçlı yönlendirmeleri önlemek için iyileştirilmiş doğrulama
- **GitHub Enterprise Server PAT bağlantıları** — GitHub Enterprise Server'a Personal Access Token bağlantıları oluşturma geri yüklendi

## Nasıl güncellenir

[Patch 3'ü](https://aka.ms/devopsserverpatch3) indirip yükleyiciyi çalıştırın. Yamanın uygulandığını doğrulamak için:

```bash
<patch-installer>.exe CheckInstall
```

Microsoft, güvenlik ve güvenilirlik için en son yamayı uygulamanızı şiddetle tavsiye ediyor.
