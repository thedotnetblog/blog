---
title: "Cosmos DB Shell Artık Genel Önizlemede — Ve İçinde Yerleşik Bir MCP Sunucusu Var"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell, veritabanı komutlarını MCP araçları olarak ortaya çıkaran yeni bir açık kaynaklı CLI'dır. AI ajanlarınız, siz de kullandığınız aynı arayüzü kullanarak kapsayıcılarda gezinebilir, sorgular çalıştırabilir ve verileri yönetebilir."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Cosmos DB hakkında tek bir soruyu yanıtlamak için portal sekmesi, SDK örneği ve yarım kalmış bir betik arasında geçiş yapmak zorunda kaldıysanız, bu projenin ortadan kaldırmak için tasarlandığı sürtünmeyi zaten biliyorsunuzdur.

Azure Cosmos DB Shell genel önizlemeye girdi. bash benzeri sözdizimine sahip açık kaynaklı bir CLI ve — onu ilginç kılan kısım — entegre bir MCP sunucusu.

## Diğer Veritabanı CLI'larından Farkı

CLI'nin kendisi kullanışlıdır: tanıdık komutlar, betikleme desteği, CI/CD entegrasyonu. Bu kısım, geliştirici odaklı bir veritabanı aracı için minimum standarttır.

İlginç kısım ise MCP sunucusu entegrasyonudur. CLI'nin ortaya çıkardığı her komut, AI ajanlarınızın çağırabileceği bir MCP aracı olarak kullanılabilir hale gelir. Özel API katmanı yok, yazılacak entegrasyon kodu yok. Ajanınız şunları yapabilir:

- `cd`, `ls`, `pwd` ile veritabanı hiyerarşilerinde gezinme
- `query` ile SQL sorguları çalıştırma ve yapılandırılmış sonuçlar alma
- `create item`, `update`, `rm` ile öğe oluşturma ve değiştirme
- `mkdb`, `mkcon`, `rmdb`, `rmcon` ile veritabanları ve kapsayıcıları yönetme
- `endpoint`, `pwd` ile mevcut bağlamı inceleme

Temel değişiklik: Ajanınız Cosmos DB API'siyle konuşmuyor — sizin kullandığınız aynı shell arayüzüyle konuşuyor. Komutlar deterministik, denetlenebilir ve açık kaynaklı olduğundan tam olarak ne olduğunu inceleyebilirsiniz.

## Açık Kaynak Temeli Önemlidir

Bu, kara kutu bir yönetilen hizmet değil. Shell açık kaynaktır, yani:

- Güvenlik ekipleri uygulamayı denetleyebilir
- Platform ekipleri kendi özel standartları için çatallanıp genişletebilir
- Geliştiriciler herkese fayda sağlayan iyileştirmelere katkıda bulunabilir

AI araçlarını benimseyen kurumsal ekipler için "tam olarak nasıl çalıştığını görebilir miyiz" giderek isteğe bağlı bir gereksinim olmaktan çıkıyor. Buradaki açık kaynak önemli bir farklılaştırıcıdır.

## Daha Kolay Hale Gelen Üç Senaryo

**Akıllı veri analizi** — bir ajanı shell'e bağlayın, doğal dilde sorular sorun, yapılandırılmış sorgu sonuçları alın. Ajan sorgu oluşturmayı ele alır; shell yürütmeyi ele alır.

**Otonom veri yönetimi** — Cosmos DB'de veri oluşturması, güncellemesi veya kaldırması gereken iş akışları, özel entegrasyon gerektirmeden MCP araçları aracılığıyla bunu yapabilir.

**Gerçek zamanlı izleme ve uyarılar** — bir ajan düzenli aralıklarla kapsayıcıları sorgulayabilir, sonuçları karşılaştırabilir ve anlamlı herhangi bir bildirim kanalı aracılığıyla anomalileri raporlayabilir.

MCP arayüzü, bu senaryoları MCP'yi destekleyen herhangi bir AI platformuyla — yalnızca Microsoft araçlarıyla değil — birleştirilebilir kılar.

## Başlarken

Shell genel önizleme aşamasındadır. Kurun, Cosmos DB bağlantınızı yapılandırın ve MCP sunucusunu etkinleştirin. Oradan, MCP uyumlu herhangi bir ajan ana bilgisayarı araçları keşfedebilir ve kullanabilir.

Orijinal gönderi: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
