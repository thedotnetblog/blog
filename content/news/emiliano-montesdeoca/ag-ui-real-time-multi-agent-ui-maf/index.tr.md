---
title: "Kara Kutu Hissi Vermeyen Gerçek Zamanlı Çoklu-Agent Arayüzleri Oluşturmak"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI ve Microsoft Agent Framework, çoklu-agent iş akışlarına gerçek zamanlı streaming, insan onayları ve agentların ne yaptığına dair tam görünürlük sunan bir frontend katmanı kazandırıyor."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Çoklu-agent sistemler hakkında şunu söylemek gerekir: demo ortamlarında inanılmaz görünürler. Üç agent iş birbirine aktarır, sorunları çözer, kararlar alır. Sonra bunu gerçek kullanıcıların önüne koymaya çalışırsınız ve... sessizlik. Dönen bir yükleme göstergesi. Hangi agentın ne yaptığını ya da sistemin neden durduğunu anlatan hiçbir şey yok. Bu bir ürün değil — bu bir güven sorunudur.

Microsoft Agent Framework ekibi, MAF iş akışlarını [AG-UI](https://github.com/ag-ui-protocol/ag-ui) ile eşleştiren [harika bir rehber](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) yayımladı. AG-UI, agent yürütme olaylarını Server-Sent Events üzerinden bir frontend'e aktarmak için kullanılan açık bir protokoldür. Ve dürüst olmak gerekirse? Bu, eksik olan köprünün ta kendisi.

## .NET geliştiricileri için neden önemli

AI destekli uygulamalar geliştiriyorsanız, muhtemelen bu duvarla karşılaşmışsınızdır. Backend orkestrasyonunuz mükemmel çalışır — agentlar birbirlerine iş devreder, araçlar tetiklenir, kararlar alınır. Ancak frontend, perde arkasında ne olduğundan habersizdir. AG-UI, agent olaylarını (`RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*` gibi) SSE üzerinden doğrudan UI katmanınıza aktarmak için standart bir protokol tanımlayarak bunu çözer.

Geliştirdikleri demo, üç agentlı bir müşteri destek iş akışı: istekleri yönlendiren bir triage agentı, para işlerini yöneten bir refund agentı ve ikame yönetimi yapan bir order agentı. Her agentın kendi araçları var ve devir teslim topolojisi açıkça tanımlanmış — "prompt'tan çöz" vibesinden eser yok.

## Devir teslim topolojisi asıl yıldız

Dikkatimi çeken şey, `HandoffBuilder`'ın agentlar arasında yönlendirilmiş bir rotalama grafiği tanımlamanıza izin vermesidir:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Her `add_handoff`, doğal dil açıklamasıyla yönlendirilmiş bir kenar oluşturur. Framework, bu topolojiye dayanarak her agent için devir teslim araçları üretir. Böylece yönlendirme kararları, LLM'in keyfine değil, orkestrasyon yapınıza dayanır. Bu, üretim güvenilirliği açısından son derece önemlidir.

## Gerçekten işe yarayan human-in-the-loop

Demo, her gerçek dünya agent uygulamasının ihtiyaç duyduğu iki kesme (interrupt) deseni sergiliyor:

**Araç onay kesmeleri** — bir agent `approval_mode="always_require"` ile işaretlenmiş bir araç çağırdığında iş akışı duraklar ve bir olay yayımlar. Frontend, araç adı ve argümanlarıyla bir onay modalı gösterir. Token yakan yeniden deneme döngüleri yok — sadece temiz bir duraklat-onayla-devam et akışı.

**Bilgi isteği kesmeleri** — bir agentın kullanıcıdan daha fazla bağlam (örneğin bir sipariş ID'si) ihtiyacı olduğunda durur ve sorar. Frontend soruyu gösterir, kullanıcı yanıtlar ve yürütme tam kaldığı yerden devam eder.

Her iki desen de standart AG-UI olayları olarak stream edilir; bu nedenle frontend'inizin her agent için özel mantığa ihtiyacı yoktur — SSE bağlantısından gelen olayı olduğu gibi gösterir.

## Bağlantı kurmak şaşırtıcı derecede basit

MAF ile AG-UI arasındaki entegrasyon tek bir fonksiyon çağrısıdır:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

`workflow_factory`, thread başına yeni bir iş akışı oluşturur; böylece her konuşma izole bir duruma sahip olur. Endpoint, tüm SSE altyapısını otomatik olarak yönetir. Zaten FastAPI kullanıyorsanız (ya da hafif bir katman olarak ekleyebiliyorsanız), bu neredeyse hiç sürtünme gerektirmez.

## Benim görüşüm

.NET geliştiricileri olarak aklımıza gelen ilk soru şu: "Bunu C#'ta yapabilir miyim?" Agent Framework hem .NET hem de Python için mevcut ve AG-UI protokolü dilden bağımsız (aslında sadece SSE). Bu nedenle, bu demo Python ve FastAPI kullansa da, desen doğrudan çevrilebilir. Aynı AG-UI olay şemasını takip eden SSE endpoint'leriyle ASP.NET Core minimal API kurabilirsiniz.

Daha büyük çıkarım şu: çoklu-agent arayüzleri artık sonradan düşünülen bir konu değil, birinci sınıf bir endişe haline geliyor. Agentların insanlarla etkileşime girdiği herhangi bir şey geliştiriyorsanız — müşteri desteği, onay iş akışları, belge işleme — MAF orkestrasyonu ve AG-UI şeffaflığının bu kombinasyonu, izlenecek yol.

## Sonuç

AG-UI + Microsoft Agent Framework, her iki dünyanın en iyisini sunar: backend'de sağlam çoklu-agent orkestrasyonu, frontend'de gerçek zamanlı görünürlük. Artık kara kutu agent etkileşimleri yok.

Daha fazla bilgi için [tam rehbere](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) ve [AG-UI protokol deposuna](https://github.com/ag-ui-protocol/ag-ui) göz atın.
