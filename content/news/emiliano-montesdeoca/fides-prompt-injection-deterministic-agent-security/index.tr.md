---
title: "FIDES, daha fazla görmek istediğim türden deterministik ajan güvenliği hikâyesi"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Agent Framework içindeki yeni FIDES yetenekleri önemlidir; çünkü prompt injection savunmasını sezgisel yöntemlerden, etiketli içeriğe ve middleware kontrollerine dayalı uygulanabilir bir politikaya doğru taşırlar."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Prompt injection savunması çoğu zaman sallantılı bir zeminde duruyormuş gibi hissedilir.

Daha güçlü bir system prompt eklersiniz. Bir filtre eklersiniz. Birkaç allowlist kurarsınız. Ve bir sonraki tuhaf girdinin varsayımları bozmayacağını umarsınız.

İşte bu yüzden **FIDES** ilginç.

Hikâyenin güçlü tarafı, güvenliği daha deterministik bir şeye doğru kaydırmasıdır:

- içeriğe etiketler
- workflow boyunca etiketlerin yayılması
- ayrıcalıklı araçlar çalışmadan önce middleware ile enforcement
- güvenilmeyen bağlamın neyi etkileyebileceğine dair net politika sınırları

## Kaynak makale doğru şekilde açık konuşuyor

Metin, prompt injection'ın "**OWASP LLM Top 10'deki 1 numaralı risk**" olduğunu söyleyerek açılıyor.

Güzel.

Burada bu tür açık sözlülüğü seviyorum, çünkü fazla ekip hâlâ ajan güvenliğini şu anda var olan bir runtime tasarım sorunu yerine gelecekteki bir endişe gibi ele alıyor.

Ve makale bunu güçlü bir pratik karşıtlıkla sürdürüyor: mevcut savunmaların çoğu sezgiseldir, FIDES ise sistemi policy ve enforcement yönüne taşımaya çalışıyor.

Tam olarak doğru değişim bu.

## Bunu başka bir güvenlik whitepaper'ından daha ikna edici yapan şey

AI güvenliği hakkındaki birçok yazı soyut kalıyor.

Bu makale daha iyisini yapıyor. Çok somut bir örnek üzerinden gidiyor: bir GitHub issue triage ajanı, kötü niyetli bir issue body, ayrıcalıklı dosya okuma ve public comment sızıntısı denemesi.

Bu faydalı, çünkü tartışmanın tamamını gerçek bir workflow içine oturtuyor.

Ve o senaryoyu gördüğünüzde, deterministik kontrollerin değeri çok daha kolay anlaşılıyor.

## Temel fikir "modeli daha akıllı yap" değil

Buradaki en önemli şey, FIDES'in modelden saldırıları sihirli biçimde daha iyi tespit etmesini istememesi.

Runtime contract'ı değiştiriyor.

Bu da şu anlama geliyor:

- içerik etiketlenir
- etiketler yayılır
- araçlar neyi kabul ettiklerini açıklar
- middleware, çalıştırmadan önce güvensiz yolları engeller

Bu çok daha sağlıklı bir yaklaşım.

Çünkü ajan gerçek sonuçları olan araçları çağırabildiğinde, güvenlik sadece modelin iyi bir gün geçirip geçirmediğine bağlı olamaz.

## Benim görüşüm

İşte ajan güvenliğinde daha çok görmek istediğim yön tam olarak bu.

"Modelin kötü talimatları görmezden geleceğine güven" değil, "policy fence'i runtime'ın içine kur".

Bu çok daha sağlıklı bir model.

Ve ajan framework'lerinin production'da ciddiye alınmasını istiyorsak, bunun gibi daha fazla hikâyeye ihtiyaçları olacak.

Orijinal gönderi: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)