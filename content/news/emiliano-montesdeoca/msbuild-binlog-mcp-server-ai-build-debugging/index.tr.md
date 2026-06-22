---
title: "Binlog MCP Server, .NET için şu anda belki de en pratik AI hata ayıklama aracı"
date: 2026-06-17
author: "Emiliano Montesdeoca"
description: "Yeni Microsoft Binlog MCP Server, AI asistanlarına MSBuild binary log'larına doğrudan erişim sağlıyor. .NET geliştiricileri için bu, build incelemesini manuel arkeolojiden çok daha hızlı, konuşmalı bir iş akışına dönüştürebilir."
tags:
  - .NET
  - MSBuild
  - MCP
  - GitHub Copilot
  - Developer Tools
---

> *Bu makale otomatik olarak çevrildi. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Karmaşık bir .NET build'inin neden başarısız olduğunu anlamaya çalışırken büyük bir `.binlog` dosyası açtıysanız, bunun ne kadar zahmetli olduğunu zaten biliyorsunuzdur.

Veri orada. Hatta fazlasıyla var.

İşte bu yüzden yeni **Microsoft Binlog MCP Server** hemen dikkatimi çekti. .NET dünyasının en bilgi dolu ama aynı zamanda en az dostane debugging artifact'lerinden birini alıp bir AI asistanı üzerinden erişilebilir hale getiriyor.

Ve bazı AI tooling duyurularının aksine, bu son derece pratik görünüyor.

## Amaç binlog'u değiştirmek değil

Amaç, geliştiricilerin MSBuild'i anlamayı bırakması değil.

Amaç, bir binlog hakkında doğal sorular sormanın çoğu zaman her property, task, target ve import chain içinde elle dolaşmaktan çok daha iyi bir ilk adım olmasıdır.

Server şu alanlar için tools sunuyor:

- errors ve warnings
- property tracing
- item ve import inspection
- performance analysis
- build comparison
- embedded file search

Bu, geliştiricilerin bugün zaten `dotnet build /bl` ile ürettiği bir şey için oldukça güçlü bir toolbox.

## Bu neden çok iyi bir MCP kullanım senaryosu

Bazı MCP örnekleri hâlâ biraz zorlanmış hissediliyor.

Bu öyle değil.

MSBuild log'ları structured, detailed ve genellikle insan odaklı bir arayüz için fazla yoğun. Bu da onları, şu işleri yapabilen bir AI asistanı için mükemmel hale getiriyor:

- verinin belirli bölümlerini sorgulamak
- ilişkili ipuçlarını birbirine bağlamak
- olası root cause'u açıklamak
- sizi uygulanabilir bir düzeltmeye yönlendirmek

AI'nin her şeyi sihirli biçimde çözdüğünü iddia etmeden, sürtünmeyi azaltabildiği tam da böyle bir görev bu.

## Geliştirici iş akışı iyileşmesi açık

En iyi tarafı, bunun normal geliştirme akışına ne kadar kolay oturduğunu hayal etmenin çok kolay olması:

1. binlog'u yakala
2. asistanını ona yönlendir
3. neyin başarısız olduğunu, neyin değiştiğini ya da neyin yavaş olduğunu sor
4. incelemeyi sıfırdan elle yeniden başlatmak yerine konuşmayı sürdür

Bu daha iyi bir loop.

Ve tooling, belirsiz tahminler yerine gerçek build log'a dayandığı için güvenilir olma şansı çok daha yüksek.

## Benim görüşüm

Bu, MCP tabanlı tooling'in .NET geliştirme deneyimini gerçekten iyileştirebileceği yerin en net örneklerinden biri gibi görünüyor.

Gösterişli olduğu için değil.

Çok somut bir workflow iyileştirmesiyle gerçek bir pain point'i ele aldığı için.

Büyük solution'larla, dalgalı CI build'lerle, property resolution sorunlarıyla veya performansa duyarlı build pipeline'larla çalışıyorsanız, elinizin altında olmasını isteyeceğim tam olarak böyle bir tool bu.

Orijinal yazı: [AI-Powered MSBuild Investigation with the Microsoft Binlog MCP Server](https://devblogs.microsoft.com/dotnet/msbuild-binlog-mcp-server/)
