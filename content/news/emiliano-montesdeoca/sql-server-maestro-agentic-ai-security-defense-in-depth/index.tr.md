---
title: "MAESTRO, Savunma Derinliği ve SQL Server'ın Artık AI için Neden Güvenlik Sınırı Olduğu"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Ajanssal AI, geleneksel STRIDE modellerinin tasarlanmadığı tehditler sunar. Microsoft SQL'in bir yönetilen yürütme sınırı sağlamak için MAESTRO çerçevesine nasıl eşlendiği burada açıklanmaktadır."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Güvenlik tehdit modelleri, kimin veya neyin talep ettiğine dair varsayımlar üzerine inşa edilir. STRIDE, tanımlanmış arayüzler aracılığıyla sistemlerle etkileşime giren insan aktörler varsayar. AI ajanları bu şekilde çalışmaz.

## STRIDE AI Ajanları için Tasarlanmadı

Ajanssal sistemler özerk çalışır, API çağrıları aracılığıyla araçları zincirler, hangi verilerin alınacağına ve hangi eylemlerin yürütüleceğine dair kararlar verir ve birden fazla kaynaktan talimat alabilir — kullanıcı komutları, araç sonuçları, alınan veriler. STRIDE tehdit modeli (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), komut enjeksiyonu, bağlam zehirlenmesi veya araç kötüye kullanımı gibi ajana özgü saldırı vektörlerini yeterince yakalamaz.

Cloud Security Alliance, AI ajanı riski için özel olarak MAESTRO çerçevesini yayımladı.

## MAESTRO Çerçevesi

MAESTRO, ajanssal AI riskini yedi katmanda düzenler:

1. **Foundation Models** — temel LLM'ler ve eğitim güvenlik açıkları
2. **Data Operations** — veri alımı, depolama ve manipülasyon
3. **Agent Frameworks** — ajan orkestrasyonu ve koordinasyon yazılım katmanı
4. **Deployment & Infrastructure** — ajanların nerede çalıştığı ve nasıl yapılandırıldığı
5. **Evaluation & Observability** — zaman içinde ajan davranışının izlenmesi
6. **Security & Compliance** — erişim kontrolleri, denetim ve düzenleyici uyumluluk
7. **Agent Ecosystem** — ajanların birbirleriyle ve harici araçlarla nasıl etkileşime girdiği

Her katmanın, geleneksel güvenlik kontrollerinin doğrudan ele almadığı belirli saldırı vektörleri vardır.

## Yönetilen Yürütme Sınırı Olarak Microsoft SQL

SQL Server 2025, MAESTRO katmanlarına somut yollarla eşlenir:

**Data Operations katmanı**: T-SQL'e entegre `AI_GENERATE_EMBEDDINGS`, vektör işlemlerini veritabanının yönetilen sınırı içinde tutar. Embedding işlemesi için verilerin model hizmetine gitmesi gerekmez.

**Security & Compliance katmanları**: Satır Düzeyinde Güvenlik (RLS) ve Dinamik Veri Maskeleme (DDM), talebin nasıl geldiğinden bağımsız olarak uygulanır — insan kullanıcıdan mı yoksa AI ajanından mı. Ajan, veritabanının kendisi tarafından uygulanan kontrolleri atlayamaz.

**Agent Frameworks katmanı**: Saklı yordamlar araç sınırları olarak hizmet eder. Ajanlara keyfi SQL erişimi vermek yerine, izin verilen işlemleri yordamlar olarak tanımlar ve bunları ajan araçları olarak açarsınız. Parametreli sorgular, yürütme düzeyinde enjeksiyonu önler.

**Evaluation & Observability katmanı**: Denetim günlüğü ve Query Store, her ajanın gerçekte ne yürüttüğünü yakalar — yalnızca ne yapmasının istendiğini değil. Bu izlenebilirlik, atıfın karmaşık olduğu ajanssal sistemlerde olay araştırmaları için çok önemlidir.

## Ajanssal AI için Savunma Derinliği

İlke, geleneksel güvenlikle aynı kalır: hiçbir tek kontrol yeterli değildir. Değişen şey, hangi kontrollerin ajanlar için en önemli olduğudur:

**Patlama yarıçapını azaltma**: saklı yordamlar aracılığıyla araç sınırlaması, güvenliği ihlal edilmiş bir ajanın yalnızca önceden tanımlanmış işlemleri yürütebileceği anlamına gelir. Keyfi sorgulara geçemez.

**Gözlemlenebilirlik**: bir olaydan sonra "bu ajan gerçekte ne yaptı?" sorusunu yanıtlayabilmelisiniz. Veritabanı düzeyinde izlenebilirlik olmadan ajanssal AI sistemlerinin, uygulama günlüğünün kapsamadığı kör noktaları vardır.

**Kısıtlı yürütme**: parametreleme, RLS ve DDM, arayanın insan olup olmadığından bağımsız olarak güvenlik varlıklarıdır. Ajanları barındırmak için bunları zayıflatmayın.

**Hesap verebilirlik**: SQL Server denetim günlüğü, kimin (hangi ajanın, hangi kimlik bilgilerini kullanarak) ne zaman ne yürüttüğünün kaydını oluşturur. Ajanssal sistemler dünyada gerçek sonuçları olan eylemler aldığında bu önem taşır.

SQL Server 2025, ajanssal riski soyut olarak çözmek için inşa edilmedi — ilişkisel bir veritabanı olmak için inşa edildi. Ancak bir kurumsal veritabanını güvenilir kılan yönetişim, tam olarak bir ajan yürütme sınırını güvenli kılan şeydir.

Orijinal gönderi: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
