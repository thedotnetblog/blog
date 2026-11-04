---
title: "Microsoft Foundry Haziran 2026: Özellik Paketlerinden Yönetilen Bir Ajan Platformuna"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Haziran ayı Foundry güncellemeleri bir platform geçişine işaret ediyor: dağıtım, araçlar, bellek, gözlemlenebilirlik ve optimizasyon, kurumsal kullanıma hazır bir ajan operasyon yığınında birleşiyor."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

Haziran 2026 Foundry dalgası sadece başka bir aylık özet değil. "Harika ajanlar oluşturmaktan" "ajanları yönetilen kurumsal sistemler olarak işletmeye" doğru bir olgunluk geçişini işaret ediyor. Bu ayrım, herhangi bir özellikten daha önemlidir.

Orijinal kaynak: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Üç güncelleme bu değişimi tanımlıyor. Birincisi, ajanların Microsoft 365 Copilot ve Teams'e yayınlanması GA'ya ulaştı ve bu, dağıtımı özel entegrasyon projelerinden görüşlü bir dağıtım şeridine taşıyor. İkincisi, Toolboxes daha güçlü keşif ve yürütme kontrolleri kazandı, buna araç arama ve routines dahil. Üçüncüsü, gözlemlenebilirlik artı optimizasyon, sonradan akla gelen bir şey değil, kasıtlı bir kapalı döngü haline geldi.

Benim görüşüm: bu, sürümdeki en önemli modeldir. İzleme, değerlendirme, optimizasyon ve kontrollü kullanıma sunma, deterministik olmayan sistemler için minimum geçerli işletim modelini oluşturur. Bu parçalardan yalnızca birine sahipseniz, telemetriniz veya ayarınız vardır, yönetişiminiz yoktur.

Foundry içinde Claude GA da stratejiktir, ancak esas olarak model kalitesi nedeniyle değil. Daha büyük değer kurumsal entegrasyondur: Entra kimlik doğrulaması, RBAC, fatura sürekliliği ve politika uyumu. Doğrudan model uç noktalarından Foundry'ye geçen ekipler bunu sağlayıcı değiştirme olarak değil, operasyonel konsolidasyon olarak çerçevelemelidir.

Otopilot ajanlar umut vericidir, ancak kuruluşlar bunlara ayık mimari seçimlerle yaklaşmalıdır. Teams'de paylaşılan alan işbirliği üretkenliği artırabilir, ancak kimlik, izin ve hesap verebilirlik karmaşıklığını hızla yükseltir. Geniş dağıtımdan önce sınırlı kapsamlar ve sıkı onay kontrol noktaları ile başlayın.

Pratik öneriler:

Zaten pilot aşamasındaysanız, yetenek genişletmeden önce enstrümantasyona öncelik verin. Önce GenAI izlemeyi kurun. Ardından genel model metriklerine değil, iş sonuçlarına bağlı değerlendirici paketleri oluşturun. Ancak bundan sonra optimize edici döngülerini ve tanıtım iş akışlarını çalıştırın.

Araç kutusu ağırlıklı ajanlar için, kataloglar büyüdükçe bağlam gürültüsünü ve yanlış araç seçimi riskini azaltmak için erken aşamada araç aramayı etkinleştirin. Bellek özellikli ajanlar için TTL ve saklama politikasını önceden tanımlayın. Yaşam döngüsü kontrolleri olmayan bellek, uyum borcu haline gelir.

Çıkarabileceğim en kesin sonuç şudur: Foundry artık daha az "hangi modeli seçmeliyim?" ve daha çok "ajan davranışını yönetilen bir yaşam döngüsü olarak çalıştırabilir miyim?" ile ilgilidir. İkinci soruyu iyi yanıtlayan ekipler, model değişimine kolayca uyum sağlayacaktır. Model sıralamalarına takılıp kalmış ekipler, her çeyrek kırılgan yığınları yeniden inşa edecektir.

Haziran sürümü bir şeyi netleştiriyor. Foundry, yalnızca bir geliştirme araç seti değil, AI sistemleri için bir operasyon platformu haline geliyor. Bu, inşa edilmesi daha zor ve benimsenmesi çok daha değerli bir üründür.