---
title: "Azure Data Studio Kullanımdan Kaldırıldı: Azure SQL İş Akışınızı VS Code'a Taşıyın"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio 6 Şubat 2025'te kullanımdan kaldırıldı, destek 28 Şubat 2026'da sona eriyor. MSSQL uzantısıyla VS Code'a geçişin tam yolu burada."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[Azure Data Studio 6 Şubat 2025'te kullanımdan kaldırıldı](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), destek 28 Şubat 2026'da sona eriyor — önerilen alternatif MSSQL uzantısıyla VS Code'dur.

## Ne Kurulacak

Başlamak için üç şey:

- **MSSQL uzantısı** — VS Code Marketplace'te "SQL Server (mssql)" arayın
- **SQL Database Projects uzantısı** — şema olarak kod, derleme doğrulaması, rehberli yayımlama
- **.NET 8 SDK** — derleme sistemi tarafından gerekli; SDK eksikliği ilk çalıştırmadaki en yaygın sorundur

## ADS Bağlantılarınızı ve Ayarlarınızı Taşıma

MSSQL uzantısı, rehberli bir akışta tek seferlik geçişi yöneten **ADS Migration Toolkit**'i içerir: kaydedilmiş bağlantılar, bağlantı grupları, ayarlar ve tuş bağlamaları otomatik olarak içe aktarılır.

## F5 Kas Hafızasını Geri Kazanma

ADS kullanıcıları sorgu çalıştırmak için F5'e güvenir. F5 dahil ADS tarzı tuş bağlamalarını geri almak için **MSSQL Database Management Keymap** uzantısını yükleyin.

## SQL Database Projects: Şema Olarak Kod

Projeye sağ tıklayın → **Yayımla** → hedefi yapılandır → oluşturulan T-SQL betiğini gözden geçir → dağıt. Dağıtım öncesindeki betik önizlemesi temel güvenlik özelliğidir. Öğe şablonları tablolar, saklı yordamlar ve görünümler için taslaklar oluşturur — SSDT ile aynı iş akışı.

Sık karşılaşılan sorun: Proje farklı bir SQL Server sürümü için oluşturulmuşsa `.sqlproj` dosyasındaki **hedef platform uyumsuzluğu** derleme hatalarına yol açar.

## Schema Compare ve Schema Designer

Uzantı ayrıca **Schema Compare** (projenizi dağıtılmış veritabanıyla karşılaştırma) ve **Schema Designer** (DDL yazmadan görsel şema düzenleme) içerir.

## Microsoft Fabric Geliştiricileri

Kurulum aynı, ancak VS Code'da açmadan önce **Fabric portalından** başlayın ve veritabanını önce Git'e bağlayın. Microsoft'un özel bir kılavuzu var: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Sonuç

Geçiş, manuel bir yeniden yapılandırma değil, tek seferlik rehberli bir akıştır. Üç aracı yükleyin, ADS Migration Toolkit'i çalıştırın, tuş bağlamalarınızı geri yükleyin — 10 dakikadan kısa sürede normale dönün.

Adım adım ekran görüntüleri ve Fabric'e özgü kılavuz için [tam makaleye](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) bakın.
