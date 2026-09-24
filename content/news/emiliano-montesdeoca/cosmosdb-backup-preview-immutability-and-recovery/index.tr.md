---
title: "Cosmos DB için Değişmez Yedekleme, Çok Geç Takdir Ettiğiniz Türden Bir Özellik"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB için Azure Backup artık genel önizlemede değişmez yedeklemeler ve uzun süreli saklama ekliyor. Önemli olan yalnızca kurtarma değil, dayanıklılığı ve kanıt korumasını yüksek riskli veya düzenlemeye tabi iş yükleri için iyileştirmek."
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

Yedekleme özellikleri, odadaki en önemli şey haline geldiği ana kadar göz ardı edilmesi kolay olan özelliklerdir.

Yeni **Azure Cosmos DB için Azure Backup** önizlemesinin ilgiyi hak ettiğini düşünmemin nedeni bu.

Buradaki ilginç kısım yalnızca "bir yedekleme seçeneği daha" değil. **Değişmez kurtarma noktaları** ve **uzun süreli saklama**nın, fidye yazılımı hazırlığı, denetlenebilirlik ve düzenlemeye tabi kurtarma gereksinimleriyle çok daha iyi uyumlu bir modele eklenmesi.

## Değişmezlik konuşmayı değiştiriyor

Saldırganlar üretim sistemlerini hedeflediğinde, bir sonraki soru artık yalnızca "yedeğimiz var mı?" değil.

Şu:

- yedeğe güvenilebilir mi?
- değiştirilebilir veya silinebilir mi?
- olay başladıktan sonra hâlâ korunan bir kurtarma noktamız var mı?

Değişmez yedeklemelerin önemli olmasının nedeni bu. Çevresindeki ortam artık güvenilir olmayabileceğinde kurtarma yolunu iyileştiriyorlar.

## Görüşüm

Bu, herkesi heyecanlandıran türden bir duyuru değil.

Ama Cosmos DB üzerinde kritik iş yükleri çalıştıran ekipler için, çeyreğin en kötü gününde merkezi hale gelen tam olarak türden bir yetenek.

Ve bunlar genellikle takip edilecek en önemli özellikler.

Orijinal yazı: [Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)
