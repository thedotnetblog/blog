---
title: "Azure DevOps Server Nisan 2026 Yaması — PR Tamamlama Düzeltmesi ve Güvenlik Güncellemeleri"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server, PR tamamlama hatalarına yönelik bir düzeltme, geliştirilmiş oturum kapatma doğrulaması ve yeniden çalışır hale getirilen GitHub Enterprise Server PAT bağlantılarıyla birlikte Patch 3'ü aldı."
tags:
  - azure-devops
  - devops
  - patches
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-devops-server-april-2026-patch" >}}).*

Self-hosted Azure DevOps Server kullanan ekipler için hızlı bir hatırlatma: Microsoft, üç hedefli düzeltmeyle birlikte [Nisan 2026 için Patch 3](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/)'ü yayınladı.

## Neler düzeltildi

- **Pull request tamamlama hataları** — iş öğesi otomatik tamamlama sırasında ortaya çıkan bir null reference exception, PR merge işlemlerinin başarısız olmasına neden olabiliyordu. Rastgele PR tamamlama hatalarıyla karşılaştıysanız, muhtemelen nedeni buydu
- **Oturum kapatma yönlendirme doğrulaması** — potansiyel kötü niyetli yönlendirmeleri önlemek amacıyla oturum kapatma sırasındaki doğrulama iyileştirildi. Bu, bir an önce uygulanmaya değer bir güvenlik düzeltmesi
- **GitHub Enterprise Server PAT bağlantıları** — GitHub Enterprise Server'a Personal Access Token bağlantıları oluşturmak bozuktu, artık düzeltildi

## Nasıl güncellenir

[Patch 3](https://aka.ms/devopsserverpatch3)'ü indirin ve yükleyiciyi çalıştırın. Yamanın uygulandığını doğrulamak için:

```bash
<patch-installer>.exe CheckInstall
```

Azure DevOps Server'ı şirket içinde çalıştırıyorsanız Microsoft, hem güvenlik hem de güvenilirlik açısından en güncel yamada kalmayı güçlü bir şekilde öneriyor. Tam ayrıntılar için [sürüm notlarına](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) bakın.
