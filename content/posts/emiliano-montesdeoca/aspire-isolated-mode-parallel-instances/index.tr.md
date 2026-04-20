---
title: "Aspire'ın İzole Modu Paralel Geliştirmedeki Port Çakışması Kabusu'nu Çözüyor"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2, --isolated modunu tanıtıyor: rastgele portlar, ayrı sırlar ve aynı AppHost'un birden fazla örneği çalıştırılırken sıfır çakışma. AI agentlar, worktree'ler ve paralel iş akışları için mükemmel."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Aynı projenin iki örneğini aynı anda çalıştırmayı denediyseniz acıyı bilirsiniz. Port 8080 zaten kullanımda.

Aspire 13.2 bunu tek bir flag ile düzeltiyor. James Newton-King [tüm detayları yazdı](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/).

## Düzeltme: `--isolated`

```bash
aspire run --isolated
```

Her çalıştırma şunları alır:
- **Rastgele portlar** — örnekler arasında çakışma yok
- **İzole kullanıcı sırları** — bağlantı dizileri ve API anahtarları her örnek için ayrı kalır

## Gerçek senaryolar

**Birden fazla checkout:**

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Her ikisi de çakışma olmadan çalışır.

**VS Code'da arka plan agentları.** Copilot Chat'in arka plan agentı bağımsız çalışmak için git worktree oluşturduğunda, izole mod her iki örneğin de çalışmasını sağlar.

## Sonuç

İzole mod, gerçek, giderek yaygınlaşan bir problemi çözen küçük bir özelliktir. 13.2'yi `aspire update --self` ile alın.
