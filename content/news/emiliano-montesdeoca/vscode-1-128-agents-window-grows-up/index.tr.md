---
title: "VS Code 1.128 Net Bir Bahis Yapıyor: Ajan Penceresi Yeni Çalışma Yüzeyi Haline Geliyor"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128, ajan iş akışlarını çoklu sohbet oturumları, GA görüntü desteği ve daha derin host/session kontrolleriyle yenilikten günlük ergonomiye dönüştürüyor."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128, öldürücü bir özellik nedeniyle değil, birkaç değişikliğin tek bir yön etrafında hizalanması nedeniyle anlamlı bir sürümdür: düzenleyici içinde ajan-ilk geliştirme yapılandırılmış, paralel ve operasyonel olarak yönetilebilir hale geliyor.

Orijinal kaynak: https://code.visualstudio.com/updates/v1_128

Öne çıkan, ajan ana bilgisayar oturumlarında daha zengin çoklu sohbet davranışıdır: eş sohbetleri, çatallar ve tek bir üst oturum altında eşzamanlı turlar. Bu, alternatif uygulamaları keşfederken veya görevleri doğrulama yollarına bölerken deneyimli geliştiricilerin tam olarak ihtiyaç duyduğu şeydir. Nadiren doğrusal olan gerçek mühendislik çalışmasını yansıtır.

Benim görüşüm: bu, Ajan Penceresinin bir sohbet panelinden çok bir çalışma alanı orkestrasyon yüzeyi gibi hissettirdiği ilk VS Code sürümüdür.

Seçili bir çalışma alanı olmadan hızlı sohbetler de göründüklerinden daha önemlidir. Kavramsal veya mimari sorular için sürtünmeyi azaltırken, projeye bağlı oturumları ayrı tutarlar. Bu ayrım, dağınıklığı azaltabilir ve kod değiştiren iş akışları için bağlam bütünlüğünü koruyabilir.

Copilot Vision'ın GA'ya ulaşması başka bir dönüm noktasıdır. Görüntüler ve PDF'ler sohbet için normal girdiler haline geldiğinde, belge yoğun ve UI yoğun görevler önemli ölçüde daha akıcı hale gelir. Ekipler artık çok modlu bağlamı gelişmiş bir eklenti olarak değil, varsayılan yetenek olarak düşünmelidir.

Pratik platform etkileri de vardır. Ajan ana bilgisayar senaryolarında BYOK desteği, yapılandırılabilir model örnekleme parametreleri ve yardımcı model varsayılanları, kurumsal model yönetişimi için artan olgunluğu gösterir. Katı sağlayıcı gereksinimleri olan kuruluşlar, herkese uyan tek beden varsayılanları yerine daha ince kontrollerle davranışı şekillendirebilir.

1.128'i benimseyen ekipler için öneriler:

Çoklu sohbet oturumlarında sohbet dallanması ve adlandırması için kurallar tanımlayın, böylece paralel keşif konuşma gürültüsüne dönüşmez. Geliştiricileri biri uygulama, biri testler veya hata analizi için olmak üzere bir sohbet tutmaya teşvik edin. Hızlı sohbetleri repo dışı sorular için kasıtlı olarak kullanın.

BYOK uç noktaları çalıştırıyorsanız, iş yükü sınıfı başına temel sıcaklık/top_p profilleri oluşturun ve istisnaları belgeleyin. Ayrıca, kazara sessiz davranış boşluklarını önlemek için yardımcı akışların Copilot tarafından sağlanan veya BYOK modellerinde çalışıp çalışmayacağına karar verin.

Son olarak, işletim sistemi düzeyinde kısayolları stratejik olarak değerlendirin. VS Code komutlarını sistem genelinde tetikleyebilmek, güç kullanıcıları için akışı iyileştirebilir, ancak yönetilmeyen kısayol yayılımı ekipler arasında tutarlılığa zarar verebilir.

VS Code 1.128 sadece özellikler eklemez. Gerçek geliştirme döngülerinde ajan işbirliğinin mekaniğini sıkılaştırır. Bir sonraki döngüde kazanan düzenleyiciler, ajan etkileşimlerine yan çubuk deneyleri olarak değil, birinci sınıf iş akışı ilkelleri olarak davrananlar olacaktır. Bu sürüm, VS Code'un bu yarışı anladığını gösteriyor.