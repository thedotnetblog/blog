---
title: "Agent Framework'te CodeAct: Ajanınızın Gecikmesini Yarıya Nasıl İndirirsiniz"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct, çok adımlı araç zincirlerini tek bir sandbox kod bloğunda birleştirir — gecikmeyi %52, token kullanımını %64 azaltır."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Bu gönderi otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Her ajan projesinde, izlemeye bakıp "bu neden bu kadar uzun sürüyor?" diye düşündüğünüz bir an gelir. Model iyi çalışıyor. Araçlar çalışıyor. Ama tek seferinde hesaplanabilecek bir sonuç için yedi gidiş-dönüş oluyor.

CodeAct'ın tam olarak çözdüğü sorun bu — ve [Agent Framework ekibi yeni `agent-framework-hyperlight` paketiyle alfa destek yayınladı](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).

## CodeAct Nedir?

[CodeAct deseni](https://arxiv.org/abs/2402.01030) zarifçe basittir: Modele tek tek çağrılacak araçların listesini vermek yerine, tek bir `execute_code` aracı verin ve *planın tamamını* kısa bir Python programı olarak ifade etmesine izin verin.

| Yaklaşım | Süre | Token |
|--------|------|--------|
| Geleneksel | 27.81s | 6.890 |
| CodeAct | 13.23s | 2.489 |
| **İyileştirme** | **%52.4** | **%63.9** |

## Güvenlik: Hyperlight Mikro-VM'leri

`agent-framework-hyperlight` paketi [Hyperlight](https://github.com/hyperlight-dev/hyperlight) mikro-VM'leri kullanır. Her `execute_code` çağrısı kendi yeni mikro-VM'ini alır. Başlatma milisaniyelerle ölçülür. İzolasyon neredeyse ücretsizdir.

Araçlarınız ana bilgisayarda çalışmaya devam eder. Modelin oluşturduğu *yapıştırıcı kod* sandbox'ta çalışır. Bu doğru ayrımdır.

## Minimum Kurulum

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## CodeAct Ne Zaman Kullanılır (Ne Zaman Kullanılmaz)

**CodeAct kullanın:**
- Görev birçok küçük araç çağrısını zincirliyor (aramalar, birleştirmeler, hesaplamalar)
- Gecikme ve token maliyeti önemliyse
- Model tarafından oluşturulan kod için güçlü izolasyon istiyorsanız

**Geleneksel araç çağrısında kalın:**
- Ajan tur başına yalnızca bir iki araç çağrısı yapıyorsa
- Her çağrının bireysel onay gerektiren yan etkileri varsa

## Şimdi Deneyin

```bash
pip install agent-framework-hyperlight --pre
```

[Agent Framework blogundaki tam gönderiyi](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) okuyun.
