---
title: "Ajan SQL için Gerçek Sınır: SQL MCP Sunucusunda OBO ile Denetlenebilirlik"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "Data API builder ve SQL MCP Server'da On-Behalf-Of kimlik doğrulaması önemli bir yönetişim kilometre taşıdır çünkü Azure SQL sonunda bir ajan eyleminin arkasındaki insanı denetleyebilir."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Kurumsal AI projelerinde acı bir gerçek vardır: birçok ekip model kalitesine takıntılıdır ve hesap verebilirliği görmezden gelir. Bir ajan üretim verilerini yazdığında veya okuduğunda, ilk olay inceleme sorusu "cevap iyi miydi?" değildir. "Bunu gerçekte kim yaptı?" olur.

Orijinal kaynak: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

Bu nedenle Data API builder 2.0 ile SQL MCP Server'daki OBO desteği ilk bakışta göründüğünden daha büyük bir olaydır. Kullanıcı adı/parola ve yönetilen kimlik yaklaşımları operasyonel olarak hala çalışır, ancak her ikisi de kimliği hizmet sınırına çöker. Günlükler uygulamayı veya ara katmanı gösterir, insan isteğinin kaynağını değil. Bu basit otomasyon için kabul edilebilir. Düzenlenmiş ajan iş akışları için kabul edilebilir değildir.

OBO ile SQL, araç ana bilgisayar kimliğini değil, **delegeli kullanıcı bağlamını** doğrular. Bu size temelde daha iyi bir denetim modeli verir: kullanıcı asıl, eylem, ifade bağlamı ve orta katman uygulama tanımlayıcısı birlikte. MCP araçlarının ve DAB varlık izinlerinin kontrol yüzeyini kaybetmeden izlenebilirlik elde edersiniz.

Benim görüşüm kesindir: ajanınız hassas SQL verilerine dokunabiliyorsa, OBO isteğe bağlı bir sağlamlaştırma görevi değil, varsayılan mimariniz olmalıdır. Kurulum daha karmaşıktır, ancak kimlik borcu her zaman daha sonra ödenir, genellikle güvenlik olayları, uyum denetimleri veya yönetici eskülasyonları sırasında.

### Pratik uygulama rehberliği

- **Kimlik akışını doğrulayarak başlayın** minimal bir "WhoAmI" görünümü ve entegrasyon testlerinde otomatik kontrollerle. SQL asıl kullanıcısı, oturum açmış kullanıcıyla eşleşmiyorsa, göndermeden önce durun ve düzeltin.
- **SQLSecurityAuditEvents için Log Analytics sorgularını** SOC panolarınıza bağlayın ve OBO yolları aracılığıyla başlatılan yüksek riskli eylemler için uyarı ayarlayın.
- **RBAC ve DAB izinlerini hizalayın** böylece kullanıcı düzeyinde kimlik ve eylem düzeyinde yetkilendirme uçtan uca tutarlı kalır.

Duyuruda ince ama önemli bir tasarım noktası önbellek davranışıdır. DAB, kullanıcı delegeli kimlik doğrulaması etkinleştirildiğinde yanıt önbelleğe almayı açıkça engeller. Bu ödünleşim doğrudur. Çok kiracılı veya düzenlenmiş ortamlarda, kullanıcı kapsamlı sonuçları sızdırabilecek performans hileleri buna değmez.

**SQL MCP Server artı OBO**, olgun bir modelin başlangıcıdır: kontrollü operatörler olarak ajanlar, sorumlu asıllar olarak kullanıcılar, denetlenebilir sistemler olarak veri düzlemleri. Mimarınız "bunu kim yaptı?" sorusuna güvenle cevap veremiyorsa, demo ne kadar cilalı görünürse görünsün, bu üretime hazır AI değildir.