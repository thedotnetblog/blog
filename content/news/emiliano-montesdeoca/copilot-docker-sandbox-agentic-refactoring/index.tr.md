---
title: "Docker Sandbox, Copilot Agent'larının Makinenizi Tehlikeye Atmadan Kodunuzu Yeniden Düzenlemesini Sağlıyor"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox, GitHub Copilot agent'larına yeniden düzenleme işlemleri için güvenli bir microVM ortamı sunuyor — izin isteği yok, ana sisteminize risk yok. Bu durum büyük ölçekli .NET modernizasyonunda neden her şeyi değiştiriyor, işte açıklıyoruz."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Copilot'un agent modunu küçük düzenlemelerin ötesinde bir şey için kullandıysanız, acısını bilirsiniz. Her dosya yazma işlemi, her terminal komutu — bir izin isteği daha. Bunu 50 proje boyunca çalıştırdığınızı düşünün. Hiç eğlenceli değil.

Azure ekibi, [GitHub Copilot agent'ları için Docker Sandbox](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/) hakkında bir yazı yayımladı ve dürüst olmak gerekirse, bu gördüğüm en pratik agentic araç geliştirmelerinden biri. MicroVM'ler kullanarak Copilot'a tamamen izole bir ortam sağlıyor; orada istediği gibi davranabilir — paket yükleyebilir, build çalıştırabilir, testleri yürütebilir — ana sisteminize dokunmadan.

## Docker Sandbox size gerçekte ne veriyor

Temel fikir basit: tam Linux ortamıyla hafif bir microVM başlatın, çalışma alanınızı içine senkronize edin ve Copilot agent'ının içinde serbestçe çalışmasına izin verin. İşi bittiğinde değişiklikler geri senkronize edilir.

Bunu sadece "bir container'da bir şeyler çalıştır"dan fazlası yapan şeyler şunlar:

- **Mutlak yolları koruyan çift yönlü çalışma alanı senkronizasyonu**. Proje yapınız sandbox içinde tamamen aynı görünür. Yol kaynaklı build hataları yok.
- **MicroVM içinde çalışan özel Docker daemon**. Agent, ana makinenizin Docker soketini bağlamak zorunda kalmadan container oluşturabilir ve çalıştırabilir. Güvenlik açısından bu büyük bir kazanım.
- **Agent'ın ağda neye erişebileceğini kontrol eden HTTP/HTTPS filtreleme proxy'leri**. Hangi registry'lere ve endpoint'lere izin verildiğine siz karar verirsiniz. Sandbox içindeki bir `npm install`'dan gelen tedarik zinciri saldırıları mı? Engellendi.
- **YOLO modu** — evet, gerçekten böyle çağırıyorlar. Agent izin istemi olmadan çalışıyor çünkü ana makinenize gerçekten zarar veremez. Her yıkıcı eylem sandbox içinde kalıyor.

## .NET geliştiricilerinin neden önemsemesi gerekiyor

Pek çok ekibin şu an karşı karşıya olduğu modernizasyon işini düşünün. .NET 9'a taşımanız gereken, 30 projelik bir .NET Framework çözümünüz var. Bu yüzlerce dosya değişikliği demek — proje dosyaları, namespace güncellemeleri, API değişiklikleri, NuGet geçişleri.

Docker Sandbox ile bir Copilot agent'ını bir projeye yönlendirebilir, microVM içinde serbestçe yeniden düzenlemesine izin verebilir, doğrulama için `dotnet build` ve `dotnet test` çalıştırabilir ve yalnızca gerçekten çalışan değişiklikleri kabul edebilirsiniz. Denemeler yaparken yerel geliştirme ortamınızı yanlışlıkla mahvetme riski yok.

Yazı ayrıca **paralel agent filosu** çalıştırmayı da anlatıyor — her biri kendi sandbox'ında — farklı projeleri aynı anda ele alıyor. Büyük .NET çözümleri veya microservice mimarileri için bu muazzam bir zaman tasarrufu. Servis başına bir agent, hepsi izole çalışıyor, hepsi bağımsız olarak doğrulanıyor.

## Güvenlik boyutu önemli

İnsanların çoğunlukla atladığı şey şu: bir AI agent'ının rastgele komutlar yürütmesine izin verdiğinizde, ona tüm makinenizle güveniyorsunuz demektir. Docker Sandbox bu modeli tersine çeviriyor. Agent, tek kullanımlık bir ortam içinde tam özerklik alıyor. Ağ proxy'si yalnızca onaylanan kaynaklardan çekebilmesini sağlıyor. Ana makine dosya sisteminiz, Docker daemon'unuz ve kimlik bilgileriniz dokunulmadan kalıyor.

Uyumluluk gereksinimleri olan ekipler için — ki bu çoğu kurumsal .NET mağazasıdır — bu, "agentic AI kullanamayız" ile "güvenle benimseyelim" arasındaki farktır.

## Sonuç

Docker Sandbox, agentic kodlamanın temel gerilimini çözüyor: agent'ların kullanışlı olabilmek için özgürlüğe ihtiyacı var, ama ana makinenizde özgürlük tehlikelidir. MicroVM'ler her ikisini de sunuyor. Büyük ölçekli herhangi bir .NET yeniden düzenleme veya modernizasyon planı yapıyorsanız, bunu şimdi kurmaya değer. Copilot'un kod zekasını güvenli bir yürütme ortamıyla birleştirmek, üretim ekiplerinin beklediği tam olarak bu.
