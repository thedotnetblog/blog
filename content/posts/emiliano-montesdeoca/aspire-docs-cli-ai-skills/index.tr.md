---
title: "Aspire 13.2 Docs CLI ile Geliyor — AI Agentınız da Kullanabilir"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2, aspire docs ekliyor — terminali terk etmeden resmi belgeleri arama, göz atma ve okuma için bir CLI. AI agentlar için araç olarak da çalışıyor."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "aspire-docs-cli-ai-skills" >}}).*

Aspire AppHost'ta derinlere daldığınız, entegrasyonlar bağladığınız ve Redis entegrasyonunun hangi parametreler beklediğini tam olarak kontrol etmeniz gereken o anı bilirsiniz. Tarayıcıya alt-tab yapıyorsunuz, aspire.dev'de arama yapıyorsunuz. Bağlam kopuyor.

Aspire 13.2 [bunun için bir düzeltme yayımladı](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). `aspire docs` CLI, doğrudan terminalden resmi Aspire belgelerini aramanızı, gözatmanızı ve okumanızı sağlıyor.

## Üç komut, sıfır tarayıcı sekmesi

```bash
# Tüm dökümanları listele
aspire docs list

# Konu ara
aspire docs search "redis"

# Sayfanın tamamını oku
aspire docs get redis-integration

# Sadece bir bölüm
aspire docs get redis-integration --section "Add Redis resource"
```

## AI agent açısı

Aynı `aspire docs` komutları AI agentlar için araç olarak çalışıyor. Eski eğitim verilerine dayalı Aspire API'lerini uydurmak yerine, agent `aspire docs search "postgres"` çağırabilir, resmi entegrasyon belgelerini bulabilir ve doğru sayfayı okuyabilir.

## Sonuç

`aspire docs`, gerçek bir problemi temiz bir şekilde çözen küçük bir özelliktir. [David Pine'ın deep dive](https://davidpine.dev/posts/aspire-docs-mcp-tools/) yazısına bakın.
