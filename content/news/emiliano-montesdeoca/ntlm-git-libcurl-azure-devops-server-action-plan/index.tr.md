---
title: "NTLM Git/libcurl'de Sona Eriyor: Azure DevOps Server Ekiplerinin Gerçek Bir Geçiş Planına İhtiyacı Var"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "Eylül 2026 NTLM kaldırması küçük bir uyumluluk sorunu değil; şirket içi Azure DevOps Server ortamları için bir kimlik mimarisi son tarihidir."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

libcurl'de yaklaşan NTLM kaldırması, teknik görünen ancak aslında organizasyonel olan değişikliklerden biridir. Azure DevOps Server'a Git over HTTPS yolunuz hala NTLM'ye bağlıysa, sorununuz araç değil, kimlik borcudur.

Orijinal kaynak: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft bu konuda sert davranmakta haklıdır. NTLM bilinen kriptografik zayıflıklara sahiptir ve modern bir kurumsal varsayılan olmamalıdır. Tehlikeli kısım, birçok ortamın aslında sessiz SPNEGO geri dönüşüyle NTLM'ye hayatta kalırken Kerberos kullandıklarına inanmalarıdır. Bu yanılsama Eylül 2026'da ortadan kalkar.

Benim görüşüm: buna bir "istemci sürümü" sorunu olarak davranmayın. NTLM bayraklarını yeniden etkinleştirmek, eski Git derlemelerini sabitlemek veya geri dönüşün mevcut kalacağını ummak, uzun vadeli risk taşıyan kısa ömürlü bir geçici çözümdür. Düzeltme stratejiniz düşürme ve geciktirme ise, operasyonel kırılganlığı aktif olarak artırıyorsunuz demektir.

Pratik bir geçiş sırası açık ve ölçülebilir olmalıdır.

İlk olarak, mevcut kimlik doğrulama davranışını şimdi doğrulayın. Gerçek geliştirici ve derleme ajanı bağlamlarında, etki alanı dışı ve uzak ağ yolları dahil, izleme tabanlı kontroller ve bilet önbellek doğrulaması çalıştırın. İkinci olarak, Kerberos'u uçtan uca düzeltin: SPN'ler, DNS takma adları, yük dengeleyici ayarları, delegasyon ve etki alanı denetleyicisi erişilebilirliği. Üçüncü olarak, etki alanına katılmamış veya çalışma grubu senaryolarını erken belirleyin ve Kerberos'un güvenilir hale getirilemediği yerlerde bir SSH şeridi tasarlayın.

Ayrıca sahiplik netliğine ihtiyacınız var. Güvenlik ekipleri politika temellerini tanımlamalı, ancak platform mühendisliği uygulama hazırlığına sahip olmalıdır. Bu, bireysel repo yöneticileri için bir yan görev olamaz. IIS, AD, ağ ucu, CI ajanları ve geliştirici iş istasyonu rehberliği genelinde koordineli değişiklikler gerektirir.

İnce bir risk otomasyondur. Derleme ajanları ve hizmet hesapları, insan kullanıcılar sorunsuz olsa bile, genellikle Kerberos biletlerinin eksik veya geçersiz olduğu bağlamlarda çalışır. Yalnızca etkileşimli geliştirici iş akışlarını test ederseniz, en kritik kırılma noktalarını kaçırırsınız.

Olumlu tarafı gerçektir. Temiz bir şekilde Kerberos veya SSH'ye geçmek yalnızca kırılmayı önlemekle kalmaz, saldırı yüzeyini azaltır ve kimlik kontrollerini modern uyum beklentileriyle hizalar. Bu geçişe şimdi başlayan ekipler Eylül'ü sıradan bir olay olarak görecek. Bekleyen ekipler, sürüm baskısı altında kimlik doğrulama hatalarını ayıklıyor olacak.

Bu arşivlenecek bir uyarı değil. Karşılık verilmesi gereken bir son tarihtir.