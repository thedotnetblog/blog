---
title: "Derin Ajanlar + Cosmos DB, Canlı Operasyonel Verilere Karşı Çalışmak İçin Pratik Bir Model Gösteriyor"
date: 2026-06-22
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB ile Deep Agents örneği, bir ajanın doğrudan operasyonel veriler üzerinde çalışması, birden çok adımda planlama yapması, yazmaları doğrulaması ve işletmenin zaten kullandığı aynı depoda temellenmesi açısından ilginçtir."
tags:
  - Azure Cosmos DB
  - AI
  - Agents
  - Azure
  - Architecture
---

Gerçek operasyonel iş akışlarına yakın duran ajan örneklerini severim.

Bu yeni **Deep Agents + Azure Cosmos DB** örneği tam olarak bunu yapıyor.

Kopuk bir demo dünyası icat etmek yerine, ajanı Cosmos DB'de saklanan bir destek bileti kuyruğunun üzerine koyuyor ve ekiplerin gerçekten önemsediği şeyleri yapmasını istiyor:

- iş triyajı
- desenleri tespit etme
- kayıtları güncelleme
- sonuçları doğrulama

Bu, bir ajan sistemi için çok daha kullanışlı bir şekildir.

## Gerçek değer "AI veritabanıyla konuşuyor" değil

Bu hikayeyi zaten gördük.

Bu örneği daha iyi yapan şey, etrafındaki operasyonel disiplindir:

- ajan belirli araçları kullanır
- yazmalar kontrollü bir yoldan geçer
- akışın bir parçası olarak okuma-sonrası-yazma doğrulaması vardır
- bölümleme ve sorgu maliyeti dikkate alınır
- sistem, gerçeklik taklidi yapan bir yan önbellek değil, canlı tarzı operasyonel veriler üzerinde çalışır

Bu kombinasyon, modeli ilginç kılan şeydir.

## Cosmos DB'nin buraya neden iyi uyduğu

Cosmos DB, bu tür bir iş yükü için iyi bir eşleşmedir çünkü veriler zaten dinamik, belge şeklinde ve operasyoneldir.

Ajan şunları yapabilir:

- biletleri doğrudan okuyabilir
- gerektiğinde kuyruk çapında sorgular çalıştırabilir
- belirli öğeleri yamalayabilir
- durumu ve geçmişi verinin kendisine yakın tutabilir

Ajan senaryoları için bu, her şeyi önce ayrı bir analitik katmandan geçirmeye zorlamaktan genellikle daha kullanışlıdır.

## Benim görüşüm

Buradaki en büyük çıkarım, ajan sistemlerinin işletmenin zaten güvendiği aynı veriler ve aynı iş akışları üzerinde çalıştıklarında çok daha ilgi çekici hale gelmeleridir.

Bu örneğin doğru yaptığı şey budur.

Ajanı, bağlantısız bir sohbet arayüzü gibi davranmak yerine, net araç sınırları olan operasyonel bir katılımcı olarak ele alır.

Bu, çalışılmaya değer bir modeldir.

Orijinal yazı: [How to Use Deep Agents with Azure Cosmos DB – Plan, act, and verify against operational data](https://devblogs.microsoft.com/cosmosdb/deep-agents-to-plan-act-verify-against-operational-data/)