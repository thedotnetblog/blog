---
title: 'Sırlar Olmadan Cosmos DB Erişimi Yeni Temel Seviyedir'
date: 2026-07-16
author: 'Emiliano Montesdeoca'
description: 'Cosmos DB uygulamanız hala anahtarlara bağlıysa, operasyonel güvenlikte zaten geridesiniz.'
tags:
  - azure-cosmos-db
  - dotnet
  - managed-identity
  - rbac
  - cloud-security
---

Orijinal kaynak: [Which Azure Cosmos DB Role Does My App Need?](https://devblogs.microsoft.com/cosmosdb/which-azure-cosmos-db-role-does-my-app-need/)

Bu Cosmos DB rehberindeki en önemli fikir bir komut, bir rol kimliği veya bir CLI hilesi değildir. Mimari bir fikirdir: **kimlik bilgilerini uygulama yapılandırması olarak ele almayı bırakın** ve kimliği çalışma zamanı durumu olarak ele almaya başlayın.

Çok fazla ekip hala bağlantı dizeleriyle gönderim yapıyor çünkü hızlı hissettiriyor. Hızlı değil. Ertelenmiş risktir. Yapılandırma dosyasındaki her anahtar, acele bir commit, kopyalanmış bir pipeline değişkeni veya sızdırılmış bir günlük bekleyen bir olay haline gelir. Yönetilen kimlik artı veri düzlemi RBAC, bu başarısızlık sınıfını neredeyse tamamen ortadan kaldırır.

Pratik zorluk, **kontrol düzlemi** ve **veri düzlemi** yetkilendirmesi arasındaki karışıklıktır. Birçok güçlü ekibin günler kaybettiği yer burasıdır. Kaynaklardaki Azure RBAC rolleri otomatik olarak belge erişimi vermez ve Cosmos veri düzlemi rolleri hesap yönetimi vermez. Ekibiniz bu ayrımı runbook'larınızda açıkça belgelemezse, kırılgan dağıtımlar ve ayıklaması zor 403'ler almaya devam edersiniz.

### Üretim ekipleri için görüşümlü önerim

- **Okuma yolları için Data Reader** ile başlayın ve yazmanın gerçekten gerekli olduğu yerlerde Data Contributor kullanın.
- **Yalnızca hesap başına tek bir uygulama sınırınız varsa** geniş kapsamlı yetkilendirin.
- **Bir hesabı hizmetler arasında paylaşıyorsanız**, denetim baskısını beklemek yerine erken aşamada veritabanı veya kapsayıcı sınırlarına daraltın.

Bu, **biriken** kararlardan biridir. .NET uygulamanızı `DefaultAzureCredential` ve yalnızca uç nokta yapılandırması ile bağladığınızda, her ortam temizlenir: yerel, CI, hazırlık ve prod. Ayrıca, izinler hakkında gizemli anahtarları avlamak yerine rol atamaları aracılığıyla akıl yürütebildiğiniz için olay müdahalesini hızlandırırsınız.

Makale ayrıca olgun ekiplerin benimsemesi gereken bir şeyi ima ediyor: **izinleri tek seferlik kurulum değil, yinelemeli tasarım** olarak ele alın. Teslim etmek için yeterince geniş başlayabilir, ardından telemetri ve erişim incelemeleriyle daraltabilirsiniz. En az ayrıcalık felsefi bir hedef değildir; bir teslimat alışkanlığıdır.

Bu yazıdan yalnızca bir şey alacaksanız, şu olsun: **önce sırları kaldırın, sonra rolleri optimize edin**. Bu sırayı tersine çeviren ekipler genellikle toplantılarda takılır. Önce sırları kaldıran ekipler genellikle gönderir, sonra sağlamlaştırır.

2026'da, **sırrız veri erişimi gelişmiş bir kalıp değildir**. Azure'da ciddi .NET sistemleri için minimum sorumlu standarttır.