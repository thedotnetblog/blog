---
title: "Docker Sandbox, Copilot Agentlarının Makinenizi Riske Atmadan Kodunuzu Yeniden Düzenlemesini Sağlıyor"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox, GitHub Copilot agentlarına yeniden düzenleme için güvenli bir mikroVM veriyor — izin istemleri yok, host'a risk yok. Bu büyük ölçekli .NET modernizasyonu için her şeyi neden değiştiriyor."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Copilot'ın agent modunu küçük düzenlemelerin ötesinde herhangi bir şey için kullandıysanız, acıyı biliyorsunuzdur. Her dosya yazma, her terminal komutu — bir izin istemi daha.

Azure ekibi, [GitHub Copilot agentları için Docker Sandbox](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/) hakkında bir yazı yayımladı.

## Docker Sandbox size gerçekte ne veriyor

Temel fikir basit: tam Linux ortamıyla hafif bir mikroVM başlatın, çalışma alanınızı senkronize edin ve Copilot agentının içeride serbestçe çalışmasına izin verin.

Bu "sadece şeyleri bir konteynerde çalıştır"dan daha fazlası:
- Mutlak yolları koruyan **çift yönlü çalışma alanı senkronizasyonu**
- MikroVM içinde çalışan **özel Docker daemon**
- Ağ erişimini kontrol eden **HTTP/HTTPS filtreleme proxy'leri**
- **YOLO modu** — agent izin istemleri olmadan çalışır

## .NET geliştiricileri neden önemsemeli

Docker Sandbox ile bir Copilot agentını bir projeye yöneltebilir, mikroVM içinde özgürce yeniden düzenlemesine izin verebilir, doğrulamak için `dotnet build` ve `dotnet test` çalıştırabilir ve yalnızca gerçekten çalışan değişiklikleri kabul edebilirsiniz.

## Sonuç

Docker Sandbox, agentic kodlamanın temel gerilimini çözüyor: agentların yararlı olması için özgürlüğe ihtiyacı var, ancak host makinenizdeki özgürlük tehlikelidir. MikroVM'ler size ikisini birden veriyor.
